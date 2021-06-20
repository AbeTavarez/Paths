# Initialize blockchain list
blockchain = []
open_transations = []
owner = 'attack-titan'


def get_last_bc_value():
    """ Returns last value of the blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new transaction value as well as the last blockchain value to the blockchain

    Arguments: 
        :sender: The sender of the transaction.
        :recipient: The recipient of the transaction.
        :amount: The amount sent with the transaction (default amount 1.0)
    """
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    open_transations.append(transaction)
    


def mine_block():
    pass

def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float. """
    recipient = input('Enter the recipient of the transaction: ')
    amount = float(input('Enter transaction amount: '))
    return (recipient, amount)


def get_user_choice():
    return input('Your choice: ')


def print_blockchain_blocks():
     # Outputs Blockchain list values
        for block in blockchain:
            print(f'Outputting Block {block}\n')
        else:
            print('='*20)

def verify_chain():
    #block_index = 0 # keeps track of the block we're currently on
    is_valid = True # flag
    for block_index in range(len(blockchain)):
        print('Verifying block....', blockchain[block_index])
        print(f'Blockchain -> {blockchain}')
        print(f'Blockchain Length: {len(blockchain)}')
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            # Compares the first block 
            print(f'Comparing Blocks {blockchain[block_index][0]} ||| {blockchain[block_index -1]}')
            is_valid = True
        else:
            is_valid = False
            break
    return is_valid

#================================================================================================#
waiting_for_input = True

while waiting_for_input:
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
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount) # sender arg is skipped here, bc is set as default on function definition
        print('Open Transactions ----> ', open_transations)
    elif user_choice == '2':
        print_blockchain_blocks()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [100000]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
       print('Invalid input!')
    if not verify_chain():
        print_blockchain_blocks()
        print('Invalid Blochain')
        break
else:
    print('User left!')
print('Done')