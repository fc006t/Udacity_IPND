# Frank Costello IPND Project 2
# Submission 2 - Added decriptions at the beginning of the functions to explain thier purpose
#   Also created a function playGame() to allow the user to replay the quiz as often as they wish





# validateInput: Pass a prompt and the acceptable values.  Return an acceptable answer. This routine will always return a string
# could be more elegant with control, but this forces the user to enter a valid answer

def validateInput(prompt, valid_answers):
  have_valid_input = False
  while not have_valid_input:
      user_input = raw_input(prompt)
      for test_valid  in valid_answers:
          if user_input.upper() == test_valid.upper(): return test_valid
      temp = raw_input( 'Sorry that is not an option. Press  Enter to try again.')



# init_quiz_statement:  Initialize the quiz based on difficulty level.  Makes it very easy to include new difficulties.
      
def init_quiz_statement(difficulty_level):

    if difficulty_level == 'Easy':
        statement = "Planets are very cool.  You were born on the planet ___1___.  Everyone "
        statement = statement + "says the red planet is ___2___.  All women are born on ____3____ and then transported "
        statement = statement + "to ___1___at light speed.  All space trash gets sucked into the giant red spot on ___4___."
        
    if difficulty_level == 'Medium':
        statement = "In baseball, the Chicago ___1___  defeat the Clevland ___2___ to win the "
        statement = statement + "___3___ Series for the first time since ___4___."
  
    if difficulty_level == 'Hard':
        statement = "The Dehing Patkai Festival is a once-a-year festival held at ___1___  in Tinsukia "
        statement = statement + "district of ___2___ . The festival is named after the majestic "
        statement = statement + "___3___ range and the mischievous Dehing ___4___."

    if difficulty_level == 'Extreme':
        statement = "___1___ is known as the Mole Pokemon,  it is evolved from and "
        statement = statement + "consists of  ___2___ Digletts that emerged from one body.  " 
        statement = statement + "They trigger earthquakes when they travel ___3___"      
        
    return statement


    

# I will be a little tricky  and not use position zero to store a quiz answer .  This makes the code 
# easier to understand later by saying answer 1 is in postion 1 of the list,  I will
# store the TOTAL expected answers to help me step through the looping as I prompt the user    
    
def init_quiz_answers(difficulty_level):
    if difficulty_level == 'Easy': return [4,'Earth','Mars','Venus','Jupiter']
    if difficulty_level == 'Medium': return [4,'Cubs','Indians','World','1908']      
    if difficulty_level == 'Hard': return [4,'Lekhapani','Assam','Patkai','River']
    if difficulty_level == 'Extreme': return [3,'Dugtrio','three','underground']
    

    
# ask_question:  Pass the number of the question in the quiz, the answer grid and if the user has requested a hint.  Ask the user the 
# quiz question, compare to the acutal answer return 'Correct' or 'Incorrect'

def ask_question(question_number,quiz_answers, give_hint):
    quiz_answers[question_number][0]
    prompt = "\n Please enter an answer for ___" + str(question_number) + '___'
    if give_hint: prompt = 'LAST TRY YOU DUMMY! Here is the first character, ** ' + quiz_answers[question_number][0] + '**  now  ' + prompt
    user_input = raw_input(prompt)
    if user_input.upper() == quiz_answers[question_number].upper(): return 'Correct'
    else: return 'Incorrect'

    
    
# update_quiz_statement - The user has given a correct answer.  Take that correct answer and replace the placeholder
# blank so the quiz statement becomes increasingly readable as the user answers the question correctly.
# Assumption: The replacement will always take the form of three dashes, the question number, then three dashes

def update_quiz_statement(quiz_statement,quiz_answers,correct_answer):

    statement_split = quiz_statement.split()    
    replace_question = '___'+str(correct_answer)+'___'    
    replace_answer=quiz_answers[correct_answer]
    index = 0
    replaced = []
    
#    print 'statement split | quiz_answers | replace_question'
#    print statement_split
#    print quiz_answers    
#    print replace_question  
    

    while index < len(statement_split):
        if replace_question in statement_split[index]: 
            if len(replace_question) == len(statement_split[index]): replaced.append(replace_answer)
            else: replaced.append(replace_answer + '.')  #need to solve for punctuation
        else: 
            replaced.append(statement_split[index])
        index += 1 
        
    print "\n\n Updated quiz statement with " + quiz_answers[correct_answer]
    
    quiz_statement = " ".join(replaced)
    
#    print quiz_statement
#    user_input = raw_input('boogie')
    return quiz_statement
 
 
 

def playGame(): 
    quiz_statement = init_quiz_statement(difficulty_level)
    quiz_answers = init_quiz_answers(difficulty_level)

    print quiz_statement
    quiz_question = 1



    #  B E G I N     U S E R     I N P U T     S E C T I O N  - Prompt the user and start the quiz


    while quiz_question <= quiz_answers[0]:
        chance_counter = 1 
        while chance_counter <= num_chances:
            if chance_counter == num_chances and wants_hint: input_result =  ask_question(quiz_question,quiz_answers,True)
            else: input_result = ask_question(quiz_question,quiz_answers,False)
            chance_counter = chance_counter + 1
            print input_result
            if input_result == 'Correct': 
                quiz_statement = update_quiz_statement(quiz_statement,quiz_answers,quiz_question)
                print '\n\n' + quiz_statement
                chance_counter = num_chances + 1  # they answered correclty before using up all the chances
        quiz_question = quiz_question + 1
        if input_result <> 'Correct': quiz_question = quiz_answers[0] + 1    #exit if incorrect on last attemp mid-quiz
        
    

    
#  B E G I N     I N I T I A L I Z A T I O N    S E C T I O N   -  Initialize all variables/prompts

    
# Validate  user input and set up quiz difficulty

wantToPlay = True
while wantToPlay:

    print ' \n ********** Welcome to the fill in the blank quiz *********** \n\n'  
    print 'You will be given a section of text where you will fill in the blanks. \n Each blank will be numbered and you will be prompted for your answers \n\n'

    difficulty_level = validateInput("Select Difficulty (Easy, Medium, Hard and Extreme)",["Easy","Medium","Hard","Extreme"])
    num_chances = validateInput("How many chances do you want to guess?  (2,3,4 or 5)", ["2","3","4","5"])
    wants_hint = validateInput("Do you want a hint on your last guess?",["Yes","No"])


    print ' \n ********** Quiz Settings You Chose *********** \n'
    print 'Difficulty Selected: ' + difficulty_level
    print 'Number of Chances ' + num_chances
    print 'Hint given on last chance? ' + wants_hint

    num_chances = int(num_chances)   # needed to convert to an intetger
    wants_hint = wants_hint=="Yes"  # needed to convert to a logical

    print ' \n ********** Begin Quiz   *********** \n\n'


    playGame()
    userInput = validateInput("Do you want to play again?",["Yes","No"])
    wantToPlay = userInput=='Yes'
    
    

