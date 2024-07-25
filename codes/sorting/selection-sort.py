# Selection Sort
# select minimum and swap
# TC: O(n^2), SC: O(1)

def selectionSort(nums):
    for i in range(len(nums) - 1):
        for j in range(i, len(nums)):
            if nums[i] > nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp

    return nums

l = [5,2,3,1]
print(selectionSort(l))