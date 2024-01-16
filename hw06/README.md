# Homework 06 - Working with For Loops

## Update Star Rating App

👉🏽 **task**:  Submit an updated star_rating_app.py and README.md with justifications. 

Look at your star rating app from HW05. Would any of your loops be better written as `for` loop? Modify the code to be a for loop.

In your README.md, justify each loop as to why you thought `while` or `for` was the better implementation. 



## Data Filters

👉🏽 **task**: Complete each function in [grade_stats.py](grade_stats.py), testing each one in [test_grade_stats.py](test_grade_stats.py).


In grade_stats, you will see a main program that reads from a CSV file (comma separated value). This ends up being a large file with a fair
number of data points. Testing such a program on a large file can be difficult. As such, writing your functions and testing them on "dummy"
data is essential to development. In this task, you will work on functions that if you try to think of the program "as a whole" 
they will be complex. However, if you can focus on the one thing the function needs to do, independent of the entire program, it becomes
easier to write and test. 

> Important!  
> This doesn't exclude testing the final program. There is an entire field in computer science that focuses on unit testing and then interaction
> testing (which your whole program is a series of interactions between the units/functions). That is a more complicated process. 
> 
> For a random, "oh that is cool" moment, it is possible to represent your program as a graph and guarantee every path is tested. 
> It is expensive, and usually reserved for mission critical applications (space shuttles!) but developers who specialize in 
> testing at that level are in high demand. 


### Functions to implement

You see the function definition and documentation implemented already in grade_stats. Except for `def get_stats(year: int, col_index: int, data: Tuple, year_index: int = 0) -> str:`. The `get_stats` function ends up calling `filter_by_year`, `filter_by_col`, and then `average`. It will also make use of pythons built in `max` and `min` commands
to generate the final formatted stats string.

### Final Program Output

Once all the functions are working (hint, you should mainly be running test_grade_stats.py), you can run grade_stats.py. The output using
the provided file should look like

```text
> python .\grade_stats.py
Course Final Grade Stats By Year
2000 stats: average=71.60, max=92.01, min=43.27
2001 stats: average=72.90, max=97.57, min=47.90
2002 stats: average=72.28, max=91.49, min=58.26
2003 stats: average=72.34, max=93.30, min=46.72
```

You can also change the file that is loaded to the [simple_file.csv](simple_file.csv), and try running it with that. It is very common to take a smaller subject of a file for your final testing, so you can verify the results "by hand". 

## Reflection and Further Thinking Questions

In your README.md, add a reflection looking back and what you have learned up until this point. Additionally, answer the following questions.

* In this assignment, we used tuples and sets over lists. Why do you think that choice was made? 
* Provide an example of when you would use a list, tuple, or set - hint, when talking about lists, sets, vs tuples terms such as mutable / immutable should be used. 
* In coding, there is something called a "pure function". This is defined as:
  * the function return values are identical for identical arguments (no variation with local static variables, non-local variables, mutable reference arguments or input streams), and
  * the function has no side effects (no mutation of local static variables, non-local variables, mutable reference arguments or input/output streams).
* The question - are the functions written pure functions?
* What do you feel the advantages of pure functions are compared to functions that may mutate the arguments?
* Going through star_rating_app.py, based on your design, which functions are pure functions, and which ones have side affects?
  * Did that changes as you modified it throughout these past few weeks?

## 📝 Grading Rubric


Add (AG) and (MG) next to tiers, add major conditions to meet to pass each tier. 

1. Learning (AG)
   * average with simple tuples
   * filter_by_col with simple tuples
2. Approaching  (AG)
   * other filter commands with simple tuples
   * filter_by_col and average with harder tuples
3. Meets  (AG)
   * Style check
   * Harder test cases including tuples in different orders
4. Exceeds  (MG)
   * README.md with questions answered. 
   * Included an discussion of memory and mutable/immutable 
   * Deeper thinking on pure functions and how that affects testing
   * Code is properly commented / updated. 


AG - Auto-graded  
MG - Manually graded


## 📚 Resources
* [What is a CSV File](https://www.howtogeek.com/348960/what-is-a-csv-file-and-how-do-i-open-it/)
* [CSV File Opening in Python](https://www.tutorialspoint.com/how-to-read-csv-file-in-python) -You DO NOT have to open the CSV file, the code is provided. Just providing this resource in case you want more details. 
* [Tuple vs List Memory Management](https://www.opensourceforu.com/2021/05/memory-management-in-lists-and-tuples/)
* [Pure Functions](https://en.wikipedia.org/wiki/Pure_function)
* [Side Effect](https://en.wikipedia.org/wiki/Side_effect_(computer_science))


### Tuple vs tuple
When working with type hints, because of the way python deals with `tuple` you have to important `Tuple` which is only a type hint. The same is true for Set, List, and others. As such, don't let it confuse you when you see Tuple, you really want to think `tuple`. 