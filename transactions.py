import time

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.timestamp = time.time()
        self.amount = amount

    def validate(self):
        """  return if a transaction is valid """
        if self.amount < 0:         # Prevent stealing by creating negative transactions
            return False
        return True