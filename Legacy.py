blockchain = [] # Test Only Dummy

# Verify blockchain
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