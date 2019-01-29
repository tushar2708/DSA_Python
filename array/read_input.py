def print_arr(arr):
    for a in arr:
        print(a)
    print()


T = int(input())
for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print(arr)