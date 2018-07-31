import PyPDF2
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


filename = r"C:\Users\PRAVEEN\Documents\JavaBasics-notes.pdf"
pdfFileObj = open(filename,'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
num_pages = pdfReader.numPages
count = 0
text = ""
#The while loop will read each page
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()

if text != "":
    text = text
else:
    text = textract.process(fileurl, method='tesseract', language='eng')

tokens = word_tokenize(text)
punctuations = ['(',')',';',':','[',']',',', '.','!','I','All','The','the','what','makes','make','why','What','Why']
stop_words = stopwords.words('english')
keywords = [word for word in tokens if not word in stop_words and not word in punctuations]

keyword = [word for word in keywords if len(word)>3]
keyword = [i for i in keyword if not i.isdigit()]
print(keyword)
from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer().fit(keyword)
print(vect.get_feature_names())

import re
keyword_weightage = []
for i in vect.get_feature_names():
    keyword_weightage.append(re.sub("[^a-zA-Z]+","", i))
keyword_weightage = [x.strip(' ') for x in keyword_weightage]
for i in range(len(keyword_weightage)):
    if keyword_weightage[i] == " ":
            del keyword_weightage[i]
keyword_weightage = [word for word in keyword_weightage if not word in stop_words and not word in punctuations]
keyword_weightage = [word for word in keyword_weightage if len(word)>3]
print(keyword_weightage)