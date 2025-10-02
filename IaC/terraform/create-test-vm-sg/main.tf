# Create an AWS security group named techXXX-firstname-tf-allow-port-22-3000-80 (tf so you know it was created by Terraform)
resource "aws_security_group" "test_sg" {
  name        = var.sg_name
  description = var.sg_description
  vpc_id      = data.aws_vpc.default.id

  tags = {
    Name = var.tag_name
  }
}

# This is to declare my data source
data "aws_vpc" "default" {
  default = true
}

# Fetch your public IP as plain text
data "http" "myip" {
  url = "https://api.ipify.org?format=text"
}

# Build the /32 CIDR
locals {
  my_ip      = trimspace(data.http.myip.response_body)
  my_ip_cidr = "${local.my_ip}/32"
}

# Allow port 22 only from my local machine; automating input of my ip address for instances where it may change.
resource "aws_vpc_security_group_ingress_rule" "allow_port22_local_ip_only" {
  security_group_id = aws_security_group.test_sg.id
  description       = "SSH from my current IP"
  ip_protocol       = "tcp"
  from_port         = 22
  to_port           = 22
  cidr_ipv4         = local.my_ip_cidr   # <-- string value (no quotes around the symbol, no brackets)
}

# Allow port 3000 from all
resource "aws_vpc_security_group_ingress_rule" "allow_port3000_from_all" {
  security_group_id = aws_security_group.test_sg.id
  cidr_ipv4         = "0.0.0.0/0"
  from_port         = 3000
  ip_protocol       = "tcp"
  to_port           = 3000
}


# Allow port 80 from all
resource "aws_vpc_security_group_ingress_rule" "allow_port80_from_all" {
  security_group_id = aws_security_group.test_sg.id
  cidr_ipv4         = "0.0.0.0/0"
  from_port         = 80
  ip_protocol       = "tcp"
  to_port           = 80
}

resource "aws_vpc_security_group_egress_rule" "allow_all_traffic_ipv4" {
  security_group_id = aws_security_group.test_sg.id
  cidr_ipv4         = "0.0.0.0/0"
  ip_protocol       = "-1" # semantically equivalent to all ports
}

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

  # attach the SSH key to be used with EC2 instance
  key_name = var.key_name

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

