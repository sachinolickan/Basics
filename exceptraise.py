def divide(x,y):
    try:
        result=x/y
        raise TypeError
    except ZeroDivisionError:
        print("division by zero is not possible")
    except TypeError:
        print("type is different")
    except:
        print("something went wromg!")
    else:
        print("result:",result)
    finally:
        print("execution over!")
divide('2',1)
