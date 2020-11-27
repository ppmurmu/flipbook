#import convertgif
from PIL import Image

def flipparser(tokens: list):
    if tokens[0][0] == "fc":
        convertflip(tokens)
    else:
        displayflip(tokens)

def convertflip(tokens: list):
    a=tokens[1][0] #filename
    b=tokens[3][0]
    open_file(a,b)
def open_file(filename, outname):
    with open(filename) as f:
        lines = f.read().splitlines()
    frames = []
    for i in lines:
        new_frame= Image.open(i)
        frames.append(new_frame)
    frames[0].save(outname, format='GIF',
                append_images=frames[1:],
                save_all=True,
                duration=400, Loop=0)
    
def displayflip(tokens: list):
    print("display images")
    
