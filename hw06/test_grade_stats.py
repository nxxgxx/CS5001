"""
Homework 6: Test Class Stats
===========================
Course:   CS 5001
Student:  UPDATE
Semester: UPDATE

A file to test every function in grade_stats.py
"""
import grade_stats

## when you import it this way, you need to include the name on the call
## so for example

def test_average_empty_list():
    """Tests average with an empty list, to make sure it doesn't blow up"""
    value = grade_stats.average(tuple()) #pass in an empty tuple
    if value != 0:
        print("Failed test_average_empty_list()")
        return 1
    return 0

def test_average_simple_list():
    """Tests average with an empty list, to make sure it doesn't blow up"""
    value = grade_stats.average(tuple([2, 2, 2])) #pass in an empty tuple
    if value != 2:
        print("Failed test_average_simple_list()")
        return 1
    return 0




def main():
    print("Running tests")
    fail_count = 0
    fail_count += test_average_empty_list()
    fail_count += test_average_simple_list()



    print(f"Failed {fail_count} tests")



if __name__ == "__main__":
    main()