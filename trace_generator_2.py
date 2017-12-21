# no modification yet

from FBF_cache import *
from ARC_cache import *
from LFU_cache import *
from LRU_cache import *
from FIFO_cache import *
from NO_cache import *
import os

dir_path = os.path.dirname(os.path.realpath(__file__)) + "\\trace\\"
#f_metric = open(dir_path+"hitRatio_and_diskIO.csv", 'w')
code_dic={1:"star",2:"triple_star",3:"triple_parity",4:"tip",5:"hdd1"}
#f_metric.write("code,prime,error_disk,stripe_number,continuous_unit,cache_size,cache_method,hit_ratio\n")

# maximum value
prime_number = (13,)
error_disk = 0
stripe_number = 100
continuous_unit = 1
cache_size_range= (1,2,4,8,16,32,64,128)
code_type_number= 5
run_times=1
scheme_comp=0

# code= 1---star
#       2---triple_star
#       3---triple_parity
#       4---tip
#       5---hdd1

#continuous_unit = 1,2,3,...,p-1     ----normal situation
#                = 0                 ----random


if (scheme_comp==0):
    #run 1 times
    for i in range (1, run_times+1):
        f_metric = open(dir_path + "hitRatio_and_diskIO"+str(i)+".csv", 'w')
        f_metric.write("code,prime,error_disk,stripe_number,continuous_unit,cache_size,cache_method,hit_ratio,diskIO\n")

        for code in range(1, code_type_number+1):
            for prime in prime_number:
                for continuous in range(0, prime):
                    (parameter_prefix, disk_io, blockcount) = NO_cache_trace(code, prime, error_disk, stripe_number, continuous, dir_path, 1)
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

else:
    # run 1 times

    #scheme == 0: conventional scheme
    #       == 1: FBF scheme
    dir_path = os.path.dirname(os.path.realpath(__file__)) + "\\SchemeCompTrace\\"
    for i in range(1, run_times + 1):
        f_metric = open(dir_path + "scheme_blockcount" + str(i) + ".csv", 'w')
        f_metric.write("code,prime,error_disk,stripe_number,continuous_unit,scheme,blockcount\n")

        for code in range(1, code_type_number + 1):
            for prime in prime_number:
                for continuous in range(1, prime):

                    #conventional scheme
                    print("i=" + str(i) + " code=" + str(code) + " prime=" + str(prime) + " continuous=" + str(
                        continuous)  + " scheme=0\n")
                    (parameter_prefix, disk_io, blockcount) = NO_cache_trace(code, prime, error_disk, stripe_number, continuous,
                                                                 dir_path, 0)
                    f_metric.write(code_dic[code] + "," + str(prime) + "," + str(error_disk) + "," + str(
                        stripe_number) + "," + str(continuous) + ",0," + str(blockcount) + "\n")

                    #FBF scheme
                    print("i=" + str(i) + " code=" + str(code) + " prime=" + str(prime) + " continuous=" + str(
                        continuous) + " scheme=1\n")
                    (parameter_prefix, disk_io, blockcount) = NO_cache_trace(code, prime, error_disk, stripe_number, continuous,
                                                                    dir_path, 1)
                    f_metric.write(code_dic[code] + "," + str(prime) + "," + str(error_disk) + "," + str(
                        stripe_number) + "," + str(continuous) + ",1," + str(blockcount) + "\n")

        f_metric.close()
