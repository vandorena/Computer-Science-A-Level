from sys import getsizeof
def test_var(input):
    print(f"{input, type(input), getsizeof(input)} bytes")

test_var(1)
test_var("1")
test_var(1.00002)
test_var([1,2,3])