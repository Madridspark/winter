# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField


@python_2_unicode_compatible
class BranchInfo(models.Model):
    name = models.CharField('大学名称', max_length=256)
    hero = models.FileField('背景图片', upload_to='./branch/hero-image-files/')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分部'
        verbose_name_plural = '分部信息'

@python_2_unicode_compatible
class FriendlyLink(models.Model):
    title = models.CharField('标题', max_length=256)
    link = models.TextField('链接', default='')
    image = models.FileField('图片', upload_to='./branch/friendly-link-image-files/')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接'


@python_2_unicode_compatible
class Tools(models.Model):
    title = models.CharField('标题', max_length=256)
    link = models.TextField('链接', default='')
    image = models.FileField('图片', upload_to='./branch/tools-image-files/')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '小助手'
        verbose_name_plural = '实用小助手'


@python_2_unicode_compatible
class Advertisements(models.Model):
    title = models.CharField('标题', max_length=256)
    link = models.FileField('介绍文件', upload_to='./branch/ads-files/text/')
    image = models.FileField('图片', upload_to='./branch/ads-files/image/')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '广告'
        verbose_name_plural = '广告列表'


@python_2_unicode_compatible
class Column(models.Model):
    name = models.CharField('栏目名称', max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '栏目'
        verbose_name_plural = '栏目'
        ordering = ['id']


@python_2_unicode_compatible
class Article(models.Model):
    column = models.ManyToManyField(Column, verbose_name='归属栏目')

    title = models.CharField('标题', max_length=256)
    titleImage = models.FileField('主题图片', blank=True, null=True, upload_to='./branch/article-title-images/')

    author = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='作者')
    content = UEditorField('内容', height=300, width=1000, default=u'', blank=True, imagePath="branch/content-images/", toolbars='besttome', filePath='branch/content-files/')

    pub_time = models.DateTimeField('发布时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)
    published = models.BooleanField('正式发布', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '发布文章'
        ordering = ['-update_time']

@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField('标题', default=' ', max_length=256)
    author = models.ForeignKey('auth.User', verbose_name='作者')
    content = models.TextField('内容', default='', blank=True)
    pub_time = models.DateTimeField('发布时间', auto_now_add=True, editable=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '帖子'
        verbose_name_plural = '帖子'
        ordering = ['-pub_time']


@python_2_unicode_compatible
class PostReply(models.Model):
    to = models.ForeignKey(Post, verbose_name='回复')
    author = models.ForeignKey('auth.User', verbose_name='作者')
    content = models.TextField('内容', default='', blank=True)
    pub_time = models.DateTimeField('发布时间', auto_now_add=True, editable=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '回帖'
        verbose_name_plural = '回帖'
        ordering = ['-pub_time']