import time
import string
import random
import tracemalloc

from random import randint 

def LCS_DP(X, Y):
    
    # Initializing the length of the strings.
    m = len(X)
    n = len(Y)
    
    # Initializing the output.
    LCS_length = 0
    LCS_example_start_index_X = 0
    
    # Initializing the DP array. It has n columns and m rows.
    L = [[0 for i in range(n)] for i in range(m)]
    
    # Traverse through the DP array.
    for i in range(m):
        for j in range(n):
        
            # If the below occurs then it means that we have a single letter matching.
            if (X[i] == Y[j]):
            
                # If the first charecter of either string matches with any charecter in the opposing string, then the substring dealt with has size 1.
                if (i == 0 or j == 0):
                    L[i][j] = 1
                    
                # Here, L[i][j] stores the number of matching charecters in X and Y such that X[i - L[i][j] + 1: i + 1] == Y[j - L[i][j] + 1: i + 1]. In effect if we find that X[i + 1] = Y[j + 1], the substring is larger by 1, So L[i + 1][j + 1] would be L[i][j] + 1, which is in effect what this line does. 
                else:
                    L[i][j] = L[i - 1][j - 1] + 1
                    
                # If we encounter a substring greater than we already have, we update the LCS size, and store the index at which we found it.
                if (L[i][j] > LCS_length):
                    LCS_length = L[i][j]
                    LCS_example_start_index_X = i - LCS_length + 1
                    
            # If a letter does not match, in effect we are dealing with two strings that do not match, and so the substring size which matches is 0
            else:
                L[i][j] = 0
     
    # Return the output as a Tuple.
    return LCS_length, LCS_example_start_index_X

def LCS_DP_Elaborate(X, Y):
    
    m = len(X)
    n = len(Y)
    
    # Here the goal is to store all possible matches of substring, while preserving the sequences of the substring matched; that is, if multiple substrings of LCS size exist such that they are not equal, store their indices in such a way as all can be easily found. I think it would be useful to see all LCS matches in all places of different types in say genetic sequences, at a significant memory cost.
    LCS_length = 0
    LCS_start_indices_X = []
    LCS_start_indices_Y = []
    
    L = [[0 for i in range(n)] for i in range(m)]
    
    for i in range(m):
        for j in range(n):
            if (X[i] == Y[j]):
                if (i == 0 or j == 0):
                    L[i][j] = 1
                else:
                    L[i][j] = L[i - 1][j - 1] + 1
                
                # If LCS size is larger than previously known, clear all data on previously presumed size.
                if (L[i][j] > LCS_length):
                    LCS_length = L[i][j]
                    LCS_start_indices_X.clear()
                    LCS_start_indices_Y.clear()
                    LCS_start_indices_X.append([i - LCS_length + 1])
                    LCS_start_indices_Y.append([j - LCS_length + 1])
                
                # This bit identifies the sequence of the substring which is LCS-sized and puts it in a list in list format.
                elif (L[i][j] == LCS_length):
                    inlist = False
                    for k in range(len(LCS_start_indices_X)):
                        if (X[LCS_start_indices_X[k][0]:LCS_start_indices_X[k][0] + LCS_length] == X[i - LCS_length + 1: i + 1]):
                            if (LCS_start_indices_X[k][len(LCS_start_indices_X[k]) - 1] == i - LCS_length + 1):
                                if (LCS_start_indices_Y[k][len(LCS_start_indices_Y[k]) - 1] != j - LCS_length + 1):
                                    LCS_start_indices_Y[k].append(j - LCS_length + 1)
                            else:
                                LCS_start_indices_X[k].append(i - LCS_length + 1)
                            inlist = True
                            break
                    if (not inlist):
                        LCS_start_indices_X.append([i - LCS_length + 1])
                        LCS_start_indices_Y.append([j - LCS_length + 1])
            else:
                L[i][j] = 0
                
    return LCS_length, LCS_start_indices_X, LCS_start_indices_Y

