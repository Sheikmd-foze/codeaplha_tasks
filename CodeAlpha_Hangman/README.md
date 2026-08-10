# Hangman 🎯

A classic command-line Hangman game built in Python. Guess the hidden word one letter at a time before you run out of attempts!

## Features

- Randomly picks a word from a predefined word list
- Displays the word as underscores, revealing correctly guessed letters
- Tracks and limits wrong guesses (6 attempts allowed)
- Prevents re-guessing the same letter
- Validates input (must be a single alphabet letter)
- Announces win or loss at the end of the game

## Word List

Currently pulls from a small built-in list:

```
apple, tiger, house, python, school
```

## Requirements

- Python 3.x (no external dependencies)

## Usage

Run the script from your terminal:

```bash
python hangman.py
```

Example session:

```
=== Welcome to Hangman ===

Word: _ _ _ _ _ 
Enter a letter: a
Correct!

Word: a _ _ _ _ 
Enter a letter: p
Correct!

Word: a p p _ _ 
Enter a letter: z
Wrong guess!
Remaining attempts: 5
...
🎉 Congratulations! You guessed the word: apple
```

## How It Works

1. A random word is chosen from the `words` list using `random.choice()`.
2. On each turn, the script rebuilds a display string showing guessed letters and underscores for the rest.
3. If the display no longer contains any underscores, the player has won.
4. Each guess is validated to ensure it's a single letter and hasn't already been guessed.
5. Correct guesses are added to the revealed word; incorrect guesses reduce the remaining attempts.
6. The game ends in a win (word fully guessed) or a loss (wrong guesses reach the maximum of 6).

## Notes / Future Improvements

- Could add ASCII art of the hangman figure that updates with each wrong guess.
- Word list could be expanded or loaded from an external file for more variety.
- Could add difficulty levels (shorter/longer words, more/fewer attempts).
- Could add a play-again loop instead of exiting after one round.

## License

Feel free to use, modify, and distribute this project.
