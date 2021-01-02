# Generated by Django 3.1.4 on 2021-01-02 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0002_auto_20201228_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mlalgorithmstatus',
            name='parent_mlalgorithm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status', to='endpoints.mlalgorithm'),
        ),
    ]
