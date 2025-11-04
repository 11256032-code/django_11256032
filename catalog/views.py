from django.shortcuts import render

def whoaml(request):
    context = {
        'student_name': '蔡承芸',
        'student_id': '11256032',
    }
    return render(request, 'whoaml.html', context)