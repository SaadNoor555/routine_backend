from rest_framework.response import Response
from rest_framework.decorators import api_view
import api
from api.serializers import PeriodSerializer
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.contrib.auth import authenticate
from base.models import Period
from django.contrib.auth.models import User

@api_view(['GET'])
def get_data(request):
    classes = Period.objects.all()
    serializer = PeriodSerializer(classes, many=True)
    print(serializer.data)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def addClass(request):
    serializer = PeriodSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print(serializer.data)
        return JsonResponse(serializer.data)

@api_view(['PUT'])
def updateClass(request):
    s_data = JSONParser().parse(request)
    serializer = PeriodSerializer(data=s_data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse('Error')

@api_view(['POST'])
def loginUser(request):
    print(request.data)
    username = request.data['username']
    password = request.data['pass1']

    user = authenticate(username=username, password=password)

    if user is not None: 
        print('hey')
        return JsonResponse(1, safe=False)
    else : 
        print('ney')
        return JsonResponse(0, safe=False)

@api_view(['POST'])
def signupUser(request):
    username = request.data['username']
    email = request.data['email']
    pass1 = request.data['pass1']
    myuser = User.objects.create_user(username, email, pass1)
    myuser.save()
    return JsonResponse(1)