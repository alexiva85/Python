import time
from functools import reduce

#декоратор, который замеряет время выполнения функций, который можно отключать и который кэширует и выдает из кэша результат

def switch(enabled=True):
    def action_decorator (func):
        #counter = []
        previous_results = {}
        def inner(*args):
            #if len(counter) == 0 and enabled is True:
            if enabled is True:
                print ('Action decorated!')
                if args not in previous_results.keys():
                    start_time = time.time()
                    result = func(*args)
                    stop_time=time.time()
                    #counter.append(1)
                    print ('Running time is: ',stop_time-start_time)
                    previous_results.update({args:result})
                    #previous_results.update({kwargs: result})
                    print('Result cached:', func,  args, '=' , previous_results[args])
                else:
                    print('From cache!!!')
                    start_time = time.time()
                    result = previous_results[args]
                    stop_time = time.time()
                    # counter.append(1)
                    print('Running time is: ',stop_time - start_time)

                return result
            else:
                result = func(*args)
                return result
        return inner
    return action_decorator

@switch()
def sum(x,y):
    return x+y


@switch()
def incr(x):
    result = reduce(lambda a,b: a*b, range(1,x))
    return result

#sum = action_decorator(sum)
#
# print(sum(4,5))
#
# print(sum(4,5))
#
# print(sum(1241241241242352351351235,123124122235252354))
#
# print(sum(1241241241242352351351235,123124122235252354))
#
# print(incr(10))

print(incr(100))

print(incr(10))

print(incr(100))

#декоратор, который проверяет тип данных функуции с заданными
def switch(*types):
    def action_decorator (func):
        def inner(*args,**kwargs):

            check = []    # список для проверки типов

            for i in args:
                print(type(i))  # для нагладности выводим тип аргументов
                if type(i) in types:
                    check.append(True)
                else:
                    check.append(False)
            for i in kwargs:
                print(type(kwargs[i])) # для нагладности выводим тип значений словаря
                if type(kwargs[i]) in types:
                    check.append(True)
                else:
                    check.append(False)
            for i in kwargs.keys():
                print(type(i))  # для нагладности выводим тип аргументов
                if type(i) in types:
                    check.append(True)
                else:
                    check.append(False)

            print(check)

            if False not in check:
                print ('Action decorated!')
                result = func(*args,**kwargs)
                return result
            else:
                print('Wrong type!')
                raise TypeError('WRONG TYPE')

        return inner
    return action_decorator

@switch(int, float, str)
def all_together(value, *args, **kwargs):
    message = kwargs.pop('message', 'default message')
    print(message)


all_together(1, 0.5)
all_together(1, 2.5, 3.5, 4)
all_together(5, 1, 1, 2, message='Done!')