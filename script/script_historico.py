import csv
import os
import re
from collections import defaultdict

# --- CONFIGURAÇÃO DE CAMINHOS ---
# Ajuste conforme a estrutura da sua pasta
CSV_CURSADAS = os.path.join('script/cursad.csv')
CSV_EM_CURSO = os.path.join('script/curso.csv')
CSV_A_CURSAR = os.path.join('script/a_cursar.csv')
OUTPUT_QMD_FILE = 'historico.qmd'

# --- MAPEAMENTO DE EMOJIS POR NÚCLEO ---
EMOJI_MAP = {
    "Ciências Sociais e Humanidades": "🌍",
    "Direito e Regulação": "⚖️",
    "Empreendedorismo e Inovação": "💡",
    "Finanças e Contabilidade": "💰",
    "Fundamentos de Gestão e Organizações": "🏢",
    "Gestão e Políticas Públicas": "🏛️",
    "Marketing e Inteligência de Mercado": "📈",
    "Metodologia Científica": "🔬",
    "Métodos Quantitativos e Computacionais": "💻",
    "Teoria Econômica": "📊",
    "Sem Núcleo": "⭐"
}

def criar_slug(texto):
    """Cria um slug limpo para URLs (ex: 'Microeconomia I' -> 'microeconomia-i')"""
    if not texto: return ""
    s = texto.lower()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[-\s]+', '-', s).strip('-')
    return s

