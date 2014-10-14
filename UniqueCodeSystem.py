class UniqueCodeSystem():
    def __init__(self, productCodeMap = {}):
        self.productCodeMap = productCodeMap
        self.method = None
        self.solution = None
        self.duplicates = []
        self.indexCount = 0

    def addProduct(self):
        isSuccess = False

        while (not isSuccess):
            productName = raw_input("Enter the product Name: ")
            print

            if (productName != ""):
                if (self.method == 1):
                    if(self.solution.generateProductMapping(productName,
                                                         self.productCodeMap,
                                                         self.duplicates)\
                                                          == 0):
                        isSuccess = True
                        print "Success!"
                        print
                    else:
                        print "Error. Please try again."
                        print
                elif (self.method == 2):
                    tempMap, indexCount, errMsg = self.solution.\
                                  generateProductMapping(productName,
                                                         self.productCodeMap,
                                                         self.indexCount)
                    if (errMsg == None):
                        self.indexCount = indexCount
                        isSuccess = True
                        print "Success!"
                        print
                    else:
                        print "Error:", errMsg, "Please try again."
                        print
            else:
                print "Invalid product name. Please try again."
                print

    def addProductFromCSV(self):
        isSuccess = False

        while (not isSuccess):
            filename = raw_input("Enter the CSV filename: ")
            print

            import os.path
            import copy
            if (filename != "" and os.path.isfile(filename)):
                if (self.method == 1):
                    try:
                        tempMap = copy.copy(self.productCodeMap)
                        self.solution.generateProductMappingFromCSV(
                                                         filename,
                                                         self.productCodeMap,
                                                         self.duplicates)
                        if(self.productCodeMap != tempMap):
                            isSuccess = True
                            print "Success!"
                            print
                        else:
                            print "Error. Please try again."
                            print
                    except:
                        print "Error. Please try again."
                        print
                elif (self.method == 2):
                    try:
                        tempMap, indexCount, errMsg = self.solution.\
                                      generateProductMappingFromCSV(filename,
                                                         self.productCodeMap,
                                                         self.indexCount)
                        if (errMsg == None):
                            self.indexCount = indexCount
                            isSuccess = True
                            print "Success!"
                            print
                        else:
                            print "Error:", errMsg, "Please try again."
                            print
                    except:
                        print "Error. Please try again."
                        print
            else:
                print "Invalid filename. Please try again."
                print

    def deleteProduct(self):
        key = raw_input("Enter product key: ")
        print

        if (key in self.productCodeMap):
            del self.productCodeMap[key]
            print "Product deleted."
            print
        else:
            print "Unable to find product."
            print

    def retrieveProduct(self):
        key = raw_input("Enter product key: ")
        print

        if (key in self.productCodeMap):
            print self.productCodeMap[key]
            print
        else:
            print "Unable to find product."
            print

    def printAllProducts(self):
        print "############ Map ############"
        print
        print "Number of Products:", len(self.productCodeMap)
        print
        for key in self.productCodeMap:
            print key+":", self.productCodeMap[key]
        print

    def menu(self):
        while (True):
            chosenMenu = raw_input(\
"""Menu (Choose an option by entering its option number):
    1. Add Product Manually
    2. Add Product(s) from CSV
    3. Delete Product
    4. Retrieve Product
    5. Print All Products

Choice: """)
            print

            if (chosenMenu == "1"):
                self.addProduct()
            elif (chosenMenu == "2"):
                self.addProductFromCSV()
            elif (chosenMenu == "3"):
                self.deleteProduct()
            elif (chosenMenu == "4"):
                self.retrieveProduct()
            elif (chosenMenu == "5"):
                self.printAllProducts()
            else:
                print "Sorry, that option is not available.\n"

    def run(self):
        while (True):
            self.method = None
            chosenMethod = raw_input(\
"""This system uses two methods, namely a hash table method as well as a
indexing method. Enter the option number to choose the method you wish you use:
1. Hash-Table Method
2. Indexing Method

Choice: """)
            print

            if (chosenMethod == "1"):
                self.method = int(chosenMethod)
                import hashSolution
                self.solution = hashSolution
                self.menu()
            elif (chosenMethod == "2"):
                self.method = int(chosenMethod)
                import indexingSolution
                self.solution = indexingSolution
                while (True):
                    self.menu()
            else:
                print "Sorry, that option is not available.\n"

##################### Main Function #####################

def main():
    codeSystem = UniqueCodeSystem()
    codeSystem.run()

    return True;

if __name__ == "__main__":
    main()
