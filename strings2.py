x=3; y=2.5; z=3+4j
print(x,type(x))
print(y,type(y))
print(z,type(z))

b1=True
b2=False

i1=1

print(bool(i1))

print(int("10")+2)
print("10"+str(2))

#0, None, {}, [], () are False

print("Values {}\t{}\t{}".format(z,y,x))

myVar=f"val {z}"
print(myVar)

big="""
Multiline
Meaning
Lines"""

print(big)
print(len(big))

print(f"Last index... {big[len(big)-1]}")
print(f"Last index... {big[-1]}")
print(f"Last index -5... {big[-5:]}")
print(f"Some... {big[-1*len(big):-15]}")


print(f"Index 2 to 5... {big[2:5]}")

v1="Hello".lower()+"   "+"world".upper().capitalize()
print(v1.title().swapcase())
print(dir(v1))