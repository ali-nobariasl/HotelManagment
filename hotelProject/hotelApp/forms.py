from django import forms

from hotelApp.models import Room, Book

class AvailabilityForm(forms.Form):

    categories = (
        ('stn','standard'),
        ('lux','luxury'),
        ('slx','superluxury'),
    )
    room_category  = forms. ChoiceField(choices = categories , required=True)
    check_in = forms.DateTimeField(
        required=True, input_formats=["%Y-%m-%dT%H:%M",])
    check_out = forms.DateTimeField(
        required=True, input_formats=["%Y-%m-%dT%H:%M",])


    #class Meta:
    #   model = Book
        #fields = "__all__"
    #    fields = ['room.category__in', 'checkin_date', 'checkout_date']



class BenefitForm(forms.ModelForm):
    class Meta:
        model = Book
        #fields = '__all__'
        fields = ['benefit',]