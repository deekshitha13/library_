list1 = ["To Kill a Mockingbird","1984","Harry Potter and the Philosopher's Stone","The Lord of the Rings","The Great Gatsby",
         "Pride and Prejudice","The Diary Of A Young Girl","The Hobbit"]
class Deeshu:
    _dict1 = {}
    def display(self,list):
        return list
    def lend(self,listing):
        print(listing)
        book = input("Enter the name of book which you want to take")
        name = input("Enter your name")
        if book in list1:
            print(f"the book {book} belongs to you now {name}")
            self._dict1[name] = book
            listing.remove(book)
            print(self._dict1)
            print(listing)
        else :
            for key,value in self._dict1.items():
                if value == book:
                    print(f"the book {value} is not present with us. It is with {key} ")
    def add(self,list):
        a = input("PLease name the book which you want to give away")
        list.append(a)
        print(list)
    def returning(self,list):
        b = input("PLease name the book which you want to return")
        c = input("Please enter your registered name")
        list.append(b)
        del self._dict1[c]
        print(list)
        print(self._dict1)

Deeshu_library = Deeshu()
while (True):
    print(
        "What do you want to do : \n"
        "If you want to 'DISPLAY' please enter d\n"
        "If you want to 'LEND' please enter l\n"
        "If you want to 'ADD' please enter a\n"
        " If you want to 'RETURN' please enter r ")
    ask_us = input()
    if ask_us == "d":
        print(Deeshu_library.display(list1))
    elif ask_us == "l":
        Deeshu_library.lend(list1)
    elif ask_us == "a":
        Deeshu_library.add(list1)
    elif ask_us == "r":
        Deeshu_library.returning(list1)
    else:
        print("error not found")