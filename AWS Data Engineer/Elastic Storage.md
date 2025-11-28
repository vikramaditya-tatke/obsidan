# EBS
- *Elastic Block Storage*
- Like [[EC2]] instances, these are locked to a single AZ.
- Can only be attached to 1 EC2 instance.
- Delete on Termination - If the EC2 instance is terminated -
	- the root EBS volume is terminated by default.
	- other attached EBS volumes are NOT terminated by default.
- **Elastic Block Volumes**: Modify volumes without downtime.
	- Increase capacity
	- Modify IOPS

# EFS
 - Per as you go
 - No need to pre-allocate capacity and IOPS
 - Cross AZs
 - Can be connected to multiple EC2 instances.
 - Only for Linux Instances.
 - Supports the NFSv4 protocol, which allows for seamless integration with existing application and workflows that rely on NFS.
 - [[Lambda]] can directly integrate with EFS, providing concurrent access to the shared data. 