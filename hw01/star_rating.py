"""
Homework 1: Star Rating App
===========================
Course:   CS 5001
Semester: UPDATE
Student:  YOUR NAME
                             
A simple assignment to practice string concatenation.  
""" 
# The block above is a docstring (short for document string). 
# It starts at the triple double quote, 
# and ends at the triple double quote
# Make sure you update it by modifying semester and your name
# Follow the instructions found at https://github.com/CS5001-khoury/HW1-Welcome


def one_star():
    """sets a single * to the variable stars."""
    stars = '' #change me
    return stars 


def two_star():
    """sets two * to the variable stars."""
    stars = '' #change me
    return stars


def three_star():
    """sets three * to the variable stars."""
    stars = ''  # change me
    return stars


def four_star():
    """sets four * to the variable stars."""
    stars = ''  # change me
    return stars

def five_star():
    """sets five * to the variable stars."""
    stars = ''  # change me
    return stars


def main():
    # fix me
    print("1 star rating:" + one_star())
    print("2 star rating:" + two_star())
    print("3 star rating:" + three_star())
    print("3 star rating:" + four_star())
    print("3 star rating:  " + five_star())
    ## also you could do the following
    rating = five_star()
    print(f"\n\nMy star rating is {rating}")  # look up format strings!
    ## print _two_ blank lines here


    ### something cool about docstrings
    help(five_star)


# This block of "magic" informs the python interpreter to start executing code in the main() function
# when the file is loaded.
if __name__ == "__main__":
    main()

