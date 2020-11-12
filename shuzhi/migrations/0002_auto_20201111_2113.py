# Generated by Django 3.1.1 on 2020-11-11 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuzhi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addr',
            options={'verbose_name': '营区', 'verbose_name_plural': '营区'},
        ),
        migrations.AlterModelOptions(
            name='shuzhizhe',
            options={'ordering': ('order',), 'verbose_name': '述职者', 'verbose_name_plural': '述职者'},
        ),
        migrations.AddField(
            model_name='shuzhizhe',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, '未述职,前来述职'), (1, '未述职，以后述职'), (2, '述职完毕')], null=True),
        ),
        migrations.AlterField(
            model_name='addr',
            name='name',
            field=models.CharField(max_length=100, verbose_name='所属营区'),
        ),
        migrations.AlterField(
            model_name='shuzhizhe',
            name='intro',
            field=models.TextField(max_length=200, verbose_name='个人简介'),
        ),
        migrations.AlterField(
            model_name='shuzhizhe',
            name='name',
            field=models.CharField(max_length=50, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='shuzhizhe',
            name='order',
            field=models.IntegerField(blank=True, null=True, verbose_name='述职顺序'),
        ),
        migrations.AlterField(
            model_name='shuzhizhe',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photo/', verbose_name='证件照'),
        ),
    ]