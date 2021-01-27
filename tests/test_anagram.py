import pytest 
import sys 
from anagram import find_anagrams_of 
from anagram_in_sentence import find_anagrams_in

@pytest.mark.parametrize('word, expected', 
                         [('win', ['win', 'iwn', 'inw', 'wni', 'nwi', 'niw']), 
                          ('te', ['te', 'et'])]) 
def test_find_anagrams_of(word, expected): 
    result = find_anagrams_of(word) 
    assert(set(result) == set(expected))
    
@pytest.mark.parametrize('sentence, expected', 
                         [(str('le chien marche vers sa niche et trouve une limace de chine nue pleine de malice qui lui fait du charme'), 
                           [['chine', 'niche', 'chien'], ['charme', 'marche'], ['une', 'nue'], ['limace', 'malice']])])
def test_find_anagrams_in_(sentence, expected):
    result = find_anagrams_in(sentence)
    result.sort()
    expected.sort()
    result = list(map(sorted, result))
    expected = list(map(sorted, expected))   
    assert result == expected
