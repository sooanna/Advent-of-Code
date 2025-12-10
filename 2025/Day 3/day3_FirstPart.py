def load_inputs(filename="day3_inputs.txt"):
    # read the file to get inputs
    with open(filename) as f:
        return [line.strip() for line in f if line.strip()]

def calculate_total_output(joltage_list):
    return sum(max_joltage for max_joltage in joltage_list)
        

def main():
    joltage_list = []
    banks = load_inputs()
    i = 1

    for bank in banks:
        first_digit = bank[0]
        second_digit = bank[i]        


        while i < len(bank) :
            
            if i == len(bank)-1 :
                break
            else:
                track_ahead = bank[i+1]


            if second_digit > first_digit:
                first_digit = second_digit
                second_digit = bank [i+1]
            elif track_ahead > second_digit:
                if second_digit > first_digit:
                    first_digit = track_ahead
                else:
                    second_digit = track_ahead
                             
            i += 1
            # print(f"Joltage: {first_digit}.{second_digit}")
        i = 1
        
        joltage_list.append(int (first_digit + second_digit))

    total_output_joltage = calculate_total_output(joltage_list)
    print(total_output_joltage)



if __name__=="__main__":
    main()