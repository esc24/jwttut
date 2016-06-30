"""
Build cloud formation template for an ec2 instance.

"""

import troposphere
import troposphere.ec2


def build_template():
    instance = troposphere.ec2.Instance("myinstance")
    instance.ImageId = "ami-4e6ffe3d"
    instance.InstanceType = "t2.micro"

    template = troposphere.Template()
    template.add_resource(instance)

    return template


if __name__ == '__main__':
    t = build_template()
    print(t.to_json())
