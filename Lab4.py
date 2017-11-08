class Animal(object):
    def __init__(self,sound,name,age,favorite_beast):
        self.sound = sound
        self.name = name
        self.age = age
        self.favorite_beast = favorite_beast
    def talk(self):
        print(self.sound)
    def eat(self, food):
        print(self+" "+food+" "+"yamy")
    def description(self):
        print(self.name + "is" +self.age +"year old and loves clones "+self.favorite_color)
naruto=Animal("i am going to be the next hokage"+" "+"kazebonshin nu gotso","uzomaki_naruto",17,"kubi")
naruto.talk()
naruto.eat("ramen")
