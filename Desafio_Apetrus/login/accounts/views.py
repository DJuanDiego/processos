from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
import csv

from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def indexView(request):
    return render(request, 'index.html')
'''
@login_required()
class DashboardView(View):
    def dashboardView(request):
        return render(request, 'dashboard.html', {})
'''

# Original
@login_required()
def dashboardView(request):
    return render(request, 'dashboard.html')

@login_required()
class DashboardView():
    def ques_1(request):
        with open('inputs/Q1_Ano.csv') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            with open('inputs/Q1_Ano.csv') as csvfile:
                plots = csv.reader(csvfile, delimiter=',')
                data = {
                    'data': [{
                        'year': item[0],
                        'value': item[1]
                    }
                        for item in plots
                    ]
                }
        return JsonResponse(data)

'''
@login_required()
class ChartData(APIView):
    def get(request, format=None):
        with open('inputs/Q1_Ano.csv') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            data = {
                'data': [{
                    'year':item[0],
                    'value':item[1]
                }
                    for item in plots
                ]
            }
        return Response(data)
'''


def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form':form})
