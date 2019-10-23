from django.shortcuts import render, redirect
from django.core.mail import send_mail
from datetime import datetime

from .forms import ConfirmationForm
from .models import Table, RestaurantSpace, Visitor

# Create your views here.


def main_page(request):
    restaurant = RestaurantSpace.objects.all().first()
    all_tables = Table.objects.all()
    all_visitor = Visitor.objects.all()
    now = datetime.now()
    form = ConfirmationForm()
    context = {
        'restaurant': restaurant,
        'all_tables': all_tables,
        'all_visitor': all_visitor,
        'today': now.strftime('%d/%m/%Y'),
        'form': form,
    }
    return render(request, 'index.html', context)


def booking_table(request):
    form = ConfirmationForm(request.POST or None)
    if form.is_valid():
        receiver_email = form.cleaned_data['visitor_email']
        send_mail('Table confirmation',
                  'Dear - {}, Your table is - {}, date is - {}'.format(form.cleaned_data['visitor_name'],
                                                                       form.cleaned_data['visitor_table'],
                                                                       form.cleaned_data['visitor_table_date']),
                  'email_sender@gmail.com', [receiver_email],
                  fail_silently=False)
        form.save()
        return redirect('main')
    else:
        form = ConfirmationForm()
    context = {
        'form': form,
    }
    return render(request, 'index.html', context)
