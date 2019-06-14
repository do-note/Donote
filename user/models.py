from django.db import models

# Create your models here.
from django.db import models

class Title(models.Model):
    title_id = models.AutoField(primary_key=True)
    title_name = models.CharField(max_length=30)

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=30)

class User(models.Model):
    username = models.CharField(max_length=30,verbose_name='用户名')
    fullname = models.CharField(max_length=30, verbose_name='姓名')
    gender = models.CharField(max_length=10,
                              choices=(('male','男'),('famale','女')),
                              default='male',
                              verbose_name='性别')
    email = models.EmailField(primary_key=True,verbose_name='邮箱')
    title = models.ForeignKey(Title,on_delete=False,verbose_name='职位')
    department = models.ForeignKey(Department,on_delete=False,verbose_name='部门')
    descrabe = models.CharField(max_length=500,verbose_name='个人介绍')
    reg_data = models.DateTimeField(verbose_name='注册日期')

