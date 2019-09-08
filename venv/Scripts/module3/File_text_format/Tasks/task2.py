import json

def parents_number(class_parents, cls):
    num = 1
    for k, v in class_parents.items():
        if cls in v:
            class_parents[k] = []
            num += parents_number(class_parents, k)
    return num

data_py = json.loads(input())
class_parents = dict()
for cls in data_py:
    class_parents[cls['name']] = cls['parents']

for cls in sorted(class_parents):
    def_class_parents = class_parents.copy()
    print(cls+" : "+str(parents_number(def_class_parents, cls)))


