from blockchain import BlockChain

if __name__ == '__main__':
    firstChain = BlockChain()
    firstChain.createFirstBlock()
    print(firstChain)
    firstChain.mine("Joris")
    firstChain.mine("Robin")
    print(firstChain)
