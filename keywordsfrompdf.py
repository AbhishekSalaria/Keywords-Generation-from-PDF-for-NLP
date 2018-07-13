import PyPDF2
import textract
from nltk.corpus import stopwords
import pandas as pd
import re
filename = 'jb.pdf'
pdfFileObj = open(filename,'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
num_pages = pdfReader.numPages
count = 0
text = ""
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()
if text != "":
   text = text
else:
   text = textract.process(filename, method='tesseract', language='eng')
review = re.sub('[^a-zA-Z]', ' ', text)
review=review.lower()
review=review.split()
alphabet = []
for letter in range(97,123):
    alphabet.append(chr(letter))
for letter in range(65, 91):
    alphabet.append(chr(letter))
stop_words = stopwords.words('english')
keywords = [word for word in review if not word in stop_words and not word in alphabet]
xy=set(keywords)
len(xy)
ls={} 
l=[] 
s=[]
for word in xy:
    coun=0
    for words in keywords:
        if word==words:
           coun +=1
    l.append(word)
    s.append(coun)
    ls[word]=coun
import numpy as np
result1=np.column_stack((l,s))  
df=pd.DataFrame(result1[:,[0,1]])
df.to_csv("result.csv")
ds3=pd.read_csv("result.csv")

