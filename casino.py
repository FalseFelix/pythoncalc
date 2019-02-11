secret=42
guess=int(input("guess a number between 1 and 99: "))
if guess==secret:
    print("yay")
elif guess>99:
    print("u stupid dump")
else:
    print("wrong")