import img2pdf
from PIL import Image
import os

def makePDF():
    os.chdir("Images")
    images=os.listdir(".")
    if len(images)==0:
        print('No Scanned Images Present !!!')
    else:
        imgList=[x for x in images if x.endswith(".jpg")]

        pdf=img2pdf.convert(imgList)

        file=open("../PDF/Report.pdf","wb")
        file.write(pdf)
        file.close()