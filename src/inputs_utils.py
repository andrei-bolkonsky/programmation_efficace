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
    
if __name__ == "__main__":
    print(read_file())
