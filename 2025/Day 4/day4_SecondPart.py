def load_inputs(filename ="day4_inputs.txt"):
    with open(filename) as f:
        return [line.strip() for line in f if line.strip()]

def validate_roll(character, adjacentRolls, forkliftRolls):
    if character == "@" and adjacentRolls < 4:
        return forkliftRolls + 1, True
    else:
        return forkliftRolls, False

def print_output(lines):
    for line in lines:
        print(f"{line} \n")

def main():
    lines = load_inputs()
    forkliftRolls = 0
    copiedForkliftRolls = 0
    loopUntil = True
    rows = len(lines)
    cols = len(lines[0])

    while loopUntil:    
        for lineNum in range(rows):
            for position in range(cols):
                character = lines[lineNum][position]

                if character == "@":
                    adjacentRolls = 0
                    
                    # Check all 8 neighboring directions
                    for dy in [-1, 0, 1]:       # dy = -1 (up), dy = 1 (down)
                        for dx in [-1, 0, 1]:   # dx = -1 (left), dx = 1 (right)
                            if dy == 0 and dx == 0:
                                continue  # skip the current position

                            ny = lineNum + dy
                            nx = position + dx

                            # check edge cases
                            if 0 <= ny < rows and 0 <= nx < cols:
                                if lines[ny][nx] == "@":
                                    adjacentRolls += 1                                    
                                
                                
                        
                    forkliftRolls, valid = validate_roll(character, adjacentRolls, forkliftRolls)
                    
                    if valid:
                        line = list(lines[lineNum])
                        line[position] = "X"
                        lines[lineNum] = "".join(line)
                    
        if forkliftRolls == copiedForkliftRolls and copiedForkliftRolls != 0:
            loopUntil = False
        else:
            print_output(lines)
            copiedForkliftRolls = forkliftRolls

    print(forkliftRolls)





if __name__=="__main__":
    main()