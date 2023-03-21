list = []
N = int(input())
for i in range(N):
    #input().split(" ") used to split user input into list of elements
    user_input = input().split(" ")
    command = user_input[0]
    if command == "insert":list.insert(int(user_input[1]), int(user_input[2]))
    elif command == "remove":list.remove(int(user_input[1]))
    elif command == "append":list.append(int(user_input[1]))
    elif command == "pop":list.pop()
    elif command == "reverse":list.reverse()
    elif command == "sort":list.sort()
    elif command == "print":print(list)
    else:print("ERROR!")