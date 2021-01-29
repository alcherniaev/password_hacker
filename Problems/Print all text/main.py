from lxml import etree

xml = '<root><elem1>I am elem1</elem1><elem2>I am elem2</elem2><elem3>I am elem3</elem3></root>'
root = etree.fromstring(xml)

for i in root:
    print(i.text)


etree.dump(root)