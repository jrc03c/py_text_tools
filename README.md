# Introduction

**py_text_tools** is just a little collection of tools for modifying text in Python. It's a Python port of [js-math-tools](https://github.com/jrc03c/js-math-tools).

# Installation

Install with `pip`:

```bash
pip install -U git+https://github.com/jrc03c/py_text_tools
```

Or install with `conda`:

```bash
conda install pip git
pip install -U git+https://github.com/jrc03c/py_text_tools
```

# API

## `camelify(text)`

Returns the text in camel-case.

```py
camelify("Hello, world!")
# helloWorld
```

## `indent(text, chars="")`

Returns the text with all lines indented by `chars`. By default, `chars` is an empty string.

```py
indent("Hello, world!", 2, "\t")
# \t\tHello, world!
```

## `kebabify(text)`

Returns the text in kebab-case.

```py
kebabify("Hello, world!")
# hello-world
```

## `snakeify(text)`

Returns the text in snake-case.

```py
snakeify("Hello, world!")
# hello_world
```

## `unindent(text)`

Returns the text with all lines unindented by the same number of characters. For example, if the _smallest_ amount of indentation is 4 spaces, then each line will be unindented by 4 spaces.

For example, suppose I have a file called `message.txt` with this content:

```
    Hello, world!
      My name is Josh.
        What's your name?
```

The smallest amount of indentation in the file is 4 spaces. So, unindenting it will move all lines to the left by 4 spaces.

```py
from py_text_tools import unindent

with open("message.txt") as file:
  message = file.read()

unindented_message = unindent(message)

with open("unindented-message.txt", "w") as file:
  file.write(unindented_message)
```

The contents of `unindented-message.txt` would be:

```
Hello, world!
  My name is Josh.
    What's your name?
```

**NOTE:** The `unindent` function does _not_ pay attention to whether indentation consists of spaces or tabs. It only cares whether or not a character is a whitespace character. It also makes no attempt to make the whitespace characters consistent (i.e., it doesn't try to begin each line with _all_ spaces or _all_ tabs); it merely removes the minimum number of whitespace characters from each line and returns the result.

## `wrap(text, max_line_length=None)`

Returns the text with all lines wrapped to a maximum length of `max_line_length`. By default, the `max_line_length` is the minimum of 80 and the number of `stdout` columns in the command line. Note that this function only wraps at spaces; it does not wrap mid-word, and it does not attempt to hyphenate words. The wrapping _does_ preserve indentation, though.

```py
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam mollis tellus eu mi condimentum, a congue ipsum luctus. Donec vel suscipit dolor, vitae faucibus massa. Curabitur rhoncus semper tortor et mattis. Nullam laoreet lobortis nibh eget viverra. Nam molestie risus vitae ante placerat convallis. Pellentesque quis tristique dui. Vivamus efficitur mi erat, nec gravida felis posuere at. Donec sapien ipsum, viverra et aliquam quis, posuere ac ligula. Aenean egestas tincidunt mauris, in hendrerit tortor malesuada id. Proin viverra sodales ex eu fermentum. Aenean nisl ipsum, tristique venenatis massa eget, tempor facilisis felis. Praesent aliquam sem vitae arcu porta commodo. Aliquam tempor sollicitudin dapibus. Nulla ullamcorper orci eu ultricies cursus."

wrap(text, 20)

# 'Lorem ipsum dolor
# sit amet,
# consectetur
# adipiscing elit. Nam
# mollis tellus eu mi
# condimentum, a
# congue ipsum luctus.
# Donec vel suscipit
# dolor, vitae
# faucibus massa.
# Curabitur rhoncus
# semper tortor et
# mattis. Nullam
# laoreet lobortis
# nibh eget viverra.
# Nam molestie risus
# vitae ante placerat
# convallis.
# Pellentesque quis
# tristique dui.
# Vivamus efficitur mi
# erat, nec gravida
# felis posuere at.
# Donec sapien ipsum,
# viverra et aliquam
# quis, posuere ac
# ligula. Aenean
# egestas tincidunt
# mauris, in hendrerit
# tortor malesuada id.
# Proin viverra
# sodales ex eu
# fermentum. Aenean
# nisl ipsum,
# tristique venenatis
# massa eget, tempor
# facilisis felis.
# Praesent aliquam sem
# vitae arcu porta
# commodo. Aliquam
# tempor sollicitudin
# dapibus. Nulla
# ullamcorper orci eu
# ultricies cursus.'
```
