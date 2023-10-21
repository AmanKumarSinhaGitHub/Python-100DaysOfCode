class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self) -> str:
        return f'{self.i}i + {self.j}j + {self.k}k'
    
    def __add__(v1, v2):
        # return f'{v1.i + v2.i}i + {v1.j + v2.j}j + {v1.k + v2.k}k'   
        return Vector(v1.i + v2.i, v1.j + v2.j, v1.k + v2.k)

vect = Vector(10,20,30)
print(vect)

vect2 = Vector(50,60,70)
print(vect2)

print(vect + vect2)