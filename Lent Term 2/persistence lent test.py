print("Enter integer (0-99):")
value = int(input())
print("Calculate additive or multiplicative persistence( a or m)")
choice = input("a or m: ")
count = 0
while value > 9:
    if choice == "a":
        value = (value//10) + (value%10)
    else:
        value = (value//10) * (value%10)
    count += 1
print("The persistence is:")
print(count)