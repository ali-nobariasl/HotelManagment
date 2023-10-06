from  .models import Room, Book
from datetime import date, datetime, time




def check_availablity(room, checkin_date, checkout_date):
    
    avalible = []

    my_books = Book.objects.filter(room = room) 
    
    for my_book in my_books:
        if my_book.checkin_date > checkout_date or my_book.checkout_date < checkin_date:
            avalible.append(True)
        else:
            avalible.append(False)  
    
    return all(avalible)



