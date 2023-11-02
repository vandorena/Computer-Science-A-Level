from sys import getsizeof
def test_var(input):
    print(f"{input, type(input), getsizeof(input)} bytes")

test_var(1)
test_var("1")
test_var(1.00002)
test_var([1,2,3])
listbig = []
for i in range(0,1000):
    listbig.append(i)
    test_var(listbig)