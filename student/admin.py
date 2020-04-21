from django.contrib import admin
from .models import Student, Teacher, Paper, Question, Grade
# Register your models here.

# 修改名称
admin.site.site_header = '在线考试系统后台'
admin.site.site_title = '在线考试系统'

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'dept', 'major', 'password', 'email', 'birth')  # 显示那些信息
    list_display_links = ('id', 'name')  # 规定点击哪些信息可以进入编辑页面
    search_fields = ['name', 'dept', 'major', 'birth']  # 指定要搜索的字段，会出席那搜索框
    list_filter = ['name', 'dept', 'major', 'birth']  # 指定列表过滤器

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'dept', 'password', 'email', 'birth')
    list_display_links = ('id', 'name')
    search_fields = ['name', 'dept', 'birth']
    list_filter = ['name','dept']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','subject','title','optionA','optionB','optionC','optionD','answer','level','score')
