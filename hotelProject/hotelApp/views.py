from django.shortcuts import render,redirect
from django.contrib import messages
from datetime import date, datetime, time

from hotelApp.helperfunctions import check_availablity
from hotelApp.models import Room, Book
from hotelApp.forms import AvailabilityForm , BenefitForm



def home(request):
    rooms = Room.objects.all()
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        avail_room_list =[]
        if form.is_valid():
            data = form.cleaned_data
            room_list = Room.objects.filter(category = data['room_category'])
            
            for room in room_list:
                if check_availablity(room, data['check_in'], data['check_out']):
                    avail_room_list.append(room)
            
            if len(avail_room_list)> 0 :
                room = avail_room_list[0]
                book = Book.objects.create(
                    user = request.user,
                    room = room,
                    checkin_date = data['check_in'],
                    checkout_date = data['check_out'],
                )
                book.save()
                messages.success(request,'You booked successfully')  
                return redirect('bookList')
        else:
            print('invalid form')    
    else:
        
        form = AvailabilityForm()
    
    
    context ={
        'rooms':rooms,
        'form': form,
    }
    return render(request, 'home.html', context= context )


def roomList(request):
    
    rooms = Room.objects.all()
    context = {
        'rooms':rooms,
    }
    return render(request, 'roomslist.html',context= context)



def bookList(request):
    
    books = Book.objects.filter(user= request.user)
    context = {
        'books':books,
    }
    return render(request, 'booklist.html',context= context)



def roomDetails(request, pk):
    
    room = Room.objects.get(pk=pk)
    context = {
        'room' : room,
    }
    return render(request, 'roomdetail.html', context= context)


def booking(request):
    
    return render(request,'booking.html')
    

def deleteBook(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('bookList')


def addBenefit(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BenefitForm(request.POST)
        if form.is_valid():
            print('valid')
            book.benefit = form.cleaned_data['benefit']
            print(form.cleaned_data['benefit'])
            book.save()
            print('saved')
            messages.success(request,'You added extra benefit to your room')  
            return redirect('bookList')        
    else:
        form = BenefitForm()

    context = {
        'book': book,
        'form': form,
    }
    return render(request, 'bookdetail.html', context= context)


