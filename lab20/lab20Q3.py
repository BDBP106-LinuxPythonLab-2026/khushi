# 3. Guess the Number
# Concepts: "until" loop (while True + break), if, counters
# Store a secret number between 1 and 50. Keep asking the user to guess until they get it
# right. After each wrong guess, print "Too high" or "Too low". When they get it, print how
# many attempts it took. As a bonus, stop after 7 attempts and reveal the number.

secret = 17
attempts = 0

while True:
    guess = int(input("Guess the number (1-50): "))
    attempts += 1

    if guess == secret:
        print("Correct! You guessed it in", attempts, "attempts.")
        break
    elif guess > secret:
        print("Too high")
    else:
        print("Too low")

    if attempts == 7:
        print("Game over! The secret number was", secret)
        break