# Inbuild module imports
import sys

# Custom module imports
from block import Block

def main():
    """
    This is the main function which initiate all the operations.
    """ 

    print("\nEnter 'B' to view the entire blockchain or 'Q' to quit any time...\n")
    
    # Instance of block
    bl = Block()

    # Infinity loop
    while True:
        # Get data
        data  = input("Enter data : ")

        if(data == "B"):
            print("\n")
            print("-------------------------------------------------\n")
            # View entire blockchain
            print(bl.bc.get_chain())
            print("\n-------------------------------------------------")
            print("\n")
        elif(data == "Q"):
            # Terminate
            sys.exit()
        else:
            # Print blockchain validation result
            if (bl.bc.validate_blockchain()):
                print("\nBlockchain valid!")
            else:
                print("\nBlockchain invalid!")
            
            # Mine new block and print
            print(f"\n{bl.mine_block(data = data)}\n")
            print("-------------------------------------------------\n")

if __name__ == "__main__":
    main()