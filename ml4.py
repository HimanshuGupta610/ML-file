import random

def main():
    print("Welcome to Coin Toss Simulator")
    
    while True:
        input("\nPress Enter to toss the coin...")
        outcome = random.randint(1, 2)
        if (outcome== 1):
            print("You got: Heads")
        else:
            print("You got: Tails")
        
        choice = input("Toss again? (y/n): ").lower()
        if choice != 'y':
            print("Thanks for playing!")
            break
main()
