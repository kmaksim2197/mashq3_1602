n = int(input())
arr = list(map(int, input().split()))
x = int(input())

l, r = 0, n - 1
while l <= r:
    mid = (l + r) // 2
    if arr[mid] == x:
        print(mid)
        break
    elif arr[mid] < x:
        l = mid + 1
    else:
        r = mid - 1
else:
    print(-1)
