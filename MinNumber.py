print("Сколько чисел хотите ввести?")
num = int(input())
count = 0

bd = []

while count <= num:
  num = int(input())
  bd.append(num)

  count += 1

print(bd)


def min_number(bd):
  bd_len = len(bd)
  counter = 0
  min_num = bd[counter]
  
  while counter < bd_len:
    if (bd[counter] < min_num):
      min_num = bd[counter]
    
    counter += 1
  
  print(min_num)

min_number(bd)
