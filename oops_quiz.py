question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"}
]

class Quiz:
    def __init__(self,question,answer):
        self.question = question
        self.answer = answer

question_list = []
for que in question_data:
    q_que = que["text"]
    q_ans = que["answer"]
    q = Quiz(q_que,q_ans)
    question_list.append(q)

score = 0 
for que in question_list:
    print(que.question)
    ans = input("TRUE/FALSE").capitalize()
    if ans == que.answer:
        score+=1
    else:
        print(score ,"/",len(question_list))
        break  

