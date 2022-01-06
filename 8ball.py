import random
#Step 1 define who is asking a question
name = "Guido"
#Step 2 write the posed question
question = "Will I work for Google?"
#Step 3 intialize the answer from the 8 ball
answer = ""
#Step 4 and 5 import random and create a int which will contain a random int 1 to 9
random_number = random.randint(1,12)
#print(random_number)

#Steps 6, 7, and 8 writing the if/elif/else statement for each condition of the random 8ball number
if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "The Lord hath decideth - Yes."
elif random_number == 11:
  answer = "Expand your mind and try again."
elif random_number == 12:
  answer = "Never within this lifetime."
else:
  answer = "Error"

#additional steps to check if name and question is provided
if question == "":
  print("The 8-Ball demands a question")
elif name == "":
  print("Question: "+ question)
  print("Magic 8-Ball's answer: " + answer)
else:
#Step 9 and 10 printing out result with formatting
  print(name + " asks: "+ question)
  print("Magic 8-Ball's answer: " + answer)
