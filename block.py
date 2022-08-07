# Inbuild module imports
from datetime import datetime as dt

# Custom module imports
from blockchain import Blockchain
import helpers as hp
class Block:

    # -----Class variables-----
    # Instance of blockchain
    bc = Blockchain()
    
    
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
        self.bc.append_new_block(genesis_block)

        # Print genesis block
        print(f"{self.bc.get_blockchain()[0]} \n")

        
    # -----Getter and setter functions-----
    def set_index(self, index : int):
        """
        This function assign a new value to the index variable of the new block.

        Parameters:
            index (int): Index of the new block.
        """ 

        self.index = index

        
    def get_index(self):
        """
        This function retrieves the index variable of the new block.

        Returns:
            int: Index of the new block.
        """  

        return self.index
 
    
    def set_proof(self, proof):
        """
        This function assign a new value to the proof variable of the new block.

        Parameters:
            proof (int): Value used to confirm the transaction and create a new block.
        """

        self.proof = proof

    
    def get_proof(self):
        """
        This function retrieves the proof variable of the new block.

        Returns:
            int: Proof of the new block.
        """  

        return self.proof

    
    def set_prev_hash(self, prev_hash):
        """
        This function assign a new value to the prev_hash variable of the new block.

        Parameters:
            prev_hash (int): Hash value of the previous block.
        """

        self.prev_hash = prev_hash

    
    def get_prev_hash(self):
        """
        This function retrieves the prev_hash variable of the new block.

        Returns:
            int: Previous hash of the new block.
        """  

        return self.prev_hash

    
    # -----Other functions-----
    def mine_block(self, data : str) -> dict:
        """
        This function mines the new block by using proof_of_work, hash_prev_block and create_block functions. And this function acts as the starting point of this script.

        Parameters:
            data (str): Actual data tob stored in the block.

        Returns:
            dict: New block for the blockchain.
        """        

        # Prepare a new block and insert it to the blockchain
        prev_block = self.bc.get_prev_block()
        prev_proof = prev_block["proof"]
        self.index = len(self.bc.get_blockchain()) + 1
        self.proof = hp.proof_of_work(prev_proof = prev_proof, index = self.index, data = data)
        self.prev_hash = hp.hash_prev_block(block = prev_block)
        block = self.create_block(index = self.index, data = data, proof = self.proof, prev_hash = self.prev_hash)
        self.bc.append_new_block(block)

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
            dict: New block for the blockchain.
        """

        # Strcuture of the block        # 
        block = {
            "index" : index,
            "time_stamp" : str(dt.now()),
            "data" : data,
            "proof" : proof,
            "prev_hash" : prev_hash
        }

        return block