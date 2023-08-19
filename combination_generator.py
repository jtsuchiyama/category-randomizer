from typing import List

class CombinationGenerator:
    expenses_path = "categories.txt"

    def __init__(self) -> None:
        print (self.read_categories())
        
    # Reads the text file given by self.expenses_path and returns a list of lists, where each list contains a single category
    def read_categories(self) -> List[List[str]]:
        # Read and split each line into a separate list entry
        read_file = open(self.expenses_path, 'r')
        lines = read_file.read().splitlines()

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
    
    # Generates a text file 'combination.txt' with all possible combinations of the categories

CombinationGenerator()

