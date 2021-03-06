class Person():
    def set_name(person, name):
        if len(name) >= 2:
            person.name = name

woman = Person()
woman.set_name('Juliana')
print(woman.name)