resource "aws_subnet" "public" {
  vpc_id     = aws_vpc.myvpc.id
  cidr_block = var.public_cidr
  map_public_ip_on_launch = "true"
}

resource "aws_subnet" "private" {
  vpc_id     = aws_vpc.myvpc.id
  cidr_block = var.private_cidr
}

resource "aws_db_subnet_group" "myvpc_subnets" {
  subnet_ids = [aws_subnet.private.id, aws_subnet.public.id]
}

resource "aws_elasticache_subnet_group" "ecash_subnets" {
  name       = "tf-test-cache-subnet"
  subnet_ids = [aws_subnet.private.id, aws_subnet.public.id]
}