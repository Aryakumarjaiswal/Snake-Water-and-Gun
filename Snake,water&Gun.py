import random
print("Welcome To Snake,Water&Gun Game:")
print("0 --> Water\n 1 --> Snake\n 2 --> Gun")
a=random.randint(0,2)
b=int(input("Enter number b/w 0 to 2 inclusively: "))
if(b!=0 and b!=1 and b!=2 ):
    print("Please Enter Valid Number!!")
else:
    print("You: ",b)
    print("Computer ",a)
    if a==b:
        print("Both Win😊")

    elif b==1 and a==0:
        print("You Win👍")
    
    elif b==0 and a==2:
        print("You Win👍")

    elif b==2 and a==1:
        print("You Win ❤️")
    else:
        print("You Lossed:((")

