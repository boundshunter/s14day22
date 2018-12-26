#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def test_simple():
    return "simple_tag"


@register.simple_tag
def test_simple_args(v1, v2, v3):
    return v1 + v2 +v3


@register.filter
def test_filter(v1, v2): # 最多只能传2个参数
    return v1 + v2