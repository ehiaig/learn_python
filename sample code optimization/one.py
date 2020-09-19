import time
import pandas as pd
import numpy as np
"""
Here's the code your coworker wrote to find the common book ids in books_published_last_two_years.txt and all_coding_books.txt to obtain a list of recent coding books.
"""
with open('books_published_last_two_years.txt') as f:
    recent_books = f.read().split('\n')
    
with open('all_coding_books.txt') as f:
    coding_books = f.read().split('\n')

    start = time.time()
recent_coding_books = []

for book in recent_books:
    if book in coding_books:
        recent_coding_books.append(book)

print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))

"""
Tip #1: Use vector operations over loops when possible

Use numpy's intersect1d method to get the intersection of the recent_books and coding_books arrays.
"""

start = time.time()

recent_books = pd.read_csv('books_published_last_two_years.txt', sep="\n", header=None)
coding_books = pd.read_csv('all_coding_books.txt', sep="\n", header=None)
recent_coding_books = np.intersect1d(recent_books, coding_books)

print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))

"""Tip #2: Know your data structures and which methods are faster

Use the set's intersection method to get the common elements in recent_books and coding_books.
"""
start = time.time()

recent_coding_books = set(recent_books).intersection(coding_books)
print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))


