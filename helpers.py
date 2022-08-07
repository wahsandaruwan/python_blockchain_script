# Inbuild module imports
import hashlib as hs
import json as js

# -----Block preparing helper functions-----
def hash_prev_block(block : dict) -> str:
    """
    This function hash the previous block of the blockchain using sha256 and returns it.

    Parameters:
        block (dict): Previous block relative to the new block.

    Returns:
        str: Hashed previous block for the new block of the blockchain.
    """  

    json_encoded_block = js.dumps(block, sort_keys=True).encode()

    return hs.sha256(json_encoded_block).hexdigest()


def custom_digest(new_proof : int, prev_proof : int, index : int, data : str) -> bytes:
    """
    This function creates a new custom digest using a custom mathamatical equation and return a encoded digest.

    Parameters:
        new_proof (int): New proof of the new block.
        prev_proof (int): Previous proof of the previous block.
        index (int): Index of the new block.
        data (str): Actual data tob stored in the block.

    Returns:
        bytes: Encoded custom digest to verify the proof.
    """  

    digest = str((new_proof ** 3) - (prev_proof ** 3) + ((index * index) / (new_proof * prev_proof))) + data

    return digest.encode()


def proof_of_work(prev_proof : str, index : int, data : str) -> int:
    """
    This function verifies the proof using custom digest and sha256 and returns a new proof to use for the new transaction.

    Parameters:
        prev_proof (str): Previous proof of the previous block.
        index (int): Index of the new block.
        data (str): Actual data tob stored in the block.

    Returns:
        int: New proof for the new block of the blockchain.
    """   

    new_proof = 1
    verify_proof = False

    while not verify_proof:
        digest = custom_digest(new_proof = new_proof, prev_proof = prev_proof, index = index, data = data)
        hash_value = hs.sha256(digest).hexdigest()

        if (hash_value[:4] == "0000"):
            verify_proof = True
        else:
            new_proof += 1
    
    return new_proof