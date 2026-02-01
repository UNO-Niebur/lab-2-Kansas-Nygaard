#Magic8Ball.py
#Name: Kansas Nygaard 
#Date: 02/01/2026
#Assignment: Lab 2: Magic 8 Ball 

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  answers = ["yes", "no", "Its too hard to tell", "theres a high possibility", "very doubtful", "signs point to yes", "concentrate and ask again", "undetermined at this time"]
  #Prompt the user for their question.
  question = input("Ask a yes or no question: ")

  #Answer question randomly with one of the options from your earlier list.
  response = random.choice(answers)
  print("Magic 8 Ball says:", response) 


if __name__ == '__main__':
  main()
