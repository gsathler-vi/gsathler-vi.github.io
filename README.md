# Site Acadêmico e Profissional - Gabriel Sathler

![Capa do Projeto](https://github.com/gsathler-vi/gsathler-vi.github.io/blob/main/preview-image.png)

[![GitHub Pages](https://img.shields.io/github/deployments/gsathler-vi/gsathler-vi.github.io/github-pages?label=GitHub%20Pages)](https://gsathler-vi.github.io) [![Último commit](https://img.shields.io/github/last-commit/gsathler-vi/gsathler-vi.github.io)](https://github.com/gsathler-vi/gsathler-vi.github.io/commits/main) [![Quarto](https://img.shields.io/badge/Made%20with-Quarto-blue)](https://quarto.org) [![Tamanho do repositório](https://img.shields.io/github/repo-size/gsathler-vi/gsathler-vi.github.io)](https://github.com/gsathler-vi/gsathler-vi.github.io)

## 📖 Sobre o Projeto

Este é um **site acadêmico e profissional** desenvolvido com [Quarto](https://quarto.org/), uma ferramenta moderna para criação de documentos técnicos e científicos. O site apresenta portfólio, experiências, certificações, histórico acadêmico e materiais didáticos.

**🌐 Acesse o site:** [https://gsathler-vi.github.io](https://gsathler-vi.github.io)

### ✨ Principais Características

- 📄 **Páginas Dinâmicas**: Sobre, Experiência, Certificações, Histórico Acadêmico
- 📝 **Sistema de Posts**: Blog com categorias, tags e RSS feed
- 📚 **Materiais Didáticos**: Tutoriais interativos com código executável
- 🎨 **Design Responsivo**: Adaptável para desktop, tablet e mobile
- 🔍 **Busca Integrada**: Sistema de busca em todo o conteúdo
- 🌙 **Tema Dual**: Suporte a modo claro e escuro
- 📊 **Visualizações Interativas**: Gráficos e tabelas dinâmicas

---

## 🎯 Replicação e Personalização

Este projeto foi desenvolvido para ser **facilmente replicável e personalizável**. Se você deseja criar seu próprio site acadêmico/profissional baseado neste template, siga o guia completo abaixo.

### 🚀 Como Usar Este Template

#### 1. **Fork ou Clone do Repositório**

```bash
# Opção 1: Clonar diretamente
git clone https://github.com/gsathler-vi/gsathler-vi.github.io.git meu-site
cd meu-site

# Opção 2: Usar como template no GitHub
# Clique em "Use this template" no repositório original
```

#### 2. **Configurar Informações Pessoais**

Edite os arquivos de configuração principais:

**`_quarto.yml`** - Configuração principal do site:
```yaml
website:
  title: "Seu Nome"  # Altere para seu nome
  site-url: "https://seu-usuario.github.io/"  # Seu domínio
  navbar:
    # Personalize os links do menu
  page-footer:
    left: "© 2025, Seu Nome"
    right:
      - icon: linkedin
        href: "https://linkedin.com/in/seu-perfil"
      - icon: github
        href: "https://github.com/seu-usuario"
```

**`_brand.yml`** - Identidade visual:
```yaml
logo:
  medium: arquivos/seu-logo.png  # Substitua pelo seu logo
```

**`theme.scss` e `styles.css`** - Cores e estilos:
```scss
// Em theme.scss, personalize as cores
$link-color: #244864;  // Sua cor primária
$text-muted: #6a737b;
```

#### 3. **Atualizar Conteúdo das Páginas**

**Página Inicial (`index.qmd`)**
```yaml
---
title: "SEU NOME"
subtitle: "Sua Área de Atuação"
about:
  template: trestles
  image: "arquivos/sua-foto.png"  # Sua foto de perfil
  links:
    - icon: linkedin
      href: "seu-linkedin"
---

Seu texto de apresentação aqui...
```

**Experiência (`experiencia.qmd`)**
- Adicione suas experiências profissionais na timeline
- Mantenha o formato HTML para estilização consistente

**Certificações (`certificacoes.qmd`)**
- Adicione seus certificados e prêmios
- Cada card usa a estrutura `.cert-card`

**Histórico Acadêmico (`historico.qmd`)**
- Atualize as estatísticas no dashboard
- Adicione suas disciplinas nos acordeões por categoria
- Cada disciplina pode ter uma página detalhada em `historico/disciplinas/`

#### 4. **Criar Conteúdo (Posts e Materiais)**

**Estrutura de Posts (`posts/`)**

Cada post fica em uma subpasta com `index.qmd`:

```markdown
---
title: "Título do Post"
author: "Seu Nome"
date: "2025-11-23"
categories: [Categoria1, Categoria2]
image: "imagem-destaque.jpg"
---

Conteúdo do post em Markdown...

## Código executável

```{python}
# Código Python que será executado
import pandas as pd
df = pd.DataFrame({"A": [1, 2, 3]})
df
```

**Estrutura de Materiais (`material/`)**

Similar aos posts, mas focado em conteúdo didático:

```markdown
---
title: "Tutorial: Nome do Material"
subtitle: "Descrição breve"
date: 11-23-2025
author: "Seu Nome"
---

## Introdução

Explicação do material...

```{python}
# Código interativo
```
---

## 🛠️ Instalação e Configuração

### Pré-requisitos

1. **Quarto CLI** (essencial)
   - Download: https://quarto.org/docs/get-started/
   - Versão recomendada: 1.4 ou superior

2. **Python 3.8+** (para materiais com código Python)
   ```bash
   python --version
   ```

3. **Git** (para controle de versão)
   ```bash
   git --version
   ```

### Instalação Passo a Passo

#### Windows (PowerShell)

```powershell
# 1. Instalar Quarto
# Baixe o instalador em: https://quarto.org/docs/get-started/
# Execute o .msi e siga o instalador

# 2. Verificar instalação
quarto --version

# 3. Clonar o repositório
git clone https://github.com/gsathler-vi/gsathler-vi.github.io.git
cd gsathler-vi.github.io

# 4. (Opcional) Criar ambiente virtual Python
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 5. Instalar dependências Python (se houver)
pip install -r requirements.txt
```

#### Linux/macOS (Bash)

```bash
# 1. Instalar Quarto
# Ubuntu/Debian
sudo wget https://github.com/quarto-dev/quarto-cli/releases/download/v1.4.550/quarto-1.4.550-linux-amd64.deb
sudo dpkg -i quarto-1.4.550-linux-amd64.deb

# macOS (com Homebrew)
brew install quarto

# 2. Verificar instalação
quarto --version

# 3. Clonar o repositório
git clone https://github.com/gsathler-vi/gsathler-vi.github.io.git
cd gsathler-vi.github.io

# 4. (Opcional) Criar ambiente virtual Python
python3 -m venv .venv
source .venv/bin/activate

# 5. Instalar dependências Python (se houver)
pip install -r requirements.txt
```

---

## 🖥️ Comandos Essenciais

### Desenvolvimento Local

```bash
# Visualizar o site com hot-reload (recarrega ao salvar)
quarto preview

# Acessar em: http://localhost:4200
```

### Build e Deploy

```bash
# Renderizar todo o site (gera pasta docs/)
quarto render

# Renderizar apenas um arquivo específico
quarto render index.qmd
quarto render posts/meu-post/index.qmd
```

### Limpeza

```bash
# Limpar cache e arquivos temporários
quarto clean

# Limpar completamente (incluindo _freeze/)
rm -rf _freeze/
```

---

## 📁 Estrutura de Pastas Detalhada

```
gsathler-vi.github.io/
│
├── _quarto.yml              # ⚙️ Configuração principal do Quarto
├── _brand.yml               # 🎨 Identidade visual (logo)
├── theme.scss               # 🎨 Variáveis SCSS personalizadas
├── styles.css               # 🎨 Estilos CSS adicionais
│
├── index.qmd                # 🏠 Página inicial
├── experiencia.qmd          # 💼 Experiências profissionais
├── certificacoes.qmd        # 🏆 Certificações e prêmios
├── historico.qmd            # 📚 Histórico acadêmico (dashboard)
├── posts.qmd                # 📝 Listagem de posts
├── material.qmd             # 📖 Listagem de materiais didáticos
│
├── arquivos/                # 📂 Recursos estáticos
│   ├── foto_perfil.png      # Foto de perfil
│   ├── logo.png             # Logo do site
│   └── ...
│
├── posts/                   # 📝 Diretório de posts do blog
│   ├── _metadata.yml        # Metadados compartilhados dos posts
│   ├── apresentacao_pesquisa/
│   │   ├── index.qmd        # Post individual
│   │   └── image.png        # Imagem destaque do post
│   └── aula_dummies/
│       ├── index.qmd
│       └── image.jpg
│
├── material/                # 📚 Materiais didáticos
│   ├── _metadata.yml
│   └── dummies/
│       ├── index.qmd        # Tutorial interativo
│       └── dataset/         # Dados utilizados no tutorial
│
├── historico/               # 📖 Disciplinas acadêmicas
│   └── disciplinas/
│       ├── cursadas/        # Disciplinas concluídas
│       │   ├── economia-brasileira-contemporânea/
│       │   │   └── index.qmd
│       │   └── ...
│       └── em_curso/        # Disciplinas em andamento
│           └── ...
│
├── script/                  # 🐍 Scripts Python auxiliares
│   ├── script_historico.py  # Gera páginas do histórico
│   └── ...
│
├── docs/                    # 🌐 Site gerado (publicado no GitHub Pages)
│   ├── index.html
│   ├── posts/
│   └── ...
│
└── _freeze/                 # ❄️ Cache de execução de código
    └── ...
```

### Explicação dos Arquivos Principais

| Arquivo/Pasta | Descrição | Quando Editar |
|--------------|-----------|---------------|
| `_quarto.yml` | Configuração do site, menu, rodapé | Ao personalizar estrutura |
| `_brand.yml` | Logo e identidade visual | Ao trocar logo |
| `index.qmd` | Página inicial | Sempre (seu perfil) |
| `posts/` | Artigos e trabalhos | Ao publicar novo conteúdo |
| `material/` | Tutoriais e materiais didáticos | Ao criar materiais de ensino |
| `docs/` | Site compilado (não editar) | Gerado automaticamente |

---

## 🎨 Personalização de Estilos

### Cores do Tema

Edite `theme.scss` para alterar as cores principais:

```scss
/*-- scss:defaults --*/
$primary-color: #2d5b7e;    // Azul principal
$link-color: #244864;       // Cor dos links
$text-muted: #6a737b;       // Texto secundário
```

### CSS Customizado

Adicione estilos específicos em `styles.css`:

```css
/* Exemplo: mudar estilo dos cards */
.disciplina-card {
  border-radius: 15px;      /* Bordas mais arredondadas */
  background: linear-gradient(to bottom, #fff, #f9f9f9);
}
```

### Responsividade

O site já possui media queries configuradas. Para ajustar:

```css
@media (max-width: 768px) {
  /* Estilos para mobile */
  .stat-card {
    padding: 1rem;
  }
}
```

---

## 📝 Criando Conteúdo

### Novo Post

1. Crie uma pasta em `posts/nome-do-post/`
2. Adicione `index.qmd` com o conteúdo:

```yaml
---
title: "Título do Post"
author: "Seu Nome"
date: "2025-11-23"
categories: [Python, Análise de Dados]
image: "thumb.png"
---

## Introdução

Seu conteúdo aqui...
```

3. Renderize: `quarto render`

### Novo Material Didático

Similar ao post, mas em `material/nome-material/`:

```yaml
---
title: "Tutorial: Análise com Python"
subtitle: "Guia Prático"
date: 11-23-2025
---

## Passo 1

```{python}
import pandas as pd
# Código executável
```
```

### Adicionar Disciplina no Histórico

1. Crie a pasta: `historico/disciplinas/cursadas/nome-disciplina/`
2. Adicione `index.qmd` com os detalhes
3. Atualize o `historico.qmd` adicionando o card correspondente

---

## 🚀 Publicação no GitHub Pages

### Primeira Configuração

1. **Criar repositório no GitHub**
   - Nome: `seu-usuario.github.io`
   - Marcar como público

2. **Configurar GitHub Pages**
   - Ir em: Settings → Pages
   - Source: Deploy from a branch
   - Branch: `main`
   - Folder: `/docs`
   - Salvar

3. **Push inicial**

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/seu-usuario/seu-usuario.github.io.git
git push -u origin main
```

### Workflow de Atualização

```bash
# 1. Fazer alterações nos arquivos .qmd

# 2. Renderizar o site
quarto render

# 3. Commit e push
git add .
git commit -m "Atualização: descrição das mudanças"
git push

# 4. Aguardar alguns minutos
# Site será atualizado automaticamente
```

---

## 🔧 Recursos Avançados

### Executar Código Python nos Documentos

```python
```{python}
#| echo: true          # Mostra o código
#| warning: false      # Oculta warnings
#| fig-width: 8        # Largura da figura

import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [1, 4, 9])
plt.show()
```

### Criar Tabelas Interativas

```python
```{python}
import pandas as pd
from great_tables import GT

df = pd.DataFrame({
    "Nome": ["Ana", "Bruno"],
    "Nota": [8.5, 9.0]
})

GT(df)
```

### Adicionar Vídeos do YouTube

```markdown
{{< video https://www.youtube.com/watch?v=ID_DO_VIDEO >}}
```

---

## 📚 Recursos e Documentação

### Documentação Oficial do Quarto

- **Site Principal**: https://quarto.org/
- **Guia de Websites**: https://quarto.org/docs/websites/
- **Referência de Opções**: https://quarto.org/docs/reference/
- **Galeria de Exemplos**: https://quarto.org/docs/gallery/

### Tutoriais Específicos

- **Markdown Básico**: https://quarto.org/docs/authoring/markdown-basics.html
- **Código Executável**: https://quarto.org/docs/computations/python.html
- **Layouts e Design**: https://quarto.org/docs/output-formats/page-layout.html
- **Customização Visual**: https://quarto.org/docs/output-formats/html-themes.html

### Comunidade e Suporte

- **GitHub Discussions**: https://github.com/quarto-dev/quarto-cli/discussions
- **Stack Overflow**: Tag `quarto`
- **Twitter**: [@quarto_pub](https://twitter.com/quarto_pub)

---

## 🤝 Contribuição

Se você melhorar algo neste template ou criar recursos interessantes, considere:

1. Fazer um fork
2. Criar uma branch para sua feature: `git checkout -b minha-feature`
3. Commit suas mudanças: `git commit -m 'Adiciona minha feature'`
4. Push para a branch: `git push origin minha-feature`
5. Abrir um Pull Request

---

## 👤 Autor

**Gabriel Sathler Victer Itaborahy**

- 🌐 Site: [gsathler-vi.github.io](https://gsathler-vi.github.io)
- 💼 LinkedIn: [gabriel-sathler](https://linkedin.com/in/gabriel-sathler)
- 🐙 GitHub: [@gsathler-vi](https://github.com/gsathler-vi)
- 📧 Email: gabrielsathler.vi@gmail.com

---

## 🙏 Agradecimentos

- **Quarto Team** - Pela ferramenta incrível
- **Comunidade Open Source** - Inspiração e recursos

---

## 📊 Composição do Projeto

- **JavaScript**: 39.8% - Interatividade e busca
- **CSS**: 31.2% - Estilos e responsividade
- **Python**: 25.2% - Scripts e análises
- **SCSS**: 3.8% - Variáveis de tema

---

**⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!**
