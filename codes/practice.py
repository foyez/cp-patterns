def minSwaps(nums):
    N = len(nums)
    total_ones = nums.count(1)
    l = 0

    window_ones = max_window_ones = 0

    for r in range(2 * N):
        if nums[r % N]:
            window_ones += 1

        if r - l + 1 > total_ones:
            window_ones -= nums[l % N]
            l += 1

        max_window_ones = max(max_window_ones, window_ones)

    return total_ones - max_window_ones

print(minSwaps([0,1,0,1,1,0,0]))
print(minSwaps([0,1,1,1,0,0,1,1,0]))
print(minSwaps([1,1,0,0,1]))