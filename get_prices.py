from books import books

books_list = books.split('\n\n')

book_price = ''
file = open(r'book_prices.py', 'w')
for book in books_list:
    book_price = book.split(' ')[-2]
    print(book_price)
    file.write(f'{book_price}\n')
