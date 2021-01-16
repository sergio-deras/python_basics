print("Look\n\tnow\b\bothing 'here' or \"there\"")
print("May be in C:\\system32")

my="Python"

print(my.startswith('P'))
print(my.startswith('Pyt'))

print(my.endswith('hon'))

print(my.islower())
print(my.isupper())

print(my.istitle())
print(my.isspace())
print(my.isalpha())
print(my.isnumeric())

her="-".join(my)

print(f"{my.center(50)}\n{her.center(50)}")

print(f"{my.ljust(50)}")
print(f"{my.rjust(50)}")

print(her.zfill(50))

import os
cols=os.get_terminal_size().columns
print(f"{my.ljust(cols)}")
print(f"{my.rjust(cols)}")
print(f"{my.center(cols)}")


his="Language  X   "

print(his.strip()+"OK") ##Initial and final
print(his.strip("La"))

#Strip does not work with inside chars since 3.6
print(his.replace("a",""))
print(his.split("a"))

print(his.count("a"))
print(his.index("X"))
print(his.index("a",3))
print(his.find("a",100))