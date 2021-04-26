#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: April 2021
# This program finds the area and perimeter of a rectangle using
#   dimensions that the user entered

import math


def main():
    # This function calculates the area and perimeter

    # Input
    rectangle_length = int(input("Enter the length of the rectangle (mm): "))
    rectangle_width = int(input("Enter the width of the rectangle (mm): "))

    # Process
    area_of_rectangle = rectangle_length * rectangle_width
    perimeter_of_rectangle = 2 * (rectangle_length + rectangle_width)

    # Output
    print("")
    print("The area is: {} mm².".format(area_of_rectangle))
    print("The perimeter is: {} mm.".format(perimeter_of_rectangle))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
