import operator
from gameComponents import characters

def array_contains(arr, val):
    '''
    Returns True if the value was found in the array or False otherwise.
    '''
    for x in arr:
        if x == val:
            return True

    return False


def get_character():
    '''
    Calculate which character is most relevant based on the user answers.
    '''
    #Create "scoring chart"
    scores = {}
    for character in characters.characters:
        scores[character["name"]] = 0

    #Start scoring "points"
    for question in characters.questions:

        answer = question["answer"]

        #If answered "yes", add points for characters with that trait
        if answer == 'yes':
            for character in characters.characters:
                #If this trait is the character's only trait, give them a big point boost (therefor the correct character will have
                # enough points to win)
                if len(character["traits"]) == 1 and character["traits"][0] == question["key"]:
                    scores[character["name"]] += 7
                # Otherwise, if just one of many traits, give them a smaller points
                elif array_contains(character["traits"], question["key"]):
                    scores[character["name"]] += 2

    #Sort the scores from greatest to least
    winner = sorted(scores.items(), key=operator.itemgetter(1), reverse=True)

    #Name and value display
    return winner[0][0]
