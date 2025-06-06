# Installation Guide

## Requirements

- Ansible 2.9 or higher
- Python 3.9 or higher
- SSH access to target hosts

## Installing the Collection

### Method 1: Direct Installation

```bash
ansible-galaxy collection install aursu.rsync
```

### Method 2: Using requirements.yml

Create a `requirements.yml` file:

```yaml
collections:
  - name: aursu.rsync
    version: "1.0.0"
```

Then install using:

```bash
ansible-galaxy collection install -r requirements.yml
```

## Verifying Installation

To verify the installation:

```bash
ansible-galaxy collection list | grep aursu.rsync
```

## Development Setup

For development work, clone the repository:

```bash
git clone https://github.com/aursu/ansible-collection-rsync.git
cd ansible-collection-rsync
```