from block import Block
from transactions import Transaction
import hashlib

#Robin Danz - Joris Monnet
#He-Arc - Security

class BlockChain:
    def __init__(self):
        self.__chain = []
        self.__currentTransactionsList = []

    def __str__(self):
        return f"\n\t----------------------------------------------------------\n\
        Chain length :{len(self.__chain)}\n\
        Chain : {[str(block) for block in self.__chain]}\n\
        Current Transactions : {[str(transac) for transac in self.__currentTransactionsList]}\n\
        ----------------------------------------------------------\n"

    def getLastBlock(self):
        return self.__chain[-1]

    def getLastTransaction(self):
        return self.__currentTransactionsList[-1]

    def getPendingTransactions(self):
        return self.__currentTransactionsList

    def getChain(self):
        return self.__chain

    def createFirstBlock(self):
        """ Creates the first block and passes it to the chain """
        firstBlock = Block(0, self.__currentTransactionsList, 0, '00')
        self.__chain.append(firstBlock)

    def createTransaction(self, sender, recipient, amount):
        """ Creates a transaction to go into the next block """
        transaction = Transaction(sender, recipient, amount)

        if transaction.validate():
            self.__currentTransactionsList.append(transaction)
            return transaction, True
        return None, False

    @staticmethod
    def validateNonce(lastNonce, lastHash, nonce):
        """ Validates the nonce created in generate function """
        sha = hashlib.sha256(f'{lastNonce}{lastHash}{nonce}'.encode())
        return sha.hexdigest()[:4] == '0000'

    def generate(self, block):
        """ Simple proof of work algorithm: Get a number p such that hash(pp') contains 4 leading zeroes with p the previous proof and p' the new proof """
        lastNonce = block.nonce
        lastHash = block.hash

        nonce = 0
        while not self.validateNonce(lastNonce, lastHash, nonce):
            nonce += 1

        print(f"MINING : Nonce validated : {nonce}")
        return nonce

    def addBlock(self, block):
        """ Creates a new block and passes it to the chain """
        if self.validateBlock(block, self.getLastBlock()):
            self.__chain.append(block)
            self.__currentTransactionsList = [] # Remove transactions from the list
            return True
        return False

    def validateBlock(self, currentBlock, previousBlock):
        """ Validates a block with reference to its previous """        
        
        # Check the block index
        if currentBlock.index != previousBlock.index + 1:
            return False
        if currentBlock.previousHash != previousBlock.hash:
            return False
        if currentBlock.hash != currentBlock.hashBlock():
            return False
        if not self.validateNonce(previousBlock.nonce, previousBlock.hash, currentBlock.nonce):
            return False
        return True

    def validateChain(self, toValidateChain):
        """ Verifies if a given chain is valid """
        # First validate both firsts blocks
        if toValidateChain[0].hashBlock() != self.__chain[0].hashBlock():
            return False

        # Then compare each block with previous 
        for x in range(1, len(toValidateChain)):
            if not self.validateBlock(toValidateChain[x], toValidateChain[x - 1]):
                return False

        return True

    def replaceChain(self, newChain):
        """ Attempts to replace the chain for a new one bigger"""

        if len(newChain) <= len(self.__chain):
            return False

        # Validate the new chain
        if not self.validateChain(newChain):
            return False

        newBlocks = newChain[len(self.__chain):]
        for block in newBlocks:
            self.addBlock(block)

    def mine(self, rewardAddress):
        """ Mines a new block into the chain """
        lastBlock = self.getLastBlock()
        index = lastBlock.index + 1
        previousHash = lastBlock.hash

        nonce = self.generate(lastBlock)

        self.createTransaction( # Reward for the miner
            sender="0",         # The miner receive coins "created", so there is no sender
            recipient=rewardAddress,
            amount=1,
        )

        # Add the block to the new chain
        block = Block(index, self.__currentTransactionsList, nonce, previousHash)

        if self.addBlock(block):
            return block

        return None

