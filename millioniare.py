def ask_question(question, answers, correct_answer):
    print question
    for answer in answers:
        print answer
    done = False
    while not done:
        response = raw_input('What is the answer?\n')
        if response == 'A' or response == 'B' or response == 'C' or response == 'D':
            if response == correct_answer:
                print 'Ding! Ding! Ding! Correct!\n'
                return True
            else:
                print 'Sorry! You lose.\n'
                return False
        else:
            print 'INVALID CHOICE!!!!  Choose A, B, C, or D'
            done = False

question = 'What is the capital of France?'
answers = ['A: London', 'B: Egypt', 'C: Paris', 'D: Moscow']
correct = ask_question(question, answers, 'C')

if correct:
    question = 'What food group will you find milk?'
    answers = ['A: Meat', 'B: Dairy', 'C: Vegetables', 'D: Grains']
    correct = ask_question(question, answers, 'B')
