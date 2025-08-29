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

# Score tracker
score = 0

# Loop through all quiz questions
for q in quiz:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)

    # Get user's answer
    user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

    # Check the answer
    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer was {q['answer']}.")

# Final score
print(f"\n🎉 You got {score} out of {len(quiz)} correct!")

# Show result message
if score == len(quiz):
    print("🏆 Excellent work!")
elif score >= len(quiz) // 2:
    print("👍 Good job!")
else:
    print("📚 Keep practicing!")