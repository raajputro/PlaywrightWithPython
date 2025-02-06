
# import itertools
# import numpy as np
# data = [1,2]
# result = list(itertools.permutations(data))
# for r in result:
#     print(r)
# print("Print using numpy")
# print(np.matrix(result))

# calculator = {
#     'add': lambda  x,y : x + y,
#     'subtract': lambda x,y : x - y,
#     'multiply': lambda x,y : x * y,
#     'divide': lambda x,y : x/y if y>0 else 0
# }
#
# result = calculator['divide'](6,0)
# print(result)

a = [1,2,3,4]
b = []

print(a)
for val_b in b:
    for val_a in a:
        if val_b == val_a:
            a.remove(val_a)
print(a)