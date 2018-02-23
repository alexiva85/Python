class Fruits:
    def __init__(self, taste, color, volume = 1):
        self.color = color
        self.taste = taste
        self.volume = volume


apple = Fruits('sweet','red',)
orange = Fruits('sweet','orange',)
class Bag:
    items = []
    def __init__(self, capacity):
        self.capacity = capacity
    def putin (self, item):
        self.items += [item]
        print (item.volume)

    #def cmeth(cls,x):
     #   print (cls,x)

   # cmeth = classmethod(cmeth)


b=Bag(10)

b.putin(apple)



def qwargs(*args,**qwargs):
    for i in args:
        print (type(i), i)
    for i in qwargs:
        print (type(i), qwargs[i])





class Field(object):
    def __init__(self,h,w):
        self.h=h
        self.w=w
        self.field = w*[0]
        for i in range(len(self.field)):
            self.field[i] = [0]*h


    def display(self):
        for i in range(len(self.field)):
            for j in range(len(self.field)):
                print (self.field[i][j], end = '')
            print('\n')

f=Field(5,5)

f.display()





a = input('Введите строку:')
if list(filter(lambda x: x not in a, 'абвгдежзиклмнопрстуфхцчшщъыьэюя')) == []:
    print ('Строка является полиндромом.')
else:
    print ('До полиндрома не хватает: ', list(filter(lambda x: x not in a, 'абвгдежзиклмнопрстуфхцчшщъыьэюя'))




def switch(enabled=True):
    print(1)
    def action_decorator (func):
        print(2)
        counter = []
        def inner(*args, **qwargs):
            print(3)
            if len(counter) == 0 and enabled is True:
                print ('Action decorated!')
                result = func(*args,**qwargs)
                counter.append(1)
                return result
            else:
                result = func(*args, **qwargs)
                return result
        return inner
    return action_decorator

@switch()
def sum(x,y):
    return x+y

#sum = action_decorator(sum)

print(sum(4,5))
print(sum(4,5))


class Basket:
    def __init__(self, **items):
        self.item = []
        self.capacity = []
        self.fact = []
        for item in items:
            self.item += [item]
            self.capacity += [items[item]]
            self.fact += [0]
        print('New Basket created')
    def put(self, item, quantity):
        if item in self.item:
            for i in range(len(self.item)):
                if item == self.item[i]:
                    if self.fact[i]+quantity <= self.capacity[i]:
                        self.fact[i]+=quantity
                    else:
                        raise ValueError('No free space available')
        else:
            raise TypeError("No such item allowed")




class Fruits:
    def __init__(self, taste, color):
        self.color = color
        self.taste = taste


apple = Fruits('sweet','red')

orange = Fruits('sweet','orange')


b = Basket(apple = 2, orange = 3, some =6)

print(b.item)
print(b.capacity)
print(b.fact)

b.put('apple',1)

print(b.item)
print(b.capacity)
print(b.fact)

b.put('orange',3)

print(b.item)
print(b.capacity)
print(b.fact)


class Cars:
    speed = 0
    def acc(self):
        self.speed += 10
    def acc_param(self, value):
        self.speed += value


car1 = Cars()

print(car1.speed)

car1.acc()

car1.acc_param(15)

print(car1.speed)

class Door:
    def open(self):
        self.opened

d1 = Door()

Door.open(d1)  == d1.open()



class Cars
    speed = 0
    def __init__(self, color, transmission = 'auto'):
        self.color = color
        self.transmission = transmission



people = {'Alice': {'phone': '2341', 'addr': 'Foo drive 23' },
          'Beth':  {'phone': '9102', 'addr': 'Bar street 42'}}
name = 'Alice'
key = 'phone'
if name in people:
  print "%s phone is %s" % (name, people[name][key])
>>> Alice phone is 2341



def some_i(x):
    print('privet',x)

some_i(2)


def outer (value):
    return some_i

outer(23)(24)


________________
def cus_range(to, from_=0,step = 1):
    while from_ <= to:
        yield from_
        from_+=step


class MyMap:
    def __init__(self, func, list_):
        self.func = func
        self.list_ = list_

    def __next__(self):
        for i in self.list_:
            return self.func(self.list_[i])

    def __iter__(self):
        print('sozdali')
        return self
