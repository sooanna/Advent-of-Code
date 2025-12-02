def main():
    file = open("day2_inputs.txt")
    line = file.read()
    barcodes = line.split(",")
    validFlag = True
    invalidIDs = []
    
    # iterate through barcode array
    for barcode in barcodes:
    # split a barcode into first and last ids
        ids = barcode.split("-")
        firstID = ids[0]
        lastID =ids[1]

        # ID is valid if they do not have any leading zeroes
        if firstID[0] != "0" and lastID[0] != "0":
            for id in range(int(firstID), int(lastID)+1):
                stringid = str(id)
                
                # if length of number is even, divide into 2 parts and compare.
                if len(stringid) % 2 == 0:
                    half = int(len(stringid) / 2)
                    firstPart = stringid[0:half]
                    secondPart = stringid[half:]

                    # if they are same, it is an invalid id
                    if firstPart == secondPart:
                        print (f"This is an invalid id: {id}")
                        invalidIDs.append(id)   # store the invalid id
            
    # sum up the invalid id
    total = sum(invalidID for invalidID in invalidIDs)

    print (total)


if __name__=="__main__":
    main()