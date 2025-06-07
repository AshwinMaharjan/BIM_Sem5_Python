from enum import Enum

class Grade(Enum):
    A=1
    B=2
    C=3

print(Grade.A)
print(Grade.A.name)
print(Grade.A.value)
