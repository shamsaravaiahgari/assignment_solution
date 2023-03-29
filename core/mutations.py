

def mutate_string(string, position, char):
    List = list(string)
    List[position] = char
    newString = "".join(List)
    return newString

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)