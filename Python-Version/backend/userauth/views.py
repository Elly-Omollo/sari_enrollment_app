from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# homepage
def index(request):

    return render(request, "app/index.html")

#     return HttpResponse(""" 
#         <!DOCTYPE html>
#         <html>
#                         <body style = "background-color:orange;">
#                             <h1 style='text-align:center;color:blue;'>this is the home page</h1>
#                         <p> this page says that you must login before you can continue</p>
#                         </body>
#         </html>

# """)

# loogin page
def login(request):
    # return HttpResponse("<h1 style='text-align:center;color:blue;'>this is the login page</h1>")
    return render(request, "login/login.html")




# creating account view
def signup(request):
    # return HttpResponse("<h1 style='text-align:center;color:blue;'>this is the account creation page</h1>")
    return render(request, "signup/signup.html")



# logout page
def logout(request):
    return HttpResponse("<h1 style='text-align:center;color:blue;'>You have just loged out. You can login again</h1>")

