from setuptools import setup, find_packeges

setup(
    name="tagdns",
    version="1.0.0",
    url="https://github.com/tuimac/tagdns.git",
    author="tuimac",
    author_email="tuimac.devadm01@gmail.com",
    description="Dynamic DNS for AWS",
    packages=find_packeges(where=src),
    package_dir={'': 'src'},
    install_requires=[
        "boto3>=1.9.0",
    ],
)
