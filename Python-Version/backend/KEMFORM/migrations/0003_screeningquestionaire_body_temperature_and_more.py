# Generated by Django 4.2.13 on 2024-06-16 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KEMFORM', '0002_remove_screeningquestionaire_hospitalizedd_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='screeningquestionaire',
            name='body_temperature',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('dont_know', "I don't know")], default=1, max_length=10, verbose_name='The patient has a measured fever greater than 38 ℃?'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='finaloutcome',
            name='final_outcome',
            field=models.CharField(choices=[('discharged_alive', 'Discharge from hospital alive'), ('death', 'Death'), ('refused_treatment', 'Refuse hospital tratment'), ('absconded', 'Absconded')], max_length=100),
        ),
        migrations.AlterField(
            model_name='screeningquestionaire',
            name='cough',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('dont_know', "I don't know")], max_length=10, verbose_name='Is the patient presenting with a cough?'),
        ),
        migrations.AlterField(
            model_name='screeningquestionaire',
            name='hospitalized',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('dont_know', "I don't know")], max_length=10, verbose_name='Has the patient been hospitalized?'),
        ),
        migrations.AlterField(
            model_name='screeningquestionaire',
            name='interview_type',
            field=models.CharField(choices=[('1', 'SARI surveillance'), ('2', 'Outbreak'), ('1', 'ILI surveillance')], max_length=100, verbose_name='What was the interview type?'),
        ),
        migrations.AlterField(
            model_name='screeningquestionaire',
            name='onset_date',
            field=models.DateField(verbose_name='Date of onset'),
        ),
        migrations.AlterField(
            model_name='screeningquestionaire',
            name='onset_of_symptoms',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('dont_know', "I don't know")], max_length=10, verbose_name='Was the onset of symptoms within the last 10 days?'),
        ),
    ]
