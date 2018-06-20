from django.db import models

# Create your models here.
# u  指定utf-8 编码
class UserMessgae(models.Model):
    name = models.CharField(max_length=20,null=True,blank=True,verbose_name=u'用户名')
    email = models.EmailField(verbose_name=u'邮箱')

    address = models.CharField(max_length=100,verbose_name=u'联系地址')
    message = models.CharField(max_length= 500,verbose_name=u'information')

    object_id= models.CharField(primary_key=True,max_length=50,default='',verbose_name='主键')

    # django 的类型
    # models.ForeignKey
    # models.DateTimeField
    # models.IntegerField

    class Meta:
        verbose_name = u'用户留言信息'
        verbose_name_plural = verbose_name
        db_table ='user_message'
        ordering =['-object_id']
