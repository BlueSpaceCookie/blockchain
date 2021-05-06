from blockchain import BlockChain
from wallet import wallet

#Robin Danz - Joris Monnet
#He-Arc - Security

if __name__ == '__main__':
    firstChain = BlockChain()
    firstChain.createFirstBlock()
    print(firstChain)
    firstWallet = wallet.create_wallet() 
    secondWallet = wallet.create_wallet()
    print("Second Wallet values = "+ str(secondWallet))

    firstChain.mine(firstWallet["address"])
    firstChain.mine(secondWallet["address"])
    firstChain.createTransaction(firstWallet["address"],secondWallet["address"],5)
    print(firstChain)

    secondChain = BlockChain()
    secondChain.createFirstBlock()
    secondChain.mine(firstWallet["address"])
    secondChain.mine(firstWallet["address"])
    secondChain.mine(firstWallet["address"])

    print(secondChain)
    firstChain.replaceChain(secondChain.getChain())
    print(firstChain)


