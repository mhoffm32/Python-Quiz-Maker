#%%

science_trivia = {
    "How many elements are there in the periodic table?": "118",
    "How many bones do sharks have?":"0",
    "What is the name of the most recent supercontinent?": "pangea",
    "What is the “powerhouse of the cell?”":'mitochondria'
}
world_capitals = {
    "Poland":"warsaw",
    "Spain":"madrid",
    "India":"new delhi",
    'Costa Rica': "san jose",
    'Peru':"lima"
}

custom_quiz = {}
correct_answers = 0

playAgain = 1

while playAgain:

    print("Type the number of the quiz you would like to take:\n1.Create Your own Quiz!\n2.Science Trivia")
    print('3.Capitals of the world')
    quiz_choice = int(input())
    if quiz_choice == 1:
        quiz_length = int(input("Enter the number of items in the quiz: "))
        for x in range(quiz_length):
            question = input("Question "+ str(x+1) + ": ")
            answer = input("Answer: ")
            custom_quiz.update({str(question):str(answer)})
        
        print('Now lets play the quiz...')
        for x,y in custom_quiz.items():
            ans = input(x+ ": ")
            if ans.lower() == y:
                print('Correct!')
                correct_answers = correct_answers+1
            else:
                print("Incorrect. The answer was "+y+", not "+ans+".")

        print("Score: " + str(correct_answers) + "/" + str(quiz_length))  

    elif quiz_choice == 2:

        for x,y in science_trivia.items():
            ans = input(x+ ": ")
            if ans.lower() == y:
                print('Correct!')
                correct_answers = correct_answers+1
            else:
                print("Incorrect. The answer was "+y+", not "+ans+".")

        print("Score: " + str(correct_answers) + "/" + str(len(science_trivia)))  

    elif quiz_choice == 3:  
        for x,y in world_capitals.items():
            ans = input(x+ ": ")
            if ans.lower() == y:
                print('Correct!')
                correct_answers = correct_answers+1
            else:
                print("Incorrect. The answer was "+y+", not "+ans+".")
        print("Score: " + str(correct_answers) + "/" + str(len(world_capitals))) 
    
    cont = input("\nType Y to play again, or N to stop")
    if cont == 'N':
        break
    else:
        continue

      




# %%
