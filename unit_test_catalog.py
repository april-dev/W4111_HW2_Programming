import pymysql

import CSVCatalog
import json

# Example test, you will have to update the connection info
# Implementation Provided
columns_batting = ["playerID", "yearID", "stint", "teamID", "lgID", "G", "AB", "R", "H", "2B", "3B", "HR", "RBI", "SB",
                   "CS", "BB", "SO", "IBB", "HBP", "SH", "SF", "GIDP"]


def reset_db():
    conn = pymysql.connect(host="127.0.0.1",
                           port=3306,
                           user="root",
                           password="april661123",
                           db="CSVCatalog")
    q = "delete from csvindexes"
    res = CSVCatalog.run_q(conn, q, args=None)
    q = "delete from csvcolumns"
    res = CSVCatalog.run_q(conn, q, args=None)
    q = "delete from csvtables"
    res = CSVCatalog.run_q(conn, q, args=None)


def create_table_test():
    reset_db()
    cat = CSVCatalog.CSVCatalog()
    # dbhost="localhost",
    # dbport=3306,
    # dbuser="root",
    # dbpw="april661123",
    # db="CSVCatalog")
    table_created = cat.create_table("Batting", "Batting.csv")

    for col in columns_batting:
        type_col = "text" if col in ["playerID", "teamID", "lgID"] else "number"
        not_null = True if col in ["playerID", "yearID", "stint"] else False
        table_created.add_column_definition(CSVCatalog.ColumnDefinition(col, type_col, not_null))

    table_created.define_index("primary", ["playerID", "yearID", "stint"], "PRIMARY")
    t = table_created.describe_table()
    print("DESCRIBE table = \n", json.dumps(t, indent=2))
    # t = cat.get_table("Batting")
    # print("Table = ", t)


#create_table_test()


def drop_table_test():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog()
    cat.drop_table("Batting")


# drop_table_test()

def add_column_test():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog()
    col = CSVCatalog.ColumnDefinition("test", "text", False)
    t = cat.get_table("Batting")
    t.add_column_definition(col)


# add_column_test()


# Implementation Provided
# Fails because no name is given
def column_name_failure_test():
    cat = CSVCatalog.CSVCatalog()
    col = CSVCatalog.ColumnDefinition(None, "text", False)
    t = cat.get_table("Batting")
    t.add_column_definition(col)


# column_name_failure_test()

# Implementation Provided
# Fails because "canary" is not a permitted type
def column_type_failure_test():
    cat = CSVCatalog.CSVCatalog()
    col = CSVCatalog.ColumnDefinition("bird", "canary", False)
    t = cat.get_table("Batting")
    t.add_column_definition(col)


# column_type_failure_test()

# Implementation Provided
# Will fail because "happy" is not a boolean
def column_not_null_failure_test():
    cat = CSVCatalog.CSVCatalog()
    col = CSVCatalog.ColumnDefinition("name", "text", "happy")
    t = cat.get_table("Batting")
    t.add_column_definition(col)


# column_not_null_failure_test()


def add_index_test():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog()
    t = cat.get_table("Batting")
    t.define_index("index_team", ["teamID"], "INDEX")


#add_index_test()


def col_drop_test():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog()
    t = cat.get_table("Batting")
    t.drop_column_definition("SH")


#col_drop_test()

def index_drop_test():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog()
    t = cat.get_table("Batting")
    t.drop_index("primary")


#index_drop_test()

# Implementation provided
def describe_table_test():
    cat = CSVCatalog.CSVCatalog()
    t = cat.get_table("Batting")
    desc = t.describe_table()
    print("DESCRIBE table = \n", json.dumps(desc, indent=2))

#describe_table_test()
