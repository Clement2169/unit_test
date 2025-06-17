import pytest
import library

def create_author ( name, my_books) :
    books = library.Books()
    for  book in my_books :
        books.add_book (book,name)
    return books

def add_author ( books, name, my_books) :
    for  book in my_books :
        books.add_book (book,name)

def test_add_book () :
    name= "clement"
    my_books = ["book1","book2","book3"]
    books = create_author(name,my_books)
    books.add_book("name","book1")
    assert(my_books == books.list_author_books(name))

def test_remove_book() :
    name= "clement"
    my_books = ["book1","book2","book3","book4"]
    expected_books = ["book1","book3","book4"]
    books = create_author(name,my_books)
    name1= "pierre"
    my_books1 = ["book1","book2","book4"]
    add_author (books,name1,my_books1)
    expected_books1 = ["book1","book4"]

    books.remove_book("book2")
    assert(expected_books == books.list_author_books(name))
    assert(expected_books1 == books.list_author_books(name1))


def test_list_books () :
    assert True

def test_list_author_books () :
    name= "clement"
    my_books = ["book1","book2","book3"]
    books = create_author(name,my_books)
    books.add_book("name","book1")
    assert(my_books == books.list_author_books(name))

def test_generate_stats () :
    name= "clement"
    my_books = ["book1","book2","book3","book4"]
    expected_books = ["book1","book3","book4"]
    books = create_author(name,my_books)
    name1= "pierre"
    my_books1 = ["book1","book2","book4"]
    add_author (books,name1,my_books1)
    expected_author = [name,name1]
    expected_len = len(my_books) + len(my_books1)
    number ,  authors = books.generate_stats ()
    assert(expected_author == list(authors))
    assert(expected_len == number)

