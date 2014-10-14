############## Unique Code Generation Functions ##############

import hash

def generateProductMappingFromCSV(filename, productCodeMap = {},
                                  duplicateList = []):
    import csv

    with open(filename, 'rU') as productsFile:
        productsList = csv.reader(productsFile, delimiter=' ', quotechar='|')
        for row in productsList:
            product = ' '.join(row)
            key = hash.hash(product)
            if (key in productCodeMap and productCodeMap[key] != product):
                productCodeMap[key].append(product)
                duplicateList.append(key);
            else:
                productCodeMap[key] = [product]

    return productCodeMap, duplicateList

def generateProductMapping(product, productCodeMap = {}, duplicateList = []):
    key = hash.hash(product)
    if (key in productCodeMap and productCodeMap[key] != [product]):
        productCodeMap[key].append(product)
        duplicateList.append(key)
        return 1
    else:
        productCodeMap[key] = [product]
        return 0


############## Test Functions ###############

def generateProduct():
    import sampleText
    from random import randint
    lengthOfSample = len(sampleText.text)
    lengthMin = 5
    lengthMax = 10
    start = randint(0,lengthOfSample)
    end = randint(start+lengthMin, start+lengthMax)
    return " ".join(sampleText.text[start:end])

def testGenerateProductMapping(numOfCases = 10**2, printStats=False):
    print "Testing..."
    productCodeMap = {}
    numOfDuplicates = 0
    duplicateList = []
    for i in xrange(numOfCases):
        product = generateProduct();
        numOfDuplicates += generateProductMapping(product, productCodeMap,
                                                 duplicateList)
        if ((float(i)/numOfCases*100)%10 == 0):
            print str(int(float(i)/numOfCases*100))+"%...",
    print "100%"
    print "Number of Duplicates:", numOfDuplicates

    if (printStats):
        hashLength = 6
        haseBase = 62

        numOfProducts = numOfCases
        spread = float(numOfProducts) / (haseBase**hashLength)
        print "Spread:", spread
        print "Duplicates/Number of Products:", float(numOfDuplicates)/ \
                                                numOfProducts
        print "Duplicate List:"
        print duplicateList
        print

        import json
        print json.dumps(productCodeMap, sort_keys=True,
                         indent=4, separators=(',', ': '))

def testGenerateProductMappingFromCSV(filename, printStats=False):
    print "Testing..."
    print
    productCodeMap, duplicateList = generateProductMappingFromCSV\
                                    ("products.csv")
    numOfDuplicates = len(duplicateList)
    print "Number of Duplicates:", numOfDuplicates

    if (printStats):
        hashLength = 6
        haseBase = 62

        numOfProducts = (len(productCodeMap) + numOfDuplicates)
        spread = float(numOfProducts) / (haseBase**hashLength)
        print "Spread:", spread
        print "Duplicates/Number of Products:", float(numOfDuplicates)/ \
                                                numOfProducts
        print "Duplicate List:"
        print duplicateList
        print

        print "############ Map ############"
        print
        for key in productCodeMap:
            print key+":", productCodeMap[key]


##################### Main Function #####################

def main():
    #testGenerateProductMappingFromCSV("products.csv", printStats=True)
    #testGenerateProductMapping(numOfCases=50*10**4, printStats=True)

    return True;

if __name__ == "__main__":
    main()
