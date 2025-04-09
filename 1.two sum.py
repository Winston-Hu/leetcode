"""
字典的key是唯一的，后面相同的key的值会代替前面的key的值
"""


def twoSum(nums: list, target: int):
    my_dict = {}

    for i, num in enumerate(nums):
        my_dict[num] = i

    for i, num in enumerate(nums):
        temp = target - num
        if temp in my_dict and (i != my_dict[temp]):
            return [i, my_dict[temp]]


def main():
    nums = [1, 3, 0, 3]
    target = 6
    res = twoSum(nums, target)
    print(res)


if __name__ == '__main__':
    main()