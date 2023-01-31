#!/usr/bin/env python
# coding: utf-8

# # Quickstart: zero to Python
# 
# Taken and modified from https://foundations.projectpythia.org/foundations/getting-started-python.html

# ## Interactively (demo)

# To run Python code interactively, one can use the standard Python prompt, which can be launched by typing ``python`` in your standard shell:
# 
#     $ python
#     Python 3.4.1 (default, May 21 2014, 21:17:51) 
#     [GCC 4.2.1 Compatible Apple Clang 4.1 ((tags/Apple/clang-421.11.66))] on darwin
#     Type "help", "copyright", "credits" or "license" for more information.
#     >>>
# 
# The ``>>>`` indicates that Python is ready to accept commands. If you type ``a = 1`` then press enter, this will assign the value ``1`` to ``a``. If you then type ``a`` you will see the value of ``a`` (this is equivalent to ``print a``):
# 
#     >>> a = 1
#     >>> a
#     1
# 
# The Python shell can execute any Python code, even multi-line statements, though it is often more convenient to use Python non-interactively for such cases.
# 
# The default Python shell is limited, and in practice, you will want instead to use the IPython (or interactive Python) shell. This is an add-on package that adds many features to the default Python shell, including the ability to edit and navigate the history of previous commands, as well as the ability to tab-complete variable and function names. To start up IPython, type:
# 
#     $ ipython
#     Python 3.4.1 (default, May 21 2014, 21:17:51) 
#     Type "copyright", "credits" or "license" for more information.
# 
#     IPython 2.1.0 -- An enhanced Interactive Python.
#     ?         -> Introduction and overview of IPython's features.
#     %quickref -> Quick reference.
#     help      -> Python's own help system.
#     object?   -> Details about 'object', use 'object??' for extra details.
# 
#     In [1]:
# 
# The first time you start up IPython, it will display a message which you can skip over by pressing ``ENTER``. The ``>>>`` symbols are now replaced by ``In [x]``, and output, when present, is prepended with ``Out [x]``. If we now type the same commands as before, we get:
# 
#     In [1]: a = 1
# 
#     In [2]: a
#     Out[2]: 1
# 
# If you now type the up arrow twice, you will get back to ``a = 1``.

# ## Running scripts (demo)

# While the interactive Python mode is very useful to exploring and trying out code, you will eventually want to write a script to record and reproduce what you did, or to do things that are too complex to type in interactively (defining functions, classes, etc.). To write a Python script, just use your favorite code editor to put the code in a file with a ``.py`` extension. For example, we can create a file called ``test.py`` containing:
# 
#     a = 1
#     print(a)
# 
# On Linux computers you can use for example the ``emacs`` editor which you can open by typing:
#     
#     emacs &
#     
# (ignore the warnings that it prints to the terminal).
# 
# We can then run the script on the command-line with:
# 
#     $ python test.py
#     1
# 
# Note: The ``print`` statement is necessary, because typing ``a`` on its own will only print out the value in interactive mode. In scripts, the printing has to be explicitly requested with the print command. To print multiple variables, just separate them with a comma after the print command:
# 
#     print(a, 1.5, "spam")

# # Using the IPython notebook

# The IPython *notebook* is allows you to write notebooks similar to e.g. Mathematica. The advantage of doing this is that you can include text, code, and plots in the same document. This makes it ideal for example to write up a report about a project that uses mostly Python code, in order to share with others. In fact, the notes for this course are written using the IPython notebook!

# Click on ``New Notebook`` on the right, which will start a new document. You can change the name of the document by clicking on the **Untitled** name at the top and entering a new name. Make sure you then save the document (make sure that you save regularly as you might lose content if you close the browser window!).
# 
# At first glance, a notebook looks like a fairly typical application - it has a menubar (File, Edit, View, etc.) and a tool bar with icons. Below this, you will see an empty cell, in which you can type any Python code. You can write several lines of code, and once it is ready to run, you can press shift-enter and it will get executed:

# In[ ]:


a = 1
print(a)


# You can then click on that cell, change the Python code, and press shift-enter again to re-execute the code. Once you have executed a cell once, a new cell will appear below. You can again enter some code, then press shift-enter to execute it.

# ## Text

