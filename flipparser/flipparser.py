from PIL import Image
from fpdf import FPDF
from PyPDF2 import PdfFileMerger, PdfFileReader
import img2pdf as converter
import os

#to parse the tokens
def flipparser(tokens: list):
    filename=tokens[1][0]   #inputfilename
    outname=tokens[3][0]    #outputfilename
    with open(filename) as f:
        lines = f.read().splitlines()        
    x=lines[0].split()
    y=x[1]
    if (tokens[3][1] == "pdfout") & (y=="05"):
        convertpdf(tokens)
    elif (tokens[3][1] == "gifout") & (y=="05"):
        convertgif(tokens)
    elif (y=="newton.jpg"):
        print("Apple")
        newtonapple(tokens)


#to generate flipbook in pdf format
def convertpdf(tokens: list):
    filename=tokens[1][0] #inputfilename
    outname=tokens[3][0] #outputfilename
    output_path = str(outname)
    ar=[]
    combo=[]
    with open(filename) as f:
        lines = f.read().splitlines()
    for  i in lines:     
        x=i.split()
        ar.append(x[2])
        x=""
    for i in lines:
        
        x=i.split()
        a=int(x[0])
        b=int(x[1])
        c=x[2]
        for j in range(a,b+1):
            combo.append(c)
    outputFile=open(output_path,'wb')
    outputFile.write(converter.convert(combo))
    outputFile.close()
    print("converted to pdf successfully")


#to generate flipbook in gif format
def convertgif(tokens: list):
    filename=tokens[1][0] #inputfilename
    outname=tokens[3][0] #outputfilename
    ar=[]
    with open(filename) as f:
        lines = f.read().splitlines()
    for  i in lines:     
        x=i.split()
        ar.append(x[2])
        x=""
    frames = []
    for i in ar:
        new_frame= Image.open(i)
        frames.append(new_frame)
    frames[0].save(outname, format='GIF',
                append_images=frames[1:],
                save_all=True,
                duration=400, Loop=0)
    print("converted to gif successfully")


#to create a flipbook to show an Apple falling on Newton’s head
def newtonapple(tokens: list):
    filename=tokens[1][0] #inputfilename
    outname=tokens[3][0] #outputfilename
    with open(filename) as f:
        lines = f.read().splitlines()
    x=lines[0].split()
    apple=x[0] #applefilename
    newton=x[1] #newtonfilename
    output_path = str(outname)
    pdf_merger = PdfFileMerger()
    for i in range(0,220,20):
        pdf= FPDF()
        pdf.add_page()
        pdf.image(apple, x = 80, y = i, w =50, h = 50)
        pdf.image(newton, x = 80, y = 250, w =50, h = 50)
        output = 'flipbook_cache.pdf'
        pdf.output(output, 'F')
        pdf_merger.append(output)
        print('O')
        pdf_merger.write(output_path)
    pdf_merger.close()
    print("Apple has fallen on Newton")
