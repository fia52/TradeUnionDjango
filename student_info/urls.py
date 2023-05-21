from django.urls import path
from . import views
from student_info.api.v1.views import StudentListCreateAPIView

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('add_student', views.AddStudentView.as_view()),
    path('get_all_students', views.ShowAllView.as_view()),
    path('update_student/<int:pk>', views.UpdateStudentView.as_view()),
    path('delete_student/<int:pk>', views.DeleteStudentView.as_view()),
    path('add_success', views.AddSuccessResultView.as_view()),
    path('update_success', views.UpdateSuccessResultView.as_view()),
    path('delete_success', views.DeleteSuccessStudentView.as_view()),
    path('load_data', views.LoadDataView.as_view()),
    path('find_student', views.FindStudentView.as_view()),
    path('delete_all', views.DeleteAllStudentView.as_view()),

    # Api
    path('api/v1/students', StudentListCreateAPIView.as_view())
]
