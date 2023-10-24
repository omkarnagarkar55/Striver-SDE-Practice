def subarraysWithXorK(a: [int], b: int) -> int:
    n = len(a)  # size of the given array.
    cnt = 0

    # Step 1: Generating subarrays:
    for i in range(n):
        xorr = 0
        for j in range(i, n):

            # step 2: calculate XOR of all elements:
            xorr = xorr ^ a[j]

            # step 3: check XOR and count:
            if (xorr == b):
                cnt += 1

    return cnt