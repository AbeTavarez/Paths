
# Coordinate is our Genesis Block.
# All Paths connects are connected to the Coordinate. 

class Coordinate():
    def __init__(self, previous_hash, index, transactions) -> None:
        previous_hash = ''
        index = 0
        transactions = list()