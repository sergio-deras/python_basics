#Error

try:
    x=4/1
    #x=4/0
    raise TypeError("Provoked")
except TypeError:
    print("A TypeError")
except ZeroDivisionError:
    print("A ZeroDivisionError")
except Exception as e:
    print(f'An exception {e}')
else:
    print("OK")
finally:
    print("The end")


a=3;b=2
try:
    assert a<b
except AssertionError:
    print("An AssertionError")