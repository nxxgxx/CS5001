# Homework 01 - Submission


* Student: YOUR NAME
* Semester: SEMESTER

## Common

* List any coding practice problems you completed, feel free to comment at needed (did it help, was it too easy, etc):

* List any other resources you used to help you complete the assignment (make sure to share good ones to the Tips,Tricks, and Resources channel in teams!):
  

## Module Specific
For all these questions, it is recommended you open up IDLE or the python interpreter and try out the code.  You can also use the python visualizer to help you visualize the code.  You can find the visualizer here: [http://www.pythontutor.com/visualize.html#mode=edit](http://www.pythontutor.com/visualize.html#mode=edit)


1. In IDLE shell or python interpreter directly, try the following code:
   ```python
   x = 10 + "5"
   ```

    a. What is the error message you get?  (copy and paste it below - you don't need to include the Traceback lines, just the error message including type of error)
    
    b. Describe in your own words the error message. What does it mean?  (you can use the internet to help you, but make sure to cite your source)

    c. There are multiple ways this error can be fixed. However, converting between types is common, and it is called "casting" (think of actors on a stage). Take time to research online how to cast between types in python.  What is the correct way to cast the string "5" to an `int`?  Write code below in the block below
    ```python
    # write your code here
    
    ```
    * Note: for HW02 we will return to casting, as it is common to take in client input as a string, and convert it to another type for processing.

2. Match the value with the correct type for `x`. Your options for types are `int`, `float`, `str`:  
   Example: x = 1.0 : float
   * x = 1
   * x = "1"
   * x = 1.0 + 1 
   * x = str(1.0)
   * x = int(1 / 2)   
    You can use the following code in the interpreter to help you:  
    ```python
    x = int(1/2)
    print(x)
    type(x)
    ```

3. In the `x = int(1 / 2)` example, what is the value of x? Why? (once again you may need to research, just cite sources)

4. If we wanted to force a range between 0 and `n-1` (let's say 6), but I could have any number as my variable. What operator would use? Why? Please write some code to show this! If you included prints in your code to test this, also include that in your code copy below. 
   ```python
   # for example
   x = 102
   r = x ?? 6 ## with ?? being the operator you use
   ## your code below this line

   ```

5. The above is one of the unique properties of the operator you just listed. It enforces a range between 0 and `n` exclusive of n. There are a number of advantages of this that you will uncover during your CS career, and to think, it ties back to elementary school mathematics (and arguably why it is hard for us to remember it!). Can you list some real world cases/examples where you could see using this operator, as usually you are free to research just cite sources. You only need one example, but you are encouraged to come up with more. 

6. The files all have docstrings with their functions. How does this help the programmer? Beyond just reading the file, what is the command you can use to pull up the docstring of any function? (you can use the internet to help, but if you look at the bottom of the star_rating.py, you may get an idea of the command name). Use the command on print to see the docstring.  Write the command below, and the printed below that. 
   ```python
   # write your command here
   ```


## Deeper Thinking

 For star_rating and hobby_card, we built strings and then printed out the results. Why would we want to build strings, and then print out the results, than just printing out the results directly? Don't need a correct answer, but we encourage you to ponder this question and come up with reasons on why this would be a good design pattern.  Write your answer below. 
