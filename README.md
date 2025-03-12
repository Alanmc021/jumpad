## LangChain FastAPI Server

**LangChain FastAPI Server** é uma aplicação web desenvolvida com FastAPI e LangChain para fornecer uma interface API simples para tradução de textos usando modelos de linguagem avançados. Este projeto demonstra a integração entre a biblioteca LangChain e o framework FastAPI, facilitando a criação de endpoints de tradução.

### Funcionalidades

- **Tradução de Texto**: Usa o LangChain para traduzir textos para o idioma especificado.
- **Endpoints API**: Implementado com FastAPI para criar e expor endpoints de serviço web.
- **Modelo de Linguagem**: Configurado para usar o modelo `gpt-4` da OpenAI para geração de texto e tradução.

### Estrutura do Projeto

- **`server.py`**: Define e executa o servidor FastAPI. Inclui o endpoint `/peticao-inicial` que aceita solicitações de tradução e retorna a resposta gerada pelo modelo.
- **`peticao_inicial.py`**: Contém a lógica para gerar a resposta usando o LangChain, definindo o modelo e o template de prompt para tradução.

### Configuração

1. **Instalação**: Instale as dependências usando o comando:
   ```bash
   pip install -r requirements.txt
