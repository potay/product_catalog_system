def changeToBase62(n, length=None):
    # Base 62: 0-9, followed by a-z, and finally A-Z.
    numOfLetters = 26
    numOfNumbers = 10
    base = numOfNumbers + numOfLetters*2
    base62 = ""
    while n > 0:
        temp = n%base
        if numOfNumbers <= temp < numOfNumbers + numOfLetters:
            number = chr(ord('a') + temp - numOfNumbers)
        elif numOfNumbers + numOfLetters <= temp < base:
            number = chr(ord('A') + temp - (numOfNumbers + numOfLetters))
        else:
            number = str(temp)
        base62 = number + base62
        n /= base

    if (length != None):
        while len(base62) < length: base62 = "0" + base62

    return base62

def generateProductMappingFromCSV(filename, productCodeMap = {},
                                  indexCount = 0):
    import csv
    length = 6
    errMsg = None

    if (len(productCodeMap) != indexCount):
        errMsg += "Invalid index count.\n"
        return None, None, errMsg

    with open(filename, 'rU') as productsFile:
        productsList = csv.reader(productsFile, delimiter=' ', quotechar='|')
        for row in productsList:
            product = ' '.join(row)
            key = changeToBase62(indexCount, length)
            if (product not in productCodeMap.values()):
                if (key in productCodeMap):
                    errMsg += "Invalid product code map. Contains key larger \
than index count.\n"
                    return None, None, errMsg
                else:
                    productCodeMap[key] = product
                indexCount += 1

    return productCodeMap, indexCount, errMsg

def generateProductMapping(product, productCodeMap = {}, indexCount = 0):
    length = 6
    errMsg = None

    if (len(productCodeMap) != indexCount):
        errMsg += "Invalid index count.\n"
        return None, None, errMsg

    key = changeToBase62(indexCount, length)
    if (product not in productCodeMap.values()):
        if (key in productCodeMap):
            errMsg += "Invalid product code map. Contains key larger than \
index count.\n"
            return None, None, errMsg
        else:
            productCodeMap[key] = product
        indexCount += 1

    return productCodeMap, indexCount, errMsg


############## Test Functions ###############

def testGenerateProductMappingFromCSV(filename, printList=False):
    productCodeMap, indexCount, errMsg = generateProductMappingFromCSV\
                                         ("products.csv")
    print "Errors:", errMsg
    print "indexCount:", indexCount

    if (printList):
        print
        print "############ Map ############"
        print
        for key in productCodeMap:
            print key+":", productCodeMap[key]


##################### Main Function #####################

def main():
    testGenerateProductMappingFromCSV("products.csv", printList=True)

    return True;

if __name__ == "__main__":
    main()
