# Custom module imports
from block import Block

# Instance of block
bl = Block()

# Infinity loop
while True:
    # Get data
    data  = input("Enter data or press 'BC' to view the entire blockchain : ")

    # Mine new block and print
    if(data == "BC"):
        print("\n")
        print("-------------------------------------------------\n")
        print(bl.view_blockchain())
        print("\n-------------------------------------------------")
        print("\n")
    else:
        print(f"\n{bl.mine_block(data)}\n")