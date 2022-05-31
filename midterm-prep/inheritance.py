class Animal:
    def __init__(self, name, group, number_of_legs, number_of_wings, lays_eggs: bool):
        self.name = name
        self.group = group
        self.number_of_legs = number_of_legs
        self.number_of_wings = number_of_wings
        self.lays_eggs = lays_eggs

    def can_fly(self):
        return 'can' if self.number_of_wings > 0 else 'cannot'

    def description(self):
        return ('a {} belongs to the {} group, and {} fly').format(self.name, self.group, self.can_fly())
    

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name, group='Bird', number_of_legs=4, number_of_wings=2, lays_eggs= True)

class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name, group='Mammal', number_of_legs=4, number_of_wings=0, lays_eggs = False)

class Finch(Bird):
    def __init__(self, name):
        super().__init__(name)

class Penguin(Bird):
    def __init__(self, name):
        super().__init__(name)

    def can_fly(self):
        return 'cannot'

finch = Finch(name='finch')
print(finch.description())