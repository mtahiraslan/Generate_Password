import random

lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="[]{}()*;/,._-"

all_variable=lower+upper+numbers+symbols
lenght=8

password="".join(random.sample(all_variable,lenght))

print(password)
