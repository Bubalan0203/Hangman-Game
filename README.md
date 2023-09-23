# Hangman-Game
Hangman is a guessing game for two or more players. One player thinks of a word, phrase, or sentence and the other(s) tries to guess it by suggesting letters or numbers within a certain number of guesses.



The code implements a text-based hangman game in Python.

It begins by defining the instructions function to display game instructions.

The play_game function is the main game logic. It allows the player to choose from different topics and then plays the hangman game accordingly.

The topics dictionary contains words related to various topics, with each topic represented by a letter ('a' for Web browsers, 'b' for Social Media, etc.).

The game starts by displaying a title using print statements.

The player can choose to play (option 1), read instructions (option 2), or quit (option 3).

If the player chooses to play, the game selects a random word from the chosen topic and starts the hangman game.

The player has 5 lives and must guess the letters of the word. Correct guesses reveal the letters, while wrong guesses reduce lives.

The game tracks correct and incorrect guesses and displays a hangman figure based on the player's remaining lives.

If the player correctly guesses the word, they earn points, and the game asks if they want to continue or quit.

If the player quits or runs out of lives, the game provides appropriate messages and displays the correct word.

The player's total score is calculated based on their performance.

If the player chooses to read instructions, the instructions function is called, and they are prompted to start the game afterward.

The game can be started again or exited with the "THANK YOU" message.

The code is wrapped in a if __name__ == "__main__": block to ensure it only runs when the script is executed directly.

Overall, this code provides a simple and interactive hangman game with various topics and instructions for the player to enjoy.





