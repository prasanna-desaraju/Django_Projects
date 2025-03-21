from django.shortcuts import render

def student_list(request):
    students = [
        {'Name': 'Alekhya', 'Marks': 85},
        {'Name': 'Bhavya', 'Marks': 35},
        {'Name': 'Charlie', 'Marks': 75},
        {'Name': 'Dhanvika', 'Marks': 90},
    ]
    passing_marks = 40  # Define passing marks threshold
    return render(request, 'reportapp/student_list.html', {'students': students, 'passing_marks': passing_marks})

