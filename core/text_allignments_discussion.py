# Ask user for input
n = int(input())

# Initialize empty string to store the logo
logo = ""

# Top cone
for i in range(1, n*2, 2):
    # Create a string of 'H's of length i centered within a string of spaces of length n*2-1
    line = (i * "H").center(n*2-1, " ")
    logo += line + "\n"

# Top square
s1 = (n * "H").center(n*2-1, " ") + (n*2+1) * " "
for i in range(n+1):
    logo += (2 * s1) + "\n"

# Middle line
s2 = (n * 5 * "H").center(n*6-1, " ")
for i in range(0, n, 2):
    logo += s2 + "\n"

# Bottom square
s3 = (n * "H").center(n*2-1, " ") + (n*2+1) * " "
for i in range(n+1):
    logo += (2 * s3) + "\n"

# Bottom cone
for i in range(n*2-1, 0, -2):
    line = (i * "H").center(n*2-1, " ")
    logo += (n*4) * " " + line + "\n"

# Print the logo
print(logo)
