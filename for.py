for i in range(5, -1, -1):
    print(i)

items = [1,2,3,5,8,13]

print("-----")
for i in items:
    print(i)


for i in [1, 2, 4, 5]:
    if i == 3:
       break
else: # executed if the loop iterates  throug all the items
    print("only executed when no item of the list is equal to 3")