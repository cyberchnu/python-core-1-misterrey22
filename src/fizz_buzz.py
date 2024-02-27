def fizz_buzz(param):
  #Type your code here
  result = ""
  if param % 3 == 0:
    result += "Fizz"
  if param % 5 == 0:
    result += "Buzz"
  if not result:
    result = str(param)
  return result

print(fizz_buzz(10))  #Виведе "Buzz"
print(fizz_buzz(6))   #Виведе "Fizz"
print(fizz_buzz(15))  #Виведе "FizzBuzz"
print(fizz_buzz(7))   #Виведе число 7