
#Simple-hangman-game by wonderbowl12

def main(sentence, blank, hangmen):
    
    guesses = []
    
    while True:
        joined_blank = "".join(blank).count('_')
        if joined_blank == 0:
            print('You won!')
            game_again()
        
        else:    
            print('\n')
            print('The length (without spaces): ', joined_blank) #Counts how many blank letters
            print("Here are your wrong guesses: \n" ,"".join(guesses)) #Prints the wrong guesses so far
            
            #Prints the blank spaces
            print("".join(blank))
            guess = input('Choose a letter! ').upper()
            if len(guess) > 1:
                print('\n!!Make sure to type only one letter!!')
            elif guess in blank:
                print('\n!!You\'ve already guessed that!!')
            elif guess in sentence:
                positions = [i for i, x in enumerate(sentence) if x == guess] #Finds position of correct guess in sentence
                for index in positions:
                    blank[index] = guess #Replaces blank space with correct guess

            else:
                #If answer is wrong, the guess is appended to the 'guesses' list and print from the hangmen list
                guesses.append(guess)
                if len(guesses) == 7:
                    print('Game over, the sentence was: {}'.format(sentence))
                    game_again()
                else:
                    print('\nWRONG')
                    print(hangmen[len(guesses)])


#asks player if they want to play again
def game_again():
    confirm = input('\nWould you like to play again? ')
    if confirm.lower() == 'yes':
        initalize()
    elif confirm.lower() == 'no':
        exit()


#Creates the sentence and list needed to build blank lines
def initalize():
    
    array = list(input('Type a sentence for someone to solve!--> '))
    blank_lines = []
    sentence_upper = "".join(array).upper()


    #Builds the blank lines
    for char in array:
        if char == ' ':
            blank_lines.append(' ')
        elif char in "!?.,:;<>()*&^%$#@\'\":\{\}-_=+~`":
            blank_lines.append(char)
        else:
            blank_lines.append('_ ')
    #Calls main function
    main(sentence_upper, blank_lines, hangmen)



#List of hangmen ascii art
hangmen = [  
   ' +---+ \n'
    '|   | \n'
    '    | \n'
    '    | \n' 
    '    | \n'
    '    | \n'
 '   =========\n', 

  '  +---+ \n'
  '  |   | \n'
  '  O   | \n'
  '      | \n'
  '      | \n'
  '      | \n'
  '  ========= \n',

  '  +---+ \n'
  '  |   | \n'
  '  O   | \n'
  '  |   | \n'
  '      | \n'
  '      | \n'
  '  ========= ',


 '   +---+\n'
 '   |   | \n'
 '   O   | \n'
 '  /|   | \n'
 '       | \n'
 '       |  \n'
'========= \n ' ,

 '   +---+ \n'
 '   |   | \n'
 '   O   |  \n'
 '  /|\  |  \n'
 '       |  \n'
 '       |   \n'
'========= \n',

'    +---+ \n'
'    |   | \n'
'    O   | \n'
'   /|\  | \n'
'   /    | \n '
'        | \n'
'=========\n',

'   +---+ \n'
'   |   | \n'
'   O   | \n'
'  /|\  | \n'
'  / \  | \n'
'       | \n'
'========= \n'
]

initalize()