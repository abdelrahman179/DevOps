# DevOps

**Terraform: **

- What is infrastructure as a code (Iac)?
- What is Terraform
- Why Terraform?
- How Terraform works?
- Terraform core
- Terraform plugins
- Installation
- State file
- Plan
- Apply
- Destroy
- Module
- Workspaces & environments
- Variables
- Variable definition files
- Backend

**Project: **
- Creating two workspaces "dev & prod"
- Creating vpc, internet gateway, public route table, private route table, route association to public and private subnets
- Security group which allow ssh from 0.0.0.0/0 & Security group that allows ssh and port 3000 from cidr only
- Create two ec2 instances "bastion" in public subnet and pub sec group and "application" in private subnet and private sec group
- Creating rds
- Creating elastic cache 
