from django.urls import path


from . import views

urlpatterns = [
    path('<page_slug>/', views.get_page),
]
