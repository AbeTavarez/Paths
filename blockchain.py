
class blockchain:
    bc_list = []

    def add_value(self, value):
        self.bc_list.append(value)

    def get_values(self):
        print(self.bc_list)



first_blockchain = blockchain()

first_blockchain.add_value(3)
first_blockchain.get_values()


