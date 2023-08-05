# Generated by Django 4.2.2 on 2023-07-07 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoop', '0003_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepairProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='repairs/%Y/%m/%d/')),
            ],
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-id']},
        ),
    ]