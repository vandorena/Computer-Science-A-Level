class Animal:
    def __init__(self,state,size,animal,maxsize):

        self._state = state
        self._size = size
        self._animal = animal
        self._maxanimalsize = maxsize

    def feed(self):
        self._size += 1
        print (f"{self._animal} is fed")
        if self._size == self._maxanimalsize:
            self._state = "full"

    def poop(self):
        self._size = self._size - 2
        print(f"{self._animal} has pooped")
        if self._size <= 0:
            print(f"{self._animal} has died")