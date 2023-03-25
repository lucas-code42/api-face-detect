import base64
import json

import requests

with open('image-1.jpg', 'rb') as f:
    imagem_bytes = f.read()

data = json.dumps({'base64_image': base64.b64encode(imagem_bytes).decode()})
response = requests.post('http://localhost:8000/detect', data=data)
print(response.json())
