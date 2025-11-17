# Site Pessoal de Portfólio - Código Aberto

Olá! Este é o código-fonte do meu site de portfólio pessoal, que você pode ver ao vivo em [gsathler-vi.github.io](https://gsathler-vi.github.io/). Eu o desenvolvi para ser uma maneira limpa e moderna de apresentar meu trabalho e minhas habilidades.

Estou muito feliz em compartilhar este projeto como um modelo de código aberto. Sinta-se à vontade para usá-lo como base para o seu próprio site de portfólio. Espero que ele ajude você a criar uma presença online incrível!

------------------------------------------------------------------------

# Guia do seu Novo Site de Portfólio

Bem-vindo ao guia do seu novo site! Este documento foi criado para ajudar você a entender como tudo funciona, mesmo que você não tenha nenhuma experiência com programação.

## 1. O Que é Este Projeto?

Imagine que você tem um caderno mágico. Nele, você escreve o conteúdo do seu portfólio – sua experiência, seus projetos, seus certificados – em texto simples, como se estivesse escrevendo um e-mail. Depois de escrever, você diz as palavras mágicas (neste caso, executa um comando simples no seu computador), e o caderno se transforma em um site profissional, bonito e pronto para ser compartilhado com o mundo.

É exatamente isso que este projeto faz. Ele usa uma ferramenta chamada **Quarto** para transformar arquivos de texto simples em um site de portfólio completo. Isso significa que você não precisa se preocupar com códigos complicados de HTML, CSS ou JavaScript. Você só precisa se concentrar em escrever o seu conteúdo.

## 2. Como as Coisas Estão Organizadas?

Seu site é como uma pasta com alguns arquivos de texto e subpastas. Aqui estão os mais importantes:

-   **O Arquivo de Configuração Principal (`_quarto.yml`)**: Pense neste arquivo como o painel de controle do seu site. É aqui que você define o título do site, o menu de navegação e a aparência geral (como as cores e as fontes). *(Para os curiosos: [Saiba mais sobre o `_quarto.yml`](https://quarto.org/docs/projects/quarto-projects.html))*

-   **As Páginas de Conteúdo (arquivos `.qmd`)**: Cada página do seu site (como "Sobre Mim", "Experiência", "Certificações") é um arquivo que termina em `.qmd`. Você pode abrir esses arquivos em um editor de texto simples para alterar seu conteúdo. *(Para os curiosos: [Saiba mais sobre como escrever em arquivos `.qmd`](https://quarto.org/docs/authoring/markdown-basics.html))*

-   **As Pastas para Itens da Lista (`/posts` e `/material`)**: Estas pastas são especiais. Qualquer coisa que você colocar aqui (como um novo trabalho, apresentação ou documento) será automaticamente adicionada a uma lista em seu site. Isso é ótimo para coisas como um blog ou uma lista de projetos, onde você está constantemente adicionando novos itens. *(Para os curiosos: [Saiba mais sobre como funcionam as listagens](https://quarto.org/docs/websites/website-listings.html))*

## 3. Como Adicionar e Atualizar Conteúdo

Esta é a parte mais importante! Aqui está o passo a passo para adicionar novos itens ao seu portfólio.

### Adicionando um Novo Trabalho ou Apresentação

Vamos supor que você queira adicionar uma nova apresentação que você fez.

1.  **Vá para a Pasta Certa**: No seu computador, vá para a pasta `posts`.

2.  **Crie uma Nova Pasta para a sua Apresentação**: Crie uma nova pasta e dê a ela um nome curto e descritivo. Por exemplo, `minha-nova-apresentacao`.

3.  **Crie um Arquivo de Texto**: Dentro desta nova pasta, crie um arquivo de texto chamado `index.qmd`. É aqui que você vai escrever o conteúdo da sua apresentação.

4.  **Preencha as Informações Principais**: No topo do arquivo `index.qmd`, você precisa adicionar um pequeno bloco de informações. Pense nisso como preencher um formulário.

    ---     
    title: "O Título da Minha Nova Apresentação"     
    author: "Seu Nome"     
    date: "2025-11-17"     
    categories: [Apresentação, Tecnologia]     
    image: "minha-imagem.png"     
    ---

    -   `title`: O título que aparecerá no site.
    -   `author`: O seu nome.
    -   `date`: A data em que você está adicionando isso.
    -   `categories`: Algumas palavras-chave que descrevem o seu trabalho.
    -   `image`: O nome de uma imagem que você quer que apareça ao lado do seu post na lista.

5.  **Adicione a Imagem (Opcional)**: Se você especificou uma imagem, certifique-se de colocar o arquivo de imagem (por exemplo, `minha-imagem.png`) na mesma pasta que o seu arquivo `index.qmd`.

6.  **Escreva o Conteúdo**: Abaixo das informações principais, escreva o que você quiser sobre a sua apresentação. Você pode usar formatação simples, como `#` para títulos e `*` para listas.

Para adicionar outros tipos de conteúdo, como **materiais ou documentos**, o processo é exatamente o mesmo, mas você usará a pasta `/material` em vez da pasta `/posts`.

*(Para os curiosos: quer aprender a fazer coisas mais avançadas no seu conteúdo? Veja os guias do Quarto sobre como adicionar [tabelas](https://quarto.org/docs/authoring/tables.html), [vídeos do YouTube](https://quarto.org/docs/authoring/videos.html), e muito mais!)*

### Atualizando as Páginas Existentes

Para alterar o conteúdo de páginas como "Experiência" ou "Certificações", basta abrir o arquivo `.qmd` correspondente (por exemplo, `experiencia.qmd`) e editar o texto diretamente.

## 4. Como Ver e Publicar o seu Site

Depois de adicionar ou atualizar seu conteúdo, você vai querer ver como ele ficou.

### Instalando o Necessário

Antes de mais nada, você precisa das ferramentas certas. Felizmente, isso é fácil. Abra o terminal (uma janela de linha de comando) no seu computador e execute o seguinte:

``` bash
pip install -r requirements.txt
```

Isso irá instalar o Quarto e tudo mais que você precisa.

### Vendo uma Prévia do seu Site

Para ver como o seu site está ficando em tempo real, use o comando de pré-visualização. Ele abrirá o site no seu navegador e o atualizará automaticamente sempre que você salvar uma alteração. É como ter um espelho mágico para o seu site.

Para iniciar a pré-visualização, execute este comando no terminal:

``` bash
quarto preview
```

*(Para os curiosos: [Veja tudo o que o `quarto preview` pode fazer](https://quarto.org/docs/reference/cli/preview.html))*

### Deixando o seu Site Pronto para a Internet

Quando você estiver feliz com a aparência do seu site, é hora de prepará-lo para ser publicado. Para isso, você usará o comando de "renderização". Ele pega todos os seus arquivos de texto e os transforma na versão final do seu site.

Para deixar o seu site pronto, execute este comando:

``` bash
quarto render
```

Isso irá criar (ou atualizar) a pasta `/docs`. Tudo o que está nesta pasta é o seu site final, pronto para ser colocado na internet.

*(Para os curiosos: [Veja tudo o que o `quarto render` pode fazer](https://quarto.org/docs/reference/cli/render.html))*

## 5. Deixando o Site com a sua Cara

Você pode personalizar a aparência do seu site de maneiras bem simples.

### Mudando o Visual com um Clique

A forma mais fácil de mudar o visual do seu site é trocando o "tema". Um tema é um conjunto de cores, fontes e estilos que dão ao seu site uma aparência única.

1.  **Abra o Arquivo de Configuração Principal** (`_quarto.yml`).
2.  **Encontre a Linha do Tema**: Procure por uma linha que se parece com `theme: cosmo`.
3.  **Escolha um Novo Tema**: Você pode substituir `cosmo` por qualquer um dos temas desta [galeria de temas](https://quarto.org/docs/output-formats/html-themes.html#bootswatch-themes). Tente `litera`, `sandstone`, ou `darkly` para ver como o visual do seu site muda completamente!
4.  **Salve o Arquivo**: Salve o arquivo e, se você estiver com o `quarto preview` rodando, seu site será atualizado com o novo visual instantaneamente.

### Fazendo Pequenos Ajustes no Estilo

Se você quiser fazer pequenas mudanças, como alterar a cor de um título ou o tamanho de uma fonte, você pode fazer isso no arquivo `styles.css`.

Pense no `styles.css` como uma folha de estilo onde você pode adicionar suas próprias regras de design. Por exemplo, se você quisesse que todos os títulos principais do seu site fossem vermelhos, você poderia adicionar o seguinte ao `styles.css`:

``` css
h1 {
  color: red;
}
```

Não tenha medo de experimentar! Se você não gostar de uma mudança, basta apagar a linha que você adicionou.

*(Para os curiosos: quer ir além e personalizar tudo no seu site? O Quarto tem um [guia completo de temas](https://quarto.org/docs/output-formats/html-themes.html) que mostra como mudar cores, fontes e muito mais.)*