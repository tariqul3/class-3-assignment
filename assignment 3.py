###3
#For each multiple of 3, print

for i in range(100):
    if i%3 == 0:
        print("Fizz" )
    elif i%5 == 0:
        print("Buzz")
    elif i%3==0 and i%5 == 0:
        print("FizzBuzz" )
    else:print(i)

