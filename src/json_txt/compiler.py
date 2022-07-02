# json_txt/compiler.py - version 1.4.6

import filemod


def collab_words_in_list(data_list):
    """collab word into strings"""
    return ''.join(data_list)


def test1(data):
    if data is None:
        print('x Test 1 Fail', 'red')
    else:
        return True

def test2(data):
    from json_txt.MainFiles import extract_values,extract_keys
    if len(extract_keys(data)) == len(extract_values(data)) == data.count(":"):
        return True

    print("X Test 3 Fail", 'red')
    print("Uneven values or number found in the values", 'red')


def compiles(data):
    data = filemod.reader(data)
    if test1(data) == test2(data):
        return data
