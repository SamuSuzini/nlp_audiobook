import pyttsx3
import pdfplumber
import os

# Inicializando a engine de NLP
engine = pyttsx3.init()

# Lendo o arquivo PDF
nome_arquivo_pdf = 'O elefante em apuros.pdf'
pdf = pdfplumber.open(nome_arquivo_pdf)

# Gerando lista de páginas do livro (exceto as páginas 1, 2, 27, 28 e 29)
paginas = pdf.pages[2:-3]

texto_livro = ''
for pagina in paginas:
    texto_livro += pagina.extract_text()

texto_final = texto_livro.replace('.', '. ').replace(',', ', ')

# Ajustando a taxa de fala para um valor mais rápido (experimentar diferentes valores)
engine.setProperty('rate', 225)  # Aumentando a taxa de 150 para 225

# Ajustando o volume para o máximo
engine.setProperty('volume', 1.0)

# Extraindo o nome do arquivo sem a extensão .pdf
nome_base = os.path.splitext(nome_arquivo_pdf)[0]

# Salvando o arquivo de áudio com o nome do livro
engine.save_to_file(texto_final, f'{nome_base}.mp3')
engine.runAndWait()
