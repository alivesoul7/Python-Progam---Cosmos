# defining the function and taking question as parameter
def asking_question(question):
   name = input(question + " ")
   return name

# stores the name that is provided by the user
name = asking_question("What is your name ?")

# displays the user entered name
print("Hello" , name)
