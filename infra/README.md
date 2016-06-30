
cloud formation 
===============

Requires: troposphere boto (not boto3!), both available on pip


config:

Add a ~/.aws/credentials file containing your AWS credentials


build:

    python ec2instance.py > ec2instance.json

run:

    cfn -r eu-west-1 -n ec2instancetemplate -b cloudformationbucket123 -c ec2instance.json ec2instancestack

note this will upload the template and trigger creation of the infrastructure



