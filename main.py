from blockchain import BlockChain
from wallet import wallet

if __name__ == '__main__':
    firstChain = BlockChain()
    firstChain.createFirstBlock()
    print(firstChain)
    firstWallet = wallet.create_wallet()
    secondWallet = wallet.create_wallet()
    firstChain.mine(firstWallet["adress"])
    firstChain.mine(secondWallet["adress"])
    firstChain.createTransaction(firstWallet["adress"],secondWallet["adress"],5)
    print(firstChain)

    secondChain = BlockChain()
    secondChain.createFirstBlock()
    secondChain.mine(firstWallet["adress"])
    secondChain.mine(firstWallet["adress"])
    secondChain.mine(firstWallet["adress"])

    print(secondChain)
    firstChain.replaceChain(secondChain.getChain())
    print(firstChain)
