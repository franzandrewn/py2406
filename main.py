import random
from functools import wraps
from time import time


def timing(func):
    @wraps(func)
    def wrap(*args, **kw):
        ts = time()
        result = func(*args, **kw)
        te = time()
        print('func:%r took %2.10f sec' % (func.__name__, te - ts))
        return result

    return wrap


@timing
def sum_list(l):
    x = 0
    for i in l:
        x += i
    return x


l = [random.randint(-1000, 1000) for x in range(10000)]
# print(sum_list(l))


# Алгоритмы поиска - алгоритм, определяющий есть ли элемент в коллекции
col = [random.randint(-100000, 100000) for _ in range(1000000)]
# print(in_list)
correct_index = random.randint(0, len(col) - 1)
correct_answer = col[correct_index]


# print("correct answer " + str(correct_answer) + " on index " + str(correct_index))


# Линейный поиск - прохождение коллеции от начала до конца, если нашли цель - дать индекс найденного как ответ
# О(n)
def linear_search(col, target):
    for i in range(len(col)):
        if col[i] == target:
            return i
    return -1


# print("linear search: " + str(linear_search(in_list, correct_answer)))

col.sort()
# print(in_list)
correct_index = random.randint(0, len(col) - 1)
correct_answer = col[correct_index]


# print("correct answer " + str(correct_answer) + " on index " + str(correct_index))


# Бинарный поиск O(log(n))
# n=10 -> log(n) = 3.
# n=100 -> log(n) = 7.
# n= 1 000 000 -> log(n) = 20.
def binary_search(col, target):
    first = 0
    last = len(col) - 1
    result = -1
    i = 0
    while (first <= last) and (result == -1):
        i += 1
        mid = (first + last) // 2
        # print("first = " + str(first) + " last = " + str(last) + " mid = " + str(mid) + " col[mid] = " + str(col[mid]) + "\n\tcol[first:last + 1] " + str(col[first:last + 1]))
        if col[mid] == target:
            result = mid
        elif col[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    print("binary times in while loop: " + str(i))
    return result


# print("binary search: " + str(binary_search(in_list, correct_answer)))


# Экспоненциальный поиск - модификация бинарного O(log(n))
def exponential_search(col, target):
    if col[0] == target:
        return 0
    index = 1
    while index < len(col) and col[index] <= target:
        index *= 2
    return binary_search(col[:min(index, len(col))], target)


# print("exponential_search: " + str(exponential_search(in_list, correct_answer)))


# Интерполяционный поиск - поиск с "предугадываниям" местонахождения элемента O(log(log(n))
# Лучше всего работает на равномерных данных
def interpolation_search(col, target):
    first = 0
    last = len(col) - 1
    i = 0
    while first <= last and target >= col[first] and target <= col[last]:
        i += 1
        index = first + int((float(last - first) / (col[last] - col[first])) * (target - col[first]))
        if col[index] == target:
            print("interpol times in while loop: " + str(i))
            return index
        elif col[index] < target:
            first = index + 1
        else:
            last = index - 1
    return -1


# print("interpolation search: " + str(interpolation_search(in_list, correct_answer)))

# O(n), O(n^2) - O-нотация
# Возможность оценить скорость работы алгоритма

# Алгоритмы сортировки - отсортировать коллекцию по возрастанию/убыванию
in_list = [5, 1, 3, 7, 23, 23, 34, 67, 2, 1, 14, 6, 2]


# Пузырьковая сортировка
def bubble_sort(col):
    for _ in range(len(col)):
        for i in range(len(col) - 1):
            if col[i] > col[i + 1]:
                col[i], col[i + 1] = col[i + 1], col[i]


# bubble_sort(in_list)
# print(in_list)

# рекурсия - возможность запускать функцию из этой же функции
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# factorial(3) -> 3 * factorial(2) -> 3 * (2 * factorial(1)) -> 3 * (2 * 1) -> 3 * 2 -> 6
# print(factorial(3))


def partition(col, low, high):
    anchor = col[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while col[i] < anchor:
            i += 1

        j -= 1
        while col[j] > anchor:
            j -= 1

        if i >= j:
            return j

        col[i], col[j] = col[j], col[i]


# быстрая сортировка
def quick_sort(col):
    def _quick_sort(col, low, high):
        if low < high:
            print("anchor_index " + str((low + high) // 2))
            anchor_index = partition(col, low, high)
            print("\t " + str(col))
            _quick_sort(col, low, anchor_index)
            _quick_sort(col, anchor_index + 1, high)

    _quick_sort(col, 0, len(col) - 1)


print(in_list, len(in_list))


# quick_sort(in_list)
# print(in_list)


# Сортировка слиянием
def merge(left_list, right_list):
    sorted_list = []
    left_list_index = 0
    left_list_len = len(left_list)
    right_list_index = 0
    right_list_len = len(right_list)

    for _ in range(left_list_len + right_list_len):
        if left_list_index < left_list_len and right_list_index < right_list_len:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_len:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_len:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(col):
    if len(col) <= 1:
        return col
    elif len(col) == 2 and col[0] <= col[1]:
        return col

    mid = len(col) // 2
    # print("left: " + str(col[:mid]) + " right: " + str(col[mid:]))
    left_list = merge_sort(col[:mid])
    right_list = merge_sort(col[mid:])
    # print("\tafter merge: " + str(merge(left_list, right_list)))

    return merge(left_list, right_list)

in_list = merge_sort(in_list)
print(in_list)
