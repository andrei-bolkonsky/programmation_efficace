import sys 
import math 

# Enable local parallel imports
sys.path.append('/Users/vcumer/Desktop/3_coding/programmation_efficace')
from sample.inputs_utils import read_file

def find_anagrams_of(word):
    """Find all anagrams.
    
    Params
    ------
    word: str 
        Sequence of characters for which all combinaisons of anagram have to be found.

    Returns
    -------
    list 
        A list of all anagrams.
    """
    outputs = []
    if len(word) == 1:
        return word
    else:
        for subword in find_anagrams_of(word[1:]):
            for k in range(len(word)):
                outputs.append(subword[:k] + word[0] + subword[k:])
    return outputs

if __name__ == "__main__":
    inputs = read_file()
    for line in inputs:
        words = line.split(' ')
        for word in words:
            print(find_anagrams_of(word))
