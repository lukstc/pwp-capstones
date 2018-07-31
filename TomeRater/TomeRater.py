# @Xukun LIU

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}
    def get_email(self):
        return self.email
    def change_email(self, address):
        self.email = address
        print("User's email address will be changed to {self.email}".format(self.email))
    def __repr__(self):
        overview = "User: {name}; Email: {email}; Books read: {books}".format(name=self.name, email=self.email, books=self.books)
        return overview
    def __eq__(self, other_user):
        if (self.name == other_user.name) and (self.email == other_user.email):
            return True
        else:
            return False
    def read_book(self,book,rating):
        self.books[book]=rating
    def get_average_rating(self):
        rating_sum = 0
        book_count = 0
        for book in self.books:
            if self.books[book] != None:
                rating_sum += self.books[book]
                book_count += 1
        return rating_sum/book_count

class Book(object):
    def __init__(self, title, isbn):
        self.title = title #strings
        self.isbn = isbn #number
        self.ratings = [] #empty list
    def __repr__(self):
        return self.title
    def get_title(self):
        return self.title
    def get_isbn(self):
        return self.isbn
    def set_isbn(self,new_isbn):
        self.isbn = new_isbn
        print("Set the new isbn: {} to book".format(new_isbn))
    def add_rating(self,rating):
        if (rating >= 0) and (rating<=4):
            self.ratings.append(rating)
        else:
            print("Invalid Rating")
    def __eq__(self,other_book):
        return (self.title == other_book.title) and (self.isbn == other_book.isbn)
    def get_average_rating(self):
        return sum(self.ratings)/len(self.ratings)
    def __hash__(self):
        return hash((self.title,self.isbn))

class Fiction(Book):
    def __init__(self,title,author,isbn):
        super(Fiction,self).__init__(title,isbn)
        self.author = author
    def get_author(self):
        return self.author
    def __repr__(self):
        return "{title} by {author}".format(title = self.title, author = self.author)

class Non_Fiction(Book):
    def __init__(self,title,subject,level,isbn):
        super().__init__(title,isbn)
        self.subject=subject
        self.level=level
    def get_subject(self):
        return self.subject
    def get_level(self):
        return self.level
    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title,level=self.level, subject=self.subject)

class TomeRater():
    #Book.__init__()
    #Book()

    def __init__(self):
        self.users={} #Email address + User Object
        self.books={} #Book Object + number of readers
    def create_book(self,title,isbn):
        b = Book(title,isbn)
        return b
    def create_novel(self,title,author,isbn):
        f = Fiction(title,author,isbn)#(self,title,author,isbn)
        return f
    def create_non_fiction(self,title,subject,level,isbn):
        n = Non_Fiction(title,subject,level,isbn)
        return n
    def add_book_to_user(self, book, email, rating = None):
        if email in self.users:
            self.users[email].read_book(book,rating)
            # User.read_book(self,book,rating)
            if not rating==None:
                book.add_rating(rating)
            # Book.add_rating(self,rating)
            if book in self.books:
                self.books[book]=self.books[book]+1
            else:
                self.books[book]=1
        else:
            print("No user with email: {email}".format(email=email))
    def add_user(self, name, email, books_list = None):
        self.users[email] = User(name,email)
        #for book in books_list:
        #    TomeRater().add_book_to_user(book,email)
        if not (books_list == None):
            for book in books_list:
                #print (book)
                self.add_book_to_user(book,email)
    def print_catalog(self):
        for book in self.books:
            print(book)
    def print_users(self):
        for user in self.users:
            print(self.users[user])
    def get_most_read_book(self):
        most_read_book_name=None
        most_read_book_time=-float("inf")
        for k,v in self.books.items():
            if v >= most_read_book_time:
                most_read_book_time = v
                most_read_book_name = k
        return most_read_book_name
    def highest_rated_book(self):
        highest_rate = -float("inf")
        highest_rated_book_name = None
        for book in self.books:
            if book.get_average_rating() >= highest_rate:
                highest_rate = book.get_average_rating()
                highest_rated_book_name = book
        return highest_rated_book_name
    def most_positive_user(self):
        most_positive_rate = -float("inf")
        most_positive_user_name = None
        for email in self.users:
            if self.users[email].get_average_rating() >= most_positive_rate:
                most_positive_rate = self.users[email].get_average_rating()
                most_positive_user_name = self.users[email]
        return most_positive_user_name

# @Xukun LIU
