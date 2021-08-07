# LCS_Solutions
Trying out different ways to solve the LCS problem.

In the file LCS_DP_Solutions.py I tried some initial DP solutions to solve the LCS problem. I wrote 4 functions.

  1.) The first one was completely based off the Wikipedia DP solution for this problem, found at: https://en.wikipedia.org/wiki/Longest_common_substring_problem#Dynamic_programming I just added one line of code to record the first time the LCS appears in the first string passed. It outputs the size of the LCS and that index.
  2.) This one is a modified version of the first one, just to store all occurences of the LCS as the indices they start at in each string. This is implemented as a list inside a list, because I wanted each list to hold LCS substrings which were equal i.e. it is possible to have two or more LCSs which have the same length but are different.
  3.) Since L[i][j] (the element in the DP array) is dependent on just L[i - 1][j - 1] we can get away with storing just two lists instead of a larger DP array. The size of these two lists is min(len(X), len(Y)) where X, Y are the two strings being compared.
  4.) Because of the above fact, it is possible to make this even more memory efficient by just traversing chains of L[i][j], L[i + 1][j + 1], ... L[i + n][j + n] for all such possible chains, storing just the value before.

I then tried to see their runtime and memory usage by using the time and tracemalloc packages, for 1000 tests each where two strings are taken and randomly filled with uppercase letters, of random size varying from 1 to 1000 charecters. I found all three to take approximately 0.05 seconds, the third one a little slower usually and the fourth a little faster (by not more than 0.03 secs). In memory usage, however, the first took the order of about 10^6 bytes, the third took 10^4 bytes and the third took about 10^3 bytes. Here is a sample output:

The Basic LCS DP Solution.

The runtime for 1000 iterations was 0.03440003395080567 seconds on average.
The peak memory usage for 1000 iterations was 2436576.8  bytes on average.

The LCS DP Solution with only 2 lists.

The runtime for 1000 iterations was 0.06720516681671143 seconds on average.
The peak memory usage for 1000 iterations was 6667.6  bytes on average.

The LCS DP Solution with only one extra storage container.

The runtime for 1000 iterations was 0.027146029472351074 seconds on average.
The peak memory usage for 1000 iterations was 230.4  bytes on average.

Next, I tried to use two libraries, one from here: https://github.com/cceh/suffix-tree and the other from here: https://github.com/ptrus/suffix-trees
Both use suffix trees to find LCS and have their own functions for computing it. Oddly, I found no order of magnitude difference in their speed in comparison to the last of the previous DP solutions, in scope of the present problem. The time and speed measuremnts were done the same way as in the last file. I observed the first library function to be slightly slower and the last one to be slightly faster than the DP, with much larger memory usage (~10^5 Bytes for the first and ~10^6 for the second). Here is a sample output:

The LCS DP Solution with only one extra storage container.

The runtime for 1000 iterations was 0.04106021404266357 seconds on average.
The peak memory usage for 1000 iterations was 204.0  bytes on average.

The first LCS Suffix Tree Library function.

The runtime for 1000 iterations was 0.06378918170928954 seconds on average.
The peak memory usage for 1000 iterations was 598885.8  bytes on average.

The second LCS Suffix Tree Library function

The runtime for 1000 iterations was 0.011165523529052734 seconds on average.
The peak memory usage for 1000 iterations was 6050373.42  bytes on average.
