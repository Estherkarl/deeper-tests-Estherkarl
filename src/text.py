# function will convert string parameter to upper case
'''def to_upper(str):
    return str.upper()

# function will check return true if all items on
# the parameter list are upper case
def to_word_list_isupper(str_list):
    for word in str_list:
        if word.islower():
            return False
    return True
'''
def to_upper(str):
    if not isinstance(str, str):
        raise TypeError("Argument must be a string")
    return str.upper()

def to_word_list_isupper(str_list):
    if not isinstance(str_list, list):
        raise TypeError("Argument must be a list")
    for word in str_list:
        if not isinstance(word, str):
            raise TypeError("List must contain only strings")
        if word.islower():
            return False
    return True
