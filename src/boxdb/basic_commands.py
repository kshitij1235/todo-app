'''
boxdb/basic_commands -> v0.9

This file contain code for
1)row,column creation and deletion
2)and gettting table

[ ] add_row() made more faster
[ ] drop_primary_key()->added
[ ] assign_primary_key()->added
'''


from filemod import writer
from tabulate import tabulate
from boxdb.settings import PRIMARY_KEY,COLUMNS
from boxdb.support import get_content, get_primary_column, get_columns, AddFlagsToColumns
from boxdb.checkups import column_exists, primary_key_exists, check_priamary_column, table_struture_exists,check_table
from boxdb.FileWriteup import write_element_in_primary
from boxdb.logs import logWarning, loginfo, logerror


def get_table(table_name, columns=None):
    """
    It is used to display table in terminal or even filture
    out some rows according to the convience
    """
    # FIXME performance impromvement is needed

    table = []
    
    if not check_table(table_name):
        return False

    if columns is None:
        columns = get_columns(table_name)

    # get the number of columns
    content = get_columns(table_name)

    if not table_struture_exists(table_name):
        return False

    # if no column input assume it to be content
    if columns != []:
        content = columns

    # get the amount of rows in column and calculate the higest
    for column in content:
        row_content = get_content(
            f"{column}.txt", COLUMNS(table_name,column))
        table.append(row_content)
    higest_col = max(map(len, table))

    # filter the empty or half filled list to replace with null
    for item in table:
        if len(item) < higest_col:
            for _ in range(higest_col):
                if len(item) != higest_col:
                    item.append("null")

    # gets all the indivisual rows

    result = [[table[j][i]
               for j in range(len(table))] for i in range(len(table[0]))]

    # column tag to represent primary_keys
    # FIXME temperory fix for flags allocation
    processed = AddFlagsToColumns(table_name, content)

    print(tabulate(result, headers=processed, showindex='always', tablefmt="fancy_grid"),
          f"\nTable config = {len(get_columns(table_name))}x{higest_col}")
    return True


def drop_primary_key(table_name):
    """
    Remove primary key from the flag file
    """
    if not check_table(table_name):
        return False

    priamary_key = primary_key_exists(table_name)
    if not priamary_key:
        logerror(table_name, "PRIMARY KEY : does not exists")
        return False
    loginfo(table_name, "PRIMARY KEY : droped sucessfully")
    writer(PRIMARY_KEY(table_name), '', 'w')
    return True


def assign_primary_key(table_name, column):
    """
    Assign primary key in the flag file
    """
    if not check_table(table_name):
        return False

    primary_key = get_primary_column(table_name)
    if column == primary_key:
        logWarning(
            table_name, f"PRIMARY KEY: {column} is already a primary key")
        return False

    if not check_priamary_column(table_name, primary_key):
        logerror(
            table_name, "PRIMARY KEY: cannot make it a primary column due to dublication")
        return False

    if not column_exists(table_name, column):
        logerror(table_name, f"COLUMN : column {column} not in table")
        return False

    if primary_key is None:
        loginfo(
            table_name, f"COLUMN : sucessfully assigned {column} as primary key")
        write_element_in_primary(table_name, column)
        return True
    logerror(table_name, "COLUMN : primary key already present")
    return False
