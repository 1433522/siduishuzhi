from django.db import models

# Create your models here.

class Addr(models.Model):
    name = models.CharField("所属营区",max_length=100)

    class Meta:
        verbose_name = "营区"
        verbose_name_plural = "营区"

    def __str__(self):
        return self.name

class Shuzhizhe(models.Model):
    STATUS_CHOICES = (
            (0,'未述职，前来述职'),
            (1,'未述职，下次述职'),
            (2,'述职完毕'),
            )
    name = models.CharField("姓名",unique=True,max_length=50)
    intro = models.TextField("个人简介",max_length=200)
    addr = models.ForeignKey(Addr, on_delete=models.DO_NOTHING,blank=True, null=True,verbose_name="所属营区")
    photo = models.ImageField("证件照",upload_to='photo/',blank=True,null=True)
    status = models.IntegerField("状态",choices=STATUS_CHOICES,default=1,blank=True,null=True)

    class Meta:
        ordering = ('addr',)
        verbose_name = "述职者"
        verbose_name_plural = "述职者"

    def __str__(self):
        return self.name
