
class BookStore:
    # Αρχικοποίηση λίστας για την αποθήκευση των βιβλίων
    def __init__(self):
        self.items = []
        pass

    # Προσθήκη νέου βιβλίου
    def addBook(self, title, author, year, price, isbn):
        # αµυντικός προγραµµατισµός
        if (type(title) == str and type(author) == str and type(isbn) == str and type(year) == int and type(price) == float):
            newBook = Book(title, author, year, price, isbn)
            try:
                self.items.append(newBook)
                print(newBook, '.(Επιτυχής προσθήκη !)')
            except:
                print(newBook, '.(Ανεπιτυχής προσθήκη !)')

        else:
            print('something went wrong with one of the values', )

    # Αναζήτηση βιβλίων με όνομα και επώνυμο του συγγραφέα
    def searchBooksByAuthor(self, author=None):
        result = []
        for i in self.items:
            if author.lower() in i.author.lower():
                result.append(i)
        return result

    # Διαγραφή βιβλίου με βάση το ISBN
    def deleteBookWithISBN(self, isbn=None):
        result = []
        for idx, i in enumerate(self.items):
            if isbn == i.isbn:
                print(i, 'διαγράφηκε.', idx)
                self.items.pop(idx)
        return result

    def __repr__(self):
        return ('Πλήθος βιβλίων: {}\n{}').format(len(self.items), '\n'.join(''.join(str(l)) for l in self.items))


class Book:
    def __init__(self, title, author, year, price, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.isbn = isbn
        pass  # Αρχικοποίηση βιβλίου

    def __repr__(self):
        return ('Βιβλίο: {}, Συγγραφέας: {}, Έτος: {}, Τιµή: {}€, ISBN: {}').format(self.title, self.author, self.year, self.price, self.isbn)


if __name__ == "__main__":
    bs = BookStore()
    print("\n0) Καταχώρηση Βιβλίων\n=====================")
    bs.addBook("Python Crash Course", "Eric Matthews",
               2016, 27.95, "1593279280")
    bs.addBook("Learning Python ", "Mark Lutz", 2021, 40.29, "1449355730")
    bs.addBook("Head First Python", "Paul Barry", 2017, 36.25, "7519813630")
    bs.addBook("Introduction to Machine Learning with Python",
               "Andreas C. Mulle", 2020, 31.99, "1449369413")
    bs.addBook("Python for Data Analysis",
               "Wes McKinney", 2022, 38.38, "1098104032")
    bs.addBook("Deep Learning with Python",
               "Francois Chollet", 2017, 30.20, "1617284433")

    print("\n1) Αναζήτηση βιβλίων με το όνομα και επώνυμο συγγραφέα\n======================================================")

    author = input("Πληκτρολογήστε Όνοµα και Επώνυµο συγγραφέα: ")

    bk = bs.searchBooksByAuthor(author)

    if bk:
        print("Τα βιβλία που βρέθηκαν είναι:")
        for b in bk:
            print("\t", b)
    else:
        print("** Δεν υπάρχουν βιβλία με αυτόν τον συγγραφέα **")

    print("\n2) Διαγραφή βιβλίου με βάση το ISBN\n===================================")

    deleteWithISBN = input("Πληκτρολογήστε ISBN:")
    bs.deleteBookWithISBN(deleteWithISBN)

    print("\n3) Εκτύπωση όλων των διαθέσιμων βιβλίων με όλη την σχετική πληροφορία\n=====================================================================")
    print(bs)
