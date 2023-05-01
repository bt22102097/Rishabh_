#Answer 3
from random import randint
play=1
while play==1:
   a=randint(0,9)
   b=randint(0,9)
   print("the multiplication problem is" ,a ,"*", b)
   c=int(input("what is your guess?"))
   if c==a*b:
    print("this is correct")
   else:
        print ("this is not correct. The correct answer is", a*b)

   play=int(input("Enter 1 to play again or 0 to exit"))
else :
            print("thanks for playing")