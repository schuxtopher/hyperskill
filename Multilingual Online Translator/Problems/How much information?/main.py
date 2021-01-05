from lxml import etree


def get_info(xlm_string):
    root = etree.fromstring(xlm_string)
    num_root_children = len(root.getchildren())
    num_root_attr = len(root.keys())

    return f"{num_root_children} {num_root_attr}"


print(get_info(input()))
