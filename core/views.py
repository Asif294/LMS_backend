from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Category,Course,Lesson,Enrollment,QuestionAnsware,Meterial
from .serializers import CategorySerializer,CourseSerializer,LessonSerializer,EnrollmentSerializer,MeterialSerializer,QuestionAnswareSerializer

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def Category_list_create(request):
    if request.method == 'GET':
        categoryes=Category.objects.all()
        serializer=CategorySerializer(categoryes,many=True)
        return Response (serializer.data)
    elif request.method == 'POST':
        if request.user.role != 'admin':
            return Response ({'detail' : "Only admin can create categories"}, status=403)
        serializer =CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def Course_list_create(request):
    if request.method == 'GET':
        if request.user.role in ['admin','student']:
            courses=Course.objects.all()
        elif request.user.role == 'teacher':
            courses=Course.objects.filter(instructor_id=request.user)
        else:
            return Response({'detail' :"Unauthorized user"},status=status.HTTP_403_FORBIDDEN)
        serializer =CourseSerializer(courses,many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        if request.user.role != 'teacher':
            return Response ({'detail' : "Only teacher can create course"}, status=403)
        serializer =CourseSerializer(instructor_id=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT','DELETE'])
@permission_classes([IsAuthenticated])
def course_details(request,pk):
    try:
        course =Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response ({'details':'Course not found'},status=status.HTTP_404_NOT_FOUND)
    if request.method =="GET":
        if request.user.role=='admin' or request.user ==course.instructor_id:
            serializer=CourseSerializer(course)
            return Response (serializer.data)
        return Response({'details':'Permission denined !!'},status=status.HTTP_403_FORBIDDEN)
    
    elif request.method =="PUT":
        if request.user.role != 'teacher' or request.user !=course.instructor_id:
            return Response({'details' :'Only course can access thsi course '},status=status.HTTP_403_FORBIDDEN)
        serializer=CourseSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.save(instructor_id=request.data)
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method =="DELETE":
        if request.user.role != 'teacher' or request.user !=course.instructor_id:
            return Response({'details' :'Only course can access thsi course '},status=status.HTTP_403_FORBIDDEN)
        serializer=CourseSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.save(instructor_id=request.data)
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#lessone create 
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def Lessone_list_create(request):
    if request.method == 'GET':
        categoryes=Lesson.objects.all()
        serializer=LessonSerializer(categoryes,many=True)
        return Response (serializer.data)
    elif request.method == 'POST':
        serializer =LessonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#meterial seaction
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def Meterial_list_create(request):
    if request.method == 'GET':
        categoryes=Meterial.objects.all()
        serializer=MeterialSerializer(categoryes,many=True)
        return Response (serializer.data)
    elif request.method == 'POST':
        serializer =MeterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#Enrollment Section
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def Enrollment_list_create(request):
    if request.method == 'GET':
        categoryes=Enrollment.objects.all()
        serializer=EnrollmentSerializer(categoryes,many=True)
        return Response (serializer.data)
    elif request.method == 'POST':
        serializer =EnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# Question Answer 
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def QuastionAnswer_list_create(request):
    if request.method == 'GET':
        categoryes=QuestionAnsware.objects.all()
        serializer=QuestionAnswareSerializer(categoryes,many=True)
        return Response (serializer.data)
    elif request.method == 'POST':
        serializer =QuestionAnswareSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)