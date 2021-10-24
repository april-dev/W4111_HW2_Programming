import CSVTable
import CSVCatalog
import json
import csv
import pymysql


# Must clear out all tables in CSV Catalog schema before using if there are any present
# Please change the path name to be whatever the path to the CSV files are
# First methods set up metadata!! Very important that all of these be run properly

# Only need to run these if you made the tables already in your CSV Catalog tests
# You will not need to include the output in your submission as executing this is not required
# Implementation is provided

def reset_db():
    conn = pymysql.connect(host="127.0.0.1",
                           port=3306,
                           user="root",
                           password="april661123",
                           db="CSVCatalog")
    q = "delete from csvindexes"
    res = CSVCatalog.run_q(conn, q, args=None)
    # q = "delete from csvcolumns"
    # res = CSVCatalog.run_q(conn, q, args=None)
    # q = "delete from csvtables"
    # res = CSVCatalog.run_q(conn, q, args=None)


# reset_db()

def drop_tables_for_prep():
    cat = CSVCatalog.CSVCatalog()
    cat.drop_table("people")
    cat.drop_table("batting")
    cat.drop_table("appearances")


# drop_tables_for_prep()

# Implementation is provided
# You will need to update these with the correct path
def create_lahman_tables():
    cat = CSVCatalog.CSVCatalog()
    cat.create_table("people", "People.csv")
    cat.create_table("batting", "Batting.csv")
    cat.create_table("appearances", "Appearances.csv")


# create_lahman_tables()

# Note: You can default all column types to text
col_people = ["playerID", "birthYear", "birthMonth", "birthDay", "birthCountry", "birthState", "birthCity", "deathYear",
              "deathMonth",
              "deathDay", "deathCountry", "deathState", "deathCity", "nameFirst", "nameLast", "nameGiven", "weight",
              "height", "bats",
              "throws", "debut", "finalGame", "retroID", "bbrefID"]


def update_people_columns():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog()
    table = cat.get_table("people")
    for col in col_people:
        type = "text" if col in ["playerID", "birthCountry", "birthState", "birthCity", "deathCountry", "deathState",
                                 "deathCity", "nameFirst", "nameLast", "nameGiven", "bats", "throws", "debut",
                                 "finalGame",
                                 "retroID", "bbrefID"] else "number"
        not_null = True if col in ["playerID", "retroID", "bbrefID"] else False
        new_col = CSVCatalog.ColumnDefinition(col, type, not_null)
        table.add_column_definition(new_col)

    # print(json.dumps(table.describe_table(), indent=2))


# update_people_columns()

col_appearances = ["yearID", "teamID", "lgID", "playerID", "G_all", "GS", "G_batting", "G_defense", "G_p", "G_c",
                   "G_1b", "G_2b", "G_3b", "G_ss", "G_lf", "G_cf", "G_rf", "G_of", "G_dh", "G_ph", "G_pr"]


def update_appearances_columns():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog()
    table = cat.get_table("appearances")
    for col in col_appearances:
        type = "text" if col in ["teamID", "lgID", "playerID"] else "number"
        not_null = True if col in ["playerID", "teamID", "yearID"] else False
        new_col = CSVCatalog.ColumnDefinition(col, type, not_null)
        table.add_column_definition(new_col)

    # print(json.dumps(table.describe_table(), indent=2))


# update_appearances_columns()

col_batting = ["playerID", "yearID", "stint", "teamID", "lgID", "G", "AB", "R", "H", "2B", "3B", "HR", "RBI", "SB",
               "CS", "BB", "SO", "IBB", "HBP", "SH", "SF", "GIDP"]


def update_batting_columns():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog()
    table = cat.get_table("batting")
    for col in col_batting:
        type = "text" if col in ["playerID", "teamID", "lgID"] else "number"
        not_null = True if col in ["playerID", "stint", "yearID"] else False
        new_col = CSVCatalog.ColumnDefinition(col, type, not_null)
        table.add_column_definition(new_col)

    # table.define_index("YearID", ["yearID"], "INDEX")
    # print(json.dumps(table.describe_table(), indent=2))


# update_batting_columns()


# Add primary key indexes for people, batting, and appearances in this test
def add_index_definitions():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog()
    table_people = cat.get_table("people")
    table_people.define_index("people", ["playerID"], "PRIMARY")

    table_appearances = cat.get_table("appearances")
    table_appearances.define_index("appearances", ["yearID", "teamID", "playerID"], "PRIMARY")

    table_batting = cat.get_table("batting")
    table_batting.define_index("batting", ["playerID", "stint", "yearID"], "PRIMARY")


# add_index_definitions()


def test_load_info():
    table = CSVTable.CSVTable("people")
    print(table.__description__.file_name)


#test_load_info()

def test_get_col_names():
    table = CSVTable.CSVTable("batting")
    names = table.__get_column_names__()
    #print(names)
    print(table.__rows__)


#test_get_col_names()

def add_other_indexes():
    """
    We want to add indexes for common user stories
    People: nameLast, nameFirst
    Batting: teamID
    Appearances: None that are too important right now
    :return:
    """
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog()
    table_people = cat.get_table("people")
    table_people.define_index("last_first", ["nameLast", "nameFirst"], "INDEX")

    table_batting = cat.get_table("batting")
    table_batting.define_index("teamID", ["teamID"], "INDEX")


# add_other_indexes()

def load_test():
    batting_table = CSVTable.CSVTable("batting", True)
    print(batting_table)


#load_test()


def dumb_join_test():
    batting_table = CSVTable.CSVTable("batting")
    appearances_table = CSVTable.CSVTable("appearances")
    result = batting_table.dumb_join(appearances_table, ["playerID", "yearID"], {"playerID": "baxtemi01"},
                                     ["playerID", "yearID", "teamID", "AB", "H", "G_all", "G_batting"])
    print(result)

#dumb_join_test()


def get_access_path_test():
    batting_table = CSVTable.CSVTable("batting")
    template = ["teamID", "playerID", "yearID"]
    index_result, count = batting_table.__get_access_path__(template)
    print(index_result)
    print(count)

#get_access_path_test()


def sub_where_template_test():
    pass


# sub_where_template_test()


def test_find_by_template_index():
    # ************************ TO DO ***************************
    pass


# test_find_by_template_index()

def smart_join_test():
    # ************************ TO DO ***************************
    batting_table = CSVTable.CSVTable("batting")
    appearances_table = CSVTable.CSVTable("appearances")
    result = batting_table.__smart_join__(appearances_table, ["playerID", "yearID"], {"playerID": "baxtemi01"},
                                     ["playerID", "yearID", "teamID", "AB", "H", "G_all", "G_batting"])
    print(result)

smart_join_test()