# It is likely that you will want to enter actual text (non-code) in the notebook. To do this, click on a cell, and in the drop-down menu in the toolbar, select 'Markdown'. This is a specific type of syntax for writing text. You can just write text normally and press shift-enter to *render* it:
# 
#     This is some plain text
# 
# To edit it, double click on the cell. You can also enter section headings using the following syntax:
# 
#     This is a title
#     ===============
# 
#     This is a sub-title
#     -------------------
# 
# which will look like:
# 
# This is a title
# ===============
# 
# This is a sub-title
# -------------------
# 
# Finally, if you are familiar with LaTeX, you can enter equations using:
# 
#     $$E = m c^2$$
# 
# on a separate line, or:
# 
#     The equation $p=h/\lambda$ is very important
# 
# to include it in a sentence. This will look like:
# 
# $$E = m c^2$$
# 
# The equation $p=h/\lambda$ is very important
# 
# For more information about using LaTeX for equations, see [this guide](http://en.wikibooks.org/wiki/LaTeX/Mathematics).

# ## A very first Python program
# 
# A Python program can be a single line:

# In[ ]:


print("Hello interweb")


# ## Loops in Python

# Why not make a `for` loop with some formatted output:

# In[ ]:


for n in range(3):
    print(f"Hello interweb, this is iteration number {n}")


# A few things to note:
# 
# - Python defaults to counting from 0 (like C) rather than from 1 (like Fortran).
# - Function calls in Python always use parentheses: `print()`
# - The colon `:` denotes the beginning of a definition (here of the repeated code under the `for` loop.
# - Code blocks are identified through indentations.
# 
# To emphasize this last point, here an example with a two-line repeated block:

# In[ ]:


for n in range(3):
    print("Hello interweb!")
    print(f"This is iteration number {n}.")
print('And now we are done.')


# In[ ]:


n = [2, 3, 5, 7]
for e in n:
    print(e)


# > Please avoid Matlab-like for statements with range

# In[ ]:


for e in range(len(n)):
    print(n[e])


# In[ ]:


m = range(5)  # m = [0, 1, 2, 3, 4]
for _ in m:
    print("hola")


# In[ ]:


for index, value in enumerate(n):
    print("The value of index ", index, " is ", value)


# ## Basic flow control
# 
# Like most languages, Python has an `if` statement for logical decisions:

# In[ ]:


if n > 2:
    print("n is greater than 2!")
else:
    print("n is not greater than 2!")


# In[ ]:


x = 15

if x == 0:
    print(x, "is zero")
elif (x > 0) and (x < 10):
    print(x, "is between 0 and 10")
elif (x > 10) and (x < 20):
    print(x, "is between 10 and 20")
else:
    print(x, "is negative")
print("Hello world")


# Python also defines the `True` and `False` logical constants:

# In[ ]:


n > 2


# In[ ]:


result = 4 < 5
print(result)


# There's also a `while` statement for conditional looping:

# In[ ]:


m = 0
while m < 3:
    print(f"This is iteration number {m}.")
    m += 1
print(m < 3)


# ## Basic Python data types
# 
# Python is a very flexible language, and many advanced data types are introduced through packages (more on this below). But some of the basic types include: 

# ## Built-In Types

# | Type        | Example        | Description                                                  |
# |-------------|----------------|--------------------------------------------------------------|
# | ``int``     | ``x = 1``      | integers (i.e., whole numbers)                               |
# | ``float``   | ``x = 1.0``    | floating-point numbers (i.e., real numbers)                  |
# | ``complex`` | ``x = 1 + 2j`` | Complex numbers (i.e., numbers with real and imaginary part) |
# | ``bool``    | ``x = True``   | Boolean: True/False values                                   |
# | ``str``     | ``x = 'abc'``  | String: characters or text                                   |
# | ``NoneType``| ``x = None``   | Special object indicating nulls                              |

# ### Integers (`int`)
# 
# The number `m` above is a good example. We can use the built-in function `type()` to inspect what we've got in memory:

# In[ ]:


m = 4


# In[ ]:


type(m)


# ### Floating point numbers (`float`)
# 
# Floats can be entered in decimal notation:

# In[ ]:


type(0.1)


# In[ ]:


n = int(3.5 / 2)


# In[ ]:


n


# In[ ]:


type(n)


# or in scientific notation:

# In[ ]:


type(4e7)


# where `4e7` is the Pythonic representation of the number $ 4 \times 10^7 $.

# ### Character strings (`str`)
# 
# You can use either single quotes `''` or double quotes `" "` to denote a string:

# In[ ]:


type("orange")


# In[ ]:


type('orange')


# <center> <img src="img/list-indexing.png" width="1600"/> </center>

# In[ ]:


p = 'orange'


# In[ ]:


p[-1]


# In[ ]:


message = "what do_you-like?"
print(message)


