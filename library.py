class  Books () :

    def __init__ (self) :
        self.books_ = {}

    def add_book(self,title:str,author:str) :
        if  author not in self.books_.keys() :
            print (f"add author {author}")
            self.books_[author] = []
        if title not in self.books_[author] :
            self.books_[author].append(title)

    def remove_book(self,title:str) :
        for author in  self.books_.keys() :
            if title in self.books_[author] :
                self.books_[author].remove(title)
        return

    def list_books ( self) :
        return  self.books_

    def list_author_books ( self, author) :
        if author in self.books_ :
            return self.books_[author]
        return []

    def generate_stats ( self) :
        books= 0
        for key in self.books_ :
            books +=  len(self.books_[key])
        return books, self.books_.keys()
