
blockchain = []


def get_last_bc_value():
    """ Returns last value of the blockchain """
    return blockchain[-1]



def add_value(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchain value to the blockchain

    Arguments: 
        :transaction_amount: The amount that should be added to the blockchain.
        :last_transaction: The last blockchain transaction (default [1])
    """
    blockchain.append([last_transaction, transaction_amount])
    print(blockchain)


def get_user_input():
    return float(input('Enter transaction amount: '))


tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(last_transaction=get_last_bc_value(), transaction_amount=tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_bc_value())