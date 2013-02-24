class Dog():
    def __init__(self,dogname,dogcolor,dogheight,dogbuild,dogmood,dogage):
        self.name = dogname
        self.color = dogcolor
        self.height = dogheight
        self.build = dogbuild
        self.mood = dogmood
        self.age = dogage
        self.Hungry = False
        self.Tired = False
    
    def Eat(self):
        if self.Hungry:
            print 'Yum Yum...Num Num'
            self.Hungry = False
        else:
            print 'Sniff Sniff...Not Hungry'
    
    def Sleep(self):
        print 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZ'
        self.Tired = False
        
    def Bark(self):
        if self.mood == 'Grumpy':
            print 'GRRRRR...Woof Woof'
        elif self.mood == 'Laid Back':
            print 'Yawn...ok...Woof'
        elif self.mood == 'Crazy':
            print 'Bark Bark Bark Bark Bark Bark Bark'
        else:
            print 'Woof Woof'

Beagle = Dog('Archie','Brown','Short','Chubby','Grumpy',12)
Lab = Dog('Nina','Black','Medium','Heavy','Laid Back',7)
Heeler = Dog('Bear','Black','Tall','Skinny','Crazy',9)

print 'My Name is %s' % Lab.name
print 'My Color is %s' % Lab.color
print 'My Mood is %s' % Lab.mood
print 'I am hungry = %s' % Lab.Hungry
Lab.Eat()
Lab.Hungry = True
Lab.Eat()
Lab.Bark()
