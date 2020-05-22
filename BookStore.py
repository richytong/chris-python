from functools import reduce

class Book:
    def __init__(self, _id, title, author, genre, price):
        self._id = _id
        self.title = title
        self.author = author
        self.genre = genre
        self.price = float(price)

    def __str__(self):
        return '''
    _______
   /      /, {title} (Item Number: {_id})
  /      //  {author}
 /______//   Genre: {genre}
(______(/    ${price}
        '''.format(**vars(self))
# vars - https://stackoverflow.com/questions/61517/python-dictionary-from-an-objects-fields

class Inventory:
    def __init__(self, books):
        self.bookMap = {}
        for book in books:
            self.add_book(book)

    def __str__(self):
        delim = '\n--------------------------------------------------------------'
        return delim + delim.join(map(str, self.bookMap.values())) + delim
# join - https://www.geeksforgeeks.org/join-function-python/
# map - https://www.geeksforgeeks.org/python-map-function/
# .values() - https://stackoverflow.com/questions/16228248/how-can-i-get-list-of-values-from-dict

    def add_book(self, book):
        'adds a book'
        self.bookMap[book._id] = book

    def get_book(self, book_id):
        'gets a book by _id'
        return self.bookMap[book_id]

    def clear(self):
        'clears all books from bookMap'
        self.bookMap = {}

    def display(self):
        print(str(self))

class Cart(Inventory):
    def checkout(self):
        total_price = reduce(
            lambda y, xi: y + xi.price,
            self.bookMap.values(),
            0
        )
        print('Total Price of Cart Items: ' + str(total_price))
        print('Thank you come again')
    # reduce: https://thepythonguru.com/python-builtin-functions/reduce/

    # note: I do not need to overload add_book from Inventory as instructed
    #       because I do not read in booklist.txt from Inventory.add_book

def parseBookLine(bookline):
    '"id,title,author,genre,price\n" -> Book(id, title, author, genre, price)'
    record = bookline.rstrip().split(',')
    return Book(*record)
# rstrip - https://stackoverflow.com/questions/275018/how-can-i-remove-a-trailing-newline
# split - turns a string into an array by "splitting" the string up based on delimiter ','

def parseBookSource(path):
    'booklist.txt -> [Book(...), Book(...), ...]'
    booklistRawText = open(path, 'r')
    books = []
    for line in booklistRawText:
        book = parseBookLine(line)
        books.append(book)
    booklistRawText.close()
    return books
# for line in: https://cmdlinetips.com/2011/08/three-ways-to-read-a-text-file-line-by-line-in-python/

def browse(inventory, cart):
    main_menu_selection = input('''
(1) Display books for sale
(2) Add to Cart
(3) Show cart
(4) Checkout
(5) Quit
> ''')
    if main_menu_selection == '1':
        inventory.display()
        browse(inventory, cart)
    elif main_menu_selection == '2':
        book_id = input('Which book would you like to buy? Please input Item Number: ')
        cart.add_book(inventory.get_book(book_id))
        browse(inventory, cart)
    elif main_menu_selection == '3':
        if len(cart.bookMap) == 0:
            print('Your cart is empty.')
        else:
            cart.display()
        browse(inventory, cart)
    elif main_menu_selection == '4':
        if len(cart.bookMap) == 0:
            print('Your cart is empty.')
        else:
            cart.checkout()
            cart.clear()
        browse(inventory, cart)
    elif main_menu_selection == '5':
        return
    else:
        print('Please input 1 - 5')
        browse(inventory, cart)

if __name__ == '__main__':
    books = parseBookSource('booklist.txt') # booklist.txt is in the same directory
    inventory = Inventory(books)
    cart = Cart([])
    browse(inventory, cart)
