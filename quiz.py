# Simple Quiz Game

print("--- Welcome to the Quiz ---")

# Question 1
answer1 = input("1. What is the capital of France? ").strip().lower()
if answer1 == "paris":
    print("Correct!")
else:
    print("Wrong! The answer is Paris.")

# Question 2
answer2 = input("2. What is 5 + 7? ").strip()
if answer2 == "12":
    print("Correct!")
else:
    print("Wrong! The answer is 12.")

# Question 3
answer3 = input("3. Which language are we using? ").strip().lower()
if answer3 == "python":
    print("Correct!")
else:
    print("Wrong! The answer is Python.")

# Question 4
answer4 = input("4. Which symbol is used for comments in Python? ").strip()
if answer4 == "#":
    print("Correct!")
else:
    print("Wrong! The answer is #.")

# Question 5
answer5 = input("5. What is 10 / 2? ").strip()
if answer5 == "5" or answer5 == "5.0":
    print("Correct!")
else:
    print("Wrong! The answer is 5.")


print("--- Quiz Finished! ---")
