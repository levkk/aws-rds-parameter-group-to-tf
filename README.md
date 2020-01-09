# AWS RDS Parameter Group To Terraform Converter

Converts AWS RDS Parameter Group to a Terraform object. Helps during database major version upgrades.

## Usage

```bash
$ aws rds describe-db-parameters --db-parameter-group-name your-parameter-group-name | python3 convert.py
```

## Depedencies

A working `awscli` with read access to RDS.
