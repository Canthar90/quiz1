from question_model import QuizQuestion
from data import question_data
from quiz_brain import QuizBrain


question_bank = []


for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = QuizQuestion(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

# print(question_bank)
quiz=QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print(f"Sorry there is no more questions your score is {quiz.score}/{quiz.question_number}")