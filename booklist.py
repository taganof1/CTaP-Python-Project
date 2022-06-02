booklist = set()
userquit = ("x", "X")
while True:
    bookadd = input("Enter the book name: ")
    booklist.add(bookadd)

    if input(userquit):
        print(booklist)
        quit