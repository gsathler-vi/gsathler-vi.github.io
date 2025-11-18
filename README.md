# gsathler-vi.github.io

![Capa do Projeto](https://github.com/gsathler-vi/gsathler-vi.github.io/preview-image.png)

[![GitHub Pages](https://img.shields.io/github/deployments/gsathler-vi/gsathler-vi.github.io/github-pages?label=GitHub%20Pages)](https://gsathler-vi.github.io) [![Último commit](https://img.shields.io/github/last-commit/gsathler-vi/gsathler-vi.github.io)](https://github.com/gsathler-vi/gsathler-vi.github.io/commits/main) [![Linguagens](https://img.shields.io/github/languages/top/gsathler-vi/gsathler-vi.github.io)](https://github.com/gsathler-vi/gsathler-vi.github.io) [![Tamanho do repositório](https://img.shields.io/github/repo-size/gsathler-vi/gsathler-vi.github.io)](https://github.com/gsathler-vi/gsathler-vi.github.io)

Índice - [Descrição do Projeto](#descrição-do-projeto) - [Status do Projeto](#status-do-projeto) - [Funcionalidades e Demonstração](#funcionalidades-e-demonstração) - [Conteúdo e Seções](#conteúdo-e-seções) - [Comportamento Responsivo e Acessibilidade](#comportamento-responsivo-e-acessibilidade) - [Acesso ao Projeto](#acesso-ao-projeto) - [Como executar localmente](#como-executar-localmente) - [Pré-requisitos](#pré-requisitos) - [Fluxos comuns](#fluxos-comuns) - [Uso do Quarto (detalhado)](#uso-do-quarto-detalhado) - [Quando/por que usar Quarto aqui](#quandopor-que-usar-quarto-aqui) - [Configuração típica (\_quarto.yml)](#configuração-típica-_quartoyml) - [Comandos úteis do Quarto](#comandos-úteis-do-quarto) - [Exemplo de fluxo de publicação com Quarto + GitHub Pages](#exemplo-de-fluxo-de-publicação-com-quarto--github-pages) - [Estrutura de pastas sugerida](#estrutura-de-pastas-sugerida) - [Tecnologias utilizadas](#tecnologias-utilizadas) - [Composição por linguagem](#composição-por-linguagem) - [Pessoas desenvolvedoras](#pessoas-desenvolvedoras) - [Observações / Dicas de manutenção](#observações--dicas-de-manutenção)

## Descrição do projeto {#descrição-do-projeto}

Site pessoal e portfólio do Gabriel Sathler (gsathler-vi), hospedado via GitHub Pages. O projeto é um site estático composto por HTML/CSS (e SCSS), JavaScript para interatividade leve, e utiliza Quarto e scripts Python para geração/transformação de conteúdo quando aplicável (por exemplo, posts técnicos, notebooks ou páginas geradas a partir de dados).

## Status do Projeto {#status-do-projeto}

Em manutenção. Publicado com GitHub Pages (branch `main`). Atualizações de conteúdo, melhorias visuais e ajustes no pipeline de geração podem ser feitas conforme necessário.

## Funcionalidades e Demonstração {#funcionalidades-e-demonstração}

Funcionalidades primárias: - Páginas estáticas principais: Home, Sobre, Projetos/Portfólio, Blog/Artigos e Contato. - Estrutura de posts/páginas que permite publicação via Quarto (quando aplicável). - Layout responsivo otimizado para dispositivos móveis e desktop. - Estilização com CSS/SCSS com organização modular. - Interações JavaScript leves: navegação, animações e componentes UI simples. - Hospedagem contínua via GitHub Pages.

Conteúdo e Seções - Home: apresentação breve e acesso rápido aos projetos. - Sobre: biografia, skills e objetivos profissionais. - Projetos/Portfólio: cards com resumo dos projetos, links para repositórios e demos. - Blog/Artigos: posts técnicos e notas (possivelmente gerados por Quarto, se presentes). - Contato: links para redes, email e formulários (se houver integração).

Comportamento Responsivo e Acessibilidade - O layout prioriza leitura em diferentes larguras de tela. - Recomenda-se validar contrastes e usar atributos ARIA onde necessário para melhorar acessibilidade.

Demonstração (produção) - URL pública: https://gsathler-vi.github.io

## Acesso ao Projeto {#acesso-ao-projeto}

Repositório: - https://github.com/gsathler-vi/gsathler-vi.github.io

## Como executar localmente {#como-executar-localmente}

Pré-requisitos - Git (para clonar) - Node.js + npm (se houver scripts / bundler) - Python 3 (opcional — útil para servir estáticos) - Quarto (opcional — se for usar o fluxo de geração com .qmd) - sass (opcional — para compilar SCSS manualmente)

Passos básicos 1. Clone: - git clone https://github.com/gsathler-vi/gsathler-vi.github.io.git - cd gsathler-vi.github.io

2.  Se houver package.json (instale dependências):
    -   npm install
3.  Compilar SCSS (se os estilos estiverem em SCSS):
    -   npx sass src/scss:dist/css --no-source-map
    -   Ajuste caminhos conforme a estrutura do projeto.
4.  Se usar Quarto para gerar conteúdo:
    -   Ver seção "Uso do Quarto" abaixo.
5.  Servir localmente:
    -   Com Python: python -m http.server 8000
    -   Com Node (ex.: live-server ou serve): npx live-server public --port=8000
    -   Acesse http://localhost:8000 (ou porta configurada)

Fluxos comuns - Desenvolvimento rápido: npm run dev (se disponível) — roda bundler/local server com hot reload. - Build para produção: npm run build (se disponível) + comando de geração do Quarto (se aplicável).

## Uso do Quarto (detalhado) {#uso-do-quarto-detalhado}

Observação: o repositório contém artefatos relacionados a Quarto e scripts Python — caso queira gerar posts ou documentos programáticos, Quarto é a ferramenta recomendada.

Quando/por que usar Quarto aqui - Produção de posts técnicos, documentação ou páginas que misturam texto e código (notebooks). - Gerar páginas a partir de arquivos .qmd que executam snippets Python e embutem resultados. - Simplifica workflow de publicação: escrever em Markdown/Quarto Markdown e renderizar para HTML estático.

Configuração típica (\_quarto.yml) - Verifique se existe um arquivo \_quarto.yml na raiz. Um exemplo mínimo: \`\`\` project: type: website output-dir: \_site

website: title: "gsathler-vi" navbar: left: - text: "Home" href: index.qmd - text: "Projetos" href: projects.qmd \`\``- Ajuste output-dir para um diretório que seja servido por GitHub Pages (ex.: root do branch`main\` ou pasta docs/).

Comandos úteis do Quarto - Instalar: siga https://quarto.org/docs/get-started/ - Renderizar todo o site: quarto render - Visualizar com live-reload: quarto preview - Renderizar um único documento: quarto render pagina.qmd

Exemplo de fluxo de publicação com Quarto + GitHub Pages 1. Configure \_quarto.yml com output-dir: docs (ou \_site que depois é copiado para docs). 2. Executar: quarto render 3. Commit dos arquivos gerados (ex.: docs/) no branch `main`. 4. Configurar GitHub Pages para servir da pasta /docs na branch main (Settings → Pages). Observação: também é possível usar workflows GitHub Actions para automatizar o build do Quarto e publicar para gh-pages.

Estrutura de pastas sugerida - assets/ → imagens, logos e recursos estáticos - src/ → código fonte (SCSS, JS modular, templates) - content/ ou posts/→ arquivos .qmd / .md (conteúdo a ser renderizado) - \_quarto.yml → configuração do Quarto (se aplicável) - docs/ ou \_site/ → saída build (publicável no GitHub Pages) - package.json → scripts e dependências de frontend (se houver) (Adapte conforme o padrão atual do repositório; a intenção aqui é guiar manutenção.)

Tecnologias utilizadas - HTML - JavaScript — interatividade e lógica de UI - CSS / SCSS — estilos - Python — scripts auxiliares / processamento de conteúdo - Quarto — geração de conteúdo a partir de .qmd / .md

Composição por linguagem - JavaScript: 39.8%\
- CSS: 31.2%\
- Python: 25.2%\
- SCSS: 3.8%

## Pessoas desenvolvedoras {#pessoas-desenvolvedoras}

-   Gabriel Sathler (gsathler-vi) — autor e mantenedor\
    GitHub: https://github.com/gsathler-vi\
    Avatar: https://avatars.githubusercontent.com/u/227610838?v=4

## Observações / Dicas de manutenção

-   Se usar Quarto, prefira automatizar o build com um workflow GitHub Actions que executa `quarto render` e publica para o branch/pasta de Pages, evitando commitar artefatos gerados manualmente.
-   Centralize variáveis de estilo em SCSS (variáveis/partials) para facilitar alterações visuais.
-   Verifique periodicamente as dependências Node/Python e atualize quando necessário para evitar problemas de build.
-   Teste responsividade em várias larguras e use ferramentas de auditoria (ex.: Lighthouse) para checar performance e acessibilidade.