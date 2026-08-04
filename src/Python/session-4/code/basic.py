'''  
this first basic module of python
 
 
fun_1: get_info
 
'''
 
 
 
 
def get_info(name: str, age: int ):
    '''  function for person information get the name and age and
        return back again to user
       
        Args:
            param_1:name get the name of person
            type_param_1: str
            param_2:age get the age from usr
            type_param_2: int
           
            return: this function return the name and age
            type_return:str
   
    '''
    return f"my name is {name}, age is {age}"




def add(x: float , y:float):
    '''
    sum funtion 
    
    args:
        param_1= user must input the first num
        type_param_1: float
        param_2= user must input the sconed num
        type_param_2: float
         retutn : this function return sum of two nums
         return type: float        
    
    '''
    return x+y





def sub(x: float , y:float):
    '''
    sub funtion 
    
    args:
        param_1= user must input the first num
        type_param_1: float
        param_2= user must input the sconed num
        type_param_2: float
         retutn : this function return sub of two nums
         return type: float        
    
    '''
    return x-y



def mult(x: float , y:float):
    '''
    multiply funtion 
    
    args:
        param_1= user must input the first num
        type_param_1: float
        param_2= user must input the sconed num
        type_param_2: float
         retutn : this function return multiply of two nums
         return type: float        
    
    '''
    return x*y



def div(x: float , y:float):
    '''
    divesion funtion 
    
    args:
        param_1= user must input the first num
        type_param_1: float
        param_2= user must input the sconed num
        type_param_2: float
         retutn : this function return div of two nums
         return type: float        
    
    '''
    return x/y