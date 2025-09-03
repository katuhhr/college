x1 = int(input("введите x1"))
y1 = int(input("введите y1"))
x2 = int(input("введите x2"))
y2 = int(input("введите y2"))
from math import sqrt

d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(d)
