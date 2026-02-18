class Person:
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def talks(self):
        print(f"A person talks always")              

person1 = Person("Hillary",30,"hinchjack08@gmail.com")
print(type(person1))
person1.display_info()

person2 = Person("Job",25,"job@outlook.mail")
person2.display_info()
person2.talks()

