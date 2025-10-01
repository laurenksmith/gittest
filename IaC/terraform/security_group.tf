

# Modify the EC2 instance created in main.tf:
# Attach the key to be used with EC2 instance

# Test infrastructure was created as intended

# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group

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


# Allow port 22 from your local machine's IP address only
resource "aws_vpc_security_group_ingress_rule" "allow_port22_local_ip_only" {
  security_group_id = aws_security_group.test_sg.id
  cidr_ipv4         = var.my_ip
  from_port         = 22
  ip_protocol       = "tcp"
  to_port           = 22
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
