# Generated by Django 4.2 on 2023-04-08 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseBill',
            fields=[
                ('bill', models.AutoField(primary_key=True, serialize=False)),
                ('purchase_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SaleBill',
            fields=[
                ('billno', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('bin', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=12, unique=True)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('notes', models.TextField(blank=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SaleItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('perprice', models.IntegerField(default=1)),
                ('totalprice', models.IntegerField(default=1)),
                ('billno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salebillno', to='transections.salebill')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saleitem', to='inventory.stock')),
            ],
        ),
        migrations.CreateModel(
            name='SaleBillDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('cost_per_unit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tax', models.CharField(blank=True, max_length=50, null=True)),
                ('total', models.IntegerField(default=0)),
                ('billno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saledetailsbillno', to='transections.salebill')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('perprice', models.IntegerField(default=1)),
                ('totalprice', models.IntegerField(default=1)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchItem', to='transections.purchasebill')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchaseitem', to='inventory.stock')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseBillDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('cost_per_unit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tax', models.CharField(blank=True, max_length=50, null=True)),
                ('total', models.IntegerField(default=0)),
                ('billno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchasedetailsbillno', to='transections.purchasebill')),
            ],
        ),
        migrations.AddField(
            model_name='purchasebill',
            name='suppliers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to='transections.suppliers'),
        ),
    ]
