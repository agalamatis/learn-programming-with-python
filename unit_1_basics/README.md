# The Absolute Basics

We begin with the absolute basics, expressions and flow control with the objective to enable the reader to conceive and write simple programs as soon as possible.

## TODO: Pedantic py-shell intro with import this

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

The integer (or `int`) data type indicates values that are whole numbers. Numbers with a decimal point, such as 3.14, are called floating-point numbers (or _float_). Note that even though the value 42 is an integer, the value 42.0 would be a floating-point number.
```python
>>> type((1 - 3) / 2)
<class 'float'>
>>> type((1 - 3) // 2)
<class 'int'>
```
You can use the _type()_ built-in function to check the data type of a value.
In addition to `int` and `float`, Python supports `Decimal` and `Fraction`. Python also has built-in support for _complex numbers_, and uses the `j` or `J` suffix to indicate the imaginary part (e.g. `3+5j`). The differences between [float](https://docs.python.org/3/tutorial/floatingpoint.html), [Decimal](https://docs.python.org/3/library/decimal.html) and [Fraction](https://docs.python.org/3/library/fractions.html) are beyond the scope of this tutorial, you can follow the links if you want to know more.
In the begining, using `float` is good enough, just don't rely on equality (which we will talk about soon), because:
```python
>>> .1 + .1 + .1 == .3
False
```

## Variables
A _variable_ is label for a part of the computer’s memory, where you can store and retrieve a value by using that label. If you want to use the value of an expression later in your program, you can store it inside a variable.
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
Besides numbers, Python can also manipulate **strings** (a list of characters), which can be expressed in several ways. They can be enclosed in single quotes (`'...'`) or double quotes (`"..."`) with the same result. A backslash (`\`) can be used to escape quotes:
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
In the interactive interpreter, the output string is enclosed in quotes and special characters are escaped with backslashes. While this might sometimes look different from the input (the enclosing quotes could change), the two strings are equivalent. The string is enclosed in double quotes if the string contains a single quote and no double quotes, otherwise it is enclosed in single quotes. The `print()` built-in function produces a more readable output, by omitting the enclosing quotes and by printing escaped and special characters:
```python
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
>>> print('"Isn\'t," they said.')
"Isn't," they said.
```
If you don’t want characters prefaced by backslash (`\`) to be interpreted as special characters, you can use raw strings by adding an `r` before the first quote:
```python
>>> print('C:\some\name')  # here \n means newline!
C:\some
ame
>>> print(r'C:\some\name')  # note the r before the quote
C:\some\name
```
String literals can span multiple lines. One way is using triple-quotes: `"""..."""` or `'''...'''`. End of lines are automatically included in the string, but it’s possible to prevent this by adding a `\` at the end of the line. The following example:
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
The built-in function len() returns the length of a string:
```python
>>> s = 'supercalifragilisticexpialidocious'
>>> len(s)
34
```
Strings will be revisited in unit 3.

## Converting data types
```python
>>> 'Alice' + 80
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not int
>>> 42 + '32'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
The first error message `TypeError: must be str, not int` means that Python thought you were trying to concatenate an integer to the string 'Alice'. The second `TypeError: unsupported operand type(s) for +: 'int' and 'str'` means that Python expects a number after the addition operator. The code will have to explicitly convert the integer to a string by using the `str()` and `int()` built-in function (there is also a `float()` one):
```python
>>> 'Alice' + str(80)
'Alice80'
>>> 42 + int('32')
74
```

## Booleans
While the integer, floating-point, and string data types have an unlimited number of possible values (but still finite), the `bool` data type has only two values: `True` and `False`. When typed as Python code, the `bool` values `True` and `False` lack the quotes you place around strings, and they always start with a capital T or F, with the rest of the word in lowercase. Like any other value, Boolean values are used in expressions and can be stored in variables.
```python
# TODO: examples!!!!!
```

## Comparison operators
_Comparison operators_ compare two values and evaluate down to a single Boolean value. They are equals to (`==`), not equals to (`!=`), less than (`<`), greater than (`>`), less than or equal to (`<=`) and greater than or equal to (`>=`). Note that an integer or floating-point value will always be unequal to a string value. The expression `42 == '42'` evaluates to `False` because Python considers the integer 42 to be different from the string '42'.
```python
# TODO: examples!!!!!
```
Another thing to be aware of is that the comparison operators beyond their mathematical interpretation when used on values of _number types_, can be used to compare the items of _compound data strures_ (e.g. _strings_):
```python
>>> a = 'a'
>>> b = 'ab'
>>> a * 2 == b
False
>>> a + 'b' == b
True
>>> a < b
True
>>> 'C' < a  # alphabetical comparison with all caps being smaller than lower!
True
```
_You might have noticed that the `==` operator (equal to) has two equal signs, while the `=` operator (assignment) has just one equal sign. In the beginning, it is easy to confuse these two operators with each other._

## Boolean operators
The three _Boolean operators_ (`and`, `or`, and `not`) are used to compare `bool` values. Like comparison operators, they evaluate these expressions down to a `bool` value. The `and` and `or` operators always take two `bool` values (or expressions), so they are considered _binary_ operators. 

The `and` operator evaluates an expression to `True` if both `bool` values are `True`; otherwise, it evaluates to `False`. 

The `or` operator evaluates an expression to `False` if both `bool` values are `False`; otherwise, it evaluates to `True`. 

Unlike the former two operators, the `not` operator operates on only one Boolean value (or expression), therefore it is a _unary_ operator. The `not` operator simply evaluates to the opposite `bool` value. 

See their _truth tables_ below:

`a` | `b` | `a or b` | `a and b` | `not a` | `not b`
--- | --- | -------- | --------- | ------- | -------
`False` | `False` | `False` | `False` | `True` | `True`
`False` | `True` | `True` | `False` | `True` | `False`
`True` | `False` | `True` | `False` | `False` | `True`
`True` | `True` | `True` | `True` | `False` | `False`

Since the _comparison operators_ evaluate to `bool` values, you can use them in _expressions_ with the _boolean operators_:
```python
>>> 4 < 5 and 5 < 6
True
>>> 4 < 5 and 9 < 6
False
>>> 1 == 2 or 2 == 2
True
```
_Comparison operators_ are evaluated after the _numerical operators_ we mentioned already, followed by `not`, then `and` and finally `or`.

These 3 operators are the most commonly used by programming laanguages and their binary combinations can produce all 16 [rules of inference](https://en.wikipedia.org/wiki/List_of_rules_of_inference#Table:_Rules_of_Inference), but any other combination of two non-self-negating pairs of operators with NOT can do too, i.e. in electronics NAND/XOR and used instead of AND/OR. But delving into more detail (_however useful_) is beyond our scope.

Something else to be aware of is that the combinations of these operations can become very complicated very quickly when representing in code real life scenarios. Mathematical logic provides several methods to simplify them, and when done correctly can provide invaluable insights into the nature of the problems. Again though this is beyond our scope, but you can start reading about how to [simplify logic operations](https://grace.bluegrass.kctcs.edu/~kdunn0001/files/Simplification/4_Simplification_print.html).

## Conditions

The _boolean expressions_ we have seen so far could all be considered _conditions_, a subset of expressions; _condition_ is just a more specific name in the context of _flow control statements_. _Conditions_ always evaluate down to a `bool` value, `True` or `False`. A _flow control statement_ decides what to do based on whether its _condition_ is `True` or `False`, and almost every _flow control statement_ uses a _condition_.

## Blocks
Lines of Python code can be grouped together in blocks. You can tell when a block begins and ends from the indentation of the lines of code. There are three rules for blocks.
* Blocks begin when the indentation increases.
* Blocks can contain other blocks.
* Blocks end when the indentation decreases to zero or to a containing block’s indentation.

## Branching with if-elif-else
Besides the while statement just introduced, Python knows the usual control flow statements known from other languages. The most well-known statement type is the `if` statement. For example:
```python
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 0:
...     x = 0
...     print('Negative changed to zero')
... elif x == 0:
...     print('Zero')
... elif x == 1:
...     print('Single')
... else:
...     print('More')
...
More
```
There can be zero or more `elif` parts, and the `else` part is optional. The keyword ‘elif’ is short for ‘else if’, and is useful to avoid excessive indentation. An `if` … `elif` … `elif` … sequence is a substitute for the _switch/case_ statements found in other languages.

TODO: explain shortly input()

## The while loop
Let's put everything we have seen together and write a program that displays a subsequence of the Fibonacci numbers:
```python
>>> a, b = 0, 1
>>> while b < 1000:
...     print(b, end=', ')
...     a, b = b, a + b
... 
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, >>> 
```
The first line contains a _multiple assignment_. The variables `a` and `b` simultaneously get the new values `0` and `1`. On the last line this is used again, demonstrating that the expressions on the right-hand side are all evaluated first before any of the assignments take place. The right-hand side expressions are evaluated from the left to the right.

The `while` _loop_ executes as long as the _condition_ (here: `b < 1000`) remains true. The test used in the example is a simple comparison.
The _body of the loop_ is the indented _block_ following the while statement. At the interactive prompt, you have to type a tab or space(s) for each indented line. It must be followed by a blank line to indicate completion (since the parser cannot guess when you have typed the last line).

The _keyword argument_ `end` of the `print()` function can be used to avoid the newline after the output, or end the output with a different string. This is the reason that the promt (`>>>`) appears in the same line as the `print()` function's output.

## The for loop and range built-in function
The `while` loop keeps looping while its condition is true, but what if you want to execute a block of code only a certain number of times? You can do this with a for loop statement and the range() function.
```python
>>> print('My name is')
>>> for i in range(5):
...     print('Jimmy Five Times (' + str(i) + ')')
... 
Jimmy Five Times (0)
Jimmy Five Times (1)
Jimmy Five Times (2)
Jimmy Five Times (3)
Jimmy Five Times (4)
```
The code in the `for` loop’s clause is run five times. The first time it is run, the variable `i` is set to `0`. The `print()` call in the clause will print `Jimmy Five Times (0)`. After python finishes an iteration through all the code inside the for loop’s clause, the execution goes back to the top of the loop, and the for statement increments `i` by one. This is why `range(5)` results in five iterations through the clause, with `i` being set to `0`, then `1`, then `2`, then `3`, and then `4`. The variable i will go up to, but will not include, the integer passed to `range()`.

Some _functions_ can be called with multiple arguments separated by a comma, and `range()` is one of them. This lets you change the integer passed to `range()` to follow any sequence of integers, including starting at a number other than zero.
```python
>>> for i in range(13, 16):
...     print(i)
... 
13
14
15
```
The first argument will be where the `for` loop’s variable starts, and the second argument will be up to, but not including, the number to stop at.

The `range()` function can also be called with three arguments. The first two arguments will be the start and stop values, and the third will be the step argument. The step is the amount that the variable is increased by after each iteration.
```python
>>> for i in range(4, 10, 2):
...     print(i)
... 
4
6
8
```
The `range()` function is flexible in the sequence of numbers it produces for for loops. For example, you can even use a negative number for the step argument to make the for loop count down instead of up.
```python
>>> for i in range(5, -1, -2):
...     print(i)
... 
5
3
1
```

## break and continue starements

## the pass statement
