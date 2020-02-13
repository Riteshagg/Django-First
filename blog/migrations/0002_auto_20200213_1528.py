# Generated by Django 3.0.2 on 2020-02-13 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Fname', models.CharField(max_length=233)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProQuantity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity_total', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.CharField(max_length=55),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['name'], name='name1'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['description'], name='description1'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['price'], name='price1'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['image'], name='image1'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['farmer_id'], name='farmer_id1'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['productCate_id'], name='productCate_id1'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['quantity'], name='quantity1'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='farmerId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Farmer'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='productid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Product'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='quantityid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.ProQuantity'),
        ),
        migrations.AddField(
            model_name='proquantity',
            name='farmerId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Farmer'),
        ),
        migrations.AddIndex(
            model_name='farmer',
            index=models.Index(fields=['Fname'], name='Farmer1'),
        ),
        migrations.AddIndex(
            model_name='farmer',
            index=models.Index(fields=['state'], name='state1'),
        ),
        migrations.AddIndex(
            model_name='farmer',
            index=models.Index(fields=['country'], name='country1'),
        ),
        migrations.AlterField(
            model_name='product',
            name='farmer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Farmer'),
        ),
        migrations.AddIndex(
            model_name='transaction',
            index=models.Index(fields=['quantityid'], name='quantity_id1'),
        ),
        migrations.AddIndex(
            model_name='transaction',
            index=models.Index(fields=['farmerId'], name='farmerId2'),
        ),
        migrations.AddIndex(
            model_name='transaction',
            index=models.Index(fields=['productid'], name='product_id1'),
        ),
        migrations.AddIndex(
            model_name='transaction',
            index=models.Index(fields=['status'], name='status'),
        ),
        migrations.AddIndex(
            model_name='proquantity',
            index=models.Index(fields=['quantity_total'], name='quantity_total1'),
        ),
        migrations.AddIndex(
            model_name='proquantity',
            index=models.Index(fields=['farmerId'], name='farmerId1'),
        ),
    ]
