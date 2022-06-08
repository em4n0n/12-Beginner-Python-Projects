import random
import time
#[1, 3, 6, 7, 9, 12, 13]
# implement naive search
def naive_search(l, target): #l would be the list, and target would be 12(the number we are looking for)
    for i in range(len(l)):
        if l[i] == target:
            return i

    return -1 #we haven't found the number yet 

def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    #getting the midpoint
    midpoint = (low + high)  // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        new_high = midpoint - 1
        return binary_search(l, target, low, new_high)
    else:
        # target > l[midpoint]
        new_low = midpoint + 1
        return binary_search(l, target, new_low, high)

if __name__ == '__main__':
    # l = [1, 3, 6, 7, 9, 12, 13]
    # target = 12
    # print(naive_search(l, target))
    # print(binary_search(l, target))

    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    target_list = [random.randint(-3*length, 3*length) for _ in range(length)]

    start = time.time()
    for target in target_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time:", (end - start), "seconds")

    start = time.time()
    for target in target_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time:", (end -start), "seconds")
