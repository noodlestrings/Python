# https://www.youtube.com/watch?v=JeznW_7DlB0
# 9:55
class Dog:
    def bark(self):
        print("bark")

    def meow(self):
        return "hey you can't do that"

    def add_one(self, x):
        return x + 1


d = Dog()  # instantiating new instance of class dog. D is object of class dog
print(type(d))  # <class '__main__.Dog'>

d.bark()

tryToMeow = d.meow()
print(tryToMeow)

print(d.add_one(68))
