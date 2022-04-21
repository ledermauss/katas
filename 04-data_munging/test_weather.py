from weather import *


def test_get_columns():
    header =  "head1   head2   head3"
    indexes = [Column("head1", 0, 4),
        Column("head2", 8, 12),
        Column("head3", 16, 20)]
    assert get_columns(header) == indexes


def test_get_content_starts():
    header =  "head1   head2   head3"
    starts = [0, 8, 16]
    assert get_content_starts(header) == starts


def test_get_content_ends():
    header =  "head1   head2   head3"
    starts = [4, 12, 20]
    assert get_content_ends(header) == starts


def test_read_dataframe():
    input_df = ["head1  head2",
            "1        2"]
    assert read_dataframe(input_df) == DataFrame([Column("head1", 0, 4, [1]), 
        Column("head2", 7, 11, [2])])


def test_get_content_indexes():
    header =  "head1   head2   head3"
    indexes = [(0, 4),
        (8, 12),
        (16, 20)]



def test_assign_content_to_columns():
    columns = [Column("head1", 0, 4), 
        Column("head2", 7, 11)]
    line =  "1                 "
    assert assign_content_to_columns(columns, line) == [Column("head1", 0, 4, [1]), 
        Column("head2", 7, 11, [None])]


def test_assign_content_to_columns_parsing():
    columns = [Column("head1", 0, 4), 
        Column("head2", 7, 11)]
    line =  "1*       XX         "
    assert assign_content_to_columns(columns, line) == [Column("head1", 0, 4, [1.0]), 
        Column("head2", 7, 11, ["XX"])]


def test_parsing():
    assert parse_content("3") == 3.0
    assert parse_content("3*") == 3.0
    assert parse_content("HH") == "HH"


def test_content_is_in_column():
    assert content_is_in_column(2, 3, 0, 10) is True


def test_content_is_in_column_shifted_left():
    assert content_is_in_column(0, 3, 2, 10) is True


def test_content_is_in_column_shifted_right():
    assert content_is_in_column(2, 20, 0, 10) is True


def test_content_is_not_in_right_column():
    assert content_is_in_column(2, 3, 5, 10) is False


def test_compute_temperature_spread():
    df = DataFrame([
        Column("head1", 0, 4, [None, None, None]), 
        Column("max", 7, 11, [1,2,3]), 
        Column("min", 8, 12, [6,5,4])
        ])
    assert df.max("max") == 3
    assert df.min("min") == 4


def test_column_eq():
    col1 =  Column("col", 0, 1, [0])
    col2 =  Column("col", 0, 1, [0])
    assert col1 == col2


def test_column_neq():
    col1 =  Column("col", 0, 1, [0])
    col2 =  Column("col", 0, 1, [])
    assert col1 != col2

def test_get_df_names():
    df = DataFrame([
        Column("head1", 0, 4, [None, None, None]), 
        Column("max", 7, 11, [1,2,3]), 
        Column("min", 8, 12, [6,5,4])
        ])
    assert df.column_names == ["head1", "max", "min"]
