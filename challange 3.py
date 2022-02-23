guess=["guess a number"]
guess= int(guess(a))
n=0

while True:
    print("type q to quit")
    answer=input(guess[n])
    if answer== "q":
        break
    elif answer== 2:
        print("hurrreeyyy")
    else:
        print("guess")
