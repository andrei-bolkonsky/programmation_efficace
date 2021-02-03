from inputs_utils import read_file, remove_accent_from, create_words_list_from
from default import DefaultValues

class TrieNode:
    """Basic node object to build a Trie struucture."""
    def __init__(self):
        self.is_word = True
        self.char = {chr(i): None for i in range(ord('a'), ord('z')+1)}

def add_node(T, w, i = 0):
    """Add nodes to a Trie structure with the the letters from the word w.

    Params
    ------
    T: Trie structure
        Trie structure on which we add some letter nodes
    w: String
        Word to add to the Trie structuure
    """
    if T == None:
        T = TrieNode()
    if len(w) == i:
        T.is_word = True
    else:
        T.char[w[i]] = add_node(T.char[w[i]], w, i + 1)
    return T

def trie(dictionary):
    """Returns dictionary coded as a Trie structure.

    Params
    ------
    dictionary: []
        List of words (String) to encode 
    """
    T = None
    for w in dictionary:
        T = add_node(T, w)
    return T

def search(T, w, dist, i = 0):
    """Make a recommendation with a word from the dictionary close to the bad spelled word w.
    
    Params
    ------
    T: Trie structure
    w: String
        The bad spelled word to correct (has to be in lower case)
    dist: Int
        Max distance to test in the trie Structure
    """
    if len(w) == i:
        if T != None and T.is_word and dist == 0:       # Init
            return ''
        else:
            return None
    
    if T == None:
        return None

    find = search(T.char[w[i]], w, dist, i + 1)

    if find != None:
        return w[i] + find
    if dist == 0:
        return None

    for c in [chr(i) for i in range(ord('a'), ord('z') + 1)]:
        find = search(T.char[c], w, dist - 1, i)
        if find != None:
            return c + find
        find = search(T.char[c], w, dist - 1, i + 1)
        if find != None:
            return c + find
    
    return search(T.char[w[i]], w, dist - 1, i + 1)

def spell_check(T, w):
    """Test different distance until we find a word to recommend.
    
    Params
    ------
    T: Trie structure
    w: String
        Word to correct
    """
    dist = 0
    while True:
        reco = search(T, w, dist)
        if reco != None:
            return reco
        dist += 1

if __name__ == "__main__":
    default_values = DefaultValues()
    words_list = create_words_list_from(default_values.BEL_AMI_PATH)
    T = trie(words_list)
    lines = read_file()
    for line in lines:
        words = list(map(remove_accent_from, line.lower().split(' ')))
        for w in words:
            print(spell_check(T, w))
