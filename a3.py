try:

    print (10 *(1/0))

    print (201/0)

    print (var*33)
except (ZeroDivisionError,NameError):
    print ('Error')