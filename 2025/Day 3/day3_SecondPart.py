def load_inputs(filename="day3_inputs.txt"):
    with open(filename) as f:
        return [line.strip() for line in f if line.strip()] 

def main():
    banks = load_inputs()
    joltage_list = []

    for bank in banks:
        max_joltage = []
        remainder = len(bank) - 12

        for digit in bank:
            while max_joltage and remainder > 0 and max_joltage[-1] < digit:
                max_joltage.pop()
                remainder -= 1
            max_joltage.append(digit)

        max_joltage = max_joltage[:12]
 
        joltageInt = int("".join(max_joltage))
        joltage_list.append(joltageInt)

    print(sum(joltage_list))

if __name__ == "__main__":
    main()
