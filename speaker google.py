import pdfplumber
from gtts import gTTS
import os

# lendo o arquivo PDF
pdf = pdfplumber.open('O elefante em apuros.pdf')

# gerando lista de páginas do livro (exceto as páginas, 1, 2, 27, 28 e 29!)
paginas = pdf.pages[2:-3]

texto_livro = ''
for pagina in paginas:
   texto_livro +=  pagina.extract_text()
   
texto_final = texto_livro.replace('.', '. ').replace(',', ', ')

# Criando um objeto gTTS com o texto e a linguagem
tts = gTTS(text=texto_final, lang='pt')

# Salvando o áudio em um arquivo
tts.save("output.mp3")

# Reproduzindo o áudio (opcional)
os.system("start output.mp3")