from array import array
from collections import deque, OrderedDict, ChainMap


# Структуры данных - специальные типы данных для хранения набора значений
# а) Линейные структуры - представляются в виде набора значений идущих друг за другом
# Массив - значения лежат в одной части памяти рядом друг с другом
# Статические массивы, динамические массивы
def array_example():
    # list в python - динамический массив
    print("python list")
    l = [1, 5.9, "123"]
    # чтение элемента по индексу, изменение элемента по индексу - O(1)
    print(l[1])
    l[1] = "qwe"
    print(l[1])
    # добавление, удаление элементов - O(n)
    # это действие может быть быстрым
    l.append(123)
    l.pop(len(l) - 1)
    # эти действия будет медленнее, скорость зависит от длины
    l.insert(1, 456)
    l.pop(1)

    # tuple - list, но неизменяем
    l = (1, 1.5, "asd")

    # нет изменения элементов, добавления или удаления элементов
    # l[1] = 2
    # l.add()
    # l.remove()

    # array.array - динамический массив, у которого можно указать тип данных
    # основано на C коде массивов
    print("array.array")
    arr = array("d", [1.0, 2.0, 300.1, -500.00001])
    print(arr[2])
    arr[2] = 0.0
    print(arr)
    arr.append(42.0)
    print(arr)

    # стандартный str в python - неизменяемый массив unicode символов
    print("str as array")
    str_ex = "\t123asd"
    print(str_ex[2])
    # невозможно изменить содержимое str
    # str_ex[2] = "f"
    # Когда происходит модификация строки - происходит создание новой строки
    print(id(str_ex))
    str_ex = str_ex.strip()
    print(id(str_ex))

    # стандартный bytes в python - неизменяемый массив байтов
    bytes_ex = bytes((0, 1, 5, 4, 96))
    print(bytes_ex)
    print(bytes_ex[4])
    # bytes_ex[4] = 100

    # стандартный bytearray в python - изменяемый массив байтов
    bytes_ex = bytearray((0, 1, 5, 4, 96))
    print(bytes_ex[4])
    bytes_ex[4] = 100
    print(bytes_ex[4])
# array_example()

def list_info():
    # Список - элементы хранятся в единичных "ячейках" в памяти
    # при этом ячейки имеют информацию про местонахождение соседних
    # Связанный список, двунаправленный список, цикличность
    pass

# Множество - набор уникальных значений
def sets():
    # стандартный set в python - изменяемое множество
    print("set")
    nums_set = {1, 3, 2, 4, 5}
    print(nums_set)
    nums_set2 = {4, 5, 6, 7}
    # Операция in - O(1)
    print(7 in nums_set)
    print(1 in nums_set)
    # Операции intersection, union, difference - примерно O(n)
    print(nums_set.intersection(nums_set2))
    print(nums_set2.intersection(nums_set))
    print(nums_set.union(nums_set2))
    print(nums_set.difference(nums_set2))
    print(nums_set2.difference(nums_set))
    # Операции добавления, удаления - O(1)
    nums_set.add(0)
    print(nums_set)
    nums_set.remove(0)
    print(nums_set)

    str_set = {"Andrew", "Victor", "Elena", 1}
    print(str_set)
    print("Victor" in str_set)
    print(1 in str_set)

    # стандартный frozenset в python - неизменяемое множество
    print("frozen set")
    frozenset_ex = frozenset({"Andrew", "Victor", "Elena"})
    print("Victor" in frozenset_ex)
# sets()

# Стек - линейная структура, работающая по принципу LIFO (Last In - First Out)
def stack_example():
    print("list as stack")
    stack_ex = []
    # Добавление элемента O(1)*
    stack_ex.append(1)
    stack_ex.append(2)
    stack_ex.append(3)
    print(stack_ex)
    # Удаление элемента O(1)
    stack_ex.pop()
    print(stack_ex)

    # deque - двусторонняя очередь, может работать как стек
    # deque основана на двунаправленном списке
    # поэтому добавление, удаление в deque - O(1)
    print("collections.deque as stack")
    deque_stack = deque()
    deque_stack.append(1)
    deque_stack.append(2)
    deque_stack.append(3)
    print(deque_stack)
    deque_stack.pop()
    print(deque_stack)
