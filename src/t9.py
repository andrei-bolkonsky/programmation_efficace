from inputs_utils import read_file, create_french_dict_from
from default import DefaultValues

def letter_to_number(l):
    t9 = "22233344455566677778889999"
    return t9[ord(l)-ord('a')]

def build_pref_dict(dico):
    pref_weight = {} 
    for word, weight in zip(dico.keys(), dico.values()):
        prefix = ''
        for c in word:
            prefix += c
            if prefix in pref_weight:
                pref_weight[prefix] += weight
            else:
                pref_weight[prefix] = weight
    
    propositions = {} 
    for pref, weight in zip(pref_weight.keys(), pref_weight.values()):
        prefix_cd = ''.join(map(letter_to_number, pref))
        if prefix_cd not in propositions or pref_weight[propositions[prefix_cd]] < pref_weight[pref]:
            propositions[prefix_cd] = pref
    
    return propositions

def t9_guess(sequence, dictionary):
    """
    Create a t9 suggestion based on a dictionary built from Maupassant's book bel ami.

    Params
    ------
    sequence: String
        A sequence of numbers such as '2665687'
    dictionary: {}
        A dictionary where keys are french words and values are associated waights
    """
    propositions = build_pref_dict(dictionary)
    if sequence in propositions:
        return propositions[sequence]
    else: 
        return None


if __name__ == "__main__":
    default_values = DefaultValues()
    dico = create_french_dict_from(default_values.BEL_AMI_PATH)
    inputs = read_file()
    for line in inputs:
        for seq in line.split(' '):
            print(f'Sequence: {seq}\nProposition: {t9_guess(seq, dico)}\n')
