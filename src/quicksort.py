from book import Book
import time
import csv

# def internal(array)
#     less = []
#     equal = []
#     greater = []
#     if len(array) > 1:
#         pivot = array[0]
#         for x.genre in array:
#             if x.genre < pivot.genre:
#                 less.append(x)
#             elif x.genre == pivot.genre:
#                 equal.append(x)
#             else x.genre > pivot.genre:
#                 greater.append(x)
#         # Don't forget to return something!
#         return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
#     # Note that you want equal ^^^^^ not pivot
#     else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
#         return array

# def quick_sort( books ):
#     stack = []
#     # left = []
#     # right = []

#     stack.insert(0, books)
#     internal(stack)

#     return 0

    # internal(stack)
    # partition

    # def sort(array=[12,4,5,6,7,3,1,15]):




#     while len(stack) > 0:
#         current = stack.pop(0)
#         if isinstance(current, object):
#             books.insert(0, current)
#         elif current != None:
#             pivot = current.pop(0)
#             while len(current) > 0:
#                 if current[0].genre < pivot.genre:
#                     # move to LHS 
#                     left.append(current.pop(0))
#                 elif current[0].genre > pivot.genre:
#                     # move to RHS
#                     right.append(current.pop(0))
                
#             # Quick Sort LHS, RHS
#             if len(right) > 0:
#                 stack.insert(0, right)
#             stack.insert(0, pivot)
#             if len(left) > 0:
#                 stack.insert(0, left)
#             # print("*"+str(len(current)))

#     return books

# Read in book data from CSV file
# provided by https://github.com/uchidalab/book-dataset
with open('book_data.csv') as csvfile:
    my_books = []
    data = csv.DictReader(csvfile)
    for book in data:
        #print(book['title'], book['author'], book['genre'])
        my_books.append(Book(book['title'], book['author'], book['genre']))

start = time.time()
sorted_books = quick_sort(my_books)
end = time.time()
print("Quick Sort took:      " + str((end - start)*1000) + " milliseconds")

for book in my_books:
    print("-" + str(book))
print("\n***SORTED books***")