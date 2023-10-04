# Boggle_Word_Checker

# Training on Boggle Word Checker | Codewars

## Question 

Write a function that determines whether a string is a valid guess in a Boggle board, as per the rules of Boggle. A Boggle board is a 2D array of individual characters, e.g.:

`[ ["I","L","A","W"],
  ["B","N","G","E"],
  ["I","U","A","O"],
  ["A","S","R","L"] ]`


Valid guesses are strings which can be formed by connecting adjacent cells (horizontally, vertically, or diagonally) without re-using any previously used cells.

For example, in the above board "BINGO", "LINGO", and "ILNBIA" would all be valid guesses, while "BUNGIE", "BINS", and "SINUS" would not.

Your function should take two arguments (a 2D array and a string) and return true or false depending on whether the string is found in the array as per Boggle rules.

Test cases will provide various array and string sizes (squared arrays up to 150x150 and strings up to 150 uppercase letters). You do not have to check whether the string is a real word or not, only if it's a valid guess.

## Solution

## Boggle Word Checker

This Python function, `find_word`, is designed to find a given word on a Boggle board. It checks whether the input word can be formed by connecting adjacent cells (horizontally, vertically, or diagonally) on the board without reusing any previously used cells.

### Function Explanation

### Parameters

- `board`: The 2D Boggle board represented as a list of lists, where each element is a character.
- `word`: The word to search for on the Boggle board.

### Function Logic

- The function starts by defining a list of directional movements (`dir`) for checking adjacent cells.
- It calculates the dimensions of the board (`m` and `n`).
- The core of the function is a depth-first search (DFS) algorithm (`dfs`). It recursively explores the board to find the word.
- The DFS function is called for each cell on the board to check if the word can be formed starting from that cell.

### Return Value

- If the function finds the word on the board, it returns `True`.
- If the word cannot be found, it returns `False`.

## Example Usage

```python
board = [
    ["G", "I", "Z"],
    ["U", "E", "K"],
    ["Q", "S", "E"]
]
word_to_find = "GEEKS"

if find_word(board, word_to_find):
    print(f"'{word_to_find}' is a valid guess.")
else:
    print(f"'{word_to_find}' is not a valid guess.")
