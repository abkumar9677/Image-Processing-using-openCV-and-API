import cv2 as cv
import numpy as np
import requests
import io
import json
img = cv.imread("screen1.jpg")
#print(img.shape)
"""
#cutting image
height,width,_= img.shape
roi = img[0:height,400:width]

"""
#print(img)
url_api = "https://api.ocr.space/parse/image"
_, compressedimage = cv.imencode("screen.jpg",img,[1,90])
file_bytes = io.BytesIO(compressedimage)
result = requests.post(url_api, files={"screen.jpg": file_bytes}, data={
                       "apikey": "109e19ff7488957"})
result = result.content.decode()
result = json.loads(result)
text_detected = result.get("ParsedResults")[0].get("ParsedText")
print(text_detected)
cv.imshow("Img",img)
cv.waitKey(0)
cv.destroyAllWindows()
