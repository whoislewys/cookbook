import requests

url = 'https://google.com'
html = requests.get(url)
print(html.text)

with open('text.html', 'w+') as infile:
  infile.write(html.text)
