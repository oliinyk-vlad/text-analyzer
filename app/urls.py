from django.urls import path
from app.views import TextCreateView, TextListView, TextDetailView

app_name = 'texts'

urlpatterns = [
    path('', TextCreateView.as_view(), name='create'),
    path('all/', TextListView.as_view(), name='list'),
    path('<int:pk>/', TextDetailView.as_view(), name='detail'),
]
