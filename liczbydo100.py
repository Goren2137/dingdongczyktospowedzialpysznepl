a = 0
for i in range(1, 100):
    if i % 15 == 0:
        print("FizzBuzz")
        a = a + 1
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
        a=a+1
    else:
        print(i)
print(a)
