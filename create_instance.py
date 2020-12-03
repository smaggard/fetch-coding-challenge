#!/bin/env python3

import yaml
import boto3
import re

YAML_FILE = 'ec2-instance.yaml'

ec2 = boto3.resource('ec2')


class CreateEC2Instance(object):
    def __init__(self, YAML_FILE):
        try:
            with open(YAML_FILE) as f:
                yaml_parsed = yaml.load(f, Loader=yaml.FullLoader)
        except Exception:
            print("Invalid YAML file provided")
            exit()

        self.instance_type = yaml_parsed['server']['instance_type']
        self.ami_type = yaml_parsed['server']['ami_type']
        self.min_count = yaml_parsed['server']['min_count']
        self.max_count = MaxCount=yaml_parsed['server']['max_count']
        self.block_devices = self.__create_block_device_list(yaml_parsed['server']['volumes'])
        self.cloud_init = self.__create_cloud_init_fs(yaml_parsed['server']['volumes'])
        self.cloud_init += self.__create_cloud_init_mounts(yaml_parsed['server']['volumes'])

    def __create_block_device_list(self, devices):
        result = []
        for device in devices:
            device_dict = {
                'DeviceName': device['device'],
                'VirtualName': device['mount'],
                'Ebs': {
                    'DeleteOnTermination': True,
                    'VolumeSize': device['size_gb'],
                    'VolumeType': 'standard',
                    'Encrypted': False
                }
            }
            result.append(device_dict)
        return result

    def __create_cloud_init_users(self, users):
        result = "#cloud-config\n"
        result += "users:\n"
        for user in users:
            result += f"  - name: {user['login']}\n"
            result += f"    gecos: {user['login']}\n"
            result += f"    primary_group: {user['login']}\n"
            result += f"    ssh_import_id: None\n"
            result += f"    lock_passwd: true\n"
            result += f"    ssh_authorized_keys:\n"
            result += f"      - {user['ssh_key']}\n"
        return result

    def __create_cloud_init_fs(self, mounts):
        result = "fs_setup:\n"
        for mount in mounts:
            result += f"  - label: {mount['mount']}\n"
            result += f"    filesystem: '{mount['type']}'\n"
            result += "    partition: 'auto'\n"
            result += f"    device: '{mount['device']}'\n"
            result += "  - cmd: mkfs -t %(filesystem)s -L %(label)s %(device)s\n"
        return result

    def __create_cloud_init_mounts(self, mounts):
        result = "mounts:\n"
        for mount in mounts:
            if mount['mount'] == '/':
                pass
            else:
                dev_name = re.sub('/dev/', '', mount['device'])
                result += f"  - [ {dev_name}, {mount['mount']} ] \n"
        result += 'mount_default_fields: [ None, None, "auto", "defaults,nofail", "0", "2" ]\n'
        return result
        

    def create_instance(self):
        print(self.instance_type)
        print(self.ami_type)
        print(self.min_count)
        print(self.max_count)
        print(self.block_devices)
        instance = ec2.create_instances(
            InstanceType=self.instance_type,
            ImageId=self.ami_type,
            MinCount=self.min_count,
            MaxCount=self.max_count,
            BlockDeviceMappings=self.block_devices,
            KeyName='smaggard',
            UserData=self.cloud_init
        )

    def test_parameters(self):
        print(self.instance_type)
        print(self.ami_type)
        print(self.min_count)
        print(self.max_count)
        print(self.block_devices)
        print(self.cloud_init)


if __name__ == "__main__":
    ec2_instance = CreateEC2Instance(YAML_FILE)
    ec2_instance.test_parameters()
    instance_id = ec2_instance.create_instance()