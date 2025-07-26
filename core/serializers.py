from rest_framework import serializers
from .models import Category , Lesson,Course ,Meterial,Enrollment,QuestionAnsware


class CategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model=Category
        fields ='__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta: 
        model=Course
        fields ='__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta: 
        model=Lesson
        fields ='__all__'

class MeterialSerializer(serializers.ModelSerializer):
    class Meta: 
        model=Meterial
        fields ='__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta: 
        model=Enrollment
        fields ='__all__'
        
class QuestionAnswareSerializer(serializers.ModelSerializer):
    class Meta: 
        model=QuestionAnsware
        fields ='__all__'