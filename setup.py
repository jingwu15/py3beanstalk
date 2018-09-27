#!/usr/bin/env python
import os
from setuptools import setup

from py3beanstalk import __version__ as src_version

PKG_VERSION = os.environ.get('BEANSTALKC_PKG_VERSION', src_version)

setup(
    name='py3beanstalk',
    version=PKG_VERSION,
    py_modules=['py3beanstalk'],

    author='jingwu',
    author_email='jingwu@vip.163.com',
    description='beanstalkd de yi ge python3 ke hu duan ku',
    long_description='''
py3beanstalk shi beanstalkd de yi ge python3 ke hu duan ku. 
beanstalkd<http://kr.github.com/beanstalkd/> shi yi ge gao su ,fen bu shi , nei cun ji de xiao xi dui lie fu wu.
''',
    url='https://github.com/jingwu15/py3-beanstalk.git',
    license='Apache License, Version 2.0',
    classifiers=[
        #'Development Status :: 1 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
