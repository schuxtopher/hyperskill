from lxml import etree


def find_attribute(xml_string, attribute_name):
    root = etree.fromstring(xml_string)
    return root.get(attribute_name)


print(find_attribute(input(), input()))
