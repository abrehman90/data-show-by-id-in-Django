# Generated by Django 3.2.5 on 2021-09-03 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceProgressModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InvoiceTypes', models.CharField(choices=[('F&D', 'Feasibility & Designs'), ('Cons', 'Consultancy'), ('Op', 'Operation')], default='Cons', max_length=5)),
                ('InvAmount', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='QuotationProgressModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QuotAmount', models.CharField(max_length=50)),
                ('QuotClientName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ReportProgressModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProjectID', models.CharField(max_length=12)),
                ('Location', models.CharField(max_length=100)),
                ('ProjectName', models.CharField(max_length=50)),
                ('NoOfBH', models.CharField(max_length=10)),
                ('DepthOfBH', models.CharField(max_length=20)),
                ('Drilling_Method', models.CharField(max_length=50)),
                ('DateOfDrilling', models.DateTimeField(auto_now=True)),
                ('ReportingOfficer', models.CharField(max_length=50)),
                ('SubmittedTo', models.CharField(max_length=50)),
                ('GroundWaterTableDepth', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='progressmodel',
            name='DateOfDrilling',
        ),
        migrations.RemoveField(
            model_name='progressmodel',
            name='DepthOfBH',
        ),
        migrations.RemoveField(
            model_name='progressmodel',
            name='Drilling_Method',
        ),
        migrations.RemoveField(
            model_name='progressmodel',
            name='GroundWaterTableDepth',
        ),
        migrations.RemoveField(
            model_name='progressmodel',
            name='InvAmount',
        ),
        migrations.RemoveField(
            model_name='progressmodel',
            name='InvoiceTypes',
        ),
        migrations.RemoveField(
            model_name='progressmodel',
            name='Location',
        ),
        migrations.RemoveField(
            model_name='progressmodel',
            name='NoOfBH',
        ),
        migrations.RemoveField(
            model_name='progressmodel',
            name='ProjectID',
        ),
        migrations.RemoveField(
            model_name='progressmodel',
            name='ProjectName',
        ),
        migrations.RemoveField(
            model_name='progressmodel',
            name='QuotAmount',
        ),
        migrations.RemoveField(
            model_name='progressmodel',
            name='QuotClientName',
        ),
        migrations.RemoveField(
            model_name='progressmodel',
            name='ReportingOfficer',
        ),
        migrations.RemoveField(
            model_name='progressmodel',
            name='SubmittedTo',
        ),
    ]