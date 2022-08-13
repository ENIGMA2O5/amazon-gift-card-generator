import random
import time
try:
    import os
    from os import system
    system("title " + "ENIGMAS Amazon Giftcard Generator,   discord ENIGMA#0420")
except:
    pass
while True:
  save = input("Want to auto save as a txt file (y/n): ")
  if save == "y" or save == "n":
    break
  else:
    print("your a dumbass its TWO fucking letters pick one")
while True:
  try:
    amount = input("Amount Of Codes: ")
    amount = int(amount)
    break
  except Exception:
    print("pick a ANY FUCKIN number U STUPID")
while True:
  try:
    delay = input("Delay: ")
    delay = float(delay)
    break
  except Exception:
    print("your a dumbass CHOOSE A FUCKING NUMBER HOW DO YOU MESS THAT UP")
donegen = 0
choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
for i in range(int(amount)):
  r1 = random.choices(choices, k=15)
  code = "".join(r1)
  if save == "y":
    file = open("amazon_codes.txt", "a")
    file.write(code + "\n")
    file.close()
  donegen = int(donegen) + 1
  print("amazon codes->: " + str(code) + "    codes Generated-> : " + str(donegen))
  time.sleep(float(delay))
print("click somthing to exit")
input("")
exit()
