from django.shortcuts import render, redirect
from django.http import HttpResponse

# Home page for input
def home(request):
    if request.method == 'POST':
        try:
            a = int(request.POST.get('Num1'))
            b = int(request.POST.get('Num2'))
            op = request.POST.get('op').strip()  # Remove spaces

            if op == '+':
                result = a + b
            elif op == '-':
                result = a - b
            elif op == '*':
                result = a * b
            elif op == '/':
                result = a / b
            elif op == '%':
                result = a % b
            else:
                return render(request, 'home.html', {'error': 'Invalid Operator'})

            # ✅ Redirect to /hello with result as query parameter
            return redirect(f'/hello?result={result}')
        
        except:
            return render(request, 'home.html', {'error': 'Invalid input'})

    return render(request, 'home.html')

# ✅ Hello view to display the result
def hello(request):
    result = request.GET.get('result')
    return render(request, 'result.html', {'result': result})

