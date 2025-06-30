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
ansible-playbook playbooks/rsync_content.yml \
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

## Running Unit Tests

To run the unit tests for this collection, the collection folder must be placed in the following directory structure:

```
ansible_collections/
└── aursu/
    └── rsync/
        └── (collection files here)
```

This structure ensures that the collection is properly recognized by Python and Ansible.

### Steps to Run Tests

1. Place the collection folder (`rsync`) into the directory structure as shown above.

2. Set the `PYTHONPATH` to include the root directory of the collection hierarchy:
   ```bash
   export PYTHONPATH=$PWD/../../..
   ```

   On Windows (PowerShell):
   ```powershell
   $env:PYTHONPATH="$PWD/../../.."
   ```

3. Run the tests using `unittest` from the `ansible_collections/aursu/rsync` folder:
   ```bash
   python -m unittest discover -s tests/unit/plugins/filter -p "*.py" -v
   ```

### Example

If your project is located in a directory structure like this:
```
<project_root>/ansible_collections/aursu/rsync
```

The `PYTHONPATH` should be set to:
```
<project_root>
```

And the tests should be run from:
```
<project_root>/ansible_collections/aursu/rsync
```

Using the following command:
```bash
python -m unittest discover -s tests/unit/plugins/filter -p "*.py" -v
```
