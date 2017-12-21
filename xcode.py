# the stripe scale is (p)*(p)
# position is defined as (x,y) instead of a number
# bug: error disk is only allowed to be disk0, code remains to be improved to allow other disk(see comments in method2)

# correctness remains to be checked
def xcode_IO_Generator(prime, error_disk, c, scheme):
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

        # 0---diagnol decoding
        if (recovery_method == 0 and i != prime-1)or (recovery_method == 1 and i == prime-2):
            recovery_sequence.append(xcode_method0(error_block_position, prime))

        # 1---anti-diagnol decoding
        if (recovery_method == 1 and i != prime-2)or (recovery_method == 0 and i == prime-1):
            recovery_sequence.append(xcode_method1(error_block_position, prime))

    return recovery_sequence


def xcode_method0(position, p):
    (x, y) = position
    sequence = []

    # if missing block is parity block
    if y == p-2:
        for j in range(0, p-2):
            block_position=(j, (j+y+2)%p)
            sequence.append(block_position)
        return set(sequence)

    # missing block is data block

    i = (y-x-2) % p

    for j in range(0, p-2):
        if j != x:
            block_position = (j, (i+j+2)%p)
            sequence.append(block_position)

    block_position = (p-2, i)
    sequence.append(block_position)
    return set(sequence)


def xcode_method1(position, p):
    (x, y) = position
    sequence = []

    # if missing block is parity block
    if y == p-1:
        for j in range(p-2):
            block_position = (j, (y+p-j-2) % p)
            sequence.append(block_position)
        return set(sequence);

    # missing block is data block
    i = (x + y+2) % p

    for j in range(0, p-2):
        if j != x:
            block_position = (j, (i+p-j-2) % p)
            sequence.append(block_position)

    block_position = (p-1, i)
    sequence.append(block_position)
    return set(sequence)