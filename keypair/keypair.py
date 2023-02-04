import boto3
import time
ec2 = boto3.client("ec2")

# Create a KeyPair
with open("key.pem","w") as f:
    create = ec2.create_key_pair(KeyName="demoKey")
    f.write(create["KeyMaterial"])
    print(create["KeyMaterial"])

time.sleep(3)
# Describe the KeyPair
get_key_pair = ec2.describe_key_pairs()
print(get_key_pair['KeyPairs'][0]["KeyName"])


# Delete a KeyPair
delete = ec2.delete_key_pair(KeyName="demoKey")
print(delete)


