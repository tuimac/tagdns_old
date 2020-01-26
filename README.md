# Tag DNS

This program get Tag information from target EC2 instances then register target Tag's value to DNS A record.
You can change the polling interval to get Tag information.
If you control access to tagdns, you can set the white list to allow source IP address zone.


## Getting Started

This program is easy to install. This program need the environment to execute Python3.


### Installation

Installing tagdns by `pip3` command. In future, I try to upload this program to PyPI.
Then you'll be much easier than now.

```
pip3 install git+https://github.com/tuimac/tagdns.git
```

### Running
There is configure file where is `/etc/tagdns/tagdns.yml` to configure tagdns's parameters
(You can change polling interval on this configuration file.)

To start tagdns process, execute the following command:

```
$ tagdns
```

There is no option now. But, I plan to create that.

## Support

Support  most Linux Distributions.
`Redhat`, `CentOS`, `Ubuntu`, `Debian`, `Amazon Linux`

## Authors

* **Kento Kashiwagi** - [tuimac](https://github.com/tuimac)

If you have some opinion and find bugs, please post [here](https://github.com/tuimac/tagdns/issues).

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Plan for the future

* Separate DNS zone by each VPC.
* Autoscale threads by the amount of access.(Now setting thread by tagdns.yml.)
* Can run on distributed environment like kubernetes or docker swarm cluster. It means to be stateless.
* Add query forward option.
* Associate with Route53.
* Saving CPU utilization.
* Add comments on the code.
* Upload to PyPI.
