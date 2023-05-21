from rest_framework import generics

from student_info.models import Student
from student_info.serializers import StudentSerializer


class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        filters = self.request.query_params

        queryset = Student.objects.all()

        if 'profcard' in filters.keys():
            queryset = queryset.filter(profcard=filters['profcard'])
            print(queryset)

        if 'profcard' in

        return queryset


class StudentRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # lookup_field = "name"
