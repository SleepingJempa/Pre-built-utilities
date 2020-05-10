def count_inversions(a):
    m = len(a)
    mid = m // 2
    if m == 2:
        return 1 if a[0] > a[1] else 0
    elif m == 1:
        return 0
    else:
        left: list = a[:mid+1]
        right: list = a[mid+1:]
        ans = count_inversions(left) + count_inversions(right)
        left.sort()
        right.sort()
        left_index = len(left) - 1
        right_index = len(right) - 1
        while left_index >= 0 and right_index >= 0:
            if left[left_index] > right[right_index]:
                ans += right_index + 1
                left_index -= 1
            else:
                right_index -= 1
        return ans


input()
print(count_inversions(list(map(int, input().split()))))
