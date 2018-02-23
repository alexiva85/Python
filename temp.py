


def cus_range(to, from_=0,step = 1):
    while from_ <= to:
        yield from_
        from_+=step



def foo(x):
    x+=1
    return x

def mymap(func,list_):
    for i in list_:
        yield func(i)


my=mymap(foo, [1,2,3])

#print(list(my))

print(next(my))

print(next(my))

print(next(my))

# Павел, объясните, пожалуйста, что не так в варианте с объектом класса:
class MyMap:
    def __init__(self, func, list_):
        self.func = func
        self.list_ = list_

    def __next__(self):
        for i in self.list_:
            return self.func(i)  # тютор пишет, что проходит более 1000 шагов и останавливается, я так понимаю почему-то зацикливается.

    def __iter__(self):
        return self

my=MyMap(foo, [1,2,3])

print(list(my))



def MyEnumC (list_):
    for i in range(len(list_)):
        yield (i,list_[i])


class MyEnum:
    def __init__(self, list_):
        self.list_=list

    def __next__(self):
        for i in range(len(self.list_)):
            return (i, self.list_[i])

    def __iter__(self):
        return self
