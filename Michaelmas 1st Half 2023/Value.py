class Value:
    def __init__(self, val):
        self._value = val

    def __add__(self,other):
        new_object = Value(self._value +other.value)
        return new_object
    
x = Value(3)
y = Value(4)

z = x + y
print(z._value)