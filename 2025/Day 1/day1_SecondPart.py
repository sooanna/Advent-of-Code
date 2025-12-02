def load_inputs(filename="day1_inputs.txt"):
    with open(filename) as f:
        return [line.strip() for line in f if line.strip()]


def rotation(point, rotate_dir, dial):
    return (point + (rotate_dir * dial)) % 100 


def calculate_password(point, inputs):
    list_of_point = []
    pointedZero = 0

    for input in inputs:
        direction = input[0]
        dial = int(input[1:])

        # rotation direction
        if direction == "L":
            rotate_dir = -1    
        else:
            rotate_dir = 1 

        # Excluding first and last click
        if dial > 1:
            for i in range(1, dial):
                # wrap around the dials                                  
                intermediate = rotation(point, rotate_dir, i)
                # 0-99 : 100 positions in total, hence % 100. Dial start from 0, hence, no shifting with -n or n.

                # count pointing to 0 during rotation
                if intermediate == 0:
                    pointedZero += 1

        # Perform rotation
        if rotate_dir == -1:
            point = rotation(point, rotate_dir, dial)
            print(f"The dial is rotated L{dial} to point at {point}.")
        else:
            point = rotation(point, rotate_dir, dial)
            print(f"The dial is rotated R{dial} to point at {point}.")

        list_of_point.append(point)

    return list_of_point, pointedZero


def find_password(list_of_point, pointedZero):
    # Count how many times 0 is pointed
    return pointedZero + sum(1 for point in list_of_point if point == 0)


def main():
    point = 50
    print(f"The dial starts by pointing at {point}.")
    inputs = load_inputs()
    list_of_point, pointedZero = calculate_password(point, inputs)
    password = find_password(list_of_point, pointedZero)
    print(f"The actual password to open the door is {password}.")


if __name__ == "__main__":
    main()