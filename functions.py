def myf():
    print(x)

def main():
    global x
    x = 10
    myf()

if __name__ == "__main__":
    main()

def fu(a,b,c=10):
    print(a,b,c)

fu(c=1,b=2,a=3)

def fux(*args):
    print(type(args))
    for each in args:
        print(each)

fux('z','y','x')

def fuxx(**kvargs):
    print(type(kvargs))
    for each in kvargs:
        print(each, kvargs[each])

fuxx(i=1,j=2,k=3)
