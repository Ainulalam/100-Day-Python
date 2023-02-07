import random  
print("This is Head and Tail game")

choice=int(input("Enter the h or 1 for head && t or 2 for tail "))

bot=int(random.randint(1,2))

if((choice=='h' or choice=='1') and bot==1):
  print("You Won")
  print("computer= head")
  print("your choice = head")
else:
  print("you loose")