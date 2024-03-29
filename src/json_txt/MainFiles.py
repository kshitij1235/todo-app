'''
json_txt/MainFile.py - version 1.4.6

'''

from filemod import writer, reader
from json_txt.SupportFuncs import collab_words_in_list, allot_values
from json_txt.compiler import compiles


def extract_keys(txt_file_data):
    """
    extract keys from file
    1)this takes list or some times even file works. 
    2)finds for each specific line where '\n' is present(this means new line)
    3)and append every thing before ':' and append it in a list
    """
     
    txt_file_data=list(txt_file_data)
    temp = []
    keys = []
    for index , element in enumerate(txt_file_data) :
        if element== "\n":
            for value_index in range(index, len(txt_file_data)):
                if txt_file_data[value_index] == ":":
                    keys.append(collab_words_in_list(temp))
                    temp.clear()
                    break
                elif txt_file_data[value_index] not in [":", "\n", " ", "}", "{"]:
                    temp.append(txt_file_data[value_index])
    return keys


def extract_values(txt_file_data):
    """extract values from file"""

    temp = []
    values = []
    for index ,element in enumerate(txt_file_data):
        if element == ":":
            for index in range(index, len(txt_file_data)):
                if txt_file_data[index] == "\n":
                    values.append(collab_words_in_list(temp))
                    temp.clear()
                    break
                elif txt_file_data[index] not in [":", "'", " ", '"', "}", '\r']:
                    temp.append(txt_file_data[index])
    values = allot_values(values)
    return values


def extract_data(data):
    """create a dictonary"""

    keys = extract_keys(data)
    values = extract_values(data)
    return {keys[index]: values[index] for index in range(len(keys))}


def load_txt(data):
    """compiling the text file"""

    try:
        return list(compiles(data))
    except FileNotFoundError:
        pass


def edit_data(filename, key, value):
    """
    edit value  from the file
    """
    
    data = list(reader(filename))
    keys = extract_keys(data)
    values = extract_values(data)

    # gettting value of element to change

    temp = keys.index(key)

    # swaping the old value witgh new one 

    values.pop(temp)
    values.insert(temp, value)

    # filling template   

    writing_file = '{ \n'
    for key , value in zip(keys,values):
        writing_file = f"{writing_file}{key}:{value}\n"
    writing_file = writing_file+"\n"+"}"
    
    # writing the date processed 
    writer(filename, writing_file, "w")
    return True


def add_data(filename, newkeys, newvalues):
    """append data into txt file"""

    # get the file data
    data = reader(filename)

    # extract keys and values
    keys = extract_keys(data)
    values = extract_values(data)

    # append new keys and values to old list
    keys.append(newkeys)
    values.append(newvalues)

    # filling up template

    write_file = "{ \n"

    for size in range(len(keys)):
        write_file = f"{write_file} {keys[size]} : {values[size]}\n"

    write_file = write_file+"\n"+"}"

    # write in file
    writer(filename, write_file, "w")

    return True
