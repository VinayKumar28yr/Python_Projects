import random 

while True:
  choice = input("Want to Roll the dice? (y/n): ")
  if choice == 'y':
      die = random.randint(1, 6)
     # die2 = random.randint(1, 6)
      print("Your output is : ",die)
  elif choice == 'n':
      print('Thanks for playing!')
      break
  else:
      print('Invalid choice!')
      
      
      
