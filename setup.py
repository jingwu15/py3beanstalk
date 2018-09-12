#!/usr/bin/env python
import os
from setuptools import setup

from beanstalkc3 import __version__ as src_version

PKG_VERSION = os.environ.get('BEANSTALKC_PKG_VERSION', src_version)

setup(
    name='beanstalkc3',
    version=PKG_VERSION,
    py_modules=['beanstalkc3'],

    author='jingwu',
    author_email='jingwu@vip.163.com',
    description='beanstalkd 的一个 python3 客户端库',
    long_description='''
beanstalkc3 是 beanstalkd 的一个 python3 客户端库. 
beanstalkd<http://kr.github.com/beanstalkd/> 是一个高速,分布式,内存级的消息队列服务
''',
    url='https://github.com/jingwu15/beanstalkc3.git',
    license='Apache License, Version 2.0',
    classifiers=[
        'Development Status :: 1 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
