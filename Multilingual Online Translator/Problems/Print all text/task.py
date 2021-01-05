from lxml import etree

xml_string = input()
root = etree.fromstring(xml_string)

for elem in root:
    print(elem.text)
