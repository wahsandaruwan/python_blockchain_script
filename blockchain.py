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
