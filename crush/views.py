from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Crush, User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from django.utils import timezone
from django.http import JsonResponse, HttpResponseBadRequest
import json
from .models import User
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

# 用户登录视图
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            class_name = data['class_name']
            student_number = data['student_number']
            unique_id = data['unique_id']
        except (KeyError, json.JSONDecodeError):
            return HttpResponseBadRequest("Invalid request data")

        try:
            user = User.objects.get(class_no=class_name, student_no=student_number, unique_id=unique_id)
            if user is not None:
                # 更新 last_login 字段为当前时间
                user.last_login = timezone.now()
                user.save(update_fields=['last_login'])
                login(request, user)
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'error', 'message': '班別/號數/學生編號輸入錯誤-Invalid credentials'})
        except User.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': '班別/號數/學生編號輸入錯誤-Invalid credentials'})
    else:
        return JsonResponse({'status': 'error', 'message': '請求方式無效-Invalid request method'})
# 显示主页面
def home(request):
    if request.user.is_authenticated:
        # 显示已登录用户的主页面
        return JsonResponse({'status': 'success', 'message': 'Welcome to the home page'})
    else:
        # 重定向到登录页面
        return JsonResponse({'status': 'error', 'message': '請登入-Please log in'})
    
# 显示用户信息
@api_view(['GET'])
def get_user(request):
    if request.user.is_authenticated:
        return Response({'status': 'success', 'user': request.user.username})
    else:
        return Response({'status': 'error', 'message': 'Please log in'}, status=401)
    

# 添加暗恋关系
# 添加暗恋关系
@api_view(['POST'])
@csrf_exempt
def add_crush(request):
    print("Request user:", request.user)
    print("Request authenticated:", request.user.is_authenticated)
    if request.user.is_authenticated:
        data = json.loads(request.body)
        crush_class_name = request.data['class_name']
        crush_student_number = request.data['student_number']
        try:
            crush_user = User.objects.get(class_no=crush_class_name, student_no=crush_student_number)
            crush = Crush(crush=crush_user, user=request.user)
            crush.save()

            # 使用序列化器序列化数据
            serialized_crush = CrushSerializer(crush)
            return Response({'status': 'success', 'crush': serialized_crush.data})
        except User.DoesNotExist:
            return Response({'status': 'error', 'message': 'Crush not found'}, status=400)
    else:
        return Response({'status': 'error', 'message': 'Please log in'}, status=401)
# 显示暗恋关系
def get_crush_info(request):
    if request.user.is_authenticated:
        user = request.user
        admirers = Crush.objects.filter(crush=user)
        crushes = Crush.objects.filter(user=user)

        admirer_count = admirers.count()
        matches = []

        for crush in crushes:
            if crush.crush in [admirer.user for admirer in admirers]:
                crush_serializer = UserSerializer(crush.crush)
                matches.append(crush_serializer.data)

        return JsonResponse({
            'status': 'success',
            'admirer_count': admirer_count,
            'matches': matches,
        })

    else:
        return JsonResponse({'status': 'error', 'message': 'Please log in'})