def LCS_DP_Mem_Op(X, Y):
    
    m = len(X)
    n = len(Y)
    
    LCS_length = 0
    LCS_example_start_index_X = 0
    
    # The idea is that to know any L[i][j] we only need L[i - 1][j - 1], so we can coveniently forget anything before that. In effect we need 2 lists in a list only; one to store the current row of L, and one to store the previous row of L. The size of these list should be min(m,n) as that would optimize the memory used further.
    if (n <= m):
    
        L = [[0 for i in range(n)] for i in range(2)]
        
        for i in range(m):
            for j in range(n):
                if (X[i] == Y[j]):
                    if (i == 0 or j == 0):
                        L[1][j] = 1
                    else:
                        L[1][j] = L[0][j - 1] + 1
                    if (L[1][j] > LCS_length):
                        LCS_length = L[1][j]
                        LCS_example_start_index_X = i - LCS_length + 1
                else:
                    L[1][j] = 0
            L[0] = L[1]
            L[1] = [0 for k in range(n)]
    
    else:
    
        L = [[0 for i in range(m)] for i in range(2)]
        
        for i in range(n):
            for j in range(m):
                if (X[j] == Y[i]):
                    if (i == 0 or j == 0):
                        L[1][j] = 1
                    else:
                        L[1][j] = L[0][j - 1] + 1
                    if (L[1][j] > LCS_length):
                        LCS_length = L[1][j]
                        LCS_example_start_index_X = j - LCS_length + 1
                else:
                    L[1][j] = 0
            L[0] = L[1]
            L[1] = [0 for k in range(m)]
    

    return LCS_length, LCS_example_start_index_X
    
def LCS_DP_Mem_Op_Improved(X, Y):
    
    m = len(X)
    n = len(Y)
    
    LCS_length = 0
    LCS_example_start_index_X = []
    
    # This is the best idea to conserve memory; since T[i][j] only depends on T[i - 1][j - 1] in the DP array, we can cut at 45 degrees across the array to evaluate all T[i][j], T[i + 1][j + 1], ...T[i + n][j + n] and so on for all such possible "strings" of T[i][j]. You'll end up needing to store only one extra variable, the substring length being considered at the point before. Also seems really easy to parallelize.
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
print("The Basic LCS DP Solution.")
print()

Program_Iterations = 1000
Average_Runtime = 0
Average_Peak_Memory_Usage = 0
for i in range(Program_Iterations):
    X = ''.join(random.choices(string.ascii_uppercase, k = randint(1, 1000)))
    Y = ''.join(random.choices(string.ascii_uppercase, k = randint(1, 1000)))
    Start_Time = time.time()
    LL, LSX = LCS_DP(X, Y)
    Average_Runtime = Average_Runtime + time.time() - Start_Time
Average_Runtime = Average_Runtime / Program_Iterations
print("The runtime for", Program_Iterations, "iterations was", Average_Runtime, "seconds on average.")
for i in range(Program_Iterations):
    X = ''.join(random.choices(string.ascii_uppercase, k = randint(1, 1000)))
    Y = ''.join(random.choices(string.ascii_uppercase, k = randint(1, 1000)))
    tracemalloc.start()
    LL, LSX = LCS_DP(X, Y)
    Current_Memory_Usage, Peak_Memory_Usage = tracemalloc.get_traced_memory()
    Average_Peak_Memory_Usage = Average_Peak_Memory_Usage + Peak_Memory_Usage
    tracemalloc.stop()
Average_Peak_Memory_Usage = Average_Peak_Memory_Usage / Program_Iterations
print("The peak memory usage for", Program_Iterations, "iterations was", Average_Peak_Memory_Usage, " bytes on average.")

print()
print("The LCS DP Solution with only 2 lists.")
print()

Program_Iterations = 1000
Average_Runtime = 0
Average_Peak_Memory_Usage = 0
for i in range(Program_Iterations):
    X = ''.join(random.choices(string.ascii_uppercase, k = randint(1, 1000)))
    Y = ''.join(random.choices(string.ascii_uppercase, k = randint(1, 1000)))
    Start_Time = time.time()
    LL, LSX = LCS_DP_Mem_Op(X, Y)
    Average_Runtime = Average_Runtime + time.time() - Start_Time
Average_Runtime = Average_Runtime / Program_Iterations
print("The runtime for", Program_Iterations, "iterations was", Average_Runtime, "seconds on average.")
for i in range(Program_Iterations):
    X = ''.join(random.choices(string.ascii_uppercase, k = randint(1, 1000)))
    Y = ''.join(random.choices(string.ascii_uppercase, k = randint(1, 1000)))
    tracemalloc.start()
    LL, LSX = LCS_DP_Mem_Op(X, Y)
    Current_Memory_Usage, Peak_Memory_Usage = tracemalloc.get_traced_memory()
    Average_Peak_Memory_Usage = Average_Peak_Memory_Usage + Peak_Memory_Usage
    tracemalloc.stop()
Average_Peak_Memory_Usage = Average_Peak_Memory_Usage / Program_Iterations
print("The peak memory usage for", Program_Iterations, "iterations was", Average_Peak_Memory_Usage, " bytes on average.")

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