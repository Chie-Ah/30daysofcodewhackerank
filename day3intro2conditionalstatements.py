# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Complete the stub code provided below  to print whether or not  is weird.

# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys


# #complete this code
# if __name__ == '__main__':
#     N = int(input().strip())


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    if N % 2 == 1:  # N is odd
        print('Weird')
    elif N % 2 == 0 and 2 <= N <= 5: #N is even & falls btwn 2 & 5
        print('Not Weird')
    elif N % 2 == 0 and 6 <= N <= 20: #N is even and falls between 6 & 20
        print('Weird')
    else: #N is even and greater than 20
        print('Not Weird')
