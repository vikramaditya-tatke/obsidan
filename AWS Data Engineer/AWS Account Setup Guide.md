# IAM Identity Center

Steps to create an AWS Account for personal use which will be named for example, `AWSPersonalAccount` - 
1. Sign-up on the AWS Console website using an email - This will generate a root user.
2. Then, setup an admin user
	1. Assign AWSAdministrator Policy to a chosen username, 
	2. Send the option to create a password by email
	3. Enable MFA.
3. Logout of the Root user
4. Login with the admin user.
5. Go to IAM Identity Center
	1. Enable IAM Identity Center in a region closet to you.
	2. Give the instance a name
	3. Create a Group called `Personal`.
	4. Create a user `Vikramaditya` and assign the user to the created group.
	5. Create a Permission Set `AdministratorAccess`.
	6. Assign this permission set to the group created in Step 3.
	7. Click on AWS Accounts in the navigation pane -> Assign this group and the user in the group to the `AWSPersonalAccount` account.
6. Now `Vikramaditya` should be provided the start_url obtained when the IAM Identity Center instance was enabled in the region.
7. He can use this to authenticate with AWS CLI so that long-term access keys are not generated and are not used.


## 1. Root User Setup

1. Create AWS account at aws.amazon.com/console
2. Enable MFA for root user
3. **Log out and don't use again**

## 2. Admin User

1. Sign in as root → IAM → Create User
2. Username: `admin-vikramaditya`
3. Attach: `AdministratorAccess` policy
4. Enable MFA
5. Log out of root, use admin user

## 3. IAM Identity Center

1. IAM Identity Center → Enable
2. Create group: `Personal`
3. Create user: `Vikramaditya` → assign to `Personal`
4. Create permission set: `AdministratorAccess`
5. Assign group to AWS account
6. **Save start URL**

## 4. CLI Setup

```warp-runnable-command
aws configure sso
# Enter start URL, region
# Select account and permission set
```

## Access Summary

- **Root**: Emergency only
- **Admin**: Console management
- **SSO**: CLI/development

## Test

```warp-runnable-command
aws sts get-caller-identity
```