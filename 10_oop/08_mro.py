# class A:
#     label = "A: Base class"

# class B(A):
#     label = "B: Masala blend"

# class C(A):
#     label = "C: Herbal blend"

# class D(C, B):
#     pass

# cup = D()
# print(cup.label)


class Baseclass:
    label = "Belongs to Base class"

class A(Baseclass):
    label = "A: belogs to class A"

class B(Baseclass):
    label = "B: Belongs toa class B"

class C(B, A):
    pass

cup = C()
print(cup.label)

