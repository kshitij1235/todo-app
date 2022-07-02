
from os import remove

from filemod import(
    delete_specific_line,
    word_search_line,
    writer,
    write_specific_line,
    read_specific_line
)

from boxdb.settings import(
    PRIMARY_KEY,
    NOT_NULL,
    COLUMNS
)

from boxdb.logs import(
    logerror,
    loginfo
)

def remove_column_and_file(table_name, element):
    """
    Remove column from data file
    Remove column file
    """
    path = f"{table_name}/{table_name}_data.txt"
    delete_specific_line(path, word_search_line(path, element))
    remove(COLUMNS(table_name,element))
    return True

def remove_column_without_file(table_name, element):
    """
    Remove column from data file
    """
    path = f"{table_name}/{table_name}_data.txt"
    delete_specific_line(path, word_search_line(path, element))
    return True


def register_column(table_name, column_name):
    """
    Add column name to file
    """
    writer(f"./{table_name}/{table_name}_data.txt", f"{column_name}\n", "a")


def write_element_in_primary(table_name, element):
    """
    Push element to the primary flag
    """
    writer(PRIMARY_KEY(table_name), f"{element}", "w")


def append_element_in_not_null(table_name, element):
    """
    Push element to the not null flag
    """
    writer(NOT_NULL(table_name), f"{element}\n", "a")


def add_blank_lines_in_columns(table_name, column, times):
    """
    fill up the column with dummy lines
    """
    return writer(f"./{table_name}/tables/{column}.txt",
                  " \n"*times, "w")


def replace_column_element_with_pk_refrence(table_name,
                                            primary_columns,
                                            primary__refrence_element,
                                            column_name,
                                            replacement,
                                            target_element=None
                                            ):
    """
    Replace primary_refrence_element to element

    column_name is the targeted column where a change is the made

    were primary_column is a primary column 
    and primary_refrence_element is the refrence element to get the row number

    now we have primary column and the row number will search for the the element in 
    column_name

    if target_element no computation is needed to search from the element but itas optional

    and then will change the element from the replacement
    """

    # get the line number from the changing column
    line = word_search_line(
        COLUMNS(table_name,primary_columns), primary__refrence_element)

    if target_element is None:
        # get the name of element to change
        target_element = read_specific_line(
            COLUMNS(table_name,column_name), line-1).strip()

    # exit point check if the replacement or changing element is same
    if target_element == replacement:
        logerror(table_name,f"TABLE : Column {column_name} is already {target_element}")
        return False

    # change the element
    write_specific_line(
        f'.\\{table_name}\\tables\\{column_name}.txt', line, replacement)
    loginfo(table_name,
        f"TABLE : changes made in {column_name},from {target_element} -> {replacement}")
    return True



def write_rows_and_columns_in_file(table_name,
                                columns,
                                rows):
    """
    fills out colums according to the row inputs 
    """
    for column, row in zip(columns, rows):
        # adding rows into columns
        writer(COLUMNS(table_name,column), f"{row} \n", "a")
    loginfo(table_name, f"ROW : sucessfully added to '{table_name}'")
    return True


def delete_a_specific_row(table_name,
        rows,
        row_to_remove,
        row_element
        ):
    """
    this delete rows specified in -> row_to_remove
    row_element is specific row element to remove 

    """
    for elements in rows:
        try:
            delete_specific_line(
                COLUMNS(table_name,elements), row_to_remove)
        except Exception:
            logerror(table_name, f"ROWS : '{row_element}' not found ")
            return False
    loginfo(table_name, f"ROWS : '{row_element}' deleted sucessfully")
    return True

def remove_element_with_linenumber(table_name,column,line):
    """
    removes a specific row element from a specfic
    column by specifing the line number
    """
    return delete_specific_line(COLUMNS(table_name,column), line)
