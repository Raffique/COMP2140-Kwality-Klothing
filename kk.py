# id#: 620106530
#name: Bradford Coore


#!/usr/bin/python3

import random
import math
import sys

class KK():
    def __init__(self):
        pass

    def transaction(self):
        items = input("Enter Number of Items:")
        pass

    def inventory(self):
        pass

    def start(self):
        print("MAIN MENU:")
        print("Transation-T")
        print("Inventory-I")
        choice = input('Select Operation:')

        if choice == "T" or "t":
            self.transaction()
        if choice == "I" or "i":
            self.inventory()

def main(): 
    KK().start()

if __name__ == "__main__":
    main()
        