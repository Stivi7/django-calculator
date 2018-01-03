from django.shortcuts import render, redirect

# Create your views here.
context = {
    'result': 0,
}

def home(request):
    return render(request, 'calc/home.html', context)

def calculate(request):
    if (request.method == 'POST'):
        ex = request.POST['numField']
        print(ex)
        result = eval(ex)
        context['result'] = result
    return redirect('home')
