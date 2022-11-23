import lxml, requests, re
from bs4 import BeautifulSoup

result = requests.get("https://www.emu.edu/business-office/contact-us")
#print(result.status_code)  #200 is good, 400/500s are bad

#print(result.headers)
#src = result.content[:200]
#print(src)
#soup = BeautifulSoup(src,'lxml')
#print(soup)

pattern = re.compile(r'[\d()]+ [\d]{3}-[\d]{4}')
phones = pattern.findall(result.text)
print(phones)
