import time
from FBF_cache_time import *
from ARC_cache import *
from LFU_cache import *
from LRU_cache import *
from FIFO_cache import *
from NO_cache import *
import os

dir_path = os.path.dirname(os.path.realpath(__file__)) + "\\trace\\"
code_dic={1:"star",2:"triple_star",3:"triple_parity",4:"tip",5:"hdd1"}

prime_number = (5,7,11,13)
error_disk = 0
stripe_number = 1
cache_size_range= 360
code_type_number=5
run_times=1
cache_size=20

# code= 1---star
#       2---triple_star
#       3---triple_parity
#       4---tip
#       5---hdd1

#run 1 times
for i in range (1, run_times+1):
    for code in range(1, code_type_number+1):
        for prime in prime_number:
                (parameter_prefix, b, counter) = NO_cache_trace(code, prime, error_disk, stripe_number,int((prime-1)/2), dir_path, 1)

                (a, b, t)=FBF_cache_trace(parameter_prefix, dir_path, cache_size)
                print(str(code_dic[code]) + ',' + str(prime) + "," + str(t*1000))