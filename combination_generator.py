from typing import List
from itertools import product
from collections.abc import Generator

class CombinationGenerator:
    cat_path = "categories.txt"
    comb_path = "combinations.txt"

    def __init__(self) -> None:
        categories = self.read_categories()
        self.write(categories)
        
    # Reads the text file given by self.expenses_path and returns a list of lists, where each list contains a single category
    def read_categories(self) -> List[List[str]]:
        # Read and split each line into a separate list entry
        read_file = open(self.cat_path, 'r')
        lines = read_file.read().splitlines()
        read_file.close()

        # Iterate through the list and separate each category into its own list in the 'categories' list
        categories = []
        category = []
        for line in lines:
            # Append the category to the 'categories' list and reset the category
            if line == '':
                categories.append(category)
                category = []

            # Add the line to the category if it's not a comment
            else:
                if line[0] != '#':
                    category.append(line)
        
        return categories
    
    # Generates all possible combinations
    def generate(self, categories) -> Generator[str,None,None]:
        # Source: https://stackoverflow.com/questions/64867925/python-nested-lists-all-combinations
        lst_positions = [l for l in categories if isinstance(l, list)]
        for p in product(*lst_positions):
            it = iter(p)
            yield [e if not isinstance(e, list) else [next(it)] for e in categories]

    # Writes to a text file 'combination.txt' with all possible combinations of the categories; Source: https://stackoverflow.com/questions/64867925/python-nested-lists-all-combinations
    def write(self,categories) -> None:
        # Open the file to be read
        write_file = open(self.comb_path, 'w') 

        # Generate and write all combinations
        for pr in self.generate(categories):
            write_file.write(str(pr) + "\n")
        
        # Close file
        write_file.close()   

CombinationGenerator()


