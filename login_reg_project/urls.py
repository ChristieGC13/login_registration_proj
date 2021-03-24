from django.urls import path, include

urlpatterns = [
    path('', include('login_reg_app.routes')),
]