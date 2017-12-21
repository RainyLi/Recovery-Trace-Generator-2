# the stripe scale is (p-1)*(p+1)
# position is defined as (x,y) instead of a number
# bug: error disk is only allowed to be disk0, code remains to be improved to allow other disk(see comments in method2)


# correctness remains to be checked

def rdp_IO_Generator(prime, error_disk, c, scheme):
    recovery_sequence = []
    for i in range(c):
        # the position of the block to be recovered
        error_block_position = (i, error_disk)

        # randomly picking the decoding method: 0==horizontal 1==diagnol
        if scheme == 1:
            recovery_method = i % 2
        else:
            recovery_method = 1
            # recovery_method=2

        # 0---horizontal decoding
        if recovery_method == 0:
            recovery_sequence.append(rdp_method0(error_block_position, prime))

        # 1---diagnol decoding
        if recovery_method == 1:
            recovery_sequence.append(rdp_method1(error_block_position, prime))


    return recovery_sequence


def rdp_method0(position, p):
    (x, y) = position
    sequence = []
    for j in range(0, p-1):
        if j != y:
            block_position = (x, j)
            sequence.append(block_position)
    return set(sequence)


def rdp_method1(position, p):
    (x, y) = position
    sequence = []


    i = (x + y) % p

    for j in range(0, p):
        if j!= y and (i - j + p + 1) % p:
            block_position = ((i - j) % p, j)
            sequence.append(block_position)

    block_position = (i , p)
    sequence.append(block_position)
    return set(sequence)