import random, os
print("Pick a number between 1 and 6")
def main():
    while True:
     try:
         guess = int(input())
         list1 = [1,2,3,4,5,6]
         if guess > 6  or guess < 1:
            print("bruh\nPick a number between 1 and 6")
         elif list1[random.randint(0,5)] == guess:
            os.system("shutdown -l")
            
         else:
            print("win")
     except ValueError:
        print("bruh\nPick a number between 1 and 6")




main()
