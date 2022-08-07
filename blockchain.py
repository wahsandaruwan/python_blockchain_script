import datetime as dt
import hashlib as hs
import json as js

class Blockchain:
    def __init__(self) -> None:
        self.chain = list()
        genesis_block = self.createBlock(id = 1, data = "This is the genesis block", proof = 1, prevHash = "0")
        self.chain.append(initial_block)

    def create_block(self, id : int, data : str, proof : int, prev_hash : str) -> dict:
        """
        This function creates a new block as a dictionary and return it.
        Parameters:
            id (int) : ID of the new block,
            data (str) : Actual data tob stored in the block,
            proof (int) : Value used to confirm the transaction and create a new block,
            prev_hash(str) : Hash value of the previous block
        Returns:
            dict: New block
        """
                
        block = {
            "id" : id,
            "time_stamp" : str(dt.datetime().now()),
            "data" : data,
            "proof" : proof,
            "prev_hash" : prev_hash
        }

        return block