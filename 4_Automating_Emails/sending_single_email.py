# import yagmail


# sender = 'vionapinto@gmail.com'
# reciever = 'vionapinto@gmail.com'

# subject = 'This is the subject'

# contents = """Here is the content of the Email! Hello!"""

#yag = yagmail.SMTP(user=sender, password=)

import os

my_email = os.getenv('email')

my_password = os.getenv('password')

print(my_email, my_password)

