import re

# Eg 1:

text = "Here is example@example.com and again another another@example.com"
pattern = re.compile("[a-z]+@[a-z]+.[a-z]+")
matches = pattern.findall(text)
print(matches)  #--> ['example@example.com', 'another@example.com']

# Eg 2:

text1 = 'Hi there you here exa_mple@example.com @blabla some more text here and there another@example.de'
pattern = re.compile("[^ ]+@[^ ]+.[a-z]+")
matches = pattern.findall(text1)
print(matches)  # --> ['exa_mple@example.com', 'another@example.de']


# Eg 3:

text3 = 'Hi there you here exa_mple@example.com @blabla.com some more text here and there another@example.de another@exampl.ne'


pattern = re.compile("[^ ]+@[^ ]+\.(?:com|de)+")
matches = pattern.findall(text3)
print(matches)


