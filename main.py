# importing module
from question import Question,get_questions

def main():
    questions=get_questions() # Funtion where our set of question and answer iies
    score =0
    incorrect_answer=[]
    for x in questions:
        print(x.question_text)         
        answe=input('Enter the answer please')

        if answe == 'quit':
            print('Quiz has been terminated')
            break 
        if answe == 'next':
            print('You skipped the question')
            continue

        if x.check_answer(answe):
            print('Correct answer')
            print('-'*50)
            score +=1
        else:
            print('Wrong!')
            incorrect_answer.append((x.question_text,x.correct_ans))
            print('-'*50)



    print(f'Your final score is {score}/{len(questions)}')

    if incorrect_answer:
        print(f'\nReview Your Wrong Answer')
        for question_text,correct_ans in incorrect_answer:
            print(f'Question: {question_text}')
            print(f'Answer: {correct_ans}')

if __name__ == '__main__':
    main()




