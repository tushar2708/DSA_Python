def max_contiguous_subarray_sum(arr):
    curr_sum = 0
    max_sum = float('-inf')
    for i in arr:
        curr_sum += + i

        max_sum = max(max_sum, curr_sum)

        if curr_sum < 0:
            curr_sum = 0

    return max_sum


def missing_number(arr):
    l = len(arr) + 1
    expected = 0
    actual = 0
    for i in range(1, l + 1):
        expected ^= i
    for i in arr:
        actual ^= i

    res = actual ^ expected
    return res


def contiguous_subarray_with_given_sum(arr, target_sum):
    curr_sum = arr[0]
    start = 0
    i = 1
    n = len(arr)
    # print(n)

    while i <= n:

        # If current sum crosses target_sum, removes items from left
        while curr_sum > target_sum and start < i - 1:
            # print("before back-curr_sum: ", curr_sum, "start:", start, "i:", i)
            curr_sum -= arr[start]
            start += 1
            # print("after back-curr_sum: ", curr_sum, "start:", start, "i:", i)

        # If current sum reaches target_sum, return sub-array
        if curr_sum == target_sum:
            return start+1, i

        if i < n:
            curr_sum += arr[i]
        # print("forward-curr_sum: ", curr_sum, "start:", start, "i:", i)
        i += 1

    return -1, -1


def sort_into_2_parts(arr, start, end, pivot):
    while start < end:
        while arr[start] < pivot and start < end:
            start += 1

        while arr[end] >= pivot and start < end:
            end -= 1

        (arr[start], arr[end]) = (arr[end], arr[start])

    print("start", start, "end", end)
    return arr, start, end


def sort_array_of_0_1_2(arr):
    n = len(arr)

    arr, s, e = sort_into_2_parts(arr, 0, n-1, 1)
    arr, s, e = sort_into_2_parts(arr, e, n-1, 2)

    return arr

def array_parted_sum(arr, pivot):
    sum_1 = 0
    sum_2 = 0
    n = len(arr)
    for i in range(pivot):
        sum_1 += arr[i]
    for i in range(pivot+1, n):
        sum_2 += arr[i]

    return sum_1, sum_2


def find_equilibrium_point(arr):
    n = len(arr)
    start = 0
    end = n-1
    pivot = n//2
    print(pivot)
    sum_1, sum_2 = array_parted_sum(arr, pivot)
    print("sum_1", sum_1, "sum_2", sum_2)
    if sum_1 == sum_2:
        return pivot

    elif sum_1 < sum_2:
        while sum_1 < sum_2 and pivot >= 0:
            print("< bfore: sum_1", sum_1, "\tsum_2", sum_2, "\tpivot", pivot, "\tarr[pivot]", arr[pivot])
            sum_1 += arr[pivot]
            pivot += 1
            sum_2 -= arr[pivot]
            print("< after: sum_1", sum_1, "\tsum_2", sum_2, "\tpivot", pivot, "\tarr[pivot]", arr[pivot], "\n")

    elif sum_1 > sum_2:
        while sum_1 > sum_2 and pivot >= 0:
            print("> bfore: sum_1", sum_1, "\tsum_2", sum_2, "\tpivot", pivot, "\tarr[pivot]", arr[pivot])
            sum_2 += arr[pivot]
            pivot -= 1
            sum_1 -= arr[pivot]
            print("> after: sum_1", sum_1, "\tsum_2", sum_2, "\tpivot", pivot, "\tarr[pivot]", arr[pivot], "\n")

    if sum_1 == sum_2:
        return pivot

    return -1
