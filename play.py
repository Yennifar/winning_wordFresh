import WordFresh as wf
import re
import Trie

if __name__ == "__main__":
    '''WordFresh play.
    Note: it relies on Python 2 to run. Do not use Python 3. Or you can. But it won't work.
    Game takes a name of the file containing English words and creates Trie lexicon from it.
    Then it asks user for a board input. (Un)comment corresponding line to input through the console or by file name.
    It looks up all the words from the lexicon and assigns a value to each word as a sum of word letters values multiplied by the length of the word.
    It sorts the list of words by value from highest to lowest and outputs the list'''
    
    lexicon = wf.lexicon_from_file('wordlist.txt')
    
    while True:
        playing = wf.is_playing()
        if not playing:
            print("Thanks for playing!")
            break
        else:
            #board = wf.read_board_from_file('board.txt')
            board = wf.read_board_from_console()
            wf.print_board(board)
            print('')
            word_list = wf.find_words(board, lexicon)
            p = re.compile('q')
            if len(word_list) > 1:
                print('The following {} words were found:'.format(len(word_list)))
                for word in word_list:
                    print(p.sub('qu', word))
                    
            elif len(word_list) == 1:
                print('The following word was found:')
                print(p.sub('qu', word[0]))
                
            else: print('This board has no words from the dictionary')
            print('')