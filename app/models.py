from django.db import models

# Create your models here.
class Profile(models.Model):
  title = models.CharField('タイトル', max_length=100, null=True, blank=True)
  subtitle = models.CharField('サブタイトル', max_length=100, null=True, blank=True)
  name = models.CharField('名前', max_length=100)
  job = models.TextField('仕事')
  introduction = models.TextField('自己紹介')
  
  github = models.CharField('GitHub', max_length=100, null=True, blank=True)
  x = models.CharField('X', max_length=100, null='', blank='')
  linkedin = models.CharField('linkedin', max_length=100, null=True, blank=True)
  facebook = models.CharField('facebook', max_length=100, null=True, blank=True)
  instagram = models.CharField('instagram', max_length=100, null=True, blank=True)
  topimage = models.ImageField(upload_to='images', verbose_name='トップ画像')
  subimage = models.ImageField(upload_to='images', verbose_name='サブ画像')
  
  def __str__(self):
    return self.name

