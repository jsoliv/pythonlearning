print("Welcome to the rollercoaster!!!")
height = int(input("What is your height in cm? "))

if height >=120:
    print("You can ride the rollercoaster!")
    idade = int(input("What is your age? "))
    if idade <=18:
        print("Please pay $7.")
    else:
        print("You age is above 18, please pay $10.")
    
else:
    print("Sorry, you cannot ride the rollercoster yet")