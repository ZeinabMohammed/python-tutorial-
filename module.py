print ("Imported module")
test = "this text to test"
def find_index(to_search, target):
    """find index of value in asequence"""
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1

