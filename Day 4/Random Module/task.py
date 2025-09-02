#import random
#import my_module
#random_integers = random.randint(1, 10)
#print(random_integers)
#print(my_module.my_favourite_number)

#for random floating number----> random.random()---->0.0<=X<1.0
#import random
#random_number_0_to_1 = random.random()
#print(random_number_0_to_1)

#random floating point number---->random.uniform(a,b)---->a <= N <= b
#random_float = random.uniform(1,10)
#print(random_float)

import random
random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 0:
    print("Heads!!")
else:
    print("Tails!!")
