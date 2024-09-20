# Quiz Program

This is a simple Python-based quiz program that asks multiple-choice questions and checks the user's answers. The program keeps track of the user's score and allows them to review any incorrect answers at the end. Additionally, the user has the option to quit the quiz at any time.

## Features
- User-friendly quiz that asks questions one at a time.
- Keeps track of correct and incorrect answers.
- Allows users to quit the quiz at any point by typing "quit".
- At the end, users can review the questions they answered incorrectly.

## How to Run the Program

1. Ensure Python is installed on your system (preferably Python 3.x).
2. Save the following files:
    - `main.py`: The main Python file that contains the quiz logic.
    - `question.py`: A file that contains the `Question` class and `get_questions()` function to define your questions.

3. To run the quiz, open your terminal or command prompt and navigate to the directory where the files are saved. Then, run the program:

    ```bash
    python main.py
    ```

## File Structure

- `main.py`: Contains the main logic for the quiz.
- `question.py`: Contains the `Question` class definition and the `get_questions()` function, which returns a list of questions.

### Example of `question.py`

```python
class Question:
    def __init__(self, question_text, correct_ans):
        self.question_text = question_text
        self.correct_ans = correct_ans

    def check_answer(self, answer):
        return answer.lower() == self.correct_ans.lower()

def get_questions():
    return [
        Question("What is the SI unit of force? (One word)", "Newton"),
        Question("What is the rate of change of velocity called? (One word)", "Acceleration"),
        Question("What type of wave is sound in air? (One word)", "Longitudinal"),
        # Add more questions here
    ]
