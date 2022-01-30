from functools import reduce
import random
from sys import argv
from itertools import count
from itertools import cycle
#Задача1
#
# hours, salary, bonus = map(int, argv[1:])
# print(hours * salary + bonus)

#Задача2
# lis = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# new_lis =[]
# for i in range(len(lis) - 1):
#     if lis[i] < lis[i + 1]:
#         new_lis.append(lis[i + 1])
#
# print(new_lis)

#Задача3
# st = [i for i in range(20,241) if i % 20 == 0 or i % 21 == 0 ]
# print(st)

#Задача4
# li = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# new_li =[li[i] for i in range(li[0], (len(li) - 1)) if li.count(i) == 1]
#
# print(new_li)

#Задача5
# li = [i for i in range (100,1001) if i % 2 == 0]
# print(li)
#
# summ_li = reduce(lambda x, y: x * y, li )
# print(summ_li)

#Задача6.1
# start = int(argv[1])
# stop = int(argv[2])
# for i in count(start, 1):
#     print(i)
#     if i == stop:
#         break

#Задача6.2
# li = ["Яблоки", "Бананы"]
# cou = 0
# for i in cycle(li):
#     print(i)
#     cou += 1
#     if cou == 15:
#         break

