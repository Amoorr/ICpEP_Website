"""

views.py is responsible for handling the user requests and displaying the corresponding outputs. 

"""


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .decorators import role_required

def login_view(request):
    """
    Function responsible for the log-in of the users. Asks for the credentials, then direct you
    to the corresponding page.
    """
    # Check if user is already authenticated
    if request.user.is_authenticated:
        # Redirect to the appropriate dashboard based on role
        if request.user.role == 'admin':
            return redirect('admin_dashboard')
        else:
            return redirect('student_dashboard')

    # Handle POST request for logging in
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password) # Checks if an account matches the credentials
            if user is not None: # If an account is present, log-in
                login(request, user)
                # Redirect to the appropriate dashboard
                if user.role == 'admin':
                    return redirect('admin_dashboard')
                else:
                    return redirect('student_dashboard')
            else:
                form.add_error(None, 'Invalid credentials')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def register(request):
    """
    Function responsible for registering an account and adding it to the database. 

    Note:
        1. It is a temporary function to create accounts seamlessly. WIll be transported to superuser soon
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user to the database
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = CustomUserCreationForm()  # Display an empty form for GET requests

    return render(request, 'accounts/register.html', {'form': form})

@login_required # Decorator where it is only accessed to logged-in users
def logout_view(request):
    """
    Responsible for logging out. Applicable to admins and students
    """
    logout(request)  # Logs out the user
    return redirect('login')  # Redirects to the login page


@login_required
@role_required('student') # Custom decorator where it is only accessed by student accounts
def student_dashboard(request):
    """
    Renders the student dashboard
    """
    return render(request, 'accounts/student_dashboard.html')

@login_required
@role_required('admin') # Custom decorator where it is only accessed by admin accounts
def admin_dashboard(request):
    """
    Renders the admin dashboard
    """
    # Render the admin dashboard page
    return render(request, 'accounts/admin_dashboard.html')


