# Blockchain-Codes-in-Python
Most of the implementable Python codes for Blockchain related Algorithms and Data Structures like Hash Functions and Hash Tables.

*  **Merkle Tree Hashing Algorithm:** 
I want to find the merkel tree hash of all the file hashes passes to this function. I am using *recurssion* to solve this problem.
 Procedure is as follows: 
    + Group all the hashes in twos
    + Concatinate the hashes in each group and compute the hash of the group
    + keep the track of the group hashes 
    + Repeat this process until we get a single hash then that becomes the hash we are looking for.
