import random
import time

def instructions():
    print("\n\n\t\t INSTRUCTIONS:")
    print("\n\n\t\t * The USER is asked to choose a topic to play with.")
    print("\n\n\t\t * Then the USER must guess the word related to the topic by guessing the letters one by one.")
    print("\n\n\t\t * The USER will be given 5 chances if he/she makes a wrong guess.")
    print("\n\n\t\t * If the USER guesses the word correctly, the USER wins else loses.")
    print("\n\n\t\t * The USER will be rewarded 10 points if all the guesses are correct.")
    print("\n\n\t\t * The USER will lose 1 point for each wrong guess.")
    print("\n\n\t\t * If the user wants to quit in the middle press '0'.")
    print("\n\n\t\t\t\t ALL THE BEST!!!")

def play_game():
    topics = {
        'a': ["safari", "chrome", "internetexplorer", "opera", "mozillafirefox", "maxthon", "slimjet", "netscape", "ucbrowser", "seamonkey"],
        'b': ["instagram", "facebook", "twitter", "whatsapp", "telegram", "snapchat", "googleplus", "pininterest", "hike", "skype"],
        'c': ["blue", "yellow", "black", "white", "pink", "brown", "orange", "green", "violet", "purple"],
        'd': ["msdhoni", "sachintendukar", "kapildev", "viratkohli", "rohitsharma", "yuvarajsingh", "ashwin", "jadeja", "hardikpandya", "rahul"],
        'e': ["gandhiji", "subashchandrabose", "bhagatsingh", "jhansirani", "mangalpandey", "bharathiyar", "kattabomman", "tipusultan", "jawa"],
        'f': ["tamilnadu", "kerala", "andrapradesh", "karnataka", "maharashta", "rajasthan", "gujarat", "uttarpradesh", "punjab", "westbengal"],
        'g': ["volleyball", "basketball", "throwball", "football", "cricket", "tennis", "badminton", "hockey", "kabbadi", "baseball"],
        'h': ["narendramodi", "jayalalitha", "karunanithi", "rajivgandhi", "indiragandhi", "kamarajar", "annadurai", "vajpayee", "manmohansingh", "lal"],
        'k': ["ganges", "brahmaputra", "godavari", "narmada", "indus", "yamuna", "kaveri", "mahanadi", "tapti", "krishna"],
        'l': ["tamil", "telugu", "malayalam", "hindi", "kanada", "sanskrit", "punjabi", "bengali", "oriya", "konkani"]
    }

    total = 0

    while True:
    
        print("\n\t\t\t\t\t\t *      *      * *      * *     *  * * * * *  * *   * *      * *      * *     * ")
        print("\n\t\t\t\t\t\t *      *     *   *     *  *    *  *          *  * *  *     *   *     *  *    * ")
        print("\n\t\t\t\t\t\t * * * **    * * * *    *   *   *  *     ***  *   *   *    * * * *    *   *   * ")
        print("\n\t\t\t\t\t\t *      *   *       *   *    *  *  *       *  *       *   *       *   *    *  * ")
        print("\n\t\t\t\t\t\t *      *  *         *  *     * *  * * * * *  *       *  *         *  *     * * ")
        print("\n\n")
        print("\n\t\t\t\t\t\t 1.PLAY \n\t\t\t\t\t\t 2.INSTRUCTIONS \n\t\t\t\t\t\t 3.QUIT")
        n = int(input("\n\t\t\t\t\t\t Press the number: "))

        if n == 1:
            lives = 5
            crt = 0
            newcrt = 0
            guess = [''] * 20
            quit_game = False
            index = random.randint(0, 9)

            ch = input("\n\t\t\t\t\t\tTOPICS\n"
                       "\t\t\t\t\t\t a. Web browsers \n"
                       "\t\t\t\t\t\t b. Social Media \n"
                       "\t\t\t\t\t\t c. Colours \n"
                       "\t\t\t\t\t\t d. Indian Cricketers\n"
                       "\t\t\t\t\t\t e. Freedom Fighters \n"
                       "\t\t\t\t\t\t f. States of India \n"
                       "\t\t\t\t\t\t g. Sports\n"
                       "\t\t\t\t\t\t h. Politicians \n"
                       "\t\t\t\t\t\t k. Rivers in India \n"
                       "\t\t\t\t\t\t l. Indian Languages\n"
                       "\n\t\t\t\t  choose the topic: ")

            if ch in topics:
                word_list = topics[ch]
                word = random.choice(word_list)
                len_word = len(word)
            else:
                print("\nInvalid topic choice.")
                continue

            while crt < len_word:
                print("\n")
                for i in range(len_word):
                    if guess[i]:
                        print(guess[i], end=' ')
                    else:
                        print("_", end=' ')
                print("\n")

                guess_letter = input("\n\nEnter a guess letter: ")

                if guess_letter == '0':
                    quit_game = True
                    break

                newcrt = crt

                for i in range(len_word):
                    if guess[i]:
                        continue

                    if word[i] == guess_letter:
                        guess[i] = word[i]
                        crt += 1

                if newcrt == crt:
                    lives -= 1
                    print("\n\nWRONG GUESS")
                    print("\n\nNumber lives remaining =", lives)

                    if lives == 0:
                        print("\n\t\t\t _______")
                        print("\t\t\t|       |")
                        print("\t\t\t|       0")
                        print("\t\t\t|      /|\\")
                        print("\t\t\t|       |")
                        print("\t\t\t|      / \\")
                        break
                else:
                    print("\n\nCORRECT GUESS\n")

                if lives == 5:
                    print("\n\t\t\t _______")
                    print("\t\t\t|       |")
                    print("\t\t\t|")
                    print("\t\t\t|")
                    print("\t\t\t|")
                    print("\t\t\t|")
                    print("\t\t\t|")
                if lives == 4:
                    print("\n\t\t\t _______")
                    print("\t\t\t|       |")
                    print("\t\t\t|       0")
                    print("\t\t\t|")
                    print("\t\t\t|")
                    print("\t\t\t|")
                    print("\t\t\t|")
                if lives == 3:
                    print("\n\t\t\t _______")
                    print("\t\t\t|       |")
                    print("\t\t\t|       0")
                    print("\t\t\t|       |")
                    print("\t\t\t|")
                    print("\t\t\t|")
                    print("\t\t\t|")
                if lives == 2:
                    print("\n\t\t\t _______")
                    print("\t\t\t|       |")
                    print("\t\t\t|       0")
                    print("\t\t\t|      /|\\")
                    print("\t\t\t|")
                    print("\t\t\t|")
                    print("\t\t\t|")
                if lives == 1:
                    print("\n\t\t\t _______")
                    print("\t\t\t|       |")
                    print("\t\t\t|       0")
                    print("\t\t\t|      /|\\")
                    print("\t\t\t|       |")
                    print("\t\t\t|")
                    print("\t\t\t|")

            if quit_game:
                print("\n\n\t\t\t\tTHE USER QUIT QUICKLY\n")
            elif lives == 0:
                print("\n\n\t\t\t\t YOU LOST :( \n")
                print("\n\n The correct word : ", word)
            else:
                print("\n\n You guessed the word", word, "correctly")
                print("\n\n\t\t\t\t YOU WON!!!\n")
                print("\n\t\t\t\t CONGRATULATIONS :)\n")

                total += 10

                if lives == 4:
                    total -= 1
                if lives == 3:
                    total -= 2
                if lives == 2:
                    total -= 3
                if lives == 1:
                    total -= 5

            print("\n\n\t\t\t\t YOUR SCORE : ", total)
            n = int(input("\n\n\t\t Press 1 if you want to continue OR Press 3 if you want to quit\n"))

            if n == 3:
                break

        elif n == 2:
            instructions()
            n = int(input("\n\n Press 1 to start the game: "))
            if n == 1:
                continue

        elif n == 3:
            print("\n\n\t\t\t\t\t\t\t\t\t ***THANK YOU***\n\n")
            break

if __name__ == "__main__":
    play_game()