# You can use either single quotes (``'``), double quotes (``"``), or triple quotes (``'''`` or ``"""``) to enclose a string (the last one is used for multi-line strings). To include single or double quotes inside a string, you can either use the opposite quote to enclose the string:

# In[ ]:


response = "I'm"
print(response)


# In[ ]:


response = 'hello'
print(response)


# In[ ]:


# length of string
print(len(response))


# In[ ]:


# Make upper-case. See also str.lower()
print(response.upper())


# In[ ]:


# Capitalize. See also str.title()
print(message.capitalize())


# In[ ]:


s = "Spam egg spam spam"
s.index(' e')  # An integer giving the position of the sub-string


# In[ ]:


s2 = s.split()


# In[ ]:


s2[2].split('p')


# In[ ]:


s2 = "Spam-egg-spam_spam"
s2.split('_')


# In[ ]:


s3 = s2.split('-')
s3


# In[ ]:


type(s3)


# In[ ]:


" ".join(['hola', 'adios'])


# In[ ]:


vv = 5.0000045


# In[ ]:


# concatenation with +
print(message + ' ' + response + ' ' +str(vv))


# ### FORMAT
# 
# a = f'{message} {response} {vv}'
# 
# a = '{} {} {}'.format(message, response, vv)
# 
# a = '{0} {2} {1}'.format(message, response, vv)

# In[ ]:



# concatenation with f
print(f'{message} {response} {vv:.2f}')


# In[ ]:


f'{5:03d}'


# In[ ]:


# concatenation with format
print('{} {} {}'.format(message, response, vv))
print('{1} -- {0} {1}'.format(message, response))


# In[ ]:


# multiplication is multiple concatenation
print(5 * response)


# In[ ]:


message


# In[ ]:


# Access individual characters (zero-based indexing)
#[first:end:step]
print(message[:8:2])


# In[ ]:


cadena1 = "cool"
print(cadena1[::-1])


# ## Exercise 
# Given a string such as the one below, make a new string that does not contain the word ``egg``:

# In[ ]:


a = "Hello, egg world!"

# enter your solution here
# "Hello world!"


# In[ ]:


s = a.split(' ')


# In[ ]:


print(s[0] + ' ' + s[2])


# In[ ]:


print('{0} {2}'.format(s[0], s[1], s[2]))


# In[ ]:


print(' '.join(a.split(', egg ')))


# In[ ]:


print(a[0:7] + a[11:17])


# ## Built-In Data Structures

# | Type Name | Example                   |Description                            |
# |-----------|---------------------------|---------------------------------------|
# | ``list``  | ``[1, 2, 3]``             | Ordered collection                    |
# | ``tuple`` | ``(1, 2, 3)``             | Immutable ordered collection          |
# | ``dict``  | ``{'a': 1, 'b': 2, 'c': 3}`` | (key,value) mapping                |

# ### Lists
# 
# A list is an ordered container of objects denoted by **square brackets**:

# In[ ]:


mylist = [0, 1, 1, 2, 3, 5, 8]


# In[ ]:


len(mylist)


# In[ ]:


mylist[-7]


# Lists are useful for lots of reasons including iteration:

# In[ ]:


for pos, number in enumerate(mylist):
    print(f'{pos + 1} - {number + 4.5}')
    
# for pos in range(len(mylist)):
#    print(mylist[pos])


# Lists do **not** have to contain all identical types:

# In[ ]:


myweirdlist = [0, 1, 1, "apple", 4e7]
for item in myweirdlist:
    print(f'{item} - {type(item)}')


# In[ ]:


ll = [['a', 'be ready', 'c'], [23, 45]]


# In[ ]:


ll[0][1].split()[1][3]


# In[ ]:


ll[0][1].split()[1][2:3]


# This list contains a mix of `int`, `float`, and `str` (character string).

# Because a list is *ordered*, we can access items by integer index:

# In[ ]:


myweirdlist[3]


# remembering that we start counting from zero!

# Python also allows lists to be created dynamically through *list comprehension* like this:

# In[ ]:


squares = [i ** 2 for i in range(11)]
squares


# In[ ]:


squares = list()
for i in range(11):
    squares.append(i**2)
squares


# In[ ]:


li = [2, 3, 5, 7]


# In[ ]:


# Change value of list
li[1] = -2.2


# In[ ]:


li


# In[ ]:


# Append a value to the end
li.append(11)
print(li)


# In[ ]:


# Addition concatenates lists
print(lst + [13, 17, 19])


# In[ ]:


lst.remove(5)
lst


# In[ ]:





# In[ ]:





# In[ ]:


# sort() method sorts in-place
lst = [2, 5, 1, 6, 3, 4]
lst.sort()
print(lst)


