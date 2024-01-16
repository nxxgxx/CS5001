"""
Homework 2: Star Rating App Version 2
===========================
Course:   CS 5001
Semester: UPDATE
Student:  SOLUTION

A simple movie rating display.
"""


def main():
    """Asks a client for a  moving and rating. 
    The rating must be between 1 & 5, and sets stars equal to that number.
    Prints out 

    Movie      stars

    There are always five spaces after the movie name. 

    If a client enters a value less than 1 or more than 5, it will 
    assume 1 and 5 respectively.

    Examples:
        In this example the client enters Thor and 3
        >>> main()    # doctest: +NORMALIZE_WHITESPACE
        Enter a movie:  Thor
        Rate between 1 and 5:  3  
        Thor     ***

        In this next example, client enters 5 (admittedly too few stars)
        >>> main()   # doctest: +NORMALIZE_WHITESPACE
        Enter a movie: Princess Bride
        Rate between 1 and 5: 5
        Princess Bride     *****
    """
    pass # move and add code here


# This block of "magic" informs the python interpreter
# to start executing code in the main() function
# when the file is loaded.
# Since you now know if statements, it is saying,
# "if this the main file being executed, call the main function()"
if __name__ == "__main__":
    main()
