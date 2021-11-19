output "public_subnet_id" {
  value = aws_subnet.public.id
}

output "private_subnet_id" {
  value = aws_subnet.private.id
}

output "vpc_id" {
    value = aws_vpc.myvpc.id
}

#-----------------------

output "public_sg_id" {
  value = "${aws_security_group.public_sg.id}"  
}

output "private_sg_id" {
  value = "${aws_security_group.private_sg.id}"  
}

output "db_sg_id" {
  value = "${aws_security_group.db_sg.id}"  
}

output "vpc_subnets_group_name" {
  value = "${aws_db_subnet_group.myvpc_subnets.id}"  
}

output "public_net_interface1_id" {
  value = "${aws_network_interface.my_public_net_interface1.id}"  
}

output "public_net_interface2_id" {
  value = "${aws_network_interface.my_public_net_interface2.id}"  
}


output "private_net_interface_id" {
  value = "${aws_network_interface.my_private_net_interface.id}"  
}

output "ecash_subnets_name" {
  value = "${aws_elasticache_subnet_group.ecash_subnets.name}"  
}
