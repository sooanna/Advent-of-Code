def main():
    file = open("day2_inputs.txt")
    line = file.read()
    barcodes = line.split(",")
    invalidFlag = False
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

                # all possible sequence of digits repeated in an id
                for repeat in range(1, len(stringid)): # repeating at least twice
                    startAt = 0
                    if len(stringid) % repeat == 0:
                        sequenceIDs = []
                        while startAt < len(stringid):  # store the sequence of digits
                            EndAt = startAt+repeat
                            sequenceIDs.append(stringid[startAt:EndAt])
                            startAt = EndAt
                        
                        # check if all the elements are same
                        invalidFlag = all(x == sequenceIDs[0] for x in sequenceIDs)
                        # check if the id is already in the invalid id list
                        duplicateFlag = any(x == id for x in invalidIDs)
                        if invalidFlag and (duplicateFlag == False):
                            print (f"This is an invalid id: {id}")
                            invalidIDs.append(id)   # store the invalid id
                            invalidFlag = False
    
    # sum up the invalid ids
    total = sum(invalidID for invalidID in invalidIDs)

    print (total)


if __name__=="__main__":
    main()