# In[ ]:


lst = [1, "two", 3.14, [0, 3, 5]]
print(lst)


# In[ ]:


type(lst[3])


# #### List indexing and slicing

# In[ ]:


lst = [2, 3, 5, 7, 11]


# In[ ]:


print(lst[0])


# In[ ]:


print(lst[1])


# In[ ]:


print(lst[-1])


# In[ ]:


print(lst[0:3])


# In[ ]:


print(lst[:3])


# In[ ]:


print(lst[::-2])  # [start:end:step] equivalent to l[0:len(l):2]


# In[ ]:


lst[0] = 100
print(lst)


# ### Dictionaries (`dict`)
# 
# A dictionary is a collection of *labeled objects*. Python uses curly braces `{}` to create dictionaries:

# In[ ]:


mypet = {
    "name": ["Fluffy", 'Fido'],
    "species": ["cat", 'dog'],
    "age": [4, 5],
}
type(mypet)


# In[ ]:


mypet


# We can then access items in the dictionary by label using square brackets:

# In[ ]:


mypet["species"]


# We can iterate through the keys (or labels) of a `dict`:

# In[ ]:


for key, values in mypet.items():
    print("The key is:", key)
    print("The value is:", values)


# In[ ]:


# Set a new key:value pair
mypet["ninety"] = 90
print(mypet)


# ### Exercises

# - Create a dictionary with the following birthday information:
# 
# > - Albert Einstein - 03/14/1879
# > - Benjamin Franklin - 01/17/1706
# > - Ada Lovelace - 12/10/1815
# > - Marie Curie - 07/11/1867
# > - Rowan Atkinson - 01/6/1955
# > - Rosalind Franklin - 25/07/1920

# - Check if Marie Curie is in our dictonary
# - Get Albert Einstein's birthday

# In[ ]:


info = {'Albert Einstein': '03/14/1879',
        'Benjamin Franklin': '01/17/1706',
        'Ada Lovelace': '12/10/1815',
        'Marie Curie': '07/11/1867',
        'Rowan Atkinson': '01/6/1955',
        'Rosalind Franklin': '25/07/1920'}

info2 = {'name': ['Albert Einstein', 'Benjamin Franklin', 'Ada Lovelace', 'Marie Curie', 'Rowan Atkinson', 
                  'Rosalind Franklin'],
         'birthday': ['03/14/1879', '01/17/1706', '12/10/1815', '07/11/1867', '01/6/1955','25/07/1920']}


# In[ ]:


# Check if Marie Curie is in dictionary
a = 'Albert Einstein'

if a in info:    
    #ksjklajkld
    print(info)


# In[ ]:





# In[ ]:


print(a in info)


# In[ ]:


info2['name'].index('Marie Curie')


# In[ ]:


# Einstein's birthday
'03/14/1879'


# In[ ]:


info['Albert Einstein']


# In[ ]:


pos_e = info2['name'].index('Albert Einstein')


# In[ ]:


info2['birthday'][pos_e]


# ## Arrays of numbers with `numpy`
# 
# The vast majority of scientific Python code makes use of *packages* that extend the base language in many useful ways.
# 
# Almost all scientific computing requires ordered arrays of numbers, and fast methods for manipulating them. That's what numpy does in the Python world.
# 
# Using any package requires an `import` statement, and (optionally) a nickname to be used locally, denoted by the keyword `as`:

# In[ ]:


import numpy as np


# In[ ]:





# Now all our calls to `numpy` functions will be preceeded by `np.`

# Create a linearly space array of numbers:

# In[ ]:


# linspace() takes 3 arguments: start, end, total number of points
numbers = np.linspace(0.0, 1.0, 11)
numbers


# We've just created a new type of object defined by numpy:

# In[ ]:


type(numbers)


# Do some arithmetic on that array:

# In[ ]:


numbers + 1


# In[ ]:


list = [3, 4, 5]


# In[ ]:


np.asarray(list) + 1


# Sum up all the numbers:

# In[ ]:


np.sum(numbers)


# ## Operators

# | Operator     | Name           | Description                                            |
# |--------------|----------------|--------------------------------------------------------|
# | ``a + b``    | Addition       | Sum of ``a`` and ``b``                                 |
# | ``a - b``    | Subtraction    | Difference of ``a`` and ``b``                          |
# | ``a * b``    | Multiplication | Product of ``a`` and ``b``                             |
# | ``a / b``    | True division  | Quotient of ``a`` and ``b``                            |
# | ``a // b``   | Floor division | Quotient of ``a`` and ``b``, removing fractional parts |
# | ``a % b``    | Modulus        | Integer remainder after division of ``a`` by ``b``     |
# | ``a ** b``   | Exponentiation | ``a`` raised to the power of ``b``                     |
# | ``-a``       | Negation       | The negative of ``a``                                  |
# | ``+a``       | Unary plus     | ``a`` unchanged (rarely used)                          |

