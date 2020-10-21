from django.shortcuts import render, redirect
from .models import Documents, Contract, Timing
from .forms import ContractForm, TimingForm, DocumentsForm, DeliveryDocumentsForm
from django.core.mail import send_mail
user_email = 'hhh'
cal_form = {'date': '',
            'title': ''}


def parse_date(date):
    return date[:4] + date[5:7] + date[8:10]


def index(request):
    contracts = Contract.objects.filter(email=user_email)
    documents = Documents.objects.filter(email=user_email)
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'documents': documents,
                                               'user': user_email, 'contracts': contracts})


def about(request):
    return render(request, 'main/about.html')


def create_contract(request):
    form = ContractForm()
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'main/create_contract.html', context)


def update_contract(request, pk):
    contract = Contract.objects.get(id=pk)
    form = ContractForm(instance=contract)

    if request.method == 'POST':
        form = ContractForm(request.POST, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form, 'contract': contract}
    return render(request, 'main/create_contract.html', context)


def delete_contract(request, pk):
    contract = Contract.objects.get(id=pk)
    if request.method == "POST":
        contract.delete()
        return redirect('/')

    context = {'item': contract}
    return render(request, 'main/delete_contract.html', context)


def create_timing(request):
    form = TimingForm()
    if request.method == 'POST':
        form = TimingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'main/create_timing.html', context)


def update_timing(request, kek):
    timing = Timing.objects.get(id=kek)
    form = TimingForm(instance=timing)

    if request.method == 'POST':
        form = TimingForm(request.POST, instance=timing)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'main/create_timing.html', context)


def delete_timing(request, kek):
    timing = Timing.objects.get(id=kek)
    if request.method == "POST":
        timing.delete()
        return redirect('/')

    context = {'item': timing}
    return render(request, 'main/delete_timing.html', context)


def table(request, contract_id):
    contract = Contract.objects.get(id=contract_id)
    timing = contract.timing_set.all()

    context = {'title': 'Сроки договора', 'contract': contract, 'timing': timing}
    return render(request, 'main/table.html', context)


def create_delivery_contract(request):
    error = ''
    if request.method == 'POST':
        form = DeliveryDocumentsForm(request.POST)
        if form.is_valid():
            form.save()
            print('------------ALL OK')
            return redirect('add_calendar')
        else:
            error = 'Форма была неверной'

    form = DeliveryDocumentsForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_delivery_contract.html', context)


def create_doc(request):
    error = ''
    if request.method == 'POST':
        form = DocumentsForm(request.POST)
        if form.is_valid():
            form.save()
            cal_form['date'] = form['term']
            cal_form['title'] = form['name_of_the_organization'].value()
            print('------------ALL OK', form['term'].value())
            title = form['name_of_the_organization'].value()
            start_data = parse_date(form['term'].value()) + 'T100000Z'
            end_data = parse_date(form['term'].value()) + 'T200000Z'
            send_link = 'http://www.google.com/calendar/event?action=TEMPLATE&text=' + title + '&dates=' + start_data + '/' + end_data + '&details=Event%20Details%20Here&location=123%20Main%20St%2C%20Example%2C%20NY'
            send_mail(
                'Test',
                send_link,
                'zhbogdanov@mail.ru',
                ['zhbogdanov90@gmail.com'],
                fail_silently=False,
            )
            return redirect('add_calendar')
        else:
            error = 'Форма была неверной'

    form = DocumentsForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def add_calendar(request):
    data = cal_form['date']
    title = cal_form['title']
    return render(request, 'main/index.html', {'date_atributes': data,
                                               'title_atributes': title})
