"""
A production facility needs an iterable object to keep track products
A class called "Production" will store the information needed.
Each item created in factory will have a string serial number "XXXXXXXX" and some date of production
Iterating objects created with Production class will return serial of all produced items sorted by date
1) 40p: Definition
    a) 10p: Basic class structure of Production
    b) 10p: Basic class structure of iterator class
    c) 10p: Method to add produced with serial
    d) 10p: Method that returns last added item
2) 40p: Execution:
    a) 10p: Create instance of Production
    b) 10p: Call method to add item: <add_item(serial, datetime)>
        - BB023871, 2020.03.05
        - KX023876, 2022.07.08
        - DD023875, 2021.07.10
    c) 10p: Call method to return last produced item <last_item_added()>
    d) 10p: Iterate the created object and write each item serial in a file on a new line
3) 20p: Documenting:
   a) 5p: type hints for arguments
   b) 5p: module documentation
   c) 5p: class documentation for all classes
   d) 5p: method documentation for all methods
"""