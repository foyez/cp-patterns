def binary_search(items, target):
    l, r = 0, len(items) - 1

    while l <= r:
        m = l + (r-l)//2

        if target == items[m]:
            return True
        elif target > items[m]:
            l = m + 1
        else:
            r = m - 1
    return False

def binary_search_recursive(items, target):
    def recursive_search(l, r):
        if l > r:
            return False

        m = l + (r - l) // 2
        if target == items[m]:
            return True
        elif target > items[m]:
            return recursive_search(m+1, r)
        else:
            return recursive_search(l, m - 1)

    return recursive_search(0, len(items) - 1)

items = [1,2,3,4,5,6]
print(binary_search(items, 3))
print(binary_search(items, 9))

print(binary_search_recursive(items, 5))
print(binary_search_recursive(items, -1))