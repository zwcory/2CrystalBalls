import math

def two_crystal_ball_root2(floors):
    n = len(floors)
    if n == 0:
        return -1

    jmp_amount = math.floor(math.sqrt(n))
    i= jmp_amount

    while i < n:
        if floors[i]:
            break
        i += jmp_amount

    # go back to last safe drop
    i -= jmp_amount
    j = 0

    while j <= jmp_amount and i < n:
        if floors[i]:
            return i
        i += 1
        j += 1


    return -1

def step_counter(floors):
    n = len(floors)
    if n == 0:
        return -1
    x = 0

    jmp_amount = math.floor(math.sqrt(n))
    i= jmp_amount

    while i < n:
        x += 1
        if floors[i]:
            break
        i += jmp_amount
    else:
    # If we exited without breaking, we need one more check
    # at the boundary (simulating going past the end)
        x += 1

    # go back to last safe drop
    i -= jmp_amount
    j = 0

    while j <= jmp_amount and i < n:
        x += 1
        if floors[i]:
            return x
        i += 1
        j += 1


    return -1