def ler_csv(caminho, status_tag):
    """Lê o CSV e retorna lista de dicionários com tratamento de erro."""
    dados = []
    if not os.path.exists(caminho):
        print(f"AVISO: Arquivo não encontrado: {caminho}")
        return dados
    
    try:
        with open(caminho, mode='r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Limpa espaços em branco das chaves e valores
                item = {k.strip(): v.strip() for k, v in row.items() if k}
                item['status_tag'] = status_tag
                dados.append(item)
    except Exception as e:
        print(f"ERRO ao ler {caminho}: {e}")
    return dados

def gerar_html_card(d):
    """Gera o HTML do card da disciplina baseado no NOVO design."""
    
    # 1. Tratar Dados
    disciplina = d.get('Disciplina', 'Sem Nome')
    instituicao = d.get('Instituição', 'N/A')
    curso = d.get('Curso', 'N/A')
    carga = d.get('Carga Horaria', '0')
    nota = d.get('Nota', '')
    
    # Tratar Período
    periodo_raw = d.get('Periodo', '')
    if periodo_raw == '100':
        periodo_display = "Extracurricular"
    else:
        periodo_display = f"{periodo_raw}º Período"

    # 2. Definir Estilos baseados no Status
    status = d['status_tag']
    slug = criar_slug(disciplina)
    
    link_href = "#" # Default
    badge_class = ""
    badge_text = ""
    nota_html = ""
    border_style = "" # Para borda colorida no hover ou estática

    if status == 'cursada':
        link_href = f"historico/disciplinas/cursadas/{slug}/"
        badge_class = "bg-cursada"
        badge_text = "Cursada"
        if nota:
            nota_html = f'<span class="nota-valor">{nota}</span>'
        
    elif status == 'em_curso':
        link_href = f"historico/disciplinas/em_curso/{slug}/"
        badge_class = "bg-em-curso"
        badge_text = "Em Curso"
        
    elif status == 'a_cursar':
        link_href = None # Não tem link
        badge_class = "bg-a-cursar"
        badge_text = "A Cursar"

    # 3. Montar o HTML do Card
    # Usando a estrutura .disciplina-card definida no CSS novo
    
    html_card = f"""
        <div class="disciplina-card">
          <h4>{disciplina}</h4>
          <div class="disciplina-meta">
            <span><i class="bi bi-building"></i> {instituicao} ({curso})</span>
            <span><i class="bi bi-calendar3"></i> {periodo_display}</span>
            <span><i class="bi bi-clock"></i> {carga}h</span>
          </div>
          <div class="disciplina-footer">
            <span class="badge-status {badge_class}">{badge_text}</span>
            {nota_html}
          </div>
        </div>
    """

    # Se tiver link, envolve em tag <a>
    if link_href:
        return f'<a href="{link_href}" class="card-link">{html_card}</a>'
    else:
        return html_card

def main():
    print("--- Iniciando Geração do Histórico ---")

    # 1. Carregar Dados
    cursadas = ler_csv(CSV_CURSADAS, 'cursada')
    em_curso = ler_csv(CSV_EM_CURSO, 'em_curso')
    a_cursar = ler_csv(CSV_A_CURSAR, 'a_cursar')
    
    todas = cursadas + em_curso + a_cursar
    
    # 2. Calcular Estatísticas
    qtd_cursadas = len(cursadas)
    qtd_ativas = len(em_curso)
    
    soma_notas = 0.0
    qtd_notas = 0
    for c in cursadas:
        try:
            n = float(c.get('Nota', 0).replace(',', '.'))
            if n > 0:
                soma_notas += n
                qtd_notas += 1
        except:
            pass
            
    media_geral = f"{soma_notas / qtd_notas:.1f}" if qtd_notas > 0 else "0.0"

    # 3. Agrupar por Núcleo
    por_nucleo = defaultdict(list)
    for disc in todas:
        nucleo = disc.get('Nucleo', 'Sem Núcleo')
        por_nucleo[nucleo].append(disc)

    # 4. Gerar HTML do Acordeão
    accordion_html = ""
    # Ordenar núcleos por relevância estratégica (ordem customizada para recrutadores)
    ordem_estrategica = [
        # 1º Grupo: O Core Estratégico (Alta Demanda e Valor Agregado)
        "Métodos Quantitativos e Computacionais",
        "Marketing e Inteligência de Mercado",
        "Finanças e Contabilidade",
        # 2º Grupo: A Base de Execução (Eficiência e Estrutura)
        "Fundamentos de Gestão e Organizações",
        "Empreendedorismo e Inovação",
        "Teoria Econômica",
        # 3º Grupo: O Diferencial de Rigor e Contexto (Especialização)
        "Metodologia Científica",
        "Gestão e Políticas Públicas",
        "Direito e Regulação",
        "Ciências Sociais e Humanidades",
        "Sem Núcleo"
    ]
    
    # Aplicar ordenação customizada: primeiro os da lista, depois os restantes alfabeticamente
    nucleos_encontrados = list(por_nucleo.keys())
    nucleos_ordenados = [n for n in ordem_estrategica if n in nucleos_encontrados]
    nucleos_extras = sorted([n for n in nucleos_encontrados if n not in ordem_estrategica])
    nucleos_ordenados.extend(nucleos_extras)
    
    for idx, nucleo in enumerate(nucleos_ordenados):
        disciplinas = por_nucleo[nucleo]
        emoji = EMOJI_MAP.get(nucleo, "⭐")
        
        # O primeiro item vem aberto por padrão
        open_attr = "open" if idx == 0 else ""
        
        cards_html = "".join([gerar_html_card(d) for d in disciplinas])
        
        accordion_html += f"""
  <details {open_attr}>
    <summary>{emoji} {nucleo}</summary>
    <div class="disciplinas-grid">
      {cards_html}
    </div>
  </details>
"""

    # 5. Montar o QMD Completo (Com o CSS Novo embutido)
    qmd_content = f"""---
title: "Histórico Escolar"
description: "Visão geral do histórico escolar com o resumo de disciplinas cursadas, em andamento e a cursar."
toc: false
format: 
  html:
    page-layout: full
---

```{{=html}}
<style>
  /* --- Variáveis do Tema --- */
  :root {{
      --primary-color: #39729E;
      --accent-color: #447099;
      --success-color: #337e2e;
      --warning-color: #244864;
      --muted-color: #6c757d;
      --bg-card: #ffffff;
  }}

  /* --- Dashboard de Estatísticas --- */
  .stats-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    margin-bottom: 3rem;
  }}

  .stat-card {{
    background-color: var(--bg-card);
    border: 1px solid #e9ecef;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    display: flex;
    align-items: center;
    justify-content: space-between;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    border-left: 5px solid var(--primary-color);
  }}

  .stat-card:hover {{
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.08);
  }}

  .stat-content h2 {{
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    color: var(--muted-color);
    margin: 0;
    font-weight: 700;
  }}

  .stat-value {{
    font-size: 2.5rem;
    font-weight: 800;
    margin: 0.2rem 0;
    line-height: 1;
    color: #333;
  }}

  .stat-icon {{
    font-size: 2.5rem;
    color: var(--primary-color);
    opacity: 0.2;
  }}

  /* --- Legenda --- */
  .legend-bar {{
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
    align-items: center;
    background: #f8f9fa;
    padding: 1rem;
    border-radius: 8px;
    border: 1px solid #e9ecef;
    margin-bottom: 2rem;
    font-size: 0.9rem;
  }}

  .legend-item {{
    display: flex;
    align-items: center;
    gap: 6px;
    font-weight: 500;
    color: #555;
  }}

  .dot {{
    width: 12px;
    height: 12px;
    border-radius: 50%;
  }}

  /* --- Acordeão (Accordion) --- */
  details {{
    margin-bottom: 1rem;
    border: 1px solid #e9ecef;
    border-radius: 8px;
    overflow: hidden;
    background: white;
    box-shadow: 0 2px 5px rgba(0,0,0,0.02);
  }}

  summary {{
    padding: 1.2rem;
    cursor: pointer;
    font-weight: 600;
    font-size: 1.1rem;
    color: var(--primary-color);
    background-color: #fff;
    list-style: none;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: background 0.2s;
  }}

  summary:hover {{
    background-color: #f8f9fa;
  }}

  summary::after {{
    content: '\\F282'; /* Bootstrap Icon Chevron Down */
    font-family: 'bootstrap-icons';
    transition: transform 0.3s;
  }}

  details[open] summary::after {{
    transform: rotate(180deg);
  }}

  details[open] summary {{
    border-bottom: 1px solid #e9ecef;
  }}

  /* --- Grid de Disciplinas --- */
  .disciplinas-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.2rem;
    padding: 1.5rem;
    background-color: #fcfcfc;
  }}

  /* --- Card de Disciplina --- */
  .disciplina-card {{
    background: white;
    border: 1px solid #e9ecef;
    border-radius: 10px;
    padding: 1.2rem;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: all 0.3s ease;
  }}

  a.card-link {{
    text-decoration: none;
    color: inherit;
    display: block;
    height: 100%;
  }}

  a.card-link:hover .disciplina-card {{
    border-color: var(--primary-color);
    transform: translateY(-3px);
    box-shadow: 0 5px 15px rgba(57, 114, 158, 0.15);
  }}

  .disciplina-card h4 {{
    font-size: 1rem;
    font-weight: 700;
    color: #333;
    margin-bottom: 1rem;
    line-height: 1.4;
    text-transform: uppercase;
  }}

  .disciplina-meta {{
    font-size: 0.85rem;
    color: #666;
    margin-bottom: 1rem;
    display: flex;
    flex-direction: column;
    gap: 4px;
  }}

  .disciplina-meta i {{
    color: var(--primary-color);
    width: 20px;
    text-align: center;
    margin-right: 5px;
  }}

  .disciplina-footer {{
    margin-top: auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid #f0f0f0;
    padding-top: 0.8rem;
  }}

  /* --- Badges --- */
  .badge-status {{
    padding: 5px 12px;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}

  .bg-cursada {{ background-color: rgba(46, 125, 50, 0.1); color: var(--success-color); }}
  .bg-em-curso {{ background-color: rgba(68, 112, 153, 0.1); color: var(--primary-color); }}
  .bg-a-cursar {{ background-color: #f1f3f5; color: var(--muted-color); }}

  .nota-valor {{
    font-weight: 700;
    color: var(--success-color);
    font-size: 0.9rem;
  }}
    /* --- Media Query for Mobile Responsiveness --- */
  @media (max-width: 768px) {{
    /* Força o grid a ter apenas uma coluna em telas menores */
    .disciplinas-grid {{
      grid-template-columns: 1fr; /* Stacks cards vertically */
      padding: 1rem; /* Reduz o preenchimento nas laterais */
    }}

    /* Ajusta os títulos e espaçamentos para telas menores */
    .nucleo-accordion summary {{
      font-size: 1.1rem;
      padding: 1rem;
    }}
    
    .nucleo-accordion summary::after {{
      right: 1rem; /* Ajusta a posição da seta para o novo padding */
    }}

    .disciplina-card h4 {{
      font-size: 1rem;
    }}
    
    /* Ajusta o dashboard de estatísticas para empilhar verticalmente */
    .grid {{
        grid-template-columns: 1fr !important; /* Força uma única coluna */
        gap: 1rem !important;
    }}
  }}
</style>

<!-- DASHBOARD DE ESTATÍSTICAS -->
<div class="stats-grid">
    
    <!-- Card 1 -->
    <div class="stat-card" style="border-left-color: var(--success-color);">
      <div class="stat-content">
        <h2>Média Geral</h2>
        <div class="stat-value" style="color: var(--success-color);">{media_geral}</div>
        <small class="text-muted">Média ponderada</small>
      </div>
      <div class="stat-icon" style="color: var(--success-color);"><i class="bi bi-graph-up-arrow"></i></div>
    </div>

    <!-- Card 2 -->
    <div class="stat-card" style="border-left-color: var(--primary-color);">
      <div class="stat-content">
        <h2>Disciplinas Cursadas</h2>
        <div class="stat-value" style="color: var(--primary-color);">{qtd_cursadas}</div>
        <small class="text-muted">Concluídas com aprovação</small>
      </div>
      <div class="stat-icon" style="color: var(--primary-color);"><i class="bi bi-check-circle-fill"></i></div>
    </div>

    <!-- Card 3 -->
    <div class="stat-card" style="border-left-color: var(--warning-color);">
      <div class="stat-content">
        <h2>Disciplinas Ativas</h2>
        <div class="stat-value" style="color: var(--warning-color);">{qtd_ativas}</div>
        <small class="text-muted">Em andamento</small>
      </div>
      <div class="stat-icon" style="color: var(--warning-color);"><i class="bi bi-hourglass-split"></i></div>
    </div>

</div>

<!-- LEGENDA -->
<div class="legend-bar">
    <div class="legend-item"><span class="dot bg-cursada" style="background-color: var(--success-color);"></span> Cursada</div>
    <div class="legend-item"><span class="dot bg-em-curso" style="background-color: var(--primary-color);"></span> Em Curso</div>
    <div class="legend-item"><span class="dot bg-a-cursar" style="background-color: #adb5bd;"></span> A Cursar</div>
    <div class="ms-auto text-muted fst-italic small"><i class="bi bi-info-circle me-1"></i> Clique no card para ver detalhes da disciplina</div>
</div>

<!-- LISTA DE DISCIPLINAS -->
<div class="disciplinas-container">
{accordion_html}
</div>
```
"""

    # 6. Escrever Arquivo
    with open(OUTPUT_QMD_FILE, 'w', encoding='utf-8') as f:
        f.write(qmd_content)
    
    print(f"Sucesso! Arquivo '{OUTPUT_QMD_FILE}' gerado.")

if __name__ == "__main__":
    main()