from setuptools import setup, find_packages
import os
import shutil
import socket

path = "/etc/tagdns/tagdns.yml"

# Deploy configuration filt to default directory.
if os.path.exists(path) is False:
    directory = path.split("/")
    path = "/".join(directory[:len(directory) - 1])
    os.mkdir(path)
    confFile = os.getcwd() + "/etc/tagdns.yml"
    shutil.copyfile(confFile, path)

# Insert IP address to configration file.
ipaddr = socket.gethostbyname(socket.gethostname())
confFile = ""
with open(path, 'r') as f:
	confFile = yaml.load(f, Loader=yaml.SafeLoader)
confFile["ipaddress"] = ipaddr
with open(path, 'w') as f:
	yaml.dump(confFile, f)

# Setuptools
setup(
    name="tagdns",
    version="1.0.0",
    url="https://github.com/tuimac/tagdns",
    author="tuimac",
    author_email="tuimac.devadm01@gmail.com",
    license="LICENSE.md",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: System :: Installation/Setup",
        "Topic :: System :: Software Distribution"
    ],
    description="Dynamic DNS for Amazon EC2",
    python_requires=">=3.6.0",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "boto3>=1.9.0",
        "setuptools"
    ],
    entry_points={
        "console_scripts": [
            "tagdns=tagdns.main:main"
        ]
    }
)
