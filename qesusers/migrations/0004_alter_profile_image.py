# Generated by Django 4.0.4 on 2022-04-13 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qesusers', '0003_alter_profile_image_alter_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pic'),
        ),
    ]
