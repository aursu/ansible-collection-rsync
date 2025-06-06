# Ansible Rsync Setup

This playbook sets up SSH key-based authentication and performs rsync from the Ansible target host to a specified destination.

## Requirements

- Ansible 2.9 or higher
- Python 3.9 or higher
- SSH access to both origin and target hosts

## Role Variables

- `target_host`: Hostname/IP of the destination host for rsync
- `source_dir`: Source directory on local host to sync
- `target_dir`: Target directory on the destination host

SSH keys are automatically generated with unique names that include:
- The target hostname (with special characters converted to underscores)
- A timestamp-based unique identifier
- Example key name: `id_rsa_target_example_com_a1b2c3d`

These keys are managed automatically and don't require manual configuration.

## Usage

1. Run the playbook with required parameters:
```bash
ansible-playbook -i inventory/inventory.yml rsync_content.yml \
  -e "target_host=target.example.com" \
  -e "source_dir=/path/to/sync" \
  -e "target_dir=/destination/path"
```

## Inventory Example

Create an inventory file with your target host:
```ini
[rsync_source]
source.example.com
```

The playbook will run on the host where it's executed (source.example.com in this example) and sync files to the specified target_host.
