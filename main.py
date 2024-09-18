from Game import Game

# main function
def main():
    game1 = Game('Michael')
    questions = game1.parser('level1_questions.txt')
    questions_objects = game1.question_former(questions)
    print(questions_objects)





main()