# stack_example()

# Очередь - линейная структура, работающая по принципу FIFO (First In - First Out)
# двунаправленная очередь
def queue_example():
    print("list as queue")
    queue_ex = []
    # Добавление элемента - O(1)
    queue_ex.append(1)
    queue_ex.append(2)
    queue_ex.append(3)
    print(queue_ex)
    # Удаление элемента - O(n)
    queue_ex.pop(0)
    print(queue_ex)

    print("collections.deque as queue")
    # добавление и удаление из deque как очереди - O(1)
    deque_queue = deque()
    deque_queue.append(1)
    deque_queue.append(2)
    deque_queue.append(3)
    print(deque_queue)
    deque_queue.popleft()
    print(deque_queue)
# queue_example()


# б) Нелинейные структуры - не представляются в виде набора значений идущих друг за другом
# Словарь (dict, map, hashtable) - хранение информации в виде пар "Ключ: Значение"
def dict_example():
    # стандартный dict в python - изменяемый словарь без определенного порядка
    dict_ex = {"one": 1, "three": 3, "two": 2}
    print(dict_ex)
    print(dict_ex["one"])
    dict_ex["one"] = 1.0
    print(dict_ex["one"])

    # collections.OrderedDict - изменяемый словарь с порядком добавления пар
    dict_ex = OrderedDict({"one": 1, "three": 3, "two": 2})
    print(dict_ex)
    dict_ex["five"] = 5
    print(dict_ex)

    # collections.ChainMap - поиск сразу по нескольким словарям
    dict1 = {"one": 1, "three": 3}
    dict2 = {"two": 2, "four": 4}
    chain = ChainMap(dict1, dict2)
    print(chain["one"])
    print(chain["five"])
# dict_example()


# Граф - структура данных, состоящая из узлов и связей между ними (ребра)
# Дерево - граф без циклов
# Бинарное дерево - деревья, узлы которого могут иметь максимум двух потомков (левый и правый)
class Node:
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right

    def __str__(self):
        return self.info


# Обход в ширину
def horizontal(root):
    queue = deque()
    queue.append(root)
    while len(queue) != 0:
        node = queue.popleft()
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
        print(node.info, [str(x) for x in list(queue)])


# Три обхода в глубину
# Прямой обход (preorder, nlr)
def preorder(root):
    if root is None:
        return
    print(root.info)
    preorder(root.left)
    preorder(root.right)


# Центрированный обход (inorder, lnr)
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.info)
    inorder(root.right)


# Обратный обход (postorder, lrn)
def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.info)


def init_tree():
    f = Node("F")
    g = Node("G")
    e = Node("E")
    d = Node("D", f, g)
    c = Node("C", e)
    b = Node("B", right=d)
    a = Node("A", b, c)
    return a


def binary_trees():
    root = init_tree()
    print("Horizontal search")
    horizontal(root)

    print("Preorder search")
    preorder(root)

    print("Inorder search")
    inorder(root)

    print("Postorder search")
    postorder(root)


binary_trees()

# input() - считать строчку у пользователя
# int() - превратить что-либо в целое число
# split() - "разрезать" строку на список по определенной строчке
# Задание 1
# Принять от пользователя набор чисел
# Сказать ему все уникальные числа из его набора
# In: 1,2,3,4,4,4,4,4,4,5,5
# Out: 1,2,3,4,5

# Задание 2
# Принять от пользователя набор чисел
# Вывести в ответ какие числа в этом наборе встречались
# и сколько раз они встречались
# In: 1,2,3,4,4,4,4,4,4,5,5
# Out: 1=1, 2=1, 3=1, 4=5, 5=2

# Задание 3
# Принять от пользователя строчку
# Вывести является ли она палиндромом
# (палиндром - строчка которая читается одинаково слева-направо и наоборот)
# In: hello
# Out: False
# In: anna
# Out: True
