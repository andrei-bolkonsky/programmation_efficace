import pytest 
import sys 

# Enable local parallel imports 
sys.path.append('/Users/vcumer/Desktop/3_coding/programmation_efficace') 
from sample.anagram import find_anagrams_of 

@pytest.mark.parametrize('word, expected', 
                         [('win', ['win', 'iwn', 'inw', 'wni', 'nwi', 'niw']), 
                          ('te', ['te', 'et'])]) 
def test_find_anagrams_of(word, expected): 
    result = find_anagrams_of(word) 
    assert(set(result) == set(expected))
