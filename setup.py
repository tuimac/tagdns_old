from setuptools import setup, find_packeges

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
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    description="Dynamic DNS for Amazon EC2",
    python_requires='>=3.6.0'
    packages=find_packeges(where=src),
    package_dir={'': 'src'},
    install_requires=[
        "boto3>=1.9.0",
    ],
)
