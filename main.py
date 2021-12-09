from gameComponents import logic, characters

#Game start
if __name__ == '__main__':

    print("------I Know Which Horror Movie Villian You Are. Let's Play------")

    #Ask each question and record answer
    for q in characters.questions:
        
        #Ask the first question
        answer = input(q["question"] + ' ')

        #Ask the question until we get a valid answer
        while not logic.array_contains(q["options"], answer):
            print(f'{answer} Try Again {q["options"]}')
            answer = input(q["question"] + ' ')

        #We have a valid answer, record it
        q["answer"] = answer


    #Calculate and print the result
    print('Scary! You are ' + logic.get_character())
