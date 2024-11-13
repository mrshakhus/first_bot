class A:
    def process(self):
        print("A process")

class B(A):
    def process(self):
        print("B process")
        super().process()

class C(A):
    def process(self):
        print("C process")
        super().process()

class D(B, C):
    def process(self):
        print("D process")
        super().process()

# Создание экземпляра класса D и вызов метода process
d = D()
d.process()

# Проверка порядка MRO
print(D.__mro__)
