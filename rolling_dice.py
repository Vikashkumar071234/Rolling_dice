import random
print("Best of luck for your game.")
random_integer=random.randint(1,6)
print(random_integer)
if random_integer==1:
    print("Worst")
elif random_integer==2:
    print("good")
elif random_integer==3:
    print("very good")
elif random_integer==4:
    print("Excellent")
elif random_integer==5:
    print("ouststanding")
else:
    print("Marvellous")