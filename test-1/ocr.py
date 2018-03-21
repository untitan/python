import pytesseract
from PIL import Image

img = Image.open('d:/baodan3.jpg')
str = pytesseract.image_to_data(img, 'chi_sim', '', 0, pytesseract.Output.DICT)
#str = pytesseract.image_to_data(img, None, '', 0, pytesseract.Output.DICT)
# print(str)

for s in str['text']:
    print(s, str['text'].index(s))
