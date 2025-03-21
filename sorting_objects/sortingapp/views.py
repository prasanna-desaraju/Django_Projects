from django.shortcuts import render, redirect 
from django.http import HttpResponse 
from .models import Person 
from faker import Faker   # type: ignore
import random 
 
def insert_rows(request): 
    fake = Faker() 
    for _ in range(5): 
        Person.objects.create( 
            name=fake.name(), 
            age=random.randint(18, 80), 
            email=fake.email() 
        ) 
    return HttpResponse("5 records inserted successfully.") 
 
def person_list(request): 
    sort_by = request.GET.get('sort',"") 
    order = request.GET.get('order',"") 
 
    valid_sort_fields = ['name', 'age', 'email'] 
 
    if sort_by not in valid_sort_fields: 
        sort_by='name' 
 
    if order == "desc": 
        sort_by = f"-{sort_by}" 
 
    persons = Person.objects.all().order_by(sort_by) 
    return render(request, 'person_list.html',{'persons': persons, 'sort_by': sort_by, 'order': 
order})