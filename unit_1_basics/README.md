# The Absolute Basics

We begin with the absolute basics, expressions and flow control with the objective to enable the reader to conceive and write simple programs as soon as possible.

## Comments
Comments in start with the hash character (#) and extend to the end of the line. A comment may appear at the start of a line or following whitespace or code, but not within a string. A hash character within a string is just a hash character.
For example:
```python
# this is the first comment
a_number = 1  # and this is the second comment
          # ... and now a third!
a_string = "# This is not a comment because it's inside quotes."
```
A good empirical rule to follow for writing useful comments is that _code tells you **how**, while comments tell you **why**_.

## Evaluating Expressions
```python
>>> 2 + 2
4
```
2 + 2 is called an _expression_, which is the most basic kind of programming instruction of a language. Expressions consist of _values_ (such as 2) and _operators_ (such as +), and they can always _evaluate_ (that is reduced) down to a single value. A single value with no operators is also considered an expression, that evaluates to itself.

## Precedence of operations
The order of operations (also called _precedence_) of math operators is similar to that of mathematics. The ** operator is evaluated first; the *, /, //, and % operators are evaluated next from left to right; and finally the + and the - operators are evaluated last, also from left to right.

Operation | Expression | Evaluation
--------- | ---------- | ----------
exponentiation | 4 ** 2 | 16
multiplication | 4 * 2 | 8
float division | 4 / 2 | 2.0
integer division | 4 // 2 | 2
modulus/remainder | 4 % 2 | 0
addition | 4 + 2 | 6
subtraction | 4 - 2 | 2

You can use parentheses to override the precedence of operations.
```python
>>> 1 + 2 * 3
7
>>> (1 + 2) * 3
9
>>> -2 ** 2
-4
>>> (-2) ** 2
4
>>> 1 + 2 * - 3
-5
>>> 1 + 2 - * 3
  File "<stdin>", line 1
    1 + 2 - * 3
            ^
SyntaxError: invalid syntax
```
The Python interactive shell couldn’t evaluate the last expression because it's syntax was wrong, therefore it and displayed a `SyntaxError` _error_ message. **Errors are your friends**, unit 4 covers in detail how to use them to our advantage.

## Data types
A _data type_ is the class of values, and every value belongs to **exactly one** data type.

The integer (or _int_) data type indicates values that are whole numbers. Numbers with a decimal point, such as 3.14, are called floating-point numbers (or _float_). Note that even though the value 42 is an integer, the value 42.0 would be a floating-point number.
```python
>>> type((1 - 3) / 2)
<class 'float'>
```
You can use the _type()_ built-in function to check the data type of a value.
In addition to int and float, Python supports _Decimal_ and _Fraction_. Python also has built-in support for _complex numbers_, and uses the `j` or `J` suffix to indicate the imaginary part (e.g. `3+5j`). The differences between [float](https://docs.python.org/3/tutorial/floatingpoint.html), [decimal](https://docs.python.org/3/library/decimal.html) and [fraction](https://docs.python.org/3/library/fractions.html) are beyond the scope of this tutorial, you can follow the links if you want to know more.
In the begining, using float is good enough, just don't rely to equality (which we will talk about soon), because:
```python
>>> .1 + .1 + .1 == .3
False
```

## Variables
A _variable_ is label for a the computer’s memory, where you can store and retrieve a value by that label. If you want to use the result of an evaluated expression later in your program, you can save it inside a variable.
You can store values in variables with an _assignment statement_, consisting of a variable name, an equal sign (called the _assignment operator_), and the value to be stored. If you enter the assignment statement `answer = 42`, then a variable named `answer` will have the integer value `42` stored in it.
```python
>>> rule = 32
>>> answer = 42
>>> answer += rule - 5
>>> answer
69
```
The `+=` operator is a shortcut for adding **and** assigning the value to the variable on the left-hand side of the assignment operator.
A variable is _initialized_ the first time a value is stored in it. After that, you can use it in expressions with other variables and values. When a variable is assigned a new value, the old value is forgotten, which is why `answer` evaluated to `69` instead of `42` at the end of the example above. This is called _overwriting_ the variable.
Variable names follow a few rules:

* It can be only one word.
* It can use only letters, numbers, and the underscore (_) character.
* It can’t begin with a number.

Variable names are case-sensitive, meaning that `answer`, `ANSWER`, and `Answer` are three different variables. For learning about conventions most python programmers use, **have a look at [PEP8](https://www.python.org/dev/peps/pep-0008/), which this tutorial follows but does not discuss since it is beyond its scope**.

## Strings
Besides numbers, Python can also manipulate strings, which can be expressed in several ways. They can be enclosed in single quotes ('...') or double quotes ("...") with the same result. \ can be used to escape quotes:
```python
>>> 'spam eggs'  # single quotes
'spam eggs'
>>> 'doesn\'t'  # use \' to escape the single quote...
"doesn't"
>>> "doesn't"  # ...or use double quotes instead
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> "\"Yes,\" they said."
'"Yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
```
In the interactive interpreter, the output string is enclosed in quotes and special characters are escaped with backslashes. While this might sometimes look different from the input (the enclosing quotes could change), the two strings are equivalent. The string is enclosed in double quotes if the string contains a single quote and no double quotes, otherwise it is enclosed in single quotes. The print() function produces a more readable output, by omitting the enclosing quotes and by printing escaped and special characters:
```python
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
>>> print('"Isn\'t," they said.')
"Isn't," they said.
```
If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:
```python
>>> print('C:\some\name')  # here \n means newline!
C:\some
ame
>>> print(r'C:\some\name')  # note the r before the quote
C:\some\name
```
String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''. End of lines are automatically included in the string, but it’s possible to prevent this by adding a \ at the end of the line. The following example:
```python
>>> print("""\
... Usage: thingy [OPTIONS]
...      -h                        Display this usage message
...      -H hostname               Hostname to connect to
... """)
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
```
Strings can be concatenated (glued together) with the + operator, and repeated with *:
```python
>>> # 3 times 'un', followed by 'ium'
>>> 3 * 'un' + 'ium'
'unununium'
```
Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
```python
>>> 'Py' 'thon'
'Python'
```
This feature is particularly useful when you want to break long strings:
```python
>>> ('Put several strings within parentheses '
...         'to have them joined together.')
'Put several strings within parentheses to have them joined together.'
```
