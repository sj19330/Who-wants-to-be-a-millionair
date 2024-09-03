import helper_functions as hf

def main():
    questions = hf.parser('level1_questions.txt')
    questions_objects = hf.question_former(questions)
    print(questions_objects)





main()