class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    #using __str__ we can return a string representation of the object when we print it directly to the console

    #we use __eq__ to check if 2 objects are equal
    # So with this, if we copied everything in book1 and pasted it in group2, it would output true, else false.

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

#What if we wanted to check if a group was greater than or lesser than another book,e.g we printed book 2 is less than group 3 (print book1 < book2) we would get an error saying "TypeError: '<' not supported between instances of 'Book' and 'Book'". So we can't use less than between two objects but we can customize that behavior by using dunder less than (__lt__):

    def __lt__(self, other):
        return self.num_pages < other.num_pages
#So after this, we should not get an error

#Another one is the greater than...:

    def __gt__(self, other):
        return self.num_pages > other.num_pages #And we get true as our output.

    #Similarly, if we tried to add, we would also get an error saying "typeerror unsupported operand type(s) for +: 'Book' and 'Book' and similarly, we can also customise this behaviour:

    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"

    #Within an object, we can also search for a keyword within one of the attributes.Let's find the word Lion within book3 we would write (print("Lion" in book3)): we would get an error saying "TypeError: argument of type 'Book' is not a container or iterable" but we can also customize this behavior

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    #We are searching for a keyword in an object.
    #
    # #Now we could search for a key giving an object.e.g if we normally typed "print(book1 ['title'])" we would get an error saying "TypeError: 'Book' object is not subscriptable." To customize this behaviour, we would use:

    def __getitem__(self, key):
        if key == "title":
           return self.title
    #We're accessing book attributes by indexing. With this object, (book1) return the value at this key "['title']."

    #what if the key is author, we get none cause we didn't set that up yet
        elif key == "author":
            return self.author

    #What about num_pages, we still would get none cause we're not set uo for that yet:
        elif key == "num_pages":
            return self.num_pages

    # Else if there is no matching key,
        else:
            return f"{key} was not found"


#Here are my three book objects. When we call teh class of books and pass in arguments, we will call the __init__ method. It's a magic method, it's automatically called behind the scenes.Within this magic methods, we can define and customize the behavior of objects and in this example, we're just assigning the attributes title,author, and num_pages. That is one built operation of python.



book1 = Book("The Hobbit", "J.R.R Tolken", 321)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S Lewis", 172)

#what would happen if we printed book one directly to the console e.g

#print(book3)
print(book3 ['mbappe'])

#   And well, those are magic methods in python.

