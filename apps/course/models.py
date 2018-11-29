# _*_ encoding:utf-8 _*_

from __future__ import unicode_literals
from datetime import datetime

from django.db import models


# Create your models here.
class course(models.Model):
	name = models.CharField(max_length=50, verbose_name='课程名')
	desc = models.CharField(max_length=300, verbose_name=u'课程介绍')
	detail = models.TextField(verbose_name=u'课程详情')
	degree = models.CharField(max_length=6,verbose_name=u'难度')
	learn_time = models.IntegerField(default=0, verbose_name='学习时长')
	studtent = models.IntegerField(default=0, verbose_name='学习人数')
	fav_numbers = models.IntegerField(default=0, verbose_name='收藏人数')
	image = models.ImageField(upload_to='course/%Y/%M', verbose_name='封面图', max_length=100)
	click_number = models.IntegerField(default=0, verbose_name='点击数')
	add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

	class Meta:
		verbose_name = '课程'
		verbose_name_plural = verbose_name

	def __unicode__(self):
		return self.name

class Lesson(models.Model):
	course = models.ForeignKey(course, verbose_name=u'课程名称')
	name = models.CharField(max_length=100, verbose_name=u'章节名')
	add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

	class Meta:
		verbose_name = '章节'
		verbose_name_plural = verbose_name

	def __unicode__(self):
		return self.name


class Video(models.Model):
	lesson = models.ForeignKey(Lesson, verbose_name='章节')
	name = models.CharField(max_length=100, verbose_name=u'视频名')
	add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

	class Meta:
		verbose_name = '视频'
		verbose_name_plural = verbose_name


class CourseResource(models.Model):
	course = models.ForeignKey(course, verbose_name=u'课程')
	name = models.CharField(max_length=100, verbose_name=u'资源名称')
	download = models.FileField(upload_to='course/resource/%Y/%M', verbose_name='资源文件', max_length=100)
	add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

	class Meta:
		verbose_name = '课程资源'
		verbose_name_plural = verbose_name
