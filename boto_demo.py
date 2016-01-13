## Before doing this at the command line:
## aws configure
## enter in the required information

import boto3
from pprint import pprint

ec2 = boto3.resource('ec2')

############################
# Creates one instance.
############################
ec2.create_instances(ImageId='ami-d05e75b8', MinCount=1, MaxCount=1, InstanceType='t2.micro')

############################
# Check health status
############################
for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
    pprint(status)
    print("The current status is {}.".format(status['SystemStatus']['Status']))

############################
# Gets a list of running instances
############################
instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

############################
# Empty array that will be used to store a list of instance ids
###########################
ids = []

############################
# Loop over instances above getting the instance id
############################
for instance in instances:
    print(instance.id, instance.instance_type)

############################
# Put the instance id into the array.
############################
	ids.append(instance.id)

############################
# Stop and Terminate the instances that are running.
############################
ec2.instances.filter(InstanceIds=ids).stop()
ec2.instances.filter(InstanceIds=ids).terminate()

