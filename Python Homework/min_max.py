L = [2,1,2,4,5,7,6]

def find_min(num_list):
    min_val = num_list[0]
    for i in range (len(num_list)):
        if num_list[i] <=min_val:
            min_val=num_list[i]
    return min_val
print (find_min(L))

def find_max(num_list):
    max_val = num_list[0]
    for i in range (len(num_list)):
        if num_list[i] >=max_val:
            max_val=num_list[i]
    return max_val
print (find_max(L))

l=[3,2,1,5,7,9]

def min_find(nums):
    if not nums:
        return None
    min_num = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] < min_num:
            min_num = nums[i]
        i += 1
    return min_num
numbers = [5, 2, 9, 1, 7]
print(min_find(numbers))

def max_find(nums):
    if not nums:
        return None
    min_num = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] > min_num:
            min_num = nums[i]
        i += 1
    return min_num
numbers = [5, 2, 9, 1, 7]
print(max_find(numbers))