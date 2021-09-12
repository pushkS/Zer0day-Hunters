# Generated by Django 3.1.4 on 2021-04-08 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210408_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='static/img/')),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='career',
            name='category',
        ),
        migrations.RemoveField(
            model_name='career',
            name='image',
        ),
        migrations.AddField(
            model_name='career',
            name='contents',
            field=models.TextField(blank=True),
        ),
    ]
