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

def format_answer_string(answers):
    return 'A.{}    B.{}    C.{}    D.{}'.format(answers[0], answers[1], answers[2], answers[3])

def format_answers(answers):
    random_indices = [0,1,2,3]
    random.shuffle(random_indices)
    correct_index = random_indices.index(0)
    correct_submition = ['A', 'B', 'C', 'D'][correct_index]
    shuffled_answers = [answers[index] for index in random_indices]
    answer_string = format_answer_string(shuffled_answers)
    return (answer_string, correct_submition)
    
def question_former(questions):
    question_indexes = random.sample(range(0, len(questions)), 5)
    question_list = [questions[index] for index in question_indexes]
    question_object_list = []
    for question in question_list:
        answer_string, correct_answer = format_answers(question[2])
        obj = {'question': question[0], 'answer string': answer_string, 'correct answer': correct_answer}
        question_object_list.append(obj)
    return question_object_list