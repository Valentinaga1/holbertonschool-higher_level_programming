# 0x00. Python - Hello, World

- About this project:
- How to use the Python interpreter
- How to print text and variables using print
- How to use strings
- What are indexing and slicing in Python
- What is the official Holberton Python coding style and how to check your code with PEP 8

## Requirements
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file at the root of the holbertonschool-higher_level_programming repo, containing a description of the repository
- A README.md file, at the root of the folder of this project, is mandatory
- Your code should use the PEP 8 style (version 1.7.*)
- All your files must be executable

## File Descriptions

### Mandatory

### [0-run](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x00-python-hello_world/0-run "0-run")
Shell script that runs a Python script.  
The Python file name will be saved in the environment variable $PYFILE  

### [1-run_inline](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x00-python-hello_world/1-run_inline "1-run_inline")  
Shell script that runs Python code. 
The Python code will be saved in the environment variable $PYCODE

### [2-print.py](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x00-python-hello_world/2-print.py "2-print.py")
Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.  
Use the function print.  

### [3-print_number.py](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x00-python-hello_world/3-print_number.py "3-print_number.py") 
Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.  
Source code: https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py
The output of the script should be:  
- the number, followed by Battery street,
- followed by a new line.  
You are not allowed to cast the variable number into a string.  
Your code must be 3 lines long.  
You have to use the new print numbers tips (with .format(...)).  

### [4-print_float.py](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x00-python-hello_world/4-print_float.py "4-print_float.py")
Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.

You can find the source code here: https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py  
The output of the program should be:  
- Float:, followed by the float with only 2 digits.  
- followed by a new line.  
You are not allowed to cast number to string.  
You have to use the new print formatting tips (with .format(...)).  

### [5-print_string.py](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x00-python-hello_world/5-print_string.py "5-print_string.py")
Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.

You can find the source code here: https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py
The output of the program should be:  
- 3 times the value of str.  
- followed by a new line.  
- followed by the 9 first characters of str.  
- followed by a new line.  
You are not allowed to use any loops or conditional statement.  
Your program should be maximum 5 lines long.  

### [6-concat.py](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x00-python-hello_world/6-concat.py "6-concat.py") 
Complete this source code to print Welcome to Holberton School!  

- You can find the source code here:https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py
- You are not allowed to use any loops or conditional statements.  
- You have to use the variables str1 and str2 in your new line of code.  
- Your program should be exactly 5 lines long.  

### [7-edges.py](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x00-python-hello_world/7-edges.py "7-edges.py")
Complete this source code:  

- You can find the source code here:https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py  
- You are not allowed to use any loops or conditional statements.  
- Your program should be exactly 8 lines long.  
- word_first_3 should contain the first 3 letters of the variable word.  
- word_last_2 should contain the last 2 letters of the variable word.  
- middle_word should contain the value of the variable word without the first and last letters.  

### [8-concat_edges.py](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x00-python-hello_world/8-concat_edges.py "8-concat_edges.py")
Complete this source code to print object-oriented programming with Python, followed by a new line.  

- You can find the source code here: https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py  
- You are not allowed to use any loops or conditional statements.  
- Your program should be exactly 5 lines long.  
- You are not allowed to create new variables.  
- You are not allowed to use string literals.  

### [9-easter_egg.py](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x00-python-hello_world/9-easter_egg.py "9-easter_egg.py")
Write a Python script that prints The Zen of Python, by TimPeters, followed by a new line.  

- Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)

### [10-check_cycle.c](https://github.com/Valentinaga1/holbertonschool-higher_level_programming/tree/master/0x00-python-hello_world/10-check_cycle.c "10-check_cycle.c") 
#### Technical interview preparation:

- You are not allowed to google anything  
- Whiteboard first  
- This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solutions runtime fast enough, does your solution require extra memory usage / mallocs, etc.  

Write a function in C that checks if a singly linked list has a cycle in it.      
- Prototype: int check_cycle(listint_t *list);  
- Return: 0 if there is no cycle, 1 if there is a cycle  

Requirements:  
- Only these functions are allowed: write, printf, putchar, puts, malloc, free  