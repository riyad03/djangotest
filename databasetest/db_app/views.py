from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import MyUser
from .forms import BookForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("test")
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = MyUser.objects.get(username=username)
            if user.check_password(password):
                # Create session or token here
                request.session['user_id'] = user.id
                return redirect('home')
            else:
                return render(request, 'login.html', {'error': 'Invalid password'})
        except MyUser.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid username'})
    return render(request, 'login.html')

def home(request):
    # Your view logic here
    return render(request, 'home.html')

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('book_list')  # Assuming 'book_list' is the URL name for the view displaying the list of books
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})