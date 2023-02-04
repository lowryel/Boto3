import boto3
import time

# Get Instance ID
ec2 = boto3.client("ec2")
response = ec2.describe_instances()
Instance_Id = response["Reservations"][0]["Instances"][0]["InstanceId"]
print(Instance_Id)

# Terminate Instance
print(time.sleep(10))
'''Terminating an instance using the instance ID'''
terminate_instance = ec2.terminate_instances(InstanceIds=[Instance_Id])
print(terminate_instance)

