#collatz conjecture by @Noulion
import time 


#conjecture-calculator
def cc(x):
    print(x)
    
    #Calcultion loop
    while x != 1:
        time.sleep(0.02)
        
        #if x is less than or equal to 0
        if x <= 0:
            break
        #if x is not even then do 3x+1
        if (x % 2) != 0:
            x = x*3+1
            print(int(x))
        #if x is even then divide by 2
        else:
            x = x / 2
            print(int(x))
                     
cc(x)
"""
The Collatz Conjecture, also known as the 
"3n + 1" sequence, proposes that starting with any positive number and applying two rules 
(if even, divide by two; if odd, triple it and add one) will always eventually lead to these following outcomes:
    0
    1-4-2 loop

src:https://science.howstuffworks.com/math-concepts/collatz-conjecture.htm
"""
