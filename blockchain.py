# Inbuild module imports
import hashlib as hs

# Custom module imports
import helpers as hp

class Blockchain:
    
    # -----Constructors-----
    def __init__(self) -> None:
        """
        This is the constructor which lets the class initialize the object's attributes.
        """ 

        self.chain = list()


    # -----Getter and setter functions-----
    def set_chain(self, chain):
        """
        This function reset the whole chain variable related to the blockchain with a new value.

        Parameters:
            chain (list): Blockchain contains all the blocks.
        """

        self.chain = chain


    def get_chain(self):
        """
        This function retrieves the whole chain variable related to the blockchain.

        Returns:
            int: Blockchain contains all the blocks.
        """  

        return self.chain
    

    # -----Other functions-----
    def append_new_block(self, block):
        """
        This function appends a new block to the blockchain.

        Parameters:
            chain (list): New block for the blockchain.
        """

        self.chain.append(block)

    
    def get_prev_block(self) -> dict:
        """
        This function retireves the previous block of the blockchain and returns it.

        Returns :
            dict : Previous block of the blockchain.
        """        
        
        return self.chain[-1]


    def validate_blockchain(self) -> bool:
        """
        This function verifies whether the blockchain is valid or not

        Returns:
            bool: Validity of the blockchain.
        """        
        curr_block = self.chain[0]
        block_index = 1

        # Verify hashes of current and next blocks of the blockchain
        while block_index < len(self.chain):
            next_block = self.chain[block_index]

            if (next_block["prev_hash"] != hp.hash_prev_block(curr_block)):
                return False

            curr_proof = curr_block["proof"]
            next_index = next_block["index"]
            next_data = next_block["data"]
            next_proof = next_block["proof"]

            digest = hp.custom_digest(new_proof = next_proof, prev_proof = curr_proof, index = next_index, data = next_data)
            hash_value = hs.sha256(digest).hexdigest()

            if (hash_value[:4] != "0000"):
                return False

            curr_block = next_block
            block_index += 1

        return True