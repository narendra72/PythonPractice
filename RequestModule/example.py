# pip install requests

import requests

response = requests.get("https://github.com/narendra72")

print(response.text)
