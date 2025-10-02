# Provider 
 provider "aws" {
  region = var.region_app
 }

 # Default VPC
 data "aws_vpc" "default" {
  default = true
 }

# Security group
resource "aws_security_group" "app_deploy_tf_sg" {  
  name        = var.sg_name_app
  description = var.sg_description_app
  vpc_id      = data.aws_vpc.default.id

  tags = { Name = var.tag_name_app }
}

# Ingress rules
resource "aws_vpc_security_group_ingress_rule" "app_allow_port22" {
  security_group_id = aws_security_group.app_deploy_tf_sg.id
  cidr_ipv4         = "45.146.10.181/32"
  ip_protocol       = "tcp"
  from_port         = 22
  to_port           = 22
}

resource "aws_vpc_security_group_ingress_rule" "app_allow_port3000" {
  security_group_id = aws_security_group.app_deploy_tf_sg.id
  cidr_ipv4         = "0.0.0.0/0"
  ip_protocol       = "tcp"
  from_port         = 3000
  to_port           = 3000
}

resource "aws_vpc_security_group_ingress_rule" "app_allow_port80" {
  security_group_id = aws_security_group.app_deploy_tf_sg.id
  cidr_ipv4         = "0.0.0.0/0"
  ip_protocol       = "tcp"
  from_port         = 80
  to_port           = 80
}

# Egress rule
resource "aws_vpc_security_group_egress_rule" "app_allow_all_traffic_ipv4" {
  security_group_id = aws_security_group.app_deploy_tf_sg.id
  cidr_ipv4         = "0.0.0.0/0"
  ip_protocol       = "-1"
}

# EC2 instance
resource "aws_instance" "app_deploy_instance" {
  ami                         = var.app_ami_id_app
  instance_type               = var.instance_type_app
  key_name                    = var.key_name_app
  associate_public_ip_address = true
  vpc_security_group_ids      = [aws_security_group.app_deploy_tf_sg.id]

    user_data = templatefile("${path.module}/run-app.sh.tftpl", {
    db_ip = aws_instance.db_deploy_instance.private_ip
  })

  tags = { Name = var.Name_app }
}
