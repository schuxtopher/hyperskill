from lxml import etree


def find_password(xml_string):
    root = etree.fromstring(xml_string)
    password = None

    for i in root.iter():
        password = i.get('password')
        if password is not None:
            break
    return password
