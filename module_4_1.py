from fake_math import divide as fake
from true_math import divide as true

result1 = int(fake(21, 3))
result2 = fake(254, 0)
result3 = int(true(25, 5))
result4 = true(125698, 0)

print(result1)
print(result2)
print(result3)
print(result4)