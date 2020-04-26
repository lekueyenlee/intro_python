## an example of the doc class

# definition of the dog class
class dog: 
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type

    def bark(self):
        print("Woof")
    
    def run(self):
        print(self.name + " is running")

dog_one = dog("Randy", 5, "labrador")
print(dog_one.name)
dog_one.bark()
dog_one.run()

print("\r")

dog_two = dog("Lucy", 2, "chiwawa")
print(dog_two.name)
dog_two.run()
print(dog_two.type)
