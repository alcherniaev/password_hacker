from lxml import etree
import requests

def find_password(xml_string):
    root = etree.fromstring(xml_string)
    for i in root:
        return i.get('password')



# testing requests
r = requests.get('https://hyperskill.org/learn/step/8603')
print(r)

if r:
    print('success')
else:
    print('fail')
print(r.encoding)
print(r.headers)
print(r.text)

