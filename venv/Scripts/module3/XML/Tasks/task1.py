from xml.etree import ElementTree

wealth_red, wealth_green, wealth_blue = 0, 0, 0
level = 2

tree = ElementTree.fromstring(input())
# print(tree.tag, tree.attrib)
# print(type(tree.tag))

for element in tree.tag:
    if element.attrib['color'] == 'red':
        wealth_red += 1
    elif element.attrib['color'] == 'green':
        wealth_green += 1
    else:
        wealth_blue += 1
#
# for child in tree:
#     if child.attrib['color'] == 'red':
#         wealth_red += level
#     elif child.attrib['color'] == 'green':
#         wealth_green += level
#     else:
#         wealth_blue += level

print(wealth_red, wealth_green, wealth_blue)