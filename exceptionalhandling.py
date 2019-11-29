print('start')
try:
    h=eval(input('enter value'))
    print('data',50/h)
except ValueError as e:
    print('not valid')
except EOFError as e:
    print('end file')
except(ZeroDivisionError,TypeError,AttributeError) as e:
    print('unknown error',e)
finally:
    print('end')