# In[ ]:


print(22 / 2 == 10 + 1)


# In[ ]:


# 25 is even
print(25 % 2 == 0)


# In[ ]:


# 66 is odd
print(66 % 2 == 0)


# In[ ]:


# check if a is between 15 and 30
a = 25
print(15 < a < 30)


# ### Boolean Operations

# In[ ]:


x = 4
print(((x < 6) and (x > 2)) and (x == 5))
# and -> &


# In[ ]:


print((x > 10) or (x % 2 == 0))
# or -> |


# In[ ]:


print(not (x < 6))


# ### Membership Operators

# | Operator      | Description                                       |
# |---------------|---------------------------------------------------|
# | ``a in b``    | True if ``a`` is a member of ``b``                |
# | ``a not in b``| True if ``a`` is not a member of ``b``            |

# In[ ]:


print(1 in [1, 2, 3])


# In[ ]:


print(2 not in [1, 2, 3])


# ## Functions

# ### Defining Functions

# In[ ]:


import time

# def NAME(input1, input 2):
#     aaaaa
#     bbbbb

#     return output1, output2   

# out = NAME(inp1, inp2)
# out = [out1, out2]

def header():
    text = "This is a function"
    text += ". Copyright " + time.strftime("%d-%m-%Y")

    return text, text 


out1, _ = header()

#print(header())
print(out1)


# In[ ]:





# In[ ]:


def header_v2(author):
    text = "This function is written by "
    text += author
    text += f". Copyright {time.strftime('%d-%m-%Y')}"

    return text


print(header_v2("Andrea Lira Loarca"))


# In[ ]:





# > Atenttion to the string format

# In[ ]:


print(header_v2('Gabriella Ruffini'))


# In[ ]:


def fibonacci(n):
    l = []
    a = 0
    b = 1
    while len(l) < n:
        l.append(a)
        c = a + b
        a = b
        b = c
    return l


# In[ ]:


print(fibonacci(10))


# In[ ]:


print(fibonacci(6))


# ### Default Argument Values

# In[ ]:


def fibonacci(n, start=0):
    fib = []
    a = 0
    b = 1
    while len(fib) < n:
        if a >= start:
            fib.append(a)
        c = a + b
        a = b
        b = c
    return fib


# In[ ]:


print(fibonacci(10))


# In[ ]:


print(fibonacci(10, 5))


# In[ ]:


## Keyword arguments


# In[ ]:


print(fibonacci(start=5, n=20))


# In[ ]:


from datetime import datetime, timedelta

dt1 = datetime(2005, 7, 14, 12, 30)

dt2 = dt1 + timedelta(hours=5)

print(dt2)


# In[ ]:


dt1


# **timedelta**(`[days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]]`)
# 
# > All arguments are optional and default to 0. Arguments may be ints, longs, or floats, and may be positive or negative.

# ### Documentation strings (docstrings)

# * Python documentation strings (docstrings) provide a convenient **way of associating documentation with Python functions** and modules.
# * Docstrings can be written following **several styles**. We use [Google Python Style Guide](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/).
# * An object's docsting is defined by including a **string constant as the first statement in the function's definition**.

# * Unlike conventional source code comments **the docstring should describe what the function does, not how**.
# * **All functions should have a docstring**.
# * This allows to inspect these comments at run time, for instance as an **interactive help system**, or **export them as HTML, LaTeX, PDF** or other formats.

# In[ ]:


def fibonacci(n, start=0):
    """Build a Fibonacci series with n elements starting at start

    Args:
        n: number of elements
        start: lower limit. Default 0

    Returns:
        A list with a Fibonacci series with n elements
    """
    fib = []
    a = 0
    b = 1
    while len(fib) < n:
        if a >= start:
            fib.append(a)
        c = a + b
        a = b
        b = c
    return fib


# ## Modules and Packages

# ### Loading Modules: the ``import`` Statement

# #### Explicit module import by alias

# In[ ]:


import numpy as np
from numpy import linspace


# In[ ]:


linspace(0, 5, 10)


# #### Explicit import of module contents

# In[ ]:


import scipy.stats as st
from scipy.stats import norm, genpareto


# ### Importing from Third-Party Modules
