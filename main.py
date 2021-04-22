from blockchain import BlockChain

if __name__ == '__main__':
    firstChain = BlockChain()
    firstChain.createFirstBlock()
    print(firstChain)
    firstChain.mine("Joris")
    firstChain.mine("Robin")
    firstChain.createTransaction("Joris","Robin",5)
    print(firstChain)

    secondChain = BlockChain()
    secondChain.createFirstBlock()
    secondChain.mine("second")
    secondChain.mine("second")
    secondChain.mine("second")

    print(secondChain)
    firstChain.replaceChain(secondChain.getChain())
    print(firstChain)
