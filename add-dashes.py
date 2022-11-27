book_titles = """
Leila Fletcher Piano Course Book 1
Leila Fletcher Piano Course Book 2
Leila Fletcher Piano Course Book 3
Leila Fletcher Piano Course Book 4
Leila Fletcher Piano Course Book 5
Leila Fletcher Piano Course Book 6
"""

# for i in range(1, 11):
#     print(f'Celebration Series Piano Etudes Level {i} 6th Edition'.lower().replace(' ', '-'))

book_titles_split = book_titles.split('\n')
for book in book_titles_split:
    print(book.lower().replace(' ', '-').replace("'", ''))