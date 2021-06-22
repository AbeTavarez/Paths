# Initialize blockchain list
genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}

blockchain = [genesis_block]
open_transations = []
owner = 'Attack-Titan'
participants = {'Attack-Titan'}
# Block for option 3
hacked_block = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{
                    'sender': 'Founding-Titan', 
                    'Recipient': 'Attack-Titan',
                    'amount': 1000000.00
                }]
            }


def hash_block(block):
    """ Hashing...
        Iterade through the last block(dict) 
        And join each value in a str separated with - to create the hashed_block
    """
    return '-'.join([str(block[key]) for key in block] )


def get_balance(participant):
    # In list comprehention we get back the first list of transations from the genesis block
    tx_sender1 = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    # Here we do the same as in the above code but we don't get back the genesis block
    tx_sender = []
    for block in blockchain:
        for tx in  block['transactions']:
            if tx['sender'] == participant:
                tx_sender.append(tx['amount'])

    print('TXSENDER --> ', tx_sender1)
    #
    amount_sent = 0
    for tx in tx_sender1:
        if len(tx) > 0:
            amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
    amount_recieved = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_recieved += tx[0]
    return amount_recieved - amount_sent



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
    participants.add(sender)
    participants.add(recipient)
    

def mine_block():
    # First we take the last block(dict) from blockchain
    last_block = blockchain[-1]
    # print('Last Block ---> ', last_block)
    
    hashed_block = hash_block(last_block)
    print(hashed_block)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': open_transations
    }
    blockchain.append(block)
    return True



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
            print('=' * 40)

def verify_chain():
    """ Verify the current blockchain and return True if it's valid"""
    for index, block in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index -1]):
            return False
    return True


#================================================================================================#
waiting_for_input = True

while waiting_for_input:
    print("""
    Please choose an option:
    1) Add a new transation transaction.
    2) Mine a new block.
    3) Output the blockchain's blocks.
    4) Output participants.
    h) Hack Blockchain.
    q) Quit.
    """)

    # user input
    user_choice = get_user_choice()

    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount) # sender arg is skipped here, bc is set as default on function definition
        # print('Open Transactions ----> ', open_transations)
    elif user_choice == '2':
        if mine_block():
            open_transations = []
    elif user_choice == '3':
        print_blockchain_blocks()
    elif user_choice == '4':
        print(participants)
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = hacked_block
    elif user_choice == 'q':
        waiting_for_input = False
    else:
       print('Invalid input!')
    if not verify_chain():
        print_blockchain_blocks()
        print('Invalid Blockhain')
        break
    print(get_balance('Attack-Titan'))
else:
    print('User left!')
print('Done')