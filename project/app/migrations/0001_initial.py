# Generated by Django 5.0.1 on 2024-04-20 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int_field', models.IntegerField(default=0)),
                ('char_field', models.CharField(max_length=32, verbose_name='String')),
                ('txt_field', models.TextField()),
                ('choises_field', models.CharField(choices=[('SP', 'Sport'), ('CS', 'Cars')], default='SP', max_length=2)),
                ('time_field', models.DateTimeField(auto_now_add=True)),
                ('update_field', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
