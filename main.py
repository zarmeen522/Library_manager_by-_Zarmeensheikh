import json

class BookCollection:
    """A class to manage a collection of books, allow users to add and organize of books."""

    def __init__(self):
     """ Initialize the new book collection with an empty list and set up the file storage."""
     self.books_list =[]
     self.storage_file ="books_data.json"
     self.read_from_file()
    
    def read_from_file(self):
        """ Load saved books from a JSON file into memory.
        if the file doesn't exist, start with an empty list."""
        try:
           with open(self.storage_file,"r") as file:
              self.books_list=json.load(file)
        except(FileNotFoundError,json.JSONDecodeError):
           self.books_list=[]
           print("No saved books found. Starting with an empty collection.")
    def save_to_file(self):
       """ Save the current book list to a jason file for permanent storage."""
       with open(self.storage_file,"w")as file:
          json.dump(self.books_list,file, indent=4)

    def create_new_book(self):
        """ Create a new book entry and add it to the collection."""
        book_title= input("Enter the Book Title:")
        book_author = input("Enter the Author's Name:")
        book_genre =input("Enter the Genre:")
        book_year = input("Enter the Year of Publication:")
        is_book_read =(input("Have you read this book before?(yes/no):").strip().lower() =="yes"
            )
        book ={
            "title":book_title,
            "author":book_author,
            "genre":book_genre,
            "year":book_year,
            "read":is_book_read
         }
        
        self.books_list.append(book)
        self.save_to_file()
        print(f"Above mentioned Book is added to the collection successfully!\n.") 

    def delete_book(self):
           """ Remove a book from the collection using its title.
           """
           Book_title =input("Enter the title of the book you want to remove:")

           for book in self.books_list:
              if book["title"].lower() ==Book_title.lower():
                self.books_list.remove(book)
                self.save_to_file()
                print(f"Book'{Book_title}' has been removed from the collection.")
                return
              print(f"Book'{Book_title}' not found in the collection.\n")

    def find_book(self):
        """ Find your book in the the collection using its Title or Author's name."""      
        search_type = input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
        search_text =input("Enter the Search term: ")
        found_books = [
              book 
              for book in self.books_list
              if search_text in book["title"].lower()
              or search_text in book["author"].lower()
        ]
    
        if found_books:
            print("Matching books found:")
            for index, book in enumerate(found_books,1):
                reading_status ="Read" if book["read"] else "Unread!"
                print(f"{index}.{book['title']} by {book['author']} ({book['year']} -{book['genre']} - {reading_status})")
        else :
                print("No books found matching your search criteria.\n")

    def update_book(self):
        """ Update the Details of a book in the collection."""
        Book_title = input("Enter the title of the book you want to update:")
        for book in self.books_list:
            if book["title"].lower() == Book_title.lower():
                new_title = input("Enter the new title (or press Enter to keep the current title):")
                new_author = input("Enter the new author (or press Enter to keep the current author):")
                new_genre = input("Enter the new genre (or press Enter to keep the current genre):")
                new_year = input("Enter the new year (or press Enter if you want to keep the same year):")
                new_read = input("Have you read this Book? (yes/no): ").strip().lower() == "yes"
                if new_title:
                    book["title"] = new_title
                if new_author:
                    book["author"] = new_author
                if new_genre:
                    book["genre"] = new_genre
                if new_year:
                    book["year"] = new_year
                book["read"] = new_read
                self.save_to_file()
                print(f"Book '{Book_title}' has been updated successfully.")
                return
        print(f"Book '{Book_title}' not found in the collection.")

    def show_all_books(self):
        """ Display all the Books in the collection."""
        if not self.books_list:
            print("No books found in the collection.")
            return
        print("Your Book collection:")
        for book in self.books_list:
            read_status ="Read" if book["read"] else "Not Read!" 
            print(f"{book['title']} by {book['author']} ({book['year']}) -{book['genre']}")
            print(f"Status:{read_status}\n")

    def show_read_books(self):
        """ Calculate and Display Statistics about your reading progress"""
        total_books=len(self.books_list)
        completed_books = sum(1 for book in self.books_list if book["read"])
        completion_rate =(
            (completed_books/ total_books*100) if total_books> 0 else 0
        )
        print(f"Total books in collection: {total_books}")
        print(f"Reading progress: {completion_rate:2f}%\n")

    def start_application(self):
        """ Run the main application loop with a user_friendly menu interface."""
        while True:
            print("Welcome to your Book Collection Manager! ")
            print("1. Add a new Book")
            print("2. Remove a Book")
            print("3. Search for Books")
            print("4. Update Book details")
            print("5. View all Books")
            print("6. View Reading progress")
            print("7. Exit")

            user_choice = input("Please choose an option(1-7): ")

            if user_choice =="1":
                self.create_new_book()
            elif user_choice =="2":
                self.delete_book()
            elif user_choice =="3":
                self.find_book()
            elif user_choice =="4":
                self.update_book()
            elif user_choice =="5":
                self.show_all_books()
            elif user_choice=="6":
                self.show_read_books()
            elif user_choice =="7":
                self.save_to_file()

                print("Thank you for using Book Collection Manager. Goodbye!")
                break   
            else:
               print("Invalid choice. Please try again.\n")
if __name__ =="__main__":
    book_manager= BookCollection()
    book_manager.start_application()


           
           
           






           
