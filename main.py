from PyPDF2 import PdfReader
import pyttsx3

# pdf path
pdf_path = input("Please enter the path of the PDF file: ")

# initialize the PDF reader
pdfReader = PdfReader(open(pdf_path, 'rb'))
speaker = pyttsx3.init()

# reading each page, extracting text and converting to speech
for page_num in range(len(pdfReader.pages)):
    text = pdfReader.pages[page_num].extract_text()
    speaker.say(text)
    speaker.runAndWait()

# saving in a mp3 file
speaker.save_to_file(text, 'my_pdf_audio.mp3')
speaker.runAndWait()

speaker.stop()
