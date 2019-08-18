import random
answer = random.sample(range(10), 4)
guess = []
count_times = 0

while guess != answer:
    a = int(input("What is your First guessing number? "))
    while a < 0 or a > 9:
        print("Please enter a number between 0 and 9")
        a = int(input("What is your First guessing number? "))
    b = int(input("What is your Second guessing number? "))
    while b < 0 or b > 9:
        print("Please enter a number between 0 and 9")
        b = int(input("What is your Second guessing number? "))
    c = int(input("What is your Third quessing number? "))
    while c < 0 or c > 9:
        print("Please enter a number between 0 and 9")
        c = int(input("What is your Third guessing number? "))
    d = int(input("What is your Forth guessing number? "))
    while d < 0 or d > 9:
        print("Please enter a number between 0 and 9")
        d = int(input("What is your Forth guessing number? "))
    guess = [a, b, c, d]
    count_cow = 0
    count_bull = 0
    for i in range(0, 4):
        for j in range(0, 4):
            if guess[i] == answer[j] and i == j:
                count_cow = count_cow + 1
            elif guess[i] == answer[j] and i != j:
                count_bull = count_bull + 1
    count_times = count_times + 1
    print("your guessing is", guess, ".")
    #print(answer)
    #print(count_cow)
    #print(count_bull)
    #print(count_times)
    print("There is %d cows and %d bulls, you have tried %d times." %(count_cow, count_bull, count_times))

print("you got the right answer!")
