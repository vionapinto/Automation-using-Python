# To read the contents of the file we can do this:

# p1 = 'Pathlib_Library/abc.txt'

# with open(p1, 'r') as file:
#     print(file.read())

## We shall do it now using Pathlib

from pathlib import Path

#p1 = Path('Pathlib_Library/abc.txt')  #--> p1 is of type: <class 'pathlib.PosixPath'>

# with open(p1, 'r') as file:
#     print(file.read())

# if p1.exists():
#     with open(p1, 'r') as file:
#         print(file.read())

# creating new file:

p1 = Path('Pathlib_Library/abc.txt')
if not p1.exists():
    with open(p1, 'w') as file:
        print(file.write('Content 1'))
# if p1.exists():
#     with open(p1, 'r') as file:
#         print(file.read())

p2 = Path('Pathlib_Library/def.txt')
if not p2.exists():
    with open(p2, 'w') as file:
        print(file.write('Content 2'))

p3 = Path('Pathlib_Library/ghi.txt')
if not p3.exists():
    with open(p3, 'w') as file:
        print(file.write('Content 3'))


