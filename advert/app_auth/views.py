# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login, logout
# from django.urls import reverse_lazy

# def login_view(request):
#     redirect_url = reversed('profile')
#     if request.method == "GET":
#         if request.user.is_authenticated:
#             return redirect(redirect_url)
#         else:
#             return render(request< 'app_auth/login.html')
        
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username = username, password = password)
#     if user is not None:
#         login(request, user)
#         return redirect(redirect_url)
#     return render(request, 'app_auth/login.html', {'error': 'Пользователь не найден'})

# @login_required(login_url=reverse_lazy{'login'})




