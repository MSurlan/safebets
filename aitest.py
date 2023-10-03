import pytesseract
import cv2
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img2 = cv2.imread("test.png")
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
binary = cv2.threshold(gray,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
text = pytesseract.image_to_string(binary)
print("-----")
print(text)
