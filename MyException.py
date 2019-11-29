class MyException(Exception):
    def __init__(self,v):
        self.v=v
        
    def __str__(self,v):
        print(v)
i=int(input())
j=int(input())
def xyz (i,j):
    return i+j
if xyz(i,j)>150:
    print(i+j)
else:
    raise MyException('Custom Exception Occurred')
