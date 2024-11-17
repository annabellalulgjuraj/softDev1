def add_chars(char1, char2):
    char1_value= ord(char1)
    char2_value= ord(char2)
    total= chr(char1_value + char2_value)

    return total, char1_value, char2_value


def subtract_chars(char1, char2):
    char1_value= ord(char1)
    char2_value= ord(char2)
    total= chr(char1_value - char2_value)

    return total, char1_value, char2_value



def main():
    char1= input("input a character: ")
    char2= input("input another character: ")

    result_of_add = add_chars(char1, char2)
    result_of_sub = subtract_chars(char1, char2)

    print (result_of_add)
    print (result_of_sub)


main()
