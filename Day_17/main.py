#Day 17 Instagram Profile

# class User:
#
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
# user_1 = User("001", "Angela")
# user_2 = User("002", "Apru")
#
# user_1.follow(user_2)
#
# print(user_2.username)
# print(user_2.followers)


#Day 17 Quiz Game App OOP

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

# for i in range(len(question_data)):
#     # print(i)
#     # print(question_data[i])
#     text = question_data[i]["text"]
#     ans = question_data[i]["answer"]
#     # print(text,ans)
#     question_object = Question(text,ans)
#     question_bank.append(question_object)

for i in question_data:
    question = i["text"]
    answer = i["answer"]
    question_object = Question(question,answer)
    question_bank.append(question_object)

quiz = QuizBrain(question_bank)
#
# switch = True
#
# if switch:
while quiz.still_has_questions():
    quiz.next_question()


print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")





