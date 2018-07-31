import random
import re
import Trie

def lexicon_from_file(lexicon_filename):
    '''takes a file of words and builds Trie from it.
    Note: each word in the list should end with a newline character.
    Args: filename (str)
    Returns: lexicon (Trie)'''
    
    lexicon = Trie.Trie()
    f = open(lexicon_filename, 'r')
    p = re.compile('qu')

    for line in f:
        if re.match('q[^u]', line): continue
        lexicon.add_word(p.sub('q', line[:-1]))
    return lexicon
    
def is_playing():
    '''Asks whether user wants to play again;
    Returns: bool'''
    ans = raw_input('Do you want to play? ')
    if not ans.lower().startswith('y'):
        return False
    
    return True

def read_board_from_file(board_filename):
    '''Reads board from console;
    Args: filename (str)
    Returns: board (char [][])'''
    board = []
    f = open(board_filename, 'r')
    for line in f:
        board.append(list(line.strip()))
    return board
    
def read_board_from_console(height = 6, width = 5):
    '''Reads board from console;
    Args: height (int) - number of rows in board - default 6,
        width (int) - number of columns in board - default 5;
    Returns: board (char [][])'''
    board = []
    print('Enter a board as 6 strings of length 5')
    for i in range(height):
        curr_line = raw_input()
        while len(curr_line) != width:
            print("Enter {}-character string.".format(width))
            curr_line = raw_input()
            
        board.append(list(curr_line.lower().strip()))
    print('')
    return board
   
def initialize_board(height = 4, width = 4):
    '''Use in case you want to randomly initialize the board;
    Randomly generates board of the desired size. Letters are used uniformly.
    Args: height (int) - number of rows in board,
        width (int) - number of columns in board;
    Returns: board (char [][])'''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    board = []
    for i in range(board_height):
        board.append([])
        for j in range(board_width):
            board[i].append(alphabet[random.randint(0, len(alphabet) - 1)])
    
    return board
    
def print_board(board):
    '''Prints board in 6 * 5 format in upper case letters;
    Args: board (int [][]);
    Returns: None'''
    for i in range(len(board)):
        print ''.join(board[i]).upper()
        
def find_words(board, lexicon):
    '''Finds all words on board that are found in lexicon. Words can be read horisontally, vertically, and diagonally;
    Args: board (int [][]),
            lexicon (Trie);
    Returns: word_list (string []) sorted from highest to lowest word value'''
    word_list = []
    result = set([])
    used_letters = set([])
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            first_letter = board[i][j]
            used_letters.add((i, j))
            find_words_from_position(first_letter, board, i, j, lexicon, result, used_letters)
            used_letters.remove((i, j))
    
    word_list = list(result)
    word_list = sorted(word_list, cmp = compare_word)
    return word_list
    
def find_words_from_position(curr, board, i, j, lexicon, wordlist, used_letters):
    '''Recursive function that looks up all words on the board;
    Args: curr (str) - current piece already found on board;
        board (int [][]),
        i (int) - current vertical position,
        j (int) - current horisontal position,
        lexicon (Trie),
        wordlist (str Set([])) - set of words that are already found,
        used_letters (tuple []) - list of letter positions that were already used for the current word;
    Returns: None. Updates wordlist'''
    if len(curr) > 2 and lexicon.has_word(curr): wordlist.add(curr)
    
    for dx in (1, 0, -1):
        x = j + dx
        if (x < 0 or x >= len(board[i])): continue
        for dy in (1, 0, -1):
            y = i + dy
            if ((dx == 0 and dy == 0) or (y, x) in used_letters or y < 0 or y >= len(board)): continue
            if lexicon.has_prefix(curr):
                used_letters.add((y, x))
                find_words_from_position(curr + board[y][x], board, y, x, lexicon, wordlist, used_letters)
                used_letters.remove((y, x))

def word_value(word):
    '''Calculates word value as a sum of letter values multiplied by length of a word;
    Args: word (str);
    Returns: word_value (int)'''

    values = {'a': 1, 'b': 4, 'c': 4, 'd': 3,
                    'e': 1, 'f': 5, 'g': 3, 'h': 5,
                    'i': 1, 'j': 8, 'k': 6, 'l': 2,
                    'm': 4, 'n': 2, 'o': 1, 'p': 4,
                    'q': 10, 'r': 2, 's': 1, 't': 2,
                    'u': 2, 'v': 5, 'w': 6, 'x': 8,
                    'y': 6, 'z': 10}
    word_value = 0
    for i in range(len(word)):
        word_value += values[word[i]]
        
    word_value *= len(word)
    return word_value
                
def compare_word(word1, word2):
    '''Comparator: compares the values of two words;
    Args: word1 (str),  word2 (str);
    Returns: comparator'''
    
    return word_value(word2) - word_value(word1)
    