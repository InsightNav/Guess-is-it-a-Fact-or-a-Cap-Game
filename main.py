import random
import os
import time
import sys
from game_engine import get_fact_pair


def slow_print(text, delay=0.01):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# skill i just picked up used as a test
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def start_game():
    score = 0
    streak = 0
    clear_screen()

    print("==========================================")
    print("   🤖  FACT OR CAP  🎯   ")
    print("==========================================")

    while True:
        print("\n⏳ generating...")
        real, fake = get_fact_pair()

        options = [real, fake]
        random.shuffle(options)
        correct = options.index(real) + 1

        print(f"\n🔥 streak: {streak} | 🏆 score: {score}")
        slow_print(f"1) {options[0]}")
        slow_print(f"2) {options[1]}")

        choice = input("\nPick the FACT (1/2 or q): ").strip().lower()

        if choice == 'q':
            print(f"\nfinal score: {score}")
            break

        if choice in ['1', '2']:
            if int(choice) == correct:
                print("\n✅ nice, that's true")
                score += (100 * (streak + 1))
                streak += 1
                time.sleep(1)
                clear_screen()
            else:
                print("\n❌ nope")
                print(f"\nFACT: {real}")
                print(f"CAP:  {fake}")
                print(f"\nscore: {score}")
                break
        else:
            print("enter 1, 2, or q")


if __name__ == "__main__":
    start_game()