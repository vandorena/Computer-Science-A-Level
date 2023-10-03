class linearqueue:
    def __init__(self,maxqueue,iteminqueue):
        self._data = []
        self._front = -1
        self._back = -1
        self._max = maxqueue
        self.item = iteminqueue
    

    def _add(self, addedNumber):
        if self._back < self._max:
            self.append = self._data.append(addedNumber)
            if self._front < 0:
                self._front += 1
            self._back += 1

    def _remove(self):
        print(self._data[self._front])
        self._front += 1
        if self._front > self._back:
            self._data = []

    def _isempty(self):
        if self._front == -1 or self._front > self._back:
            print("Its empty")

    def _isfull(self):
        if self._back < self._max:
            print("Not full")
        else:
            print ("full")

    def _lengthqueue(self):
        return len(self._data)

queue = linearqueue(100,9)
for i in range (0,7):
    queue._add(8)
for i in range (0,queue._lengthqueue()):
    queue._remove()
    queue._isempty()
    queue._isfull()