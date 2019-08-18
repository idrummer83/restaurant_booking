from django.shortcuts import render, redirect
from django.core.mail import send_mail


from .forms import DateForm, ConfirmationForm
from .models import Table

# Create your views here.

def main_page(request):
    all_tables = Table.objects.all()
    context = {
        'all_tables': all_tables
    }
    return render(request, 'index.html', context)


def form_table(request, pk):
    all_tables = Table.objects.all()
    table = Table.objects.filter(id=pk).first()
    form = DateForm(request.POST or None, instance=table)
    if form.is_valid():
        table.table_number = table.table_number
        form.save()
        return redirect('/confirm/{}'.format(pk))
    context = {
        'form': form,
        'all_tables': all_tables
    }
    return render(request, 'form.html', context)


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