def ends_with_ab(string):
    state = 0

    for ch in string:
        if state == 0:
            if ch == 'a':
                state = 1
            else:
                state = 0

        elif state == 1:
            if ch == 'a':
                state = 1
            elif ch == 'b':
                state = 2
            else:
                state = 0

        elif state == 2:
            if ch == 'a':
                state = 1
            else:
                state = 0

    return state == 2


# Main Program
s = input("Enter a string: ")

if ends_with_ab(s):
    print("Accepted: String ends with 'ab'")
else:
    print("Rejected: String does not end with 'ab'")