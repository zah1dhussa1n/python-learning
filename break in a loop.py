question=["what is your name","what is your favt game","what is your father name"]
n = 0
while True:
    print("type q to quit")
    answer = input(question[n])
    if answer == "q":
        break
    n+=1
    if n>2:
        n=0
