print("DocString")

def add(a,b):
  """ This is the function Which Add two number"""
  return a+b

print(add(10,20))
print(add.__doc__)
# help(add)

# Key Rules 8

# Indentation

# Use 4 spaces per indentation level.

# Don’t use tabs.

# Line Length

# Maximum 79 characters per line.

# Comments/docstrings: 72 characters max.

# Blank Lines

# 2 blank lines between top-level functions or classes.

# 1 blank line between methods inside a class.

# Imports

# Place at the top of the file.

# Order:

# Standard library

# Third-party libraries

# Local application imports

# Naming Conventions

# Functions/variables → snake_case

# Classes → PascalCase

# Constants → UPPER_CASE

# Whitespace

# Put spaces around operators (=, +, -, etc.).
# Comments

# Write meaningful comments.

# Inline: after code with #.

# Block: full separate lines.

# Docstrings

# Use triple quotes (""" """") for documenting modules, functions, and classes.

# Follow PEP 257 guidelines for style.