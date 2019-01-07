# _*_ encoding:utf-8 _*_

from __future__ import unicode_literals
from datetime import datetime

from django.db import models


# Create your models here.

class CityDict(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'城市名')
    desc = models.CharField(max_length=200, verbose_name=u'描述')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u'城市'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'课程名')
    desc = models.TextField(verbose_name=u'课程描述')
    category = models.CharField(max_length=20,
                                verbose_name=u'机构类别',
                                choices=(('pxjg', u'培训机构'), ('gr', u'个人')),
                                default='pxjg')
    num_fav = models.IntegerField(verbose_name=u'收藏数', default=0)
    image = models.ImageField(upload_to='org/%Y/%M', verbose_name='封面图', max_length=100)
    city = models.ForeignKey(CityDict, verbose_name=u'所在城市')
    students = models.IntegerField(verbose_name=u'学生数', default=0)
    course_num = models.IntegerField(verbose_name=u'课程数', default=0)
    address = models.TextField(verbose_name=u'课程地址')
    click_nums = models.IntegerField(verbose_name=u'点击数', default=0)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u'课程组织'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name=u'所属机构')
    name = models.CharField(max_length=50, verbose_name=u'老师名')
    desc = models.TextField(verbose_name=u'老师介绍')
    work_year = models.IntegerField(default=0, verbose_name=u'工作年限')
    work_company = models.CharField(max_length=50, verbose_name=u'任职公司')
    work_position = models.CharField(max_length=50, verbose_name=u'公司职位')
    points = models.CharField(max_length=10, verbose_name=u'教学特点')
    image = models.ImageField(upload_to='teacher/%Y/%M', verbose_name='教师照片', max_length=100)

    class Meta:
        verbose_name = u'教师'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name