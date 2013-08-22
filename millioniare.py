def ask_question(question, answers, correct_answer):
    print question
    for answer in answers:
        print answers
    done = False
    while not done:
        response = raw_input('What is the answer?\n')
        if response == 'A' or response == 'B' or response == 'C' or response == 'D':
            if response == correct_answer:
                return True
            else:
                return False
        else:
            print 'INVALID CHOICE!!!!  Choose A, B, C, or D'
            done = False

print 'What is the capital of France?'
print 'A: London'
print 'B: Egypt'
print 'C: Paris'
print 'D: Moscow'
done = False
correct = False
while not done:
    response = raw_input('What is the answer?\n')
    if response == 'A':
        print 'You are wrong!'
        done = True
    elif response == 'B':
        print 'Eqypt is not even a city, so you are wrong!'
        done = True
    elif response == 'C':
        print 'You are CORRECT!!! Ding ding ding!!!'
        done = True
        correct = True
    elif response == 'D':
        print 'Moscow? Really? You are wrong!'
        done = True
    else:
        print 'INVALID CHOICE!!!!  Choose A, B, C, or D'
        done = False
if correct:
    print 'What food group will you find milk?'
    print 'A: Meat'
    print 'B: Dairy'
    print 'C: Vegetables'
    print 'D: Grains'
    done = False
    while not done:
        response = raw_input('What is the answer?\n')
        if response == 'A':
            print 'Buzz! Wrong!'
            done = True
        elif response == 'B':
            print 'Ding ding ding!!! Correct!!'
            done = True
        elif response == 'C':
            print 'Milk does not come from a plant. You are wrong.'
            done = True
        elif response == 'D':
            print 'Definitely not.  You are wrong.'
            done = True
        else:
            print 'INVALID CHOICE!!!!  Choose A, B, C, or D'
            done = False
