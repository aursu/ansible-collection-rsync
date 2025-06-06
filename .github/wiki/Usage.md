# Usage Guide

## Basic Configuration

1. Create an inventory file:
```ini
[rsync_source]
source.example.com
```

2. Define required variables:

| Variable | Description | Required |
|----------|-------------|----------|
| target_host | Destination host for rsync | Yes |
| source_dir | Source directory on local host | Yes |
| target_dir | Target directory on destination | Yes |

## Running the Playbook

Basic execution:
```bash
ansible-playbook -i inventory/inventory.yml rsync_content.yml \
  -e "target_host=target.example.com" \
  -e "source_dir=/path/to/sync" \
  -e "target_dir=/destination/path"
```

## Transfer Options

Default rsync configuration:
- Checksum-based comparison (-c)
- Archive mode (-a)
- Progress monitoring (--info=PROGRESS2,STATS3)
- Long-running support (up to 12 hours)
- Status updates every 60 seconds

## SSH Key Management

The collection manages SSH keys automatically:
- Generates unique key pairs
- Names based on target hostname
- Example: `id_rsa_target_example_com_[unique_id]`
- Distributes keys securely
