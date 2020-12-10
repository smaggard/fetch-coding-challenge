# Create EC2 Instance

create_instance.py is a python application for reading in a YAML file and creating an EC2 Instance for it.

This application assumes you have your aws configuration stored in ~/.aws/ if you have not done so already,
please follow the directions located athttps://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html

## Setup
1. Install requirements.
```pip3 -r requirements.txt```
   
2. Setup AWS Credentials 
   This application assumes you have your aws configuration stored in ~/.aws/ if you have not done so already
please follow the directions located at https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html

## Usage
```python3 create_instance.py --yaml <yamlfile> --keyfile <keyname> --parse true (optional prints config used to create instance)```


## Example yaml
```
---
# This YAML configuration specifies a server with two volumes and two users
server:
  instance_type: t2.micro
  ami_type: ami-04d29b6f966df1537
  architecture: x86_64
  root_device_type: ebs
  virtualization_type: hvm
  min_count: 1
  max_count: 1
  volumes:
    - device: /dev/xvda
      size_gb: 10
      type: ext4
      mount: /
    - device: /dev/xvdf
      size_gb: 100
      type: xfs
      mount: /data
  users:
    - login: user1
      ssh_key: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCyqN62QleFIkOMxOLflydRCWNOhV2Rfj1yD6aCBqxxMe2pUnVsoZH+gf2G/5bz6N23mwiSUXkm2z+TQqCsmerovcOo49zxJWPbgKdRhyyCrsI5O4fv//bAbMYpKC/UYqxzdxcR/CsOh9O6KEtqd/OzW7j+rdulSoO4xrQkZWN7OMzDPsThSlgiYyvVNNKeu0sEjk2dlxo8ywwnTZd+kIo2KQHO6S+3PX8p+n/sruCx0SGvPL4mOd6oUuIZe0SiAwT/jfb2wqzjd2afdl8GWSvafTJt+f3+9uHCYcGV7wfWOTM3QCavbql3u7L0es1Y4pSoEBUXA2XVGCfIzbvFNJ7U86sPhKNnElq0UP1nMrQSGQGRVmvQ+n6784F4hwsBTQ9CRMpKj5mRCKFofinCF2Qtra4w2ihIWg2BlQD/CiBiQPPn/RJz7KLXphW6WwEqbcA6htiC5PaBkaRkhPndz2UNlXtQmIHJLj6BJfv4ovSh5Qu0aMcI4AJ33J/4wv+Tg7U= user1@localhost
    - login: user2
      ssh_key: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCyg6aqEHYoI1vhvGAGxFXlUb8ZBOfRbwxMCWgepAOZ9wSyV6oXwxLSeGXqbkp3nL0nB/cBAO15JVOlazmxWyn2eIegzzbbYsl5j3xxytwVWGJBy29F0McETYUCfLF/p8whOJGMHcbSHbn9zg/FeALke9T0U+iFBLNTiETo8tSCykV8WHpgfvKkYSKiZQY6gTjO83aOEANCv4XqTpYS6RCufybzgUY2eD/V7+bNyGboa+HaUrnFYgGdNE2z+ZSNLkPWw+VmDoVHgFjvReU3kyX2RNJL1tVdiQht8MA925q/bZdY1jnt5yVyb0zXbXiMsKbgX+45aNbpiAR/gX+CHr0ZB5et0gVE6g/Hi1UAmIPpwFNjTlWnvX76t94lntV+BGRWHMk7uX2inbTVkJEnlYwYT/JBFN6xgF5Cs3ZUxBOzzAE5g2+ViNiKpCfm2exyUhvzEa1DfIdALClGTPidtYl6Lj8yYoXgFrlF2gH8Z3m3+K7jA2AXvFpYWKOGiGeK9jc=  user2@localhost
```
