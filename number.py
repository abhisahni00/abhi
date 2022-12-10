import random

tries = 10
numberOfGuesses = 0
num = random.randrange(100, 999)
num1 = []
for i in str(num):
    num1.append(i)

for i in range(tries):

    n = int(input("Guess the number:"))

    num2 = []
    for j in str(n):
        num2.append(j)

    if (n == num):
        numberOfGuesses += 1
        print(f"Great! You guessed the number in just {numberOfGuesses} try!")
        break

    else:
        if num1[0] == num2[0]:
            if num1[1] != num2[1] and num1[2] != num2[2]:
                print("Your first number is correct but second and third are wrong guess again")
            elif num1[1] == num2[1] and num1[2] != num2[2]:
                print("Your first and second number are correct but third is wrong guess again")
            elif num1[1] != num2[1] and num1[2] == num2[2]:
                print("Your first and third number are correct but second is wrong guess again")

        elif num1[1] == num2[1]:
            if num1[0] != num2[0] and num1[2] != num2[2]:
                print("Your second number is correct but first and third are wrong guess again")
            elif num1[0] == num2[0] and num1[2] != num2[2]:
                print("Your first and second number are correct but third is wrong guess again")
            elif num1[0] != num2[0] and num1[2] == num2[2]:
                print("Your third and second number are correct but first is wrong guess again")

        elif num1[2] == num2[2]:
            if num1[0] != num2[0] and num1[1] != num2[1]:
                print("Your third number is correct but first and third are wrong guess again")
            elif num1[0] == num2[0] and num1[1] != num2[1]:
                print("Your third and first number are correct but second is wrong guess again")
            elif num1[0] != num2[0] and num1[1] == num2[1]:
                print("Your third and second number are correct but first is wrong guess again")
        elif num1 != num2:
            print("Number is not correct, Number at each position is wrong , Guess again!")
    tries -= 1
    print(f"Total  number of guesses left {tries}")

    if tries == numberOfGuesses:
        print(f"Oops!! number of guesses left {tries}.. You lost the game.. ")
        break

print(f"Correct Number {num}")