import itertools
from verify import Verify

class PasswordGuesser:
    def __init__(self, verify:Verify):
        self.verify = verify
        self.optionMatrix = []
        self.all_combinations = [] 
        self.__createOptionMatrix()
        self.__findAllCombinations()

    # Create a matrix of all options
    def __createOptionMatrix(self):
        self.optionMatrix.extend(self.verify.getPossibleStrings())
        for optionList in self.verify.getPossibleDates():
            self.optionMatrix.extend(optionList)
       
    # Creation de combinaisons part 1
    def __pwdOptions(self):
        passwordOptions = []
        for length in range(max(6,len(self.optionMatrix)+1)):
            passwordOptions.extend(itertools.combinations(self.optionMatrix, length))
        return passwordOptions

    # Creation de combinaisons part 2
    def __getResults(self, passwordOptions):
        results=[]
        for combination in passwordOptions:
            results.extend(itertools.product(*combination))
        return results
    
    # Permutations des combinaisons
    def __combineResults(self, results):
        for tuple in results:
            combinations =[]
            combinations=itertools.permutations(tuple,len(tuple))
            for option in combinations:
                password = ""
                for element in option:
                    password += element
                self.all_combinations.append(password)

    # Find all possible combinations using up to 5 elements
    def __findAllCombinations(self): 
        
        passwordOptions = self.__pwdOptions()
        
        results=self.__getResults(passwordOptions)

        self.__combineResults(results)

