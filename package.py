# Created by Ryan Nguyen
# Created on December 2020
# This program tells a user if their package
#   will be accepted or not, based on weight and volume


def main():
    # This function calculates weight and volume

    # input
    weight_as_string = input("Enter weight of package: ")
    length_as_string = input("Enter length of package: ")
    width_as_string = input("Enter width of package: ")
    height_as_string = input("Enter height of package: ")

    print("")

    # process + output
    # tests if every variable is an integer
    try:
        weight_as_number = int(weight_as_string)
        length_as_number = int(length_as_string)
        width_as_number = int(width_as_string)
        height_as_number = int(height_as_string)
    # volume calculation
        volume = weight_as_number*length_as_number*height_as_number
        if weight_as_number > 0 and length_as_number > 0 and width_as_number > 0 and height_as_number:
            if weight_as_number < 27:
                if volume < 10000:
                    print("We will accept your package!")
                else:
                    print("Volume must not exceed 10 000cm²")
            else:
                print("Package must not exceed 27kg")
        else:
            print("Dimensions and weight must be positive")
    except Exception:
        print("Invalid integer")
        

if __name__ == "__main__":
    main()
