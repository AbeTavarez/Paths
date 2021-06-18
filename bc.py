# Initialize blockchain list
blockchain = []


def get_last_bc_value():
    """ Returns last value of the blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchain value to the blockchain

    Arguments: 
        :transaction_amount: The amount that should be added to the blockchain.
        :last_transaction: The last blockchain transaction (default [1])
    """
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float. """
    return float(input('Enter transaction amount: '))


def get_user_choice():
    return input('Your choice: ')


def print_blockchain_blocks():
     # Outputs Blockchain list values
        for block in blockchain:
            print(f'Outputting Block {block}\n')  




# Get the first transaction and add the value to the blockchain
tx_amount = get_transaction_value()
add_value(tx_amount)


while True:
    print("""
    Please choose an option:
    1) Add a new transation value
    2) Output the blockchain blocks
    q) Quit
    """)

    # user input
    user_choice = get_user_choice()

    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_bc_value())
    elif user_choice == '2':
        print_blockchain_blocks()
    elif user_choice == 'q':
        break
    else:
       print('Invalid input!')