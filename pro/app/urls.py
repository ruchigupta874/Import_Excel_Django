from django.urls import path
from . import views

app_name = 'app'

urlpatterns=[
    path('filter', views.filter, name='filter'),
    #path('update/<int:pk>/',views.UpdateView.as_view(),name='update')
    #path('employee_list/', views.EmployeeListView.as_view(), name='employee_list'),
    path('employee_create/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('update_single/<int:pk>/', views.EmployeeUpdateView.as_view(), name='update_single'),
    path('employee_delete/<int:pk>/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
    path('employee_update/', views.update, name='update'),
    path('updated_record',views.updated_record,name='updated_record'),
    path('import_excel', views.import_sheet,name='import_excel'),

    #path('pub_update/<int:pk>/', views.PublisherUpdateView.as_view(), name='pub_update'),
]