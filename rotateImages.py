from PIL import Image
import os

def rotateImages(rotationAmt):
  for image in os.listdir(os.getcwd()):
    img = Image.open(image)
    img.rotate(rotationAmt).save(image)
    img.close()
    
# examples of use
rotateImages(270)
rotateImages(270)
