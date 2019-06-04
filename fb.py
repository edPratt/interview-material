# print all numbers up to n
# if n is multiple of 3 print fizz
# if n is multiple of 5 print buzz
# if n is multiple of 3 and 5 print fizzbuzz
def fizz_buzz(n):
    for number in xrange(n+1):
        if (number % 3 == 0 and number % 5 == 0):
            print(number, "fizzbuzz")
        elif (number % 3 == 0):
            print(number, "fizz")
        elif (number % 5 == 0):
            print(number, "buzz")
        else:
            print(number)

if __name__ == "__main__":
    fizz_buzz(100)
