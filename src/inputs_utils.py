from sys import stdin
from re import sub

def read_file():
    """
    Read a txt file content from the standard input. 

    Returns
    -------
        Returns a list of strings, each element is a line of the file.
    """
    inputs = stdin.readlines()
    return list(map(lambda x: x.strip().replace('\n', ''), inputs)) # spaces and '\n' char are removed for the elements of the list.  

def remove_accent_from(string):
    return string.replace('à', 'a')\
                 .replace('ä', 'a')\
                 .replace('â', 'a')\
                 .replace('é', 'e')\
                 .replace('è', 'e')\
                 .replace('ê', 'e')\
                 .replace('ë', 'e')\
                 .replace('ï', 'i')\
                 .replace('î', 'i')\
                 .replace('ô', 'o')\
                 .replace('ö', 'o')\
                 .replace('ü', 'u')\
                 .replace('û', 'u')\
                 .replace('ù', 'u')\
                 .replace('ç', 'c')\
                 .replace('\'', '')\
                 .replace('-', '')\
                 .replace('°', '')

def create_french_dict_from(file_path):
    """Transform a text file containing (weight, word) tuuples into python dictionnary."""
    with open(file_path, 'r', encoding="ISO-8859-1") as file:
        lines = file.readlines()

    french_dict = {}
    for line in lines:
        couple = line.strip().replace('\n', '').split(' ')
        word = remove_accent_from(couple[1].lower())
        weight = int(couple[0])
        if word in french_dict:
            french_dict[word] += weight
        else:
            french_dict[word] = weight
        for c in word:
            if ord(c) < ord('a') or ord(c) > ord('z'):
                del french_dict[word]
                break

    return french_dict

if __name__ == "__main__":
    print(read_file())
