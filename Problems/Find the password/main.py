from lxml import etree


def find_password(xml_string):
    root = etree.fromstring(xml_string)
    for i in root:
        return i.get('password')


