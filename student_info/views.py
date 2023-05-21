from django.db.models import F
from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView, ListView, UpdateView, DeleteView

from .models import Student
from .forms import StudentForm


class IndexView(TemplateView):
    template_name = 'student_info/index.html'


class AddStudentView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_info/student_form.html'
    success_url = '/add_success'


class ShowAllView(ListView):
    template_name = 'student_info/all_students.html'
    model = Student
    context_object_name = 'students'


class UpdateStudentView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_info/student_form.html'
    success_url = '/update_success'


class DeleteStudentView(DeleteView):
    model = Student
    success_url = '/delete_success'


class FindStudentView(View):
    def get(self, request):
        return render(request, 'student_info/find_student.html')

    def post(self, request):
        pole_name = request.POST['pole_name']
        value = request.POST['value']
        pole_value_dict = {pole_name: value}
        students = Student.objects.filter(**pole_value_dict)
        return render(request, 'student_info/all_students.html', context={'students': students})


class DeleteAllStudentView(View):
    pass

class AddSuccessResultView(TemplateView):
    template_name = 'student_info/add_success.html'


class UpdateSuccessResultView(TemplateView):
    template_name = 'student_info/update_success.html'


class DeleteSuccessStudentView(TemplateView):
    template_name = 'student_info/delete_success.html'


class LoadDataView(View):
    def get(self, request):
        return render(request, 'student_info/load_data.html')

    def post(self, request):
        for record in self.csv_parser(request.FILES['data']):
            new_line = Student(group=record['group'],
                               fio=record['fio'],
                               birthdate=record['birthdate'],
                               sex=record['sex'],
                               financing_form=record['financing_form'],
                               profcard=record['profcard'],
                               student_book=record['student_book'],
                               role=record['role'],
                               comment=record['comment'],
                               telegram_id=record['telegram_id'],
                               )
            new_line.save()
        return render(request, 'student_info/success_load.html')

    @staticmethod
    def csv_parser(file) -> list[dict]:
        data = str(file.read(), 'utf-8')
        data_list = []
        data_split = data.lstrip(';\n\r').replace('\r', '').split('\n')[1:-1]
        for string in data_split:
            student_data = [val if val else None for val in string.split(';')]
            parsed_student_data = {
                "group": student_data[2],
                "fio": student_data[3],
                "birthdate": student_data[4],
                "sex": student_data[5],
                "financing_form": student_data[6],
                "profcard": student_data[7],
                "student_book": student_data[8],
                "role": student_data[9],
                "comment": student_data[11],
                "telegram_id": student_data[12],
            }
            parsed_student_data = {
                key: val.strip() if type(val) == str else val
                for key, val in parsed_student_data.items()
            }
            data_list.append(parsed_student_data)
        return data_list

