""" 

This is the main view for the application. It is responsible for
displaying the information to the client, and getting input from the client.
"""
from enum import Enum
import sys
from . import todo_list
from typing import Tuple
from string import punctuation

class ViewOptions(Enum):
    """ The options for the view """
    EXIT = 1
    LIST = 2
    ADD = 3
    REMOVE = 4
    COMPLETE = 5
    SAVE = 6
    LOAD = 7
    NEW = 8
    UNKNOWN = 9



def print_welcome() -> None:
    """ Print the welcome message """
    print('Welcome to the TODO List Manager')
    print('Type "help" to get a list of commands.')
    print()

def print_goodbye() -> None:
    """ Print the goodbye message """
    print('Goodbye')

def print_error(message: str) -> None:
    """ Print an error message
    Args:
        message (str): error message to print
    """
    print(f'Error: {message}', file=sys.stderr)

def print_list(todolist: todo_list.TodoList) -> None:
    """ Print the list
    Args:
        todo_list (TodoList): list to print
    """
    print(todolist)
    for i in range(0, todolist.size()):
        print(f'{i+1}. {todolist.get_item(i)}')

def print_menu() -> None:
    """ Print the menu """
    print('Type any of the following commands. You can also type the number.')
    print('1. Exit - exit the program. It will save the list if one is loaded')
    print('2. List - list the todo item in a list (if a list has been loaded)')
    print('3. Add - add a todo item to the list, you can follow it with the item. For example "add buy coconuts"')
    print('4. Remove - remove a todo item from the list, you can follow it with the item. For example "remove buy coconuts')
    print('5. Complete - complete a todo item from the list, you can follow it with the item. For example "complete buy coconuts')
    print('6. Save - save the list to a file.')
    print('7. Load - load a list from a file. You can also put the file name after the command. For example "load shopping_list.csv')
    print('8. New - create a new list, can be combined with the name of the list. For example "new shopping_list"')

def get_filename() -> str:
    """ Get the filename from the user
    Returns:
        str: filename
    """
    filename = input('Enter a filename: ').strip()
    if filename.endswith('.csv'):
        return filename
    else:
        print_error('Filename must end with .csv')
        return get_filename()
    
def get_list_name() -> str:
    """ Get the list name from the user. 

    The name may not contain any punctuation or spaces.
    Returns:
        str: list name
    """
    name = input('Enter a list name: ').strip()
    if any(char in name for char in punctuation) or ' ' in name:
        print_error('List name may not contain punctuation or spaces')
        return get_list_name()
    else:
        return name

def get_add_info() -> Tuple[str, str]:
    """ Get the information for adding a todo item
    Returns:
        tuple: (name, description)
    """
    name = input('Enter the name of the item: ').strip()
    description = input('Enter the description of the item (hit return for blank): ').strip()
    return (name, description)

def get_item_query() -> str:
    """ Get the item to query for
    Returns:
        str: item to query for
    """
    return input('Enter the item name or index value: ').strip()

def get_command() -> Tuple[ViewOptions, Tuple]:
    """ Get the command from the user
    Returns:
       tuple: command, args (if any)
    """
    command = input('What would you like to do? ').strip()
    if ' ' in command:
        command, *args = command.split(' ')
    else:
        args = []
    args = tuple(args)
    command = command.lower()    
    if command == 'exit' or command == '1':
        return (ViewOptions.EXIT, args)
    elif command == 'list' or command == '2':
        return (ViewOptions.LIST, args)
    elif command == 'add' or command == '3':
        return (ViewOptions.ADD, args)
    elif command == 'remove' or command == '4':
        return (ViewOptions.REMOVE, args)
    elif command == 'complete' or command == '5':
        return (ViewOptions.COMPLETE, args)
    elif command == 'save' or command == '6':
        return (ViewOptions.SAVE, args)
    elif command == 'load' or command == '7':
        return (ViewOptions.LOAD, args)
    elif command == 'new' or command == '8':
        return (ViewOptions.NEW, args)
    else:
        return (ViewOptions.UNKNOWN, args)