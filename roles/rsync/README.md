# Ansible Role: rsync

This role sets up and manages rsync operations between hosts, including SSH key management for secure file transfers.

## Features

- Automated SSH key generation and distribution
- Configurable rsync operations between hosts
- Progress monitoring and statistics
- Support for long-running transfers
- Secure key management

## Role Structure

This role includes the following tasks:

1. **SSH Key Setup** (`tasks/ssh_keys.yml`):  
   Generates and distributes SSH keys for secure connections.

2. **Rsync Operations** (`tasks/rsync.yml`):  
   Configures and executes rsync commands to sync files.

3. **Cleanup** (`tasks/cleanup.yml`):  
   Cleans up temporary files and keys after the operation.

## Example Usage

```yaml
- name: Sync files between hosts
  hosts: all
  roles:
    - role: aursu.rsync
      vars:
        target_host: "target.example.com"
        source_dir: "/path/to/source"
        target_dir: "/path/to/destination"
```

## Required Variables

```yaml
target_host: "target.example.com"    # Destination host for rsync
source_dir: "/path/to/source"        # Source directory on the local host
target_dir: "/path/to/destination"   # Target directory on the destination host
```

## Optional Variables

```yaml
ssh_user: "root"                     # SSH user for connection (default: current user)
ssh_strict_host_checking: false      # Disable strict host checking (default: false)
```

## Author

Alexander Ursu ([alexander.ursu@gmail.com](mailto:alexander.ursu@gmail.com))

## License

MIT
