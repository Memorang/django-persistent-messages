import os
from setuptools import (
    find_packages,
    setup,
)


setup(
    name='django-persistent-messages',
    author='philomat',
    maintainer='gjcourt',
    version='0.1.1',
    description='A Django app for unified and persistent user messages/notifications, built on top of Django\'s messages framework',
    long_description=open('README.md').read(),
    license='MIT',
    url='http://github.com/memorang/django-persistent-messages',
    keywords=['messages', 'django', 'persistent',],
    packages=find_packages()
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)
