def quiz_message(grade):
    if grade < 60:
        outcome = 'failed'
    else:
        outcome = 'passed'
    print('You', outcome, 'the quiz with a grade of', grade)


grade1 = int(input('grade1 = '))
quiz_message(grade1)


def quiz_message(grade):
    outcome = 'failed' if grade < 60 else 'passed'
    print('You', outcome, 'the quiz with a grade of', grade)


grade2 = int(input('grade2 = '))
quiz_message(grade2)
