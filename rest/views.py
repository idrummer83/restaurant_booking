from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.db.models import Prefetch
from datetime import datetime

from .forms import DateForm, ConfirmationForm
from .models import Table, RestaurantSpace, Visitor

# Create your views here.


def main_page(request):
    restaurant = RestaurantSpace.objects.all().first()
    # all_tables = Table.objects.prefetch_related(Prefetch('visitor_table', Visitor.objects.all()))
    all_tables = Table.objects.all()
    all_visitor = Visitor.objects.all()
    # all_tables = Visitor.objects.prefetch_related(Prefetch('visitor_table', Table.objects.all()))
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


def booking_table(request, pk):
    # all_tables = Table.objects.all()
    table = Table.objects.filter(id=pk).first()
    form = ConfirmationForm(request.POST or None, instance=table)

    if form.is_valid():
        visitor_table = form.cleaned_data['visitor_table']
        visitor_table_date = form.cleaned_data['visitor_table_date']
        visitor_name = form.cleaned_data['visitor_name']
        visitor_email = form.cleaned_data['visitor_email']

        q = Visitor(visitor_table=visitor_table, visitor_table_date=visitor_table_date, visitor_name=visitor_name, visitor_email=visitor_email)
        q.save()
        return redirect('/confirm/{}'.format(pk))
    else:
        form = ConfirmationForm()
    context = {
        'form': form,
        # 'all_tables': all_tables
    }
    return render(request, 'index.html', context)


def email_confirmation(request, pk):
    table = Table.objects.filter(id=pk).first()
    if request.method == 'POST':
        form = ConfirmationForm(request.POST or None)
        if form.is_valid():
            receiver_email = form.cleaned_data['visitor_email']
            send_mail('Table confirmation',
                      'Your table is - {}, date is - {}'.format(table.table_number, table.table_date),
                      'email_sender@gmail.com', [receiver_email],
                      fail_silently=False)
            form.save()
            return redirect('/')
    else:
        form = ConfirmationForm()
        context = {
            'form': form,
            'table_id': pk
        }
        return render(request, 'email_confirmation.html', context)


# def form_table(request, pk):
#     all_tables = Table.objects.all()
#     table = Table.objects.filter(id=pk).first()
#     form = DateForm(request.POST or None, instance=table)
#     if form.is_valid():
#         table.table_number = table.table_number
#         form.save()
#         return redirect('/confirm/{}'.format(pk))
#     context = {
#         'form': form,
#         'all_tables': all_tables
#     }
#     return render(request, 'form.html', context)
