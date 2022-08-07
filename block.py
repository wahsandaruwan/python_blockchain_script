class Block:
    
    # -----Constructors-----
    def __init__(self) -> None:
        """
        This is the constructor which lets the class initialize the object's attributes.
        """        
        # Instance variables
        index : int
        data : str
        proof : int
        prev_hash : str

        # Initialize the genesis block
        genesis_block = self.create_block(index = 1, data = "This is the genesis block", proof = 1, prev_hash = "0")

    # -----Getter and setter functions-----
    def set_index(self, index : int):
        """
        This function assign a new value to the index variable of the new block.

        Parameters:
            index (int): Index of the new block.
        """ 

        self.index = index

    def get_index(self):
        return self.index

    def set_proof(self, proof):
        """
        This function assign a new value to the proof variable of the new block.

        Parameters:
            proof (int): Value used to confirm the transaction and create a new block.
        """

        self.proof = proof

    def get_proof(self):
        return self.proof

    def set_prev_hash(self, prev_hash):
        """
        This function assign a new value to the prev_hash variable of the new block.

        Parameters:
            prev_hash (int): Hash value of the previous block.
        """

        self.prev_hash = prev_hash

    def get_prev_hash(self):
        return self.prev_hash

    # -----Other functions-----
    def mine_block(self, data : str) -> dict:
        """
        This function mines the new block by using proof_of_work, hash_prev_block and create_block functions. And this function acts as the starting point of this script.

        Parameters:
            data (str): Actual data tob stored in the block.

        Returns:
            dict: New block of the blockchain.
        """        
        prev_block = self.get_prev_block()
        prev_proof = prev_block["proof"]
        self.index = len(self.chain) + 1
        self.proof = self.proof_of_work(prev_proof = prev_proof, index = index, data = data)
        self.prev_hash = self.hash_prev_block(block = prev_block)
        block = self.create_block(index = index, data = data, proof = proof, prev_hash = prev_hash)
        self.chain.append(block)

        return block
    
    def create_block(self, index : int, data : str, proof : int, prev_hash : str) -> dict:
        """
        This function creates a new block for the blockchain as a dictionary and return it.

        Parameters:
            index (int) : Index of the new block.
            data (str) : Actual data tob stored in the block.
            proof (int) : Value used to confirm the transaction and create a new block.
            prev_hash(str) : Hash value of the previous block.
        Returns:
            dict: New block of the blockchain.
        """
                
        block = {
            "index" : index,
            "time_stamp" : str(dt.now()),
            "data" : data,
            "proof" : proof,
            "prev_hash" : prev_hash
        }

        return block