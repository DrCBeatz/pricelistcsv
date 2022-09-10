from django.urls import path, reverse_lazy
from . import views
from django.conf.urls.static import static
from django.conf import settings

# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')

app_name='plc'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('upload_csv', views.upload_csv, name='upload_csv'),
    path('update_productlist_csv', views.update_productlist_csv, name='update_productlist_csv'),

    path('product_list/', views.ProductListView.as_view(), name='product_list'),
    path('product_list/create', views.ProductListCreateView.as_view(success_url=reverse_lazy('plc:product_list')), name='product_list_create'),
    path('product_list/<int:pk>', views.ProductListDetailView.as_view(), name='product_list_detail'),
    path('product_list/<int:pk>/update', views.ProductListUpdateView.as_view(success_url=reverse_lazy('plc:product_list')), name='product_list_update'),
    path('product_list/<int:pk>/delete', views.ProductListDeleteView.as_view(success_url=reverse_lazy('plc:product_list')), name='product_list_delete'),

    path('price_list/', views.PriceListView.as_view(), name='price_list'),
    path('price_list/create', views.PriceListCreateView.as_view(success_url=reverse_lazy('plc:price_list')), name='price_list_create'),
    path('price_list/<int:pk>', views.PriceListDetailView.as_view(), name='price_list_detail'),
    path('price_list/<int:pk>/update', views.PriceListUpdateView.as_view(success_url=reverse_lazy('plc:price_list')), name='price_list_update'),
    path('price_list/<int:pk>/delete', views.PriceListDeleteView.as_view(success_url=reverse_lazy('plc:price_list')), name='price_list_delete'),

    path('output_csv/', views.OutputCsvListView.as_view(), name='output_csv_list'),
    path('output_csv/create', views.OutputCsvCreateView.as_view(success_url=reverse_lazy('plc:output_csv_list')), name='output_csv_create'),
    path('output_csv/<int:pk>', views.OutputCsvDetailView.as_view(), name='output_csv_detail'),
    path('output_csv/<int:pk>/update', views.OutputCsvUpdateView.as_view(success_url=reverse_lazy('plc:output_csv_list')), name='output_csv_update'),
    path('output_csv/<int:pk>/delete', views.OutputCsvDeleteView.as_view(success_url=reverse_lazy('plc:output_csv_list')), name='output_csv_delete'),

    path('return_product_columns/<int:pk>', views.return_product_columns.as_view(), name='return_product_columns'),
    path('return_price_columns/<int:pk>', views.return_price_columns.as_view(), name='return_price_columns'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)