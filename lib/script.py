from capitals import states
import random
print("")
print("-----------------------------------")
print("Welcome to the State Capital Game!")
print("-----------------------------------")
print("")
print("When prompted with a state, please give us the state's capital.")
print("")


def play():
    random.shuffle(states)
    score = 0
    for i in range(len(states)):
        guess = str(
            input(f'{i+1}: What’s the capital of {(states[i]["name"])}? '))
        if guess == str(states[i]["capital"]):
            score += 1
            print(
                f' 🎉 Correct! +1 Point. Score is now {score}! 🎉')
        else:
            print(f"😕 Incorrect. Score is {score}!")
    print("--------------------------------------------")
    print(f"        Game Over. Final Score: {score}!")
    print("     Would you like to play again? Yes/No      ")
    play_again = str(input())
    if play_again == "Yes":
        play()
    else:
        print(" Goodbye! ")
        exit()


play()
