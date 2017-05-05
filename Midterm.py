# The queue ADT
class queue:
    def _init_(self):                # Create a new empty queue
        self.items = []

    def is_empty(self):
        return self.items ==[]      # Test whether the queue is empty

    def enqueue(self,item):
        self.items.insert(0,item)    # adds a new item to the rear of the queue.

    def dequeue(self):
        return self.items.pop()     # Removes the front item from the queue

    def size(self):
        return len(self.items)      # Returns the number of items in the queue


# Cars lined up at a car wash
# New car arrives in line on average every 10 minutes
# It takes 15 minutes to wash a car before another car can wash

import random


class car(object):
    def __init__(self, num, current_time):
        self.arrive_time = current_time
        self.num = num

    def getarrivetime(self):
        return self.arrive_time

    def getcarnum(self):
        return self.num


class carwash(object):
    def __init__(self):
        self.arrivals = quene()
        self.wait_times = []
        self.car_count = 1
        self.busy = False
        self.washtimer = 1

    def addcar(self, current_time):
        self.arrivals.enqueue(car(self.car_count, current_time))
        self.car_count += 1

    def finished(self, current_time):
        p = self.arrivals.dequeue()
        self.addwaittime(current_time, p.getArriveTime())
        self.busy = True

    def addwaittime(self, current_time, arrive_time):
        self.wait_times.append(current_time - arrive_time)

    def iswashlinebusy(self):
        return self.busy

    def clearwashline(self):
        if self.washtimer == 15:
            self.busy = False
            self.washlinetimer = 1
        self.washlinetimer += 1

    def waitingtowash(self):
        return self.arrivals.size()


def randomarrival(arrival_num):
    chance = random.randrange(1, arrival_num + 1)
    return chance == 10


def carline_simulation(time):
    a = carwash()
    current_time = 0
    while current_time < time:
        current_time += 1
        if randomarrival(10):
            a.addcar(current_time)
        if a.waitingtowash() > 0:
            if not a.iswashlinebusy():
                a.finished(current_time)
            else:
                a.clearwashline()
    return a.wait_times, a.waitingtowash()



# Limit stack’s capacity to maxlen elements
class Empty(Exception):
    pass
class ArrayStack(object):

    if len(self) >= maxlen:
        print 'Stack Overflow!'

    def __init__(self):
         self.items = []

    def size(self):
         return len(self.items)

    def push(self, item):
        self.items.insert(0, item)

    def isEmpty(self):
        return self.items == []

    def top(self):
        return self.items[0]

    def pop(self):
        return self.items.pop(0)

    def Full(self):
        if len(self) == maxlen:
            return ('Stack is anomally')


S = ArrayStack()
S.push('hello')
S.push('true')
print S.pop()
