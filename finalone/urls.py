from django.contrib import admin
from django.urls import path, include

from finalone.views import  ImportExcelDataAPIView, SignInAPIView, SignupAPIView, UserCreateAPIView, UserDetailAPIView, UserUpdateAPIView,ExportUsersToExcelAPIView, UserDeleteAPIView, UserListView

urlpatterns = [
    path('signup/',SignupAPIView.as_view(), name='signup'),
    path('signin/',SignInAPIView.as_view(), name='signin'),
    path('user/create/', UserCreateAPIView.as_view(), name='user-create'),
    path('user/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('user/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('user/delete/<int:pk>/', UserDeleteAPIView.as_view(), name='user-delete'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('export-users/', ExportUsersToExcelAPIView.as_view(), name='export-users'),
    path('import-users/', ImportExcelDataAPIView.as_view(), name='import-users'),
    
]    

