# Conversor de PDF para Audiobook
📸 Demonstração

![nlp_audio_book](https://github.com/SamuSuzini/nlp_audiobook/assets/168037378/ddb8aa2b-5887-4d62-9e42-0a5a5137b5a2)


🛠️ **Tecnologias Utilizadas**
- **Python**: Linguagem de programação usada para automatizar a conversão.
- **pyttsx3**: Biblioteca para conversão de texto em fala.
- **pdfplumber**: Biblioteca para extração de texto de arquivos PDF.
- **os**: Módulo para manipulação de arquivos e diretórios.

✨ **Funcionalidades Principais**
- Converte um arquivo PDF em um audiobook.
- Ignora páginas específicas (1, 2, 27, 28 e 29) durante a conversão.
- Ajusta a taxa de fala para uma velocidade mais rápida (225 palavras por minuto).
- Define o volume da fala para o máximo.
- Salva o audiobook com o mesmo nome do arquivo PDF original.

📋 **Requisitos**
- Python 3.x
- Bibliotecas: pyttsx3, pdfplumber, os

📦 **Instalação**
1. Clone o repositório:
    ```bash
    git clone https://github.com/seuusuario/seuprojeto.git
    cd seuprojeto
    ```
2. Instale as dependências:
    ```bash
    pip install pyttsx3 pdfplumber
    ```

🚀 **Como Usar**
1. Coloque o arquivo PDF desejado na mesma pasta do script.
2. Atualize o nome do arquivo PDF na linha correspondente do script:
    ```python
    nome_arquivo_pdf = 'O elefante em apuros.pdf'
    ```
3. Execute o script:
    ```bash
    python conversor.py
    ```
4. O arquivo de áudio será gerado com o mesmo nome do arquivo PDF, mas com a extensão `.mp3`.

Obrigado por visitar o meu projeto! 😊
