# Ansible Rsync Collection

This Ansible collection provides functionality for setting up and managing rsync operations with automatic SSH key management.

## Features

- Automated SSH key generation and distribution
- Configurable rsync operations between hosts
- Progress monitoring and statistics
- Support for long-running transfers
- Secure key management

## Quick Start

```yaml
# Install the collection
ansible-galaxy collection install aursu.rsync

# Run the playbook
ansible-playbook -i inventory/inventory.yml rsync_content.yml \
  -e "target_host=target.example.com" \
  -e "source_dir=/path/to/sync" \
  -e "target_dir=/destination/path"
```

See the sidebar for detailed documentation on installation, usage, and configuration.