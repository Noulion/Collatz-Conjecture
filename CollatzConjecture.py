#collatz conjecture by @Noulion
import time
from termcolor import colored as css 


#conjecture-calculator
def cc(x):
    print(css(x, 'green', attrs=['bold']))
    
    #Calcultion loop, while x isn't 1 do the following:
    while x != 1:
        time.sleep(0.02)
        
        #if x is less than or equal to 0
        if x <= 0:
            break
        #if x is not even then do 3x+1
        if (x % 2) != 0:
            x = x*3+1
            print(css(int(x), 'green', attrs=['bold']))
        #if x is even then divide by 2
        else:
            x = x / 2
            print(css(int(x), 'green', attrs=['bold']))

#main-body
def main():
    while True:
        try:
            cc_x = int(input('Type a number to calculate: '))
            if cc_x == cc_x:
                cc(cc_x)
        except ValueError:
            print('Number only')
main()
"""
The Collatz Conjecture, also known as the 
"3n + 1" sequence, proposes that starting with any positive number and applying two rules 
(if even, divide by two; if odd, triple it and add one) will always eventually lead to the following outcome:
    1-4-2 loop

src:https://science.howstuffworks.com/math-concepts/collatz-conjecture.htm
"""
