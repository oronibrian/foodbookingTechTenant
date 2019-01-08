from django.urls import path
from.views import OrderCreateView
urlpatterns = [
    path('', OrderCreateView.as_view(),name='meal-create'),

    # path('<int:pk>', MealRUDView.as_view(),name='meal-rud')
]