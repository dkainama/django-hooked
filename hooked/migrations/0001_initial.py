# Generated by Django 2.0.1 on 2018-02-22 07:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import hooked.models
import hooked.tokens
import jsonfield.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebHookClientApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('identifier', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Identifier')),
                ('secret', models.CharField(default=hooked.tokens.generate_random_secret, editable=False, max_length=255, verbose_name='Shared secret')),
                ('need_authorization', models.BooleanField(default=True, verbose_name='Secure endpoint for this app?')),
                ('modified', models.DateTimeField(blank=True, null=True, verbose_name='Modified on')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'App',
            },
        ),
        migrations.CreateModel(
            name='WebHookTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', jsonfield.fields.JSONField()),
                ('meta', jsonfield.fields.JSONField()),
                ('status', models.IntegerField(choices=[(1, 'Awaiting'), (2, 'Progress'), (3, 'Processed'), (4, 'Failed')], default=hooked.models.TransactionStatus(1))),
                ('event', models.CharField(editable=False, max_length=255, verbose_name='Event')),
                ('modified', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hooked.WebHookClientApp')),
            ],
            options={
                'verbose_name': 'Transaction',
            },
        ),
    ]
