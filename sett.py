# banned_words = {'bad', 'spam', 'scam'}

# sen = input("ENTER YOUR SENTENSE :-  ").lower().split()
# sen_se = set(sen)
# for words in sen_se:
#     if words in banned_words:
#         print(f"you cant use banned words{banned_words}")
#         break
    
# else:
#     print(f"SENTENSE IS CLEAR") 
    

# choice = int(input("ENTER 1 FOR ADD 2 FOR REMOVE AND 3 FOR VIEW "))

# if choice == 1:
#     wor = input("ENTER WORDS").lower()
#     banned_words.add(wor)
#     print(banned_words)
# elif choice == 2:
#     wor = input("ENTER WORDS").lower()
#     banned_words.remove(wor)
# elif choice == 3:
#     print(f"banned words are{banned_words}")
# else:
#     print("NOTHING")


questions = [
    {
        'A': {1, 2, 3},
        'B': {2, 3, 4},
        'operation': 'union',
        'answer': {1, 2, 3, 4}
    },
    {
        'A': {5, 6, 7},
        'B': {6, 8, 9},
        'operation': 'intersection',
        'answer': {6}
    },
    {
        'A': {10, 20, 30},
        'B': {20},
        'operation': 'difference',
        'answer': {10, 30}
    }
]

score = 0

for q in questions:
    print(f"\nSet A = {q['A']}")
    print(f"Set B = {q['B']}")
    op = q['operation']
    print(f"What is A {op} B?")
    
    user_input = input("Enter your answer as comma-separated values (e.g. 1,2,3): ")
    user_set = set(map(int, user_input.split(',')))
    
    if user_set == q['answer']:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Incorrect. Correct answer: {q['answer']}")

print(f"\n🎉 Your total score: {score} out of {len(questions)}")
