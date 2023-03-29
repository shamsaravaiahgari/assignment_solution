def merge_the_tools(string, k):
    # Break the long string into smaller groups of letters
    groups = []
    for i in range(0, len(string), k):
        group = string[i: i + k]
        groups.append(group)

    # Remove repeated letters from each group and print the result
    for group in groups:
        unique_letters = []
        for letter in group:
            if letter not in unique_letters:
                unique_letters.append(letter)
        print(''.join(unique_letters))


if __name__ == '__main__':
    string = input("Enter a string: ")
    k = int(input("Enter the group size: "))
    merge_the_tools(string, k)
