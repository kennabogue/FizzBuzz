#FizzBuzz Challenge
#Kenna Bogue


print('FizzBuzz Challenge')
print('----------------------------------')
    
FizzBuzz = ["FizzBuzz" if (i%3 == 0 and i %5 == 0) else "Fizz" if (i%3 == 0) else "Buzz" if (i%5 == 0) else i for i in range(1,101)]
for i in FizzBuzz:
    print(i)
