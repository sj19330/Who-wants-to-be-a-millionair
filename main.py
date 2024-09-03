import random

def parser(filename): 
    with open(filename) as file: 
        questions= []
        for line in file: 
            split_line = line[:-1].split(' : ')
            correct_answer = split_line[1]
            answers = split_line[1:]
            question = split_line[0]
            questions.append([question, correct_answer, answers])

        return questions


def question_former(questions):
    question_indexes = random.sample(range(0, len(questions)), 5)
    question_list = [questions[index] for index in question_indexes]
    print(question_list)

def main():
    questions = parser('level1_questions.txt')
    question_former(questions)





main()