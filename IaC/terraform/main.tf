# create an ec2 instance
# provide cloud provider name
provider "aws" {
  # where to create - which region
  region = var.region
}

# specify which resource to create ec2 instance
resource "aws_instance" "test_instance" {
  # which ami ID ami-0c1c30571d2dae5c9 (for ubuntu 22.04 lts)
  ami = var.app_ami_id

  # which type of instance (size)
  instance_type =  var.instance_type

  # add a public ip address to this instance
  associate_public_ip_address = true
  
  # aws_access_key = sdksdgshk (NEVER DO THIS)
  # aws_secret_Key = sdlgsjglsjg4 (NEVER DO THIS)

  # Use security group you created
  vpc_security_group_ids = [aws_security_group.test_sg.id]


  # name the instance e.g. tech511-lauren-tf-test-vm
  tags = {
    Name = var.Name
  }
}

