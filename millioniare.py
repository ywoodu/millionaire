print 'What is the capital of France?'
print 'A: London'
print 'B: Egypt'
print 'C: Paris'
print 'D: Moscow'
done = False
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
    elif response == 'D':
        print 'Moscow? Really? You are wrong!'
        done = True
    else:
        print 'INVALID CHOICE!!!!  Choose A, B, C, or D'
        done = False
