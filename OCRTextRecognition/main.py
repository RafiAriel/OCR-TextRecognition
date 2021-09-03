import io
import json
import cv2
import numpy as np
import requests

img = cv2.imread("img.jpg")
url_api = "https://api.ocr.space/parse/image"
flag, compressed_image = cv2.imencode(".jpg", img)
file_bytes = io.BytesIO(compressed_image)
result = requests.post(url_api,
                       files={"img.jpg": file_bytes},
                       data={"apikey": "#KEY",
                             "language": "eng"})

result = result.content.decode()
result = json.loads(result)

parsed_results = result.get("ParsedResults")[0]
text_detected = parsed_results.get("ParsedText")
print(text_detected)
