from xml.etree import ElementTree

def wealth_cube(tree, level, wealth_dict):
    for child in tree:
        if child.attrib['color'] == 'red':
            wealth_dict['red'] += level
        elif child.attrib['color'] == 'green':
            wealth_dict['green'] += level
        else:
            wealth_dict['blue'] += level
        wealth_cube(child, level+1, wealth_dict)
    return wealth_dict

wealth_dict = {'red': 0, 'green': 0, 'blue': 0}

tree = ElementTree.fromstring(input())

if tree.attrib['color'] == 'red':
    wealth_dict['red'] += 1
elif tree.attrib['color'] == 'green':
    wealth_dict['green'] += 1
else:
    wealth_dict['blue'] += 1

answer = wealth_cube(tree, 2, wealth_dict)
print(answer['red'], answer['green'], answer['blue'])