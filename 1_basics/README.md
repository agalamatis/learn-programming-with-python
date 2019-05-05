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
A good empirical rule to follow for writing useful comments is that _code tells you **how**, while comments tells you **why**_.

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
exponentiation | 3 ** 2 | 9
multiplication | 3 * 2 | 6
float division | 3 / 2 | 1.5
floor division | 3 // 2 | 1
modulus/remainder | 3 % 2 | 1
addition | 3 + 2 | 5
subtraction | 3 - 2 | 1
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
