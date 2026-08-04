class Books:
    def __init__(self):
        self.name = ""
        self.book_ID = ""
        self.Author = ""
        self.status = False

    def self_name(self):
        self.name = input("Enter your book name: ")

    def self_book_ID(self):
        self.book_ID = int(input("Enter your Book ID: "))

    def self_Author(self):
        self.Author = input("Enter book Author name: ")

    def self_status(self):
        choice = input("Is the book available? (yes/no): ")

        if choice.lower() == "yes":
            self.status = True
            print("Book is available")
        else:
            self.status = False
            print("Book is not available")

    def display(self):
        print("\nBook Details")
        print("Book Name :", self.name)
        print("Book ID :", self.book_ID)
        print("Author :", self.Author)

        if self.status:
            print("Status : Available")
        else:
            print("Status : Not Available")


b1 = Books()

b1.self_name()
b1.self_book_ID()
b1.self_Author()
b1.self_status()
b1.display()