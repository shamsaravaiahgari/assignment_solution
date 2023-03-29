def print_formatted(number):
    # Determine the maximum width of binary representation
    width = len(bin(number)[2:])
    # Loop through integers from 1 to number and print the desired values
    for i in range(1, number + 1):
        # Decimal value
        dec = str(i).rjust(width, ' ')
        # Octal value
        octal = oct(i)[2:].rjust(width, ' ')
        # Hexadecimal value
        hexa = hex(i)[2:].upper().rjust(width, ' ')
        # Binary value
        binary = bin(i)[2:].rjust(width, ' ')
        # Print the formatted values
        print(f"{dec} {octal} {hexa} {binary}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

