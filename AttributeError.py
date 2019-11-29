try:
    print(5+'omnee')
except TypeError as e:
    print('Error Handlled',e)
try:
     h="kush1"
     h=float(h)
except ValueError as e:
    print("Error handled",e)
class Atrributes():
    pass
try:
    print(object.attribute)
except AttributeError as e:
    print('Error handled',e)
    

 
        
    
