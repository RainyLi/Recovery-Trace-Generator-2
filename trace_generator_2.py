# no modification yet

from FBF_cache import *
from ARC_cache import *
from LFU_cache import *
from LRU_cache import *
from FIFO_cache import *
from NO_cache_2 import *

import os

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/trace/"
#f_metric = open(dir_path+"hitRatio_and_diskIO.csv", 'w')
code_dic={1:"star",2:"triple_star",3:"triple_parity",4:"tip",5:"hdd1", 6:"evenodd", 7:"rdp", 8:"xcode"}
#f_metric.write("code,prime,error_disk,stripe_number,continuous_unit,cache_size,cache_method,hit_ratio\n")

# maximum value
prime_number = (5,7,11,13,17)
error_disk = 0
stripe_number = 100
continuous_unit = 1
cache_size_range= (1,2,4,8,16,32,64,128)
run_times=1
scheme_comp=0

# code= 6---evenodd
#       7---rdp
#       8---xcode

#continuous_unit = 1,12,3,...,p-1     ----normal situation
#                = 0                 ----random

for i in range (1, run_times+1):
        f_metric = open(dir_path + "hitRatio_and_diskIO"+str(i)+".csv", 'w')
        f_metric.write("code,prime,error_disk,stripe_number,continuous_unit,cache_size,cache_method,hit_ratio,diskIO\n")

        for code in range(6, 9):
            for prime in prime_number:
                for continuous in range(prime-1, prime):
                    (parameter_prefix, disk_io, blockcount) = NO_cache_trace_2(code, prime, error_disk, stripe_number, continuous, dir_path, 1)
                    f_metric.write(code_dic[code] + "," + str(prime) + "," + str(error_disk) + "," + str(stripe_number) + "," + str(continuous) + ",0,-,0,"+str(disk_io)+"\n")

                    for cache_size in cache_size_range:
                        #print the progress
                        print("i="+str(i)+" code=" + str(code)+" prime=" + str(prime)+" continuous=" + str(continuous) + " cache=" + str(cache_size) + "\n")

                        (hit_ratio, disk_io) = FIFO_cache_trace(parameter_prefix, dir_path, cache_size)
                        f_metric.write(
                            code_dic[code] + "," + str(prime) + "," + str(error_disk) + "," + str(stripe_number) + "," + str(continuous) + "," + str(
                                cache_size) + ",FIFO," + str(hit_ratio) + "," + str(disk_io) + "\n")

                        (hit_ratio, disk_io) = LRU_cache_trace(parameter_prefix, dir_path, cache_size)
                        f_metric.write(
                            code_dic[code] + "," + str(prime) + "," + str(error_disk) + "," + str(stripe_number) + "," + str(continuous) + "," + str(
                                cache_size) + ",LRU," + str(hit_ratio) + ","+ str(disk_io) + "\n")

                        (hit_ratio, disk_io) = LFU_cache_trace(parameter_prefix, dir_path, cache_size)
                        f_metric.write(
                            code_dic[code] + "," + str(prime) + "," + str(error_disk) + "," + str(stripe_number) + "," + str(continuous) + "," + str(
                                cache_size) + ",LFU," + str(hit_ratio) + ","+ str(disk_io) + "\n")

                        (hit_ratio, disk_io) = ARC_cache_trace(parameter_prefix, dir_path, cache_size)
                        f_metric.write(
                            code_dic[code] + "," + str(prime) + "," + str(error_disk) + "," + str(stripe_number) + "," + str(continuous) + "," + str(
                                cache_size) + ",ARC," + str(hit_ratio) + ","+ str(disk_io) + "\n")

                        (hit_ratio, disk_io, time) = FBF_cache_trace(parameter_prefix, dir_path, cache_size)
                        f_metric.write(
                            code_dic[code] + "," + str(prime) + "," + str(error_disk) + "," + str(stripe_number) + "," + str(continuous) + "," + str(
                                cache_size) + ",FBF," + str(hit_ratio) + ","+ str(disk_io) + "\n")

        f_metric.close()


