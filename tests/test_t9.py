import pytest
from t9 import t9_guess
from default import DefaultValues
from inputs_utils import create_french_dict_from

def test_t9():
    default_values = DefaultValues()
    dico = create_french_dict_from(default_values.BEL_AMI_PATH)
    code = '2665687'
    expected = 'bonjour'
    assert expected == t9_guess(code, dico)
