#import convertgif
from PIL import Image
#from PyPDF2 import PdfFileMerger, PdfFileReader
#from fpdf import FPDF
import img2pdf as converter
import os


def flipparser(tokens: list):
    if tokens[3][1] == "pdfout":
        convertpdf(tokens)
    elif tokens[3][1] == "gifout":
        convertgif(tokens)

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
        print(c)
        for j in range(a,b+1):
            print(j)
            combo.append(c)
    outputFile=open(output_path,'wb')
    outputFile.write(converter.convert(combo))
    outputFile.close()
    print("converted to pdf successfully")

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
    
