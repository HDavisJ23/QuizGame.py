print("Welcome to Quiz of Knowledge \n")

a = "Sparta"
b = "Athens"
c = "Nafplio"

score = 0

correct_answer = 'b'

question = ("1.What is the capital of Greece?")
print(question)
print(f'\na. {a}')
print(f'b. {b}')
print(f'c. {c}')

user_answer = input("\nWhat is you answer? (Please enter a, b or c) \n")
if user_answer == correct_answer :
    print("\nCongradulations smart guy")
    score = score + 10
else:
    print("\nWhat a shame you low life do better :(.")
    
print(f"\nScore:{score}")






print("\n2.What is the capital of Delaware?\n")

print("a. Delmar\n")
print("b. Dover\n")
print("c. Willmington\n")

answer_1 = 'a'
answer_2 = 'b'
answer_3 = 'c'
correct_answer = 'b'

user_answer = input("what is your answer? (Please enter a, b or c)\n")

if user_answer == correct_answer:
    print("\nDang slow down your to smart.")
    score = score + 10
else:
    print("\nyour kinda slow pal")




print("\n3. Final question: who always say's LOVE YA")

print("\na. Gmom Sylvia")
print("\nb. Gmom Slim")
print("\nc. Momma Mims")

answer_1 = 'a'
answer_2 = 'b'
answer_3 = 'c'

correct_answer = 'a'

user_answer = input("what is your answer? (Please enter a, b or c)\n")
if user_answer == correct_answer:
    print("\nGoodness you know I love smart ones :) ")
    score = score + 10
else:
    print("\nyou disgust me")

print(f"\nFINAL SCORE:{score}")










      

