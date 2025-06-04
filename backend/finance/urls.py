from django.urls import path
from .views import IncomeListCreateView, ExpenseListCreateView

urlpatterns = [
    path('incomes/', IncomeListCreateView.as_view(), name='income-list-create'),
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
]

from .views import register, login

urlpatterns += [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
]
