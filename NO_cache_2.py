#this file is used to check whether double-disk-recovery codes are correct
# include
#       evenodd
#       rdp
#       xcode

# 2 means it is used for the optimizatin of 2DFTs and it is version2.0

# correctness remains to be checked

from evenodd import *
from rdp import *
from xcode import *

import random

def recovery_sequence_blockcounter_2(recovery_sequence):
    error_block_num = len(recovery_sequence)

    recovery_block_set = set([])
    for i in range(error_block_num):
        for block_position in recovery_sequence[i]:
            recovery_block_set.add(block_position)
    return len(recovery_block_set)



def origin_trace_simple_2(recovery_sequence, code, prime, error_disk, stripe_number, continuous, dir_path, scheme):
    request_count=0

    if code == 6:
        parameter_prefix = "evenodd"
    elif code == 7:
        parameter_prefix = "rdp"
    elif code == 8:
        parameter_prefix = "xcode"

    parameter_prefix=parameter_prefix+"_p=" + str(prime) + "_error=" + str(error_disk) + "_stripe=" + str(
        stripe_number) + "_continuous=" + str(continuous) + "_scheme=" + str(scheme)
    f_origin_name = parameter_prefix + "_origin.trace"

    f_origin = open(dir_path + f_origin_name, "w")
    error_block_num = len(recovery_sequence)

    for i in range(0, stripe_number):
        for j in range(error_block_num):
            for block_position in recovery_sequence[j]:
                device_number = block_position[1]
                block_number = block_position[0] + error_block_num * i

                origin_trace = '0 ' + str(device_number) + ' ' + str(block_number) + ' 1 1\n'
                f_origin.write(origin_trace)
                request_count = request_count+1

    f_origin.close()
    involvedblockcounter=recovery_sequence_blockcounter_2(recovery_sequence)
    return (parameter_prefix,request_count, stripe_number*involvedblockcounter)



def NO_cache_trace_2(code, prime, error_disk, stripe_number, continuous, dir_path, scheme):

    if (continuous!=0):
        #generate recovery scheme on stripe
        if code==6:
            recovery_sequence = evenodd_IO_Generator(prime, error_disk, continuous, scheme)
        elif code==7:
            recovery_sequence = rdp_IO_Generator(prime, error_disk, continuous, scheme)
        elif code==8:
            recovery_sequence = xcode_IO_Generator(prime, error_disk, continuous, scheme)

        #generate trace on stack given recovery scheme
        return origin_trace_simple_2(recovery_sequence, code, prime, error_disk, stripe_number, continuous, dir_path, scheme)


