def fact(n :int) :

    """
Calculate n! using recursion.
 
Parameters
----------
num : int
 
Returns
-------
int
"""
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    if n==0 or n==1:
        return 1
    return n*fact(n-1)



def is_prime(n:int) -> bool:
    
    """
    Check whether a number is prime.
    
    Parameters
    ----------
    num : int
    Number to test.
    
    Returns
    -------
    bool
    True if prime, otherwise False.
    """
    if n <2 :
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True




def common_divisor(num1:int,num2:int) -> int:
   limit = min(num1,num2)
   divisors = []
   
   for divisor in range(1,limit+1):
       if num1%divisor==0 and num2%divisor==0:
           divisors.append(divisor)
   return divisors




