import pytest
from inputs_utils import create_words_list_from
from spell_check import spell_check, trie
from default import DefaultValues

def test_spell_check():
    inputs = ['bimjour', 'arnoir']
    expected = ['bonjour', 'armoir']

    default_values = DefaultValues()
    words_list = create_words_list_from(default_values.BEL_AMI_PATH)
    T = trie(words_list)

    assert expected == [spell_check(T, w) for w in inputs]
