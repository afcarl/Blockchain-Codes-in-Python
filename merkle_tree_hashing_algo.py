"""
This is implementation of Markle Tree Hashing Algorithm
"""

import hashlib

class MerkelTreeHash(object):
    def __init__(self):
        pass

    def find_merkel_hash(self, file_hashes):
        """
        Here I want to find the merkel tree hash of all the file hashes passes to this function.
        Note I am using recurssiom to solve this problem.
        
        This is simple procedure I follow for finding the hash given a list of hashes .
        First group all the hashes in twos
        Next concatinate the hashes in each group and compute the hash of the group,
        then keep the track of the group hashes 
        Repeat this process until We get a sing;e hash then that becomes the hash we are looking for.
        
        """

        blocks = []

        if not file_hashes:
            raise ValueError('Missing required file hashes for computing merkel tree hash')

        #first Sort the hashes
        for m in sorted(file_hashes):
            blocks.append(m)

        list_len = len(blocks)

        """
        Adjust the blocks of hashes until we have an enen No. of items in the blocks
        This entails appending to the end of the block 
        the last entry
        To do this we use modulus math to determine when we have even no. of items
        """
        while list_len % 2 != 0:
            blocks.extend(blocks[-1:])
            list_len = len(blocks)

        #now we have even no of items in the block, we need to group then in twos
        secondary = []
        for k in [blocks[x:x+2] for x in xrange(0, len(blocks), 2)]:
            # k is a list with only 2 items, which is what we want
            # This is so that we can concatinate them and create a new hash from them
            hasher = hashlib.sha256()
            hasher.update(k[0] + k[1])
            secondary.append(hasher.hexdigest())

        """
        Because this is recurssive method, we need to determine when we only have a single item in the list
        This marks the end of the iterations and we return the last hash as the MARKEL ROOT
        """
        if len(secondary) == 1:
            return secondary[0][0:64]
            # I am only returning the first 64 characters, however you want to return the entire hash, just remove the
            # last section [0:64]

        else:

            #  If the no of items in the lists is more than one, we still need to iteraye through this
            #  so we pass it back to the method. We pass the secondary list since it holds the second iteration results.
            return self.find_merkel_hash(secondary)

if __name__ == "__main__":

    """
    Time to test the class
    we will test by generating 13 random hashes then try their markel tree hash.
    You can always build hashes from say a directly a list of hashes from it to be passes this implementation.
    """
    import uuid
    file_hashes = []

    for i in range(0,13):
        file_hashes.append(str(uuid.uuid4().hex))

    print 'Finding the merkel tree hash of {0} random hashes'.format(len(file_hashes))

    cls = MerkelTreeHash()
    mk = cls.find_merkel_hash(file_hashes)
    print 'The merkel tree hash of the hashes below is: {0}'.format(mk)
    print '...'
    print file_hashes
    #Run the Test

