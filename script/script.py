import csv
import os
import re

# --- CONFIGURAÇÃO ---
CSV_CURSADAS = 'script\cursad.csv'
CSV_EM_CURSO = 'script\curso.csv'
PASTA_CURSADAS = os.path.join('historico', 'disciplinas', 'cursadas')
PASTA_EM_CURSO = os.path.join('historico', 'disciplinas', 'em_curso')
# --------------------
def criar_slug_diretorio(titulo):
    """Converte um título de disciplina em um nome de pasta seguro."""
    s = titulo.lower()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[-\s]+', '-', s).strip('-')
    return s

def processar_disciplinas(caminho_csv, pasta_destino, status_cursada=True):
    """
    Função genérica para processar um CSV de disciplinas e criar os arquivos .qmd.
    """
    print(f"Processando disciplinas de '{caminho_csv}'...")
    try:
        with open(caminho_csv, mode='r', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row = {k.strip(): v for k, v in row.items()}

                slug_diretorio = criar_slug_diretorio(row['Disciplina'])
                caminho_diretorio = os.path.join(pasta_destino, slug_diretorio)
                os.makedirs(caminho_diretorio, exist_ok=True)
                caminho_arquivo_qmd = os.path.join(caminho_diretorio, 'index.qmd')

                # Extrai o conteúdo da ementa, começando após o '---'
                ementa_raw_content = row.get('Ementa', '').strip()
                if ementa_raw_content:
                    separator = '---'
                    parts = ementa_raw_content.split(separator, 1)
                    body_content = parts[1].strip() if len(parts) > 1 else ementa_raw_content
                else:
                    body_content = "### Ementa\n\n*Aguardando o plano de ensino detalhado.*"

                # --- LÓGICA ATUALIZADA PARA O CABEÇALHO YAML E CORPO ---
                
                # Define a lista de categorias, agora incluindo a instituição
                categories = f'["{row["Instituição"]}", "{row["Nucleo"]}", "{row["Curso"]}"]'

                if status_cursada:
                    if row['Periodo'] == '100':
                        periodo_texto = "Extracurricular"
                    else:
                        periodo_texto = f"Período: {row['Periodo']}"
                    
                    subtitle = f"Nota: {row['Nota']} | {periodo_texto}"
                    # A nova descrição detalhada vai para o cabeçalho YAML
                    description = f"Disciplina cursada na {row['Instituição']} como parte do currículo de {row['Curso']}, sob a orientação do professor(a) {row['Docente']} ({row['Titulação']})."
                    
                    conteudo_qmd = f"""---
title: "{row['Disciplina']}"
subtitle: "{subtitle}"
description: "{description}"
categories: {categories}
carga_horaria: {row['Carga Horaria']}
nota: {row['Nota']}
periodo: {row['Periodo']}
toc: true
---

{body_content}
"""
                else: # Disciplinas em curso
                    subtitle = f"Período: {row['Periodo']}"
                    # A nova descrição detalhada vai para o cabeçalho YAML
                    description = f"Disciplina em andamento na {row['Instituição']} como parte do currículo de {row['Curso']}, sob a orientação do professor {row['Docente']} ({row['Titulação']})."
                    
                    conteudo_qmd = f"""---
title: "{row['Disciplina']}"
subtitle: "{subtitle}"
description: "{description}"
categories: {categories}
carga_horaria: {row['Carga Horaria']}
periodo: {row['Periodo']}
toc: true
---

{body_content}
"""
                with open(caminho_arquivo_qmd, 'w', encoding='utf-8') as f:
                    f.write(conteudo_qmd)
                print(f"  -> Criado/Atualizado: {caminho_arquivo_qmd}")

    except FileNotFoundError:
        print(f"AVISO: Arquivo '{caminho_csv}' não encontrado. Pulando esta etapa.")
    except Exception as e:
        print(f"ERRO ao processar o arquivo '{caminho_csv}': {e}")
    print("-" * 20)

def main():
    """Função principal para executar o script."""
    print("Iniciando a criação automática de arquivos de disciplina...")
    print(f"Os arquivos serão gerados dentro de '{PASTA_CURSADAS}' e '{PASTA_EM_CURSO}'.")
    print("-" * 20)

    processar_disciplinas(CSV_CURSADAS, PASTA_CURSADAS, status_cursada=True)
    processar_disciplinas(CSV_EM_CURSO, PASTA_EM_CURSO, status_cursada=False)

    print("Processo concluído!")

if __name__ == "__main__":
    main()