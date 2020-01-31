def main():
    print("Task to return alternate char from string")
    string_alternative()
    # created a function
def string_alternative():
    strInput = input("Enter string: ")
    strOutput = strInput[::2]
    # reading alternative alphabet in string
    print(strOutput)

if __name__  == "__main__":
    main()
     #calling the main function