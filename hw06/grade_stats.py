"""
Homework 6: Class Stats
===========================
Course:   CS 5001
Student:  UPDATE
Semester: UPDATE

This simple application helps figure out the stats of a course exam file
"""
from typing import Tuple, Set
import csv

# uncomment and comment to try different files
DATA_FILE = "exam_grades.csv"
#  DATA_FILE = "simple_file.csv"


def average(data: Tuple[float]) -> float:
    """Calculates the average value for a range of values

    See:
      len(list)
      sum(list)

    Args:
        data (Tuple[float]): a range of values in a tuple

    Returns:
        float: the average, if len(data) is 0, returns 0
    """
    return 0


def filter_by_col(index: int, data: Tuple) -> Tuple:
    """Given a list of lists (tuple of tuples),
    it will pull a single column out of the lists.


    For example:

        Given the following tuple
        ((1, 2, 3),
         (4, 5, 6),
         (7, 8, 9))

        >>>filter_by_col(1, ((1, 2, 3),(4, 5, 6), (7, 8, 9)))
        (2, 5, 8)
        >>>filter_by_col(0, ((1, 2, 3),(4, 5, 6), (7, 8, 9)))
        (1, 4, 7)


    Args:
        index (int): column index, assumes all inner lists have it
        data (Tuple): a tuple of tuples with each inside list the same length

    Returns:
        Tuple: a tuple of values that exist in that index
    """
    return ()


def filter_by_year(year: int, data: Tuple, year_index: int = 0) -> Tuple[Tuple]:
    """Takes a grades tuple of tuples, and pulls
    out every row that matches the year given.


    Args:
        year (int): year
        data (Tuple[Tuple]): A tuple of tuples with year being a defining characteristic
        year_index (int, optional): column year is in. Defaults to 0.

    Returns:
        Tuple[Tuple]: a "filtered" list containing only the rows with year
    """
    return ()


def get_all_years(data: Tuple[Tuple], year_index: int = 0) -> Set:
    """Looks through a grades list, and grabs all *unique* years.

    Args:
         data (Tuple[Tuple]): A tuple of tuples with year being a defining characteristic

    Returns:
        Set: a unique set of years
    """
    return set()


def get_stats(year: int, col_index: int, data: Tuple, year_index: int = 0) -> str:
    """Generates a string of stats for a given year and a provided dataset

    Args:
        year (int): the  year to grab
        col_index (int): the column to look at
        data (Tuple): the dataset which is a tuple of tuples
        year_index (int, optional): the index to look at. Defaults to 0.

    Returns:
        str: in format of:   f"{year:.0f} stats: average={avg:.2f}, max={mx:.2f}, min={mn:.2f}"
    """
    return ""


# We will not use this main, so you may modify it


def main():
    grades, fields = get_grades(DATA_FILE)
    year_index = fields.index("year")
    years = get_all_years(grades, year_index=year_index)
    col_index = fields.index("course_grade")  ## can assume match
    print("Course Final Grade Stats By Year")
    year_stat = [get_stats(year, col_index, grades, year_index) for year in years]
    print("\n".join(year_stat))


# DO NOT MODIFY
# Doing this here, so you have more data to work with.
# you may 'hard code' data for your tests to make sure things are working
def get_grades(file: str) -> Tuple[Tuple[Tuple], Tuple]:
    """Reads a Comma Separated Value file and dumps the contents
    into a tuple of tuples. Converts all numbers to floats.

    File contents could look like

    ((2000.0, 84.5, 69.5, 86.5, 76.2564),
     (2000.0, 80.0, 74.0, 67.0, 75.3882),
     (2000.0, 56.0, 70.0, 71.5, 67.0564),
     (2000.0, 64.0, 61.0, 67.5, 63.4538))

    Will also return matching field names
    ('year', 'exam1', 'exam2', 'exam3', 'course_grade')

    Returns:
        Tuple[Tuple[Tuple[int, int, int, int, int]], Tuple]: The first
        of the tuple is the file contents convert to flow, the second value
        is a tuple of the field names as strings.
    """
    contents = []
    with open(file) as csv_file:
        csv_read = csv.reader(csv_file, delimiter=",")
        fields = next(csv_read)  # skip the first row
        for row in csv_read:
            contents.append(tuple([float(x) for x in row]))

        return tuple(contents), tuple(fields)


if __name__ == "__main__":
    main()
