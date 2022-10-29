import os, PyPDF2, glob
from PIL import Image

def img_pdf(PdF):
    pdfR = open(PdF,'wb') 
    pdfW = PyPDF2.PdfFileWriter()
    files = glob.glob('pliki/*.jpg')
    i=0
    for file in files:
        print(file)
        image1 = Image.open(file)
        im1 = image1.convert('RGB')
        num1 = str(i)+'.pdf'
        i+=1
        im1.save(num1)
        pdfRa_=open(num1,'rb')
        pdfRa = PyPDF2.PdfFileReader(pdfRa_)
        pdfW.addPage(pdfRa.getPage(0))
        pdfW.write(pdfR)
        pdfRa_.close()
        os.unlink(num1)
    pdfR.close() 

def pdf_pdf(PdF):
    pdfR = open(PdF,'wb') 
    pdfW = PyPDF2.PdfFileWriter()
    files = glob.glob('pliki/*.pdf')
    for file in files:
        print(file)
        pdfRa_=open(file,'rb')
        pdfRa = PyPDF2.PdfFileReader(pdfRa_)
        for pageN in range(pdfRa.numPages):
            pageObj = pdfRa.getPage(pageN)
            pdfW.addPage(pageObj)
        pdfW.write(pdfR)
        pdfRa_.close()
    pdfR.close() 

def main():
    pDf = input("Podaj nazwe pdf: ")
    pDf=pDf+'.pdf'
    choice = input("img -> pdf (img), pdfy -> pdf (pdf) ?: ")
    if choice == "img":
        img_pdf(pDf)
    else:
        pdf_pdf(pDf)   

if __name__=="__main__":
    main()