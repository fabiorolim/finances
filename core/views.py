from django.shortcuts import render
from core.models import Account
from django.http import HttpResponse
import csv


# Create your views here.
def home(request):
    accounts = Account.objects.all()
    return render(request, 'home.html', {'accounts': accounts})


def download_csv(request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="dados.csv"'
    query = Account.objects.values('id', 'account_data', 'description', 'value',
                                   'type', 'type_payment', 'category').all()
    fields = query.get(id=1).keys()
    writer = csv.DictWriter(response, fieldnames=fields)
    writer.writeheader()

    for data in query:
        writer.writerow(data)

    return response
