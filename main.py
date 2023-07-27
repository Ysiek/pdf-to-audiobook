import PyPDF2
from gtts import gTTS

pdf_file = open("<PDF_FILE_PATH>.pdf", 'rb')

pdf_reader = PyPDF2.PdfReader(pdf_file)
page = pdf_reader.pages

text = None
if len(page) == 1:
    text = page[0].extract_text()
else:
    text = []
    for num in range(0, len(page)):
        text.append(page[num].extract_text())
    text = ''.join(text)
tts = gTTS(text, lang="en")
tts.save('audio.mp3')
