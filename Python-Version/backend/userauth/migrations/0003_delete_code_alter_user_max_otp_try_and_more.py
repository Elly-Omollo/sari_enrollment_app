# Generated by Django 4.2.13 on 2024-06-16 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0002_code_user_max_otp_try_user_otp_expiry_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='code',
        ),
        migrations.AlterField(
            model_name='user',
            name='max_otp_try',
            field=models.CharField(default=3, max_length=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='otp_expiry',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
