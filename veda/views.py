from django.shortcuts import render
from django.http import HttpResponse
from . import db
import json
import random
import requests
import time 

def index(request):
    return render(request, 'index.html')


def normal_login(request):
    return render(request, 'auth/login.html')

def dashboard(request):
    with open('veda/data/quotes.json') as file:
        quote = json.load(file)
    rand_int = random.randint(0,1000)
    return render(request, 'dashboard/board.html', {"quote_widget": True, "quote_text" : quote[rand_int]['text'], "quote_author" : quote[rand_int]['author']})

def planner(request):
    return render(request, 'planner/index.html')

def file_explorer(request):
    cursor, conn = db.connect()
    cursor.execute('SELECT * FROM FILES')
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]  # Get the column names
    data = []
    for row in rows:
        row_data = {}
        for i, column in enumerate(columns):
            row_data[column] = row[i]
        data.append(row_data)
    json_data = json.dumps(data)
    parsed_data = json.loads(json_data)
    
    return render(request, 'file-explorer/index.html', {"search_enabled": True, "quote_widget": False, "data": parsed_data})


def render_latex(request):
    if request.method == 'POST':
        equation = request.POST.get('equation', '')
        return render(request, 'components/render_latex.html', {'equation': equation, 'latex_enabled' : True})
    else:
        return render(request, 'components/render_latex.html',{'latex_enabled' : True})



def json_table_view(request):
    # Fetch JSON data from localhost:8080/getothers
    response = requests.get('http://localhost:8080/getothers')
    json_data = response.json()

    # Simulate a delay of 2 seconds
    time.sleep(2)

    # Render the table using Flowbite
    return render(request, 'table.html', {'data': json_data})


def paths_view(request):
    response = requests.get('http://localhost:8080/paths')
    print(response.content)  # Print the response content for debugging
    paths = response.json()
    return render(request, 'paths.html', {'paths': paths})


