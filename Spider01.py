import requests
url = "http://c.biancheng.net/view/2011.html"
strHtml = requests.get(url)
strHtml.encoding = strHtml.apparent_encoding
print(strHtml.text)
