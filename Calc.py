# Импорт библиотек
import time

# Функции, отвечающие за различные действия (сложение, вычитание, умножение, деление)
def addition(num1, num2):
  result = num1 + num2

  return result

def subtraction(num1, num2):
  result = num1 - num2

  return result

def multiplication(num1, num2):
  result = num1 * num2

  return result

def division(num1, num2):
  result = num1 / num2

  return result


print("Добро пожаловать в Калькулятор!")

count = 25

# Загрузка
for i in range(4):
  time.sleep(1)
  print("Загрузка...", count, "%")
  count += 25

time.sleep(0.6)

print("Введите два числа")

num1 = int(input())
num2 = int(input())


print("Введите действие с числами (+, -, *, /)")

symbol = input()
 
if (symbol == "+"):
  print(addition(num1, num2))

elif (symbol == "-"):
  print(subtraction(num1, num2))

elif (symbol == "*"):
  print(multiplication(num1, num2))

else:
  print(division(num1, num2))
