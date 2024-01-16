# Homework 10: Working with Classes

For this homework, you will be developing two classes with their supporting methods, and two support functions. The classes will work in a larger ToDo application.  When we talk about Object Oriented Programming (OOP) and design, this is actually a common situation where your purpose is to develop a set of classes that can be used (consumed) in a variety of ways in a larger application, or even multiple applications. 


## Class 1: ListItem

List item contains the information about every 'todo' item. It has the following properties:
* short_name - a short name for the item
* details - a longer description of the item, defaults to the empty string `''`
* completed - a boolean value indicating if the item is completed, defaults to `False`. This property is a 'readonly' property after the object is created, and should not be allowed to be set directly. Instead the `toggle_status(self)` method should be used to toggle the status of the item.

You will need to implement the following methods:

* `__init__(self, short_name, details='', completed=False)` - the constructor for the class. It should set the properties to the values passed in.
* `__str__(self)` - returns a string representation of the object. It should return the following format: `short_name (details) X` if the item is completed, or `short_name (details)` if the item is not completed. The `X` is a literal character, not a variable.
* `toggle_status(self)` - toggles the status of the item. If the item is completed, it should set it to not completed, and vice versa.

You may need an additional method with a decorator to help you with making completed readonly. 


### Test ListItem
The beauty of encapsulation is that you can isolate and test the entire object before moving onto the next part of the program. You should create a series of tests for the ListItem class (in a file called test_list_item.py). You need to make sure you have complete test coverage of every method in the class. Remember your edge cases. 

If you are feeling a challenge, you are free to explore unittest - it is a unit testing framework built into python. You can read more about it here: https://docs.python.org/3/library/unittest.html

An example setup using it, could be as follows:

```python
import unittest
from todo_list.py import ListItem

class TestListItem(unittest.TestCase):
    def test_str(self):
      """ Tests a string of item with no details, and not completed """
      item = ListItem('test')
      self.assertEqual(str(item), 'test ()')

__if__ == '__main__':
    unittest.main()
```

You can then run the file, and it will run every method that starts with `test` as a test. While this is **not** required, it is a powerful feature of python. In CS 5004 you will explore JUnit and unit testing in Java, and this is a great way to get a head start.

**NOTE** The bare minimum requirements is that you have a file that tests every method in the class. You can use whatever method you want to do this. The TAs will look to make sure you have complete coverage (meaning every path is tested)

## Class 2: ToDoList

The ToDoList class is a collection of ListItem objects. It has the following properties:
* name - the name of the list. This is public/able to modified directly. It should default to `"New List"` if no name is provided.
* items - this should be a  private property that is a list of ListItem objects. It should be initialized to an empty list. At no point should anyone be able to access the items *outside* of the class.

The ToDoList class should have the following methods:
* `size(self)` - returns the total number of items in the list
* `add_item(self, item: ListItem)` - adds an item to the list. It should check to make sure the item is a ListItem object, and if not, raise a TypeError. You may need to research the `isinstance` function to do this.
* `remove_item(self, item: ListItem)` - removes an item from the list. 
* `get_item(self, index: int)` - returns the item at the specified index. If the index is out of range, it should raise an IndexError (which is the default behavior of python lists, so nothing additional to add). 
* `find_item(self, short_name: str)` - returns the first item in the list that matches the short_name. If no item is found, it should return None. If you are choosing to use typing for a return type, you can use the optional typing syntax to indicate that it can return None. It would look like:
  ```python
  def find_item(self, short_name: str) -> Optional[ListItem]:
   ...
  ```
* `__str__(self)` - returns a string representation of the list. However, in this case, it will only print the list name and number of items in the following format. With name replaced by the name of the list, and # replaced by the number of items in the list.
  ```
  Name (# items)
  ```

Overall, this list acts like a container protecting the underlying python list by controlling access through the provided methods. 

### Test Class ToDoList
As with ListItem, you should write a test class (test_todo_list.py) to test the ToDoList class. You should make sure you have complete test coverage of every method in the class. Remember your edge cases.

If you are using unittest, you can test exceptions with the `assertRaises` method in unit test. For example:
```python
 def test_add_item_raises_type_error(self) -> None:
        """Test the TodoList add_item method raises a TypeError"""
        todo_list = TodoList("test list")
        with self.assertRaises(TypeError):
            todo_list.add_item("testing with a string")
```

As mentioned unittest it not required, but having complete code coverage is required. 


## Supporting Functions
Additionally, you will want to add two additional *functions* to todo_list.py. These functions will be used to read and write the list to a file.

