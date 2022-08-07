from datetime import datetime as dt
import hashlib as hs
import json as js

class Blockchain:
    def __init__(self) -> None:
        self.chain = list()
        genesis_block = self.create_block(index = 1, data = "This is the genesis block", proof = 1, prev_hash = "0")
        self.chain.append(genesis_block)

    def mine_block(self, data : str) -> dict:
        prev_block = self.get_prev_block()
        prev_proof = prev_block["proof"]
        index = len(self.chain) + 1
        proof = self.proof_of_work(prev_proof = prev_proof, index = index, data = data)

    def custom_digest(self, new_proof : int, prev_proof : int, index : int, data : str) -> bytes:
       digest = str((new_proof ** 3) - (prev_proof ** 3) + ((index * index) / (new_proof * prev_proof))) + data

       return digest.encode()

    def proof_of_work(self, prev_proof : str, index : int, data : str) -> int:
        new_proof = 1
        verify_proof = False

        while not verify_proof:
            print(new_proof)
            digest = self.custom_digest(new_proof = new_proof, prev_proof = prev_proof, index = index, data = data)
            hash_value = hs.sha256(digest).hexdigest()

            if hash_value[:8] == "00000000":
                verify_proof = True
            else:
                new_proof += 1
        
        return new_proof


    def get_prev_block(self) -> dict:
        """
        This function returns the previous block of the block chain.
        Returns :
            dict : Previous block
        """        
        return self.chain[-1]

    def create_block(self, index : int, data : str, proof : int, prev_hash : str) -> dict:
        """
        This function creates a new block as a dictionary and return it.
        Parameters:
            index (int) : Index of the new block,
            data (str) : Actual data tob stored in the block,
            proof (int) : Value used to confirm the transaction and create a new block,
            prev_hash(str) : Hash value of the previous block
        Returns:
            dict: New block
        """
                
        block = {
            "index" : index,
            "time_stamp" : str(dt.now()),
            "data" : data,
            "proof" : proof,
            "prev_hash" : prev_hash
        }

        return block