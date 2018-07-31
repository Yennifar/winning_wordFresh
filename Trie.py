class Node:
    '''A node of a trie that holds a letter and has a dictionary of child nodes
    API:
    get_data()
    get_children()
    add_child()'''
    
    def __init__(self, letter):
        '''creates a node that holds a given letter and an empry list of child nodes'''
        self.data = letter
        self.children = {}
        
    def __str__(self):
        '''prints the data of the node (letter)'''
        return self.data
    
    def get_data(self):
        '''returns node's data (letter)'''
        return self.data
    
    def get_children(self):
        '''returns node's children as a dictionary'''
        return self.children
    
    def add_child(self, Node):
        '''adds child Node with its empty dict of children to the dict of the self Node children'''
        self.children[Node] = {}

class Trie:
    '''A Trie that holds a lexicon.
    API:
    add_word()
    has_prefix()
    has_word()'''
    
    def __init__(self):
        '''creates an empty tree - a root Node that holds an empty string'''
        self.root = Node('')
    
    def add_word(self, word):
        '''adds word to the trie letter by letter. End of the word is marked by newline character;
        Args: word (str) - word to be added into the trie;'''
        curr = self.root
        
        for i in range(len(word)):
            curr_children = curr.get_children()
            present_letters = map(Node.get_data, curr_children.keys())
            
            if word[i] not in present_letters:
                curr.add_child(Node(word[i]))
            
            curr_children = curr.get_children()
                
            for key in curr_children.keys():
                if key.get_data() == word[i]:
                    curr = key
                    break;
        
        curr.add_child(Node(''));
            
    def has_prefix(self, prefix):
        '''determines if the string prefix is a substring of any word in the trie;
        Args: prefix (str) - substring of interest;
        Returns: bool'''
        
        curr = self.root;
        for i in range(len(prefix)):
            is_present = False;
            curr_children = curr.get_children()
            
            for key in curr_children.keys():
                if key.get_data() == prefix[i]:
                    curr = key
                    is_present = True
                    
            if not is_present: return False

        return is_present
    
    def has_word(self, word):
        '''determines if the string word is a valid finished word in the trie.
        Whether the word is valid is determined by a newline character in the last letter's children;
        Args: word (str) - word of interest;
        Returns: bool'''
        curr = self.root
        valid_word = False

        for i in range(len(word)):
            prefix_present = False
            curr_children = curr.get_children()
            
            for key in curr_children.keys():
                if key.get_data() == word[i]:
                    curr = key
                    prefix_present = True
                    
            if not prefix_present: return False
            
        present_letters = map(Node.get_data, curr.get_children().keys())
        if '' in present_letters: valid_word = True

        return prefix_present and valid_word