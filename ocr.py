from PIL import Image
import pytesseract

image_path = 'path_to_your_image.png'  

img = Image.open(image_path)

# Perform OCR on the image
extracted_text = pytesseract.image_to_string(img)


print("Extracted Text:")
print(extracted_text)
