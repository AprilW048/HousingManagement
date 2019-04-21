# Generated by Django 2.1.7 on 2019-04-20 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('admin_id', models.IntegerField(primary_key=True, serialize=False)),
                ('admin_username', models.CharField(max_length=20)),
                ('admin_pwd', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='amenity',
            fields=[
                ('amenity_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('amenity_type', models.CharField(max_length=30)),
                ('amenity_capacity', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='lease',
            fields=[
                ('lease_id', models.AutoField(primary_key=True, serialize=False)),
                ('rent_fee', models.FloatField(default=0.0)),
                ('movein_date', models.DateField(null=True)),
                ('moveout_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='maintenance',
            fields=[
                ('maintenance_id', models.AutoField(primary_key=True, serialize=False)),
                ('apply_date', models.DateField(null=True)),
                ('maintenance_location', models.CharField(max_length=50, null=True)),
                ('maintenance_category', models.CharField(max_length=50, null=True)),
                ('maintenance_describe', models.CharField(max_length=500)),
                ('maintenance_status', models.CharField(default='Submitted', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fee', models.FloatField(default=0.0)),
                ('pay_date', models.DateField(null=True)),
                ('payment_type', models.CharField(max_length=50)),
                ('pay_record', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_subject', models.CharField(max_length=100)),
                ('post_message', models.CharField(max_length=500)),
                ('post_img', models.ImageField(upload_to='image/')),
                ('post_date', models.DateTimeField(null=True)),
                ('post_tag', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='renter',
            fields=[
                ('renter_id', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('renter_pwd', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=20)),
                ('carplate', models.CharField(max_length=20, null=True)),
                ('balance', models.FloatField(default=0.0)),
                ('birthday', models.DateField(max_length=50, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='reply',
            fields=[
                ('reply_id', models.AutoField(primary_key=True, serialize=False)),
                ('reply_subject', models.CharField(max_length=100)),
                ('reply_message', models.CharField(max_length=500)),
                ('reply_img', models.ImageField(upload_to='image/')),
                ('reply_date', models.DateTimeField(null=True)),
                ('parent_reply', models.IntegerField(null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='housing.post')),
                ('renter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='housing.renter')),
            ],
        ),
        migrations.CreateModel(
            name='reservation',
            fields=[
                ('reservation_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField(null=True)),
                ('start_time', models.CharField(max_length=50, null=True)),
                ('reserve_date', models.DateField(null=True)),
                ('Amenity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='housing.amenity')),
                ('Renter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='housing.renter')),
            ],
        ),
        migrations.CreateModel(
            name='room',
            fields=[
                ('room_number', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('room_type', models.CharField(max_length=5)),
                ('room_description', models.CharField(max_length=500, null=True)),
                ('room_status', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='renter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='housing.renter'),
        ),
        migrations.AddField(
            model_name='payment',
            name='renter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='housing.renter'),
        ),
        migrations.AddField(
            model_name='payment',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='housing.room'),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='renter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='housing.renter'),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='housing.room'),
        ),
        migrations.AddField(
            model_name='lease',
            name='renter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='housing.renter'),
        ),
        migrations.AddField(
            model_name='lease',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='housing.room'),
        ),
    ]