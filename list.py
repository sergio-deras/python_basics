my_vals=[False,1,"OK",1.5,True]
print(my_vals)
print(type(my_vals))

print(my_vals[0])
print(my_vals[-1])

my_vals[3]=3

print(my_vals.index(3))

print(my_vals[2:])
print(my_vals[2:4])


print(my_vals.count("OK"))
the_vals=my_vals
other_vals=my_vals.copy()
my_vals.clear()

print(other_vals)
print(the_vals)

print(id(other_vals))
print(id(my_vals))
print(id(the_vals))

the_vals.append("0")
print(the_vals)

the_vals.insert(0,-1)
print(the_vals)

the_vals.extend(other_vals)
print(the_vals)

the_vals.remove(True)
print(the_vals)

print(the_vals.pop())
print(the_vals)

print(the_vals.pop(2))
print(the_vals)

the_vals = [8,21,1,5]
the_vals.sort()
print(the_vals)


the_vals.reverse()
print(the_vals)

the_vals.sort(reverse=True)
print(the_vals)









