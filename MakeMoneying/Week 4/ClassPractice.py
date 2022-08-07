class MySatus:
    def __init__(self, age:int, name:str, height:float, weight:float):
        self.age = age
        self.name = name
        self.height = height
        self.weight = weight

    def print_name(self):
        print(self.name)

    def print_age(self):
        print(self.age)

    def print_height(self):
        print(self.height)

    def print_weight(self):
        print(self.weight)

a = MySatus(34, "yamada", 170, 78)
a.print_age()