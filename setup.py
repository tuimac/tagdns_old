from setuptools import setup, find_packages
import sys
import os

CONFIG = "/etc/tagdns"

if os.path.exists(CONFIG) is False:
    os.mkdir(CONFIG)
    print(os.getcwd())

setup(
    name="tagdns",
    version="1.0.0",
    url="https://github.com/tuimac/tagdns.git",
    author="tuimac",
    author_email="tuimac.devadm01@gmail.com",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    description="Dynamic DNS for Amazon EC2",
    python_requires='>=3.6.0',
    packages=find_packages(where='tagdns'),
    package_dir={'': 'tagdns'},
    install_requires=[
        "boto3>=1.9.0",
    ],
    entry_points={
        'console_scripts'=[
            'tagdns = src.main:run'
    }
)
