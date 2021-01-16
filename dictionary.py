

d={"zero":0,1:"one",2:"two",3:"three",4:"four",5:"five"}


print(d[2])
print(d.get("zero"))
print(d["zero"])

print(d.keys())
print(d.values())

d.pop("zero")
d.popitem()
print(d)
d.setdefault("zero","zero")
print(d.get("zero"))



