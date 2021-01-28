from inputs_utils import read_file

def merge(left, right):
    """Rebuilt a list from two sublists using the ascending order of the index.
    
    Params
    ------
    left: [int]
        Sorted list
    left: [int]
        Sorted list
    """
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    else:
        if left[0] <= right[0]:
            return [left[0]] + merge(left[1:], right)
        if left[0] > right[0]:
            return [right[0]] + merge(left, right[1:])
        
def sort(l):
    """Sort a list using a merge-sort method.
    
    Params
    ------
    l: [int]
        List to sort
    """
    n = len(l)
    if n <= 1:
        return l
    else:
        left = l[:n//2]
        right = l[n//2:]
        return merge(sort(left), sort(right))

if __name__ == "__main__":
    inputs = read_file()
    for line in inputs:
        l = list(map(int, line.split(' ')))
        print(sort(l))
