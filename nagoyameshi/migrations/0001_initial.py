# Generated by Django 4.2.7 on 2024-07-16 03:23

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='カテゴリ名')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='会社名')),
                ('address', models.CharField(max_length=100, verbose_name='所在地')),
                ('phone', models.CharField(max_length=15, verbose_name='電話番号')),
                ('history', models.DateField(verbose_name='設立日')),
                ('terms', models.TextField(verbose_name='規約')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='店舗名')),
                ('img', models.ImageField(upload_to='nagoyameshi/restaurant/img', verbose_name='店舗画像')),
                ('description', models.TextField(verbose_name='店舗説明文')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='編集日')),
                ('budget', models.PositiveIntegerField(verbose_name='予算')),
                ('capacity', models.PositiveIntegerField(verbose_name='受け入れ可能人数')),
                ('start', models.TimeField(verbose_name='営業開始')),
                ('end', models.TimeField(verbose_name='営業終了')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nagoyameshi.category', verbose_name='カテゴリ')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('comment', models.TextField(verbose_name='コメント')),
                ('stars', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='評価')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nagoyameshi.restaurant', verbose_name='対象飲食店')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='レビューユーザー')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='予約日時')),
                ('people', models.PositiveIntegerField(verbose_name='予約人数')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nagoyameshi.restaurant', verbose_name='対象飲食店')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='予約者')),
            ],
        ),
        migrations.CreateModel(
            name='Fav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='登録日')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nagoyameshi.restaurant', verbose_name='対象飲食店')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='お気に入り登録ユーザー名')),
            ],
        ),
    ]
