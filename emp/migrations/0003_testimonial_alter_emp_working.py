# Generated by Django 4.2.2 on 2023-11-21 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0002_alter_emp_address_alter_emp_department_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('Testimonial', models.TextField(null=True)),
                ('picture', models.ImageField(null=True, upload_to='testimonials/')),
                ('rating', models.IntegerField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='emp',
            name='working',
            field=models.BooleanField(default=True),
        ),
    ]
