import hashlib
from time import time

class Block:
    def __init__(self, index, transactions, nonce, previousHash):
        self.index = index
        self.timestamp = time()
        self.transactions = transactions
        self.nonce = nonce
        self.previousHash = previousHash
        self.hash = self.hashBlock()

    def hashBlock(self):
        """ Calculates the hash of the block """
        sha = hashlib.sha256()
        return sha.hexdigest()