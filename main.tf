module "network"{
    source = "./network"
    cidr = var.cidr
    public_cidr = var.public_subnet_cidr
    private_cidr = var.private_subnet_cidr
}