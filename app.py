import pyttsx3
import PyPDF2

book = open('Demo.pdf' , 'rb')
pdfreader = PyPDF2.PdfFileReader(book)
engine = pyttsx3.init()
page = pdfreader.getPage(0)
text = page.extractText()
engine.say(text)
engine.runAndWait()