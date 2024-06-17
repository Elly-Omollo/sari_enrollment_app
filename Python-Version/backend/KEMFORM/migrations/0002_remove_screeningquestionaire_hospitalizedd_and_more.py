# Generated by Django 4.2.13 on 2024-06-16 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KEMFORM', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='screeningquestionaire',
            name='hospitalizedd',
        ),
        migrations.AddField(
            model_name='screeningquestionaire',
            name='hospitalized',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('dont_know', "I don't know")], default=1, max_length=10, verbose_name='Did the patient report a history of fever?'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='screeningquestionaire',
            name='cough',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('dont_know', "I don't know")], max_length=10, verbose_name='Did the patient report a history of fever?'),
        ),
        migrations.AlterField(
            model_name='screeningquestionaire',
            name='history_of_fever_report',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('dont_know', "I don't know")], max_length=10, verbose_name='Did the patient report a history of fever?'),
        ),
        migrations.AlterField(
            model_name='screeningquestionaire',
            name='onset_of_symptoms',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('dont_know', "I don't know")], max_length=10, verbose_name='Did the patient report a history of fever?'),
        ),
    ]