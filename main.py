from blockchain import BlockChain
from user import User

if __name__ == '__main__':
    firstChain = BlockChain()
    firstChain.createFirstBlock()
    print(firstChain)
    joris = User("Joris")
    robin = User("Robin")
    firstChain.mine(joris.id)
    firstChain.mine(robin.id)
    firstChain.createTransaction(joris.id,robin.id,5)
    print(firstChain)

    secondChain = BlockChain()
    secondChain.createFirstBlock()
    secondChain.mine(joris.id)
    secondChain.mine(joris.id)
    secondChain.mine(joris.id)

    print(secondChain)
    firstChain.replaceChain(secondChain.getChain())
    print(firstChain)
