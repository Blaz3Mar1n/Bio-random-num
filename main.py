import random
import time

t1 = time.time()

def clear():
  for i in range(100):
    print()

txt = ""
for i in range(50):
    txt+=str(random.randint(0,9))

clear()
print('\033[1m' + txt + '\033[1m')

while True:
  if(time.time()- t1 > 10):
    clear()
    break

inp = input()

score = 0
counter = -1
for i in inp:
  counter+=1
  if(i == txt[counter]):
    score+=1
  else:
    break

clear()
print(score)
