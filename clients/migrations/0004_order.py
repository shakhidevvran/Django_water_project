# Generated by Django 4.1 on 2022-09-02 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_client_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания заказа')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='дата и время изменения заказа')),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('contacts', models.CharField(max_length=255)),
            ],
        ),
    ]