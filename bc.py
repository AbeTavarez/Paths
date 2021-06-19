# Initialize blockchain list
blockchain = []


def get_last_bc_value():
    """ Returns last value of the blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction):
    """ Append a new value as well as the last blockchain value to the blockchain

    Arguments: 
        :transaction_amount: The amount that should be added to the blockchain.
        :last_transaction: The last blockchain transaction (default [1])
    """
    if last_transaction == None:
        last_transaction = [1]
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

def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        print(block)
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid

#================================================================================================
while True:
    print("""
    Please choose an option:
    1) Add a new transation transaction
    2) Output the blockchain's blocks
    h) Hack Blockchain
    q) Quit
    """)

    # user input
    user_choice = get_user_choice()

    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_bc_value())
    elif user_choice == '2':
        print_blockchain_blocks()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [100000]
    elif user_choice == 'q':
        break
    else:
       print('Invalid input!')
    if not verify_chain():
        print('Invalid Blochain')
        break