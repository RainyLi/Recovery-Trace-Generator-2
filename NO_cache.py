from star import *
from triple_star import *
from triple_parity import *
from tip import *
from hdd1 import *
import random
def recovery_sequence_blockcounter(recovery_sequence):
    error_block_num = len(recovery_sequence)

    recovery_block_set = set([])
    for i in range(error_block_num):
        for block_position in recovery_sequence[i]:
            recovery_block_set.add(block_position)
    return len(recovery_block_set)



def origin_trace_simple(recovery_sequence, code, prime, error_disk, stripe_number, continuous, dir_path, scheme):
    request_count=0
    if code==1:
        parameter_prefix = "star"
    elif code==2:
        parameter_prefix = "triple_star"
    elif code==3:
        parameter_prefix = "triple_parity"
    elif code==4:
        parameter_prefix = "tip"
    elif code==5:
        parameter_prefix = "hdd1"
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
                request_count=request_count+1

    f_origin.close()
    counter=recovery_sequence_blockcounter(recovery_sequence)
    return (parameter_prefix,request_count, stripe_number*counter)

def origin_trace_random(code, prime, error_disk, stripe_number, continuous, dir_path, scheme):
    request_count=0
    if code==1:
        parameter_prefix = "star"
    elif code==2:
        parameter_prefix = "triple_star"
    elif code==3:
        parameter_prefix = "triple_parity"
    elif code==4:
        parameter_prefix = "tip"
    elif code==5:
        parameter_prefix = "hdd1"
    parameter_prefix=parameter_prefix+"_p=" + str(prime) + "_error=" + str(error_disk) + "_stripe=" + str(
        stripe_number) + "_continuous=" + str(continuous) + "_scheme=" + str(scheme)
    f_origin_name = parameter_prefix + "_origin.trace"

    f_origin = open(dir_path + f_origin_name, "w")

    # generate recovery scheme per stripe based on continuous, and write to corresponding parameter_origin.trace
    counter=0
    if code==1:
        recovery_sequence_list=[]
        for c in range(1, prime-1):
            recovery_sequence_list.append(star_IO_Generator(prime, error_disk, c, scheme))
        for i in range(0, stripe_number):
            c = random.randint(1, prime-2)
            recovery_sequence = recovery_sequence_list[c-1]
            counter=counter+recovery_sequence_blockcounter(recovery_sequence)
            error_block_num = len(recovery_sequence)
            for j in range(error_block_num):
                for block_position in recovery_sequence[j]:
                    device_number = block_position[1]
                    block_number = block_position[0] + error_block_num * i

                    origin_trace = '0 ' + str(device_number) + ' ' + str(block_number) + ' 1 1\n'
                    f_origin.write(origin_trace)
                    request_count = request_count + 1
    elif code==2:
        recovery_sequence_list=[]
        for c in range(1, prime-1):
            recovery_sequence_list.append(triple_star_IO_Generator(prime, error_disk, c, scheme))
        for i in range(0, stripe_number):
            c = random.randint(1, prime-2)
            recovery_sequence = recovery_sequence_list[c - 1]
            counter = counter + recovery_sequence_blockcounter(recovery_sequence)
            error_block_num = len(recovery_sequence)
            for j in range(error_block_num):
                for block_position in recovery_sequence[j]:
                    device_number = block_position[1]
                    block_number = block_position[0] + error_block_num * i

                    origin_trace = '0 ' + str(device_number) + ' ' + str(block_number) + ' 1 1\n'
                    f_origin.write(origin_trace)
                    request_count = request_count + 1
    elif code==3:
        recovery_sequence_list=[]
        for c in range(1, prime-1):
            recovery_sequence_list.append(triple_parity_IO_Generator(prime, error_disk, c, scheme))
        for i in range(0, stripe_number):
            c = random.randint(1, prime-2)
            recovery_sequence = recovery_sequence_list[c - 1]
            counter = counter + recovery_sequence_blockcounter(recovery_sequence)
            error_block_num = len(recovery_sequence)
            for j in range(error_block_num):
                for block_position in recovery_sequence[j]:
                    device_number = block_position[1]
                    block_number = block_position[0] + error_block_num * i

                    origin_trace = '0 ' + str(device_number) + ' ' + str(block_number) + ' 1 1\n'
                    f_origin.write(origin_trace)
                    request_count = request_count + 1
    elif code==4:
        recovery_sequence_list=[]
        for c in range(1, prime-1):
            recovery_sequence_list.append(tip_IO_Generator(prime, error_disk, c, scheme))
        for i in range(0, stripe_number):
            c = random.randint(1, prime-2)
            recovery_sequence = recovery_sequence_list[c - 1]
            counter = counter + recovery_sequence_blockcounter(recovery_sequence)
            error_block_num = len(recovery_sequence)
            for j in range(error_block_num):
                for block_position in recovery_sequence[j]:
                    device_number = block_position[1]
                    block_number = block_position[0] + error_block_num * i

                    origin_trace = '0 ' + str(device_number) + ' ' + str(block_number) + ' 1 1\n'
                    f_origin.write(origin_trace)
                    request_count = request_count + 1
    elif code==5:
        recovery_sequence_list=[]
        for c in range(1, prime-1):
            recovery_sequence_list.append(hdd1_IO_Generator(prime, error_disk, c, scheme))
        for i in range(0, stripe_number):
            c = random.randint(1, prime-2)
            recovery_sequence = recovery_sequence_list[c - 1]
            counter = counter + recovery_sequence_blockcounter(recovery_sequence)
            error_block_num = len(recovery_sequence)
            for j in range(error_block_num):
                for block_position in recovery_sequence[j]:
                    device_number = block_position[1]
                    block_number = block_position[0] + error_block_num * i

                    origin_trace = '0 ' + str(device_number) + ' ' + str(block_number) + ' 1 1\n'
                    f_origin.write(origin_trace)
                    request_count = request_count + 1

    f_origin.close()
    return (parameter_prefix,request_count, counter)



def NO_cache_trace(code, prime, error_disk, stripe_number, continuous, dir_path, scheme):

    if (continuous!=0):
        #generate recovery scheme on stripe
        if code==1:
            recovery_sequence = star_IO_Generator(prime, error_disk, continuous, scheme)
        elif code==2:
            recovery_sequence = triple_star_IO_Generator(prime, error_disk, continuous, scheme)
        elif code==3:
            recovery_sequence = triple_parity_IO_Generator(prime, error_disk, continuous, scheme)
        elif code==4:
            recovery_sequence = tip_IO_Generator(prime, error_disk, continuous, scheme)
        elif code==5:
            recovery_sequence = hdd1_IO_Generator(prime, error_disk, continuous, scheme)
        #generate trace on stack given recovery scheme
        return origin_trace_simple(recovery_sequence, code, prime, error_disk, stripe_number, continuous, dir_path, scheme)

    else:
        return origin_trace_random(code, prime, error_disk, stripe_number, continuous, dir_path, scheme)


