import hashlib
import datetime
image_path1 = "param.jpg"
with open(image_path1,"rb") as image_file:
   image_bytes1=image_file.read()
image_path2 = "Turing.png"
with open(image_path2,"rb") as image_file:
   image_bytes2=image_file.read()
class PhotoBlock:
    def __init__(self, previous_hash, photo_data, timestamp=None):
        self.previous_hash = previous_hash
        self.photo_data = photo_data
        self.timestamp = timestamp or datetime.datetime.now()
        self.hash = self.calculate_hash()
    def calculate_hash(self):
        data = f"{self.previous_hash}{self.photo_data}{self.timestamp}".encode('utf-8')
        return hashlib.sha256(data).hexdigest()
class PhotoBlockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    def create_genesis_block(self):
        return PhotoBlock(previous_hash="0", photo_data="Genesis Block")
    def add_block(self, photo_data):
        previous_block = self.chain[-1]
        new_block = PhotoBlock(previous_block.hash, photo_data)
        self.chain.append(new_block)
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True
if __name__ == "__main__":
    blockchain = PhotoBlockchain()
    blockchain.add_block("image_bytes1")
    blockchain.add_block("image_bytes2")
    print(f"Is the blockchain valid? {blockchain.is_chain_valid()}")
    for block in blockchain.chain:
        print(f"Hash: {block.hash}")
        print(f"Photo Data: {block.photo_data}")
        print(f"Timestamp: {block.timestamp}")
        print("---")