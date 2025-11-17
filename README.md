# Site Pessoal de Portfólio - Código Aberto

Olá! Este é o código-fonte do meu site de portfólio pessoal, que você pode ver ao vivo em [gsathler-vi.github.io](https://gsathler-vi.github.io/). Eu o desenvolvi para ser uma maneira limpa e moderna de apresentar meu trabalho e minhas habilidades.

Estou muito feliz em compartilhar este projeto como um modelo de código aberto. Sinta-se à vontade para usá-lo como base para o seu próprio site de portfólio. Espero que ele ajude você a criar uma presença online incrível!

---

# 📖 Guia de Utilização do Projeto

Bem-vindo a este guia. O objetivo deste documento é fornecer as instruções necessárias para que você possa utilizar este projeto para criar e gerenciar seu próprio site de portfólio.

## 🚀 1. Visão Geral do Projeto

Este projeto utiliza o **Quarto**, um poderoso gerador de sites estáticos. Em vez de escrever código complexo (HTML, CSS, JavaScript), você cria seu conteúdo em arquivos de texto simples usando Markdown. O Quarto então processa esses arquivos e os transforma em um site profissional e completo.

> **💡 Dica:** Este sistema permite que você se concentre no que é mais importante: o conteúdo do seu portfólio.

## 📁 2. Estrutura do Projeto

O projeto é organizado em uma estrutura de pastas e arquivos simples e intuitiva. Abaixo estão os componentes essenciais:

-   **Arquivo de Configuração Principal (`_quarto.yml`)**: Este é o centro de controle do seu site. Aqui você define o título, o menu de navegação, a aparência visual e outras configurações globais.
    <details>
    <summary>Saiba mais</summary>
    Para um mergulho profundo em todas as opções de configuração, veja a [documentação oficial do `_quarto.yml`](https://quarto.org/docs/projects/quarto-projects.html).
    </details>

-   **Páginas de Conteúdo (arquivos `.qmd`)**: Cada página do site (como "Sobre Mim", "Experiência", "Certificações") é um arquivo `.qmd`. Você pode editar o conteúdo dessas páginas usando um editor de texto.
    <details>
    <summary>Saiba mais</summary>
    Aprenda tudo sobre a sintaxe do Quarto Markdown na [documentação oficial](https://quarto.org/docs/authoring/markdown-basics.html).
    </details>

-   **Diretórios de Conteúdo Dinâmico (`/posts` e `/material`)**: Essas pastas são usadas para conteúdo que é atualizado com frequência, como posts de blog ou projetos. Cada novo item adicionado a essas pastas será automaticamente listado nas páginas correspondentes do site.
    <details>
    <summary>Saiba mais</summary>
    Veja como as [listagens de páginas](https://quarto.org/docs/websites/website-listings.html) funcionam em detalhes.
    </details>

## ✍️ 3. Gerenciamento de Conteúdo

Esta seção detalha como adicionar e atualizar o conteúdo do seu site.

### Adicionando um Novo Item (Trabalho, Apresentação, etc.)

1.  **Escolha o Diretório Apropriado**:
    -   Para trabalhos e apresentações, utilize a pasta `/posts`.
    -   Para materiais e documentos, utilize a pasta `/material`.

2.  **Crie uma Nova Pasta**: Dentro do diretório escolhido, crie uma nova pasta para o seu item. Use um nome curto e descritivo (ex: `nova-apresentacao`).

3.  **Crie o Arquivo `index.qmd`**: Dentro da nova pasta, crie um arquivo chamado `index.qmd`.

4.  **Adicione o Cabeçalho YAML**: No topo do arquivo `index.qmd`, adicione um bloco de metadados para descrever seu conteúdo.
    ```yaml
    ---
    title: "Título da Nova Apresentação"
    author: "Seu Nome"
    date: "2025-11-17"
    categories: [Apresentação, Tecnologia]
    image: "imagem-de-destaque.png"
    ---
    ```
    -   `title`: O título que será exibido no site.
    -   `author`: O seu nome.
    -   `date`: A data de publicação.
    -   `categories`: Palavras-chave para categorizar seu trabalho.
    -   `image`: Uma imagem de destaque para o seu post (opcional).

5.  **Adicione a Imagem de Destaque (Opcional)**: Se você especificou uma `image`, coloque o arquivo de imagem na mesma pasta que o `index.qmd`.

6.  **Escreva o Conteúdo**: Abaixo do cabeçalho, escreva o conteúdo do seu post em Markdown.

> **🚀 Dica Avançada:** quer aprender a fazer coisas mais avançadas no seu conteúdo? Veja os guias do Quarto sobre como adicionar [tabelas](https://quarto.org/docs/authoring/tables.html), [vídeos do YouTube](https://quarto.org/docs/authoring/videos.html), e muito mais!

### Atualizando as Páginas Existentes
Para modificar páginas como "Experiência" ou "Certificações", edite diretamente os arquivos `.qmd` correspondentes (ex: `experiencia.qmd`).

## 🖥️ 4. Visualização e Publicação do Site

Siga os passos abaixo para visualizar e publicar seu site.

### Instalação de Dependências
Primeiro, instale as ferramentas necessárias. Abra um terminal e execute o seguinte comando:
```bash
pip install -r requirements.txt
```

### Visualização em Tempo Real
Para visualizar o site no seu computador e ver as alterações em tempo real, use o comando de pré-visualização. Ele irá abrir o site no seu navegador e o atualizará automaticamente sempre que você salvar um arquivo.

Execute este comando no terminal:
```bash
quarto preview
```
<details>
<summary>Saiba mais</summary>
Veja tudo o que o [`quarto preview`](https://quarto.org/docs/reference/cli/preview.html) pode fazer.
</details>

### Publicação do Site
Quando estiver satisfeito com o resultado, prepare o site para a publicação. O comando a seguir irá gerar a versão final e otimizada do seu site na pasta `/docs`.

Execute este comando:
```bash
quarto render
```
> **✅ Dica:** O conteúdo da pasta `/docs` está pronto para ser publicado em qualquer serviço de hospedagem, como o GitHub Pages.

<details>
<summary>Saiba mais</summary>
Veja tudo o que o [`quarto render`](https://quarto.org/docs/reference/cli/render.html) pode fazer.
</details>

## 🎨 5. Personalização Visual

Você pode personalizar a aparência do seu site de forma simples e rápida.

### Alterando o Tema Visual
A maneira mais fácil de alterar o design do site é trocando o tema.

1.  **Abra o arquivo `_quarto.yml`**.
2.  **Encontre a linha `theme: cosmo`**.
3.  **Escolha um Novo Tema**: Substitua `cosmo` por um dos temas da [galeria de temas do Bootswatch](https://quarto.org/docs/output-formats/html-themes.html#bootswatch-themes). Experimente `litera`, `sandstone`, ou `darkly` para ver a mudança.
4.  **Salve o arquivo**: Se o `quarto preview` estiver em execução, o site será atualizado automaticamente com o novo tema.

### Adicionando Estilos Personalizados
Para ajustes de estilo mais específicos, você pode adicionar suas próprias regras de CSS no arquivo `styles.css`.

Por exemplo, para alterar a cor dos títulos principais para vermelho, adicione o seguinte ao `styles.css`:
```css
h1 {
  color: red;
}
```
> **🎨 Dica de Design:** quer ir além e personalizar tudo no seu site? O Quarto tem um [guia completo de temas](https://quarto.org/docs/output-formats/html-themes.html) que mostra como mudar cores, fontes e muito mais.
