import requests
from  bs4   import     BeautifulSoup
url="http://mlr.cs.umass.edu/ml/datasets.html"
response=requests.get(url)
content=response.content
soup=BeautifulSoup(content,"html.parser")
print(soup.title)
print(soup.title.get_text())
print(soup.body)
print(response.status_code)
tables = soup.find_all('table', {'cellpadding':'3'})
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
table = tables[0] # the result is a list, we are taking out data from it
for td in table.find('tr').find_all('td'):
    print(td.text)


