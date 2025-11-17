# Prompt para IA: Gerar Documentação Abrangente do Projeto

**Objetivo:**

Analisar o projeto de site de portfólio pessoal baseado em Quarto e gerar uma documentação abrangente que permita a outro desenvolvedor entender, replicar e manter o projeto facilmente.

**Instruções:**

1.  **Analisar o repositório:** Comece escaneando todos os arquivos e diretórios, excluindo a pasta `/docs`, que contém o resultado do site.
2.  **Identificar a tecnologia:** Reconheça que o projeto foi construído usando o framework Quarto.
3.  **Gerar a documentação:** Crie um guia detalhado com as seguintes seções:

    ---

    ### **Documentação do Projeto**

    #### **1. Visão Geral do Projeto**
    -   Comece com uma breve introdução explicando que este é um site de portfólio pessoal construído com Quarto.
    -   Descreva o objetivo principal do site: exibir experiência profissional, trabalhos acadêmicos e projetos pessoais.

    #### **2. Estrutura do Projeto**
    -   Forneça uma descrição clara e hierárquica dos arquivos e diretórios mais importantes.
    -   Explique a função de cada componente principal:
        -   `_quarto.yml`: O arquivo de configuração central que controla a navegação, aparência e configurações de compilação do site.
        -   `index.qmd`: A página principal "Sobre Mim".
        -   `experiencia.qmd`, `certificacoes.qmd`, `posts.qmd`, `material.qmd`: Explique que estas são as páginas de conteúdo primário.
        -   Diretórios `/posts` e `/material`: Descreva como essas pastas contêm os itens de conteúdo individuais (como posts de blog ou documentos) em subdiretórios, cada um com seu próprio `index.qmd`.

    #### **3. Gerenciamento de Conteúdo**
    -   Crie um guia passo a passo para gerenciar o conteúdo. Esta seção é crucial para um usuário não técnico.
    -   **Como adicionar um novo post de blog ou apresentação:**
        1.  Explique o processo de criação de um novo subdiretório em `/posts`.
        2.  Detalhe a estrutura do arquivo `index.qmd` dentro dele, incluindo o cabeçalho YAML (título, autor, data, categorias, imagem).
    -   **Como adicionar um novo material ou documento:**
        1.  Explique que o processo é idêntico ao de adicionar um post de blog, mas deve ser feito no diretório `/material`.
    -   **Como atualizar páginas estáticas:**
        1.  Forneça instruções claras sobre como editar `experiencia.qmd` e `certificacoes.qmd` para adicionar novas entradas, destacando o uso de HTML básico para formatação.

    #### **4. Compilando e Visualizando o Site**
    -   Explique os pré-requisitos necessários, especificamente que a CLI do Quarto deve estar instalada.
    -   Forneça os comandos de shell exatos para:
        -   **Visualizar o site localmente:** `quarto preview` (mencione que ele recarrega automaticamente).
        -   **Compilar o site:** `quarto render` (e observe que a saída vai para o diretório `/docs`).

    ---

4.  **Resultado Final:**
    -   A documentação final deve ser bem estruturada, clara e concisa.
    -   Use Markdown para formatação, incluindo blocos de código para comandos e caminhos de arquivo.
