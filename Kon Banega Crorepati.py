import random
from termcolor import cprint

QUESTION = "question"
OPTIONS = "options"
ANSWER = "answer"

def ask_question(index, question, options):
  print(f"Question {index}: {question}")
  for option in options:
    print(option)

  return input("Your answer: ").upper().strip()  

def run_quiz(quiz):
  random.shuffle(quiz)

  score = 0

  for index, item in enumerate(quiz, 1):
    answer = ask_question(index, item[QUESTION], item[OPTIONS])

    if answer == item[ANSWER]:
      cprint("Correct!", "green")
      score += 1
    else:
      cprint(f"Wrong! The correct answer is {item[ANSWER]}", "red")
    
    print()

  print(f"Quiz over! Your final score is {score} out of {len(quiz)}")


def main():  
  quiz = [
    {
      QUESTION: "What is the capital of France?",
      OPTIONS: ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
      ANSWER: "C"
    },
    {
      QUESTION: "Which planet is known as the red planet?",
      OPTIONS: ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
      ANSWER: "B"
    },
    {
      QUESTION: "What is the largest ocean on Earth?",
      OPTIONS: ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"],
      ANSWER: "D"
    },
    {
        QUESTION: "Which god is also known as ‘Gauri Nandan’? ",
        OPTIONS:["A. HANUMAN", "B. Ganesh", "C. Ram", "D. Krishna" ],
        ANSWER: "B"
    },
    {
        QUESTION: "The fine step-well complex of 'Agrasen ki Baoli' is located at",
        OPTIONS: ["A. Gwalior", "B. Jodhpur","C. New Delhi", "D. Amritsar"],
        ANSWER: "C"
    },
    {
        QUESTION: "Which one of the following places is famous for the Great Vishnu Temple?",
        OPTIONS: ["A. Bordubar, Indonesia", "B. Bamiyan, Afghanistan","C. Panja Sahib, Pakistan", "D. Ankorvat, Cambodia"],
        ANSWER: "D"
    },
    {
        QUESTION: "Where is the largest Buddhist Monastery in India located?",
        OPTIONS: ["A. Sarnath, Uttar Pradesh","B. Tawang, Arunachal Pradesh","C. Gangtok, Sikkim","D. BODH GAYA, Bihar"],
        ANSWER: "B"
        
    },
    {
        QUESTION: "Which Indian monument was originally built as a victory tower to commemorate the defeat of the Khan of Khambhat?",
        OPTIONS: ["A. Qutub Minar","B. India Gate ","C. Charminar", "D. Vijay Stambha"],
        ANSWER: "D"
    },
    {
        QUESTION: "Who was the first Indian woman to win a medal in the Olympics?",
        OPTIONS: ["A. P.T. Usha","B. Kunjarani Devi","C. Bachendri Pal","D. Karnam Maleshwari"],
        ANSWER: "D"
    },
  ]  
  run_quiz(quiz)

if __name__ == "__main__":
  main()