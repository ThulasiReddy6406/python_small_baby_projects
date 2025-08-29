quiz = [
    {
        "question": "1. What is the capital of France?",
        "options": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
        "answer": "C"
    },
    {
        "question": "2. Who wrote 'Romeo and Juliet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. J.K. Rowling"],
        "answer": "B"
    },
    {
        "question": "3. What is the largest planet in our Solar System?",
        "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "4. Which language is primarily used for Android development?",
        "options": ["A. Python", "B. Swift", "C. Java", "D. C#"],
        "answer": "C"
    },
    {
        "question": "5. What does CPU stand for?",
        "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Computer Power Unit", "D. Control Processing Unit"],
        "answer": "B"
    }
]

scores = 0 

for q in "questons":
    print("\n", q["questions"])
    for op in "options":
        print(op["options"])

ans = input("enter your answer")
if ans == op["options"]:
    print("nice")
    scores+=1
else:
    print("wrong")