from inputs_utils import read_file

def find_anagrams_in(sentence):
    """Find pairs of anagrams the sentence.
    
    Params
    ------
    sentence: str 
        Sequence of words.

    Returns
    -------
    list 
        A list of anagrams.
    """
    words_unique = list(set(sentence.lower().split(" ")))               # removed duplicates
    words_signature = [''.join(sorted(w)) for w in words_unique]        # find each word signature

    freq = {} # freq will store the words' index for those with the same signature
    
    for i in range(len(words_signature)):
        w = words_signature[i]
        if w in freq:
            freq[w].append(i)
        else:
            freq[w] = [i] 

    outputs = [[words_unique[i] for i in freq[w]] for w in freq.keys() if len(freq[w]) > 1]
    
    return outputs

if __name__ == "__main__":
    inputs = read_file()
    for line in inputs:
        print(find_anagrams_in(line))
