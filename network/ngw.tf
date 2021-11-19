resource "aws_network_interface" "my_public_net_interface1" {
  subnet_id   = aws_subnet.public.id
  security_groups = [aws_security_group.public_sg.id]
}

resource "aws_network_interface" "my_public_net_interface2" {
  subnet_id   = aws_subnet.public.id
  security_groups = [aws_security_group.public_sg.id]
}


resource "aws_network_interface" "my_private_net_interface" {
  subnet_id   = aws_subnet.private.id
  security_groups = [aws_security_group.private_sg.id]
}