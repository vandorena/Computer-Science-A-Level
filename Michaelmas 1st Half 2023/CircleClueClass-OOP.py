class Circlequeue:
    def __init__(self,maxqueue):
        self.frontpointer = -1
        self.backpointer = -1
        self.fullqueue = maxqueue
        self.value = []
        for i in range (0,maxqueue):
            self.value.append(0)
        self.beginningcount = 0
    
    def queueappend(self,itemappend):

        if self.frontpointer == -1 and self.backpointer == -1:
            self.frontpointer = 0
            self.backpointer = 0
            self.value[self.backpointer] = itemappend
            print(f"Added first value of {itemappend}")
        else:
            if ((self.backpointer  + 1) % self.fullqueue) != 0:
                self.backpointer = (self.backpointer +1)% self.fullqueue
                self.value[self.backpointer] = itemappend
                print(f"added {itemappend}")
    
            else:
                print("Back to beginning of queue")
                self.backpointer = 0
                self.value[self.backpointer] = itemappend
                self.beginningcount = self.beginningcount + 1
        self.backpointer += self.backpointer


    def queuepop(self):
        if self.frontpointer == -1 and self.backpointer == -1:
            print("Queue is empty, cannot pop")
        else:
            newobject = self.value[self.frontpointer]
            if self.frontpointer == self.backpointer and self.beginningcount == 0:
                self.frontpointer = -1
                self.backpointer = -1
            elif self.frontpointer == self.backpointer and self.beginningcount != 0:
                self.frontpointer = 0
                print("Gone back one iteration")
                self.beginningcount = self.beginningcount -1 
            else:
                self.frontpointer = (self.frontpointer + 1) % self.fullqueue

newqueue = Circlequeue(3)
for i in range (0,4):
    newqueue.queueappend(i)
print(newqueue.value)
