import time
import string
import random
import tracemalloc
import collections
import itertools

from random import randint
from suffix_tree import *
from suffix_trees import STree

def LCS_DP_Mem_Op_Improved(X, Y):
    
    m = len(X)
    n = len(Y)
    
    LCS_length = 0
    LCS_example_start_index_X = []
    
    Substring_Length = 0
    
    for tj in range(n):
        i = 0
        j = tj
        while (j < n and i < m):
            if (X[i] == Y[j]):
                Substring_Length += 1
            else:
                Substring_Length = 0
            if (Substring_Length > LCS_length):
                LCS_length = Substring_Length
                LCS_example_start_index_X = i - LCS_length + 1
            i = i + 1
            j = j + 1
                
    if (m > 1):
        for ti in range(1,m):
            i = ti
            j = 0
            while (j < n and i < m):
                if (X[i] == Y[j]):
                    Substring_Length += 1
                else:
                    Substring_Length = 0
                if (Substring_Length > LCS_length):
                    LCS_length = Substring_Length
                    LCS_example_start_index_X = i - LCS_length + 1
                i = i + 1
                j = j + 1
    
    return LCS_length, LCS_example_start_index_X
    
# Testing for random strings of length varying between 1 and 1000 charecters; If one wants to see for random strings of 1000 charecters exactly, replace all occurences of randint(1, 1000) with 1000 using ctrl + H.

print()
print("The LCS DP Solution with only one extra storage container.")
print()

Program_Iterations = 1000
Average_Runtime = 0
Average_Peak_Memory_Usage = 0
for i in range(Program_Iterations):
    X = ''.join(random.choices(string.ascii_uppercase, k = randint(1, 1000)))
    Y = ''.join(random.choices(string.ascii_uppercase, k = randint(1, 1000)))
    Start_Time = time.time()
    LL, LSX = LCS_DP_Mem_Op_Improved(X, Y)
    Average_Runtime = Average_Runtime + time.time() - Start_Time
Average_Runtime = Average_Runtime / Program_Iterations
print("The runtime for", Program_Iterations, "iterations was", Average_Runtime, "seconds on average.")
for i in range(Program_Iterations):
    X = ''.join(random.choices(string.ascii_uppercase, k = randint(1, 1000)))
    Y = ''.join(random.choices(string.ascii_uppercase, k = randint(1, 1000)))
    tracemalloc.start()
    LL, LSX = LCS_DP_Mem_Op_Improved(X, Y)
    Current_Memory_Usage, Peak_Memory_Usage = tracemalloc.get_traced_memory()
    Average_Peak_Memory_Usage = Average_Peak_Memory_Usage + Peak_Memory_Usage
    tracemalloc.stop()
Average_Peak_Memory_Usage = Average_Peak_Memory_Usage / Program_Iterations
print("The peak memory usage for", Program_Iterations, "iterations was", Average_Peak_Memory_Usage, " bytes on average.")

print()
print("The first LCS Suffix Tree Library function.")
print()

Program_Iterations = 1000
Average_Runtime = 0
Average_Peak_Memory_Usage = 0
for i in range(Program_Iterations):
    X = ''.join(random.choices(string.ascii_uppercase, k = randint(1, 1000)))
    Y = ''.join(random.choices(string.ascii_uppercase, k = randint(1, 1000)))
    Start_Time = time.time()
    Suffix_Tree = Tree({'X': X, 'Y': Y})
    Ans = Suffix_Tree_1.common_substrings()
    Average_Runtime = Average_Runtime + time.time() - Start_Time
Average_Runtime = Average_Runtime / Program_Iterations
print("The runtime for", Program_Iterations, "iterations was", Average_Runtime, "seconds on average.")
for i in range(Program_Iterations):
    X = ''.join(random.choices(string.ascii_uppercase, k = randint(1, 1000)))
    Y = ''.join(random.choices(string.ascii_uppercase, k = randint(1, 1000)))
    tracemalloc.start()
    Suffix_Tree = Tree({'X': X, 'Y': Y})
    Ans = Suffix_Tree_1.common_substrings()
    Current_Memory_Usage, Peak_Memory_Usage = tracemalloc.get_traced_memory()
    Average_Peak_Memory_Usage = Average_Peak_Memory_Usage + Peak_Memory_Usage
    tracemalloc.stop()
Average_Peak_Memory_Usage = Average_Peak_Memory_Usage / Program_Iterations
print("The peak memory usage for", Program_Iterations, "iterations was", Average_Peak_Memory_Usage, " bytes on average.")

print()
print("The second LCS Suffix Tree Library function")
print()

Program_Iterations = 1000
Average_Runtime = 0
Average_Peak_Memory_Usage = 0
for i in range(Program_Iterations):
    X = ''.join(random.choices(string.ascii_uppercase, k = randint(1, 1000)))
    Y = ''.join(random.choices(string.ascii_uppercase, k = randint(1, 1000)))
    Start_Time = time.time()
    Suffix_Tree = STree.STree([X, Y])
    Ans = Suffix_Tree.lcs()
    Average_Runtime = Average_Runtime + time.time() - Start_Time
Average_Runtime = Average_Runtime / Program_Iterations
print("The runtime for", Program_Iterations, "iterations was", Average_Runtime, "seconds on average.")
for i in range(Program_Iterations):
    X = ''.join(random.choices(string.ascii_uppercase, k = randint(1, 1000)))
    Y = ''.join(random.choices(string.ascii_uppercase, k = randint(1, 1000)))
    tracemalloc.start()
    Suffix_Tree = STree.STree([X, Y])
    Ans = Suffix_Tree.lcs()
    Current_Memory_Usage, Peak_Memory_Usage = tracemalloc.get_traced_memory()
    Average_Peak_Memory_Usage = Average_Peak_Memory_Usage + Peak_Memory_Usage
    tracemalloc.stop()
Average_Peak_Memory_Usage = Average_Peak_Memory_Usage / Program_Iterations
print("The peak memory usage for", Program_Iterations, "iterations was", Average_Peak_Memory_Usage, " bytes on average.")

print()