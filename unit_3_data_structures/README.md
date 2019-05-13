# Data structures and an introduction to algorithms

Python's data structures will be explored and compared, followed by modules and how they work will be explained. This will be followed by an introduction to algorithm analysis and a much more involved look into data structures, ending with a quick discussion at what python's standard library offers.

## Strings
Strings can be _concatenated_ (glued together) with the `+` operator, and repeated with `*` operator:
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
Strings can be _indexed_ (subscripted), with the indeces starting at 0. There is no separate character _type_; a character is simply a _string_ of size one:
```python
>>> word = 'Python'
>>> word[0]  # character in position 0
'P'
>>> word[5]  # character in position 5
'n'
```
Indices may also be negative numbers, to start counting from the end. Note that since -0 is the same as 0, negative indices start from -1.:
```python
>>> word[-1]  # last character
'n'
>>> word[-6]  # first character
'P'
```
In addition to _indexing_, _slicing_ (obtaining a part of the string, called a _substring_):
```python
>>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
'tho'
```
Note how the start is always included, and the end always excluded. This makes sure that `s[:i] + s[i:]` is always equal to `s`:
```python
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'
```
Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.
```python
>>> word[:2]   # character from the beginning to position 2 (excluded)
'Py'
>>> word[4:]   # characters from position 4 (included) to the end
'on'
>>> word[-2:]  # characters from the second-last (included) to the end
'on'
```
Attempting to use an index that is too large will result in an `IndexError`:
```python
>>> word[42]  # the word only has 6 characters
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```
However, out of range slice indexes are handled gracefully when used for slicing:
```python
>>> word[4:42]
'on'
>>> word[42:]
''
```
Python strings cannot be changed, they are _immutable_. Therefore, assigning to an indexed position in the string results in an `TypeError`:
```python
>>> word[0] = 'J'
  ...
TypeError: 'str' object does not support item assignment
>>> word[2:] = 'py'
  ...
TypeError: 'str' object does not support item assignment
```
If you need a different string, you should create a new one:
```python
>>> 'J' + word[1:]
'Jython'
```
Beyond these basics about strings covered here, there an excellent article about [formatting](https://realpython.com/python-string-formatting/) and it is worth your time to have a quick glance at all [the string methods](https://docs.python.org/3.6/library/stdtypes.html#string-methods).

##  Lists

Python knows a number of compound data types, used to group together other values. The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type.
```python
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
```
Like strings (and all other built-in sequence type), lists can be indexed and sliced:
```python
>>> squares[0]  # indexing returns the item
1
>>> squares[-1]
25
>>> squares[-3:]  # slicing returns a new list
[9, 16, 25]
```
All slice operations return a new list containing the requested elements. This means that the following slice returns a new (shallow) copy of the list:
```python
>>> squares[:]
[1, 4, 9, 16, 25]
```
Lists also support operations like concatenation:
```python
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:
```python
>>> cubes = [1, 8, 27, 65, 125]  # something's wrong here
>>> 4 ** 3  # the cube of 4 is 64, not 65!
64
>>> cubes[3] = 64  # replace the wrong value
>>> cubes
[1, 8, 27, 64, 125]
```
You can also add new items at the end of the list, by using the append() method (we will see more about methods later):
```python
>>> cubes.append(216)  # add the cube of 6
>>> cubes.append(7 ** 3)  # and the cube of 7
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
```
Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:
```python
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # replace some values
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # now remove them
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> # clear the list by replacing all the elements with an empty list
>>> letters[:] = []
>>> letters
[]
```
The built-in function len() also applies to lists:
```python
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)
4
```
It is possible to nest lists (create lists containing other lists), for example:
```python
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
```
