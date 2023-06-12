from django.contrib import admin

# Register your models here.
from .models import User, Crush

# 注册 User 模型
admin.site.register(User)

# 注册 Crush 模型
admin.site.register(Crush)
