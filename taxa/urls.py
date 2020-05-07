from django.urls import path


from . import views

urlpatterns = [
    path('findTaxaByFilter/', views.get_taxa_by_filter),
    path('findTaxaByName/', views.get_taxa_by_name),
    path('findTaxaByParent/', views.get_taxa_by_parent),
    path('taxa/<int:aphia_id>/', views.get_taxon),
    path('taxa/', views.get_taxa),
]
