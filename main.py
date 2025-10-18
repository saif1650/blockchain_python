import time
import hashlib
class Block :
    def __init__(self, index, data, previous_hash, miner):
        self.index = index
        self.timestamp = time.ctime()
        self.data = data
        self.previous_hash = previous_hash
        self.miner = miner
        self.hash = self.calculate_hash()
        

    def calculate_hash(self):
        content = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.miner}"
        return hashlib.sha256(content.encode()).hexdigest()

    def show_block(self):
        print(f"Block #{self.index}")
        print(f"Timestamp :{self.timestamp}")
        print(f"Data : {self.data}")
        print(f"Hash : {self.hash}")
        print(f"Previous_Hash : {self.previous_hash}")
        print(f"Miner : {self.miner}")


genesis_block = Block(1, "First Transaction Data","0", "Saif")
genesis_block.show_block()

block2 = Block(2, "Second Transaction Data", genesis_block.hash,"Ali")
block2.show_block()