* `load_list_from_file(filename: str) -> TodoList` - this function should read the file specified by filename, and return a TodoList object. The file will be a CSV file, with the following format:
  ```
  short_name,details,completed
  ```
  There is no header, and all the lines will be the data. Each row represents a ListItem. The completed column will be a boolean value, either `True` or `False`.  Though it will actually come in as a string, so you will need to convert it to a boolean.

  The name of the file is the name of the list, minus the .csv part. So if the file name was ShoppingList.csv, the list would be called ShoppingList. 

* `save_list_to_file(list: TodoList) -> None` - this function should write the list to a file. The file name should be the name of the list, with a .csv extension. The format of the file should be the same as the load function, writing each property of the ListItem on a separate line.


A sample file might look like this:
```
milk,2%,False
eggs,dozen,False
bread,white,True
```

While you can manage the CSV file yourself, you may want to look into the csv module. It has a reader and writer that will make this much easier. You can read more about it here: https://docs.python.org/3/library/csv.html or at the links below in resources. Either is fine. 

### Test Load/Save Functions
Make sure to have tests for your load and save functions!


## Putting it together
Now that you have done part, you can put it all together with [app.py](app.py) and [view.py](view.py). The program isn't the fanciest program in the world, and you can definitely find ways to improve it. However, the main goal was to
look at writing classes, making sure they are fully tested, and then using them in a program.

You will want to look through the code (and even) run it to see how it works with your classes. Afterwards, there are a number of questions you should answer in a README.md file that you will need to submit with your code.


## README.md Questions

1. The ToDoList class encloses a python list. What are some advantages and disadvantages of this approach? 
2. Which file(s) contains your print() and input() statements? What is the advantage of this design, both for testing and future implementation?
3. It is actually common to store the various function in view, into their own class. You can then setup that object for the rest of the application to use. Why would this be a common design choice? Think about it in terms of testing, and also changing what your view is doing.
4. There was one method in the ToDoList class in which the 'coverage' of cases was not fully defined, and potentially could have caused errors in the program. What method was it, and what are some issues you may have uncovered?
5. What are some features you would want to add to this application? (just getting you to ideate / dream about things)
6. If we wanted to change the ToDoList to behave more like a `Stack` (Module 11), what functions would we want to change? What would we need to add? What would we need to remove?
7. Why did we create the ListItem in the ToDoList instead of just letting the outside code pass in an already existing ListItem? What are the advantages and disadvantages of this approach? Hint: think about memory, and concerns with memory!
8. Describe Encapsulation in your own words. How did you use it in this project?
9. BONUS: In print list, you will notice an odd combination of for loops:
   ```python
   print(todolist)
   for i in range(0, todolist.size()):
      print(f'{i+1}. {todolist.get_item(i)}')
   ```   
   This isn't a very "python" way to do this, really we would want it to look like
   ```python
   print(todolist)
   for i, item in enumerate(todolist):
      print(f'{i+1}. {item}')
   ```
   However, for that to to work, we have to add some built in methods we would have implement `__iter__` and `__next__`. What are these methods, and what do they do? Why do we need them to make the above code work? - and a **stretch problem/goal**, can you modify your ToDoList class to include them, and then modify the code in print_list()? (be careful to not change your other methods)


There is a lot of power beyond python, and building your own objects (types!). You will further explore this power in CS 5004, but with another OOP focused language, Java.


## 📝 Grading Rubric

This is a two week assignment, so you will want to make sure you are working on it each week.


1. Learning (AG)
   * ListItem - created and most methods implemented
2. Approaching  (AG)
   * ToDoList - created and most methods implemented
3. Meets  (AG)
   * Edge cases and harder cases for both ListItem and ToDoList
   * Code Style Check
4. Exceeds  (MG)
   * Code is fully documented (docstring)
   * Test coverage is complete for classes
   * Questions answered in README.md correctly


AG - Auto-graded  
MG - Manually graded


## 📚 Additional Resources
* isInstance() - https://docs.python.org/3/library/functions.html#isinstance
* isinstance() - https://www.w3schools.com/python/ref_func_isinstance.asp
* isinstance() - https://www.geeksforgeeks.org/python-isinstance-method/
* Python UnitTesting - https://www.geeksforgeeks.org/unit-testing-python-unittest/
* Real Python UnitTesting - https://realpython.com/python-testing/
* Python CSV Reader - https://docs.python.org/3/library/csv.html
* Python CSV Tutorial - https://www.geeksforgeeks.org/reading-writing-csv-files-python/
* Python CSV Tutorial - https://www.w3schools.com/python/python_csv.asp
 