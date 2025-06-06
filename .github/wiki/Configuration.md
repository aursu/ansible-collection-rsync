# Configuration Guide

## Role Variables

### Required Variables

| Variable | Description | Default |
|----------|-------------|---------|
| target_host | Destination host for rsync operations | none |
| source_dir | Source directory on local host | none |
| target_dir | Target directory on destination host | none |

### Optional Variables

| Variable | Description | Default |
|----------|-------------|---------|
| ssh_user | SSH user for connections | current user |
| ssh_strict_host_checking | Enable SSH strict host checking | false |

## SSH Key Configuration

### Key Generation

- Keys are generated automatically
- Naming convention: `id_rsa_target_<hostname>_<unique_id>`
- Keys are stored in the user's `.ssh` directory
- Private keys are protected with proper permissions (600)

### Key Distribution

- Public key is copied to target host
- Added to authorized_keys automatically
- Temporary keys are cleaned up after transfer

## Transfer Settings

### Rsync Options

Default rsync command options:
```bash
rsync -ca --info=PROGRESS2,STATS3
```

| Option | Purpose |
|--------|---------|
| -c | Use checksums for file comparison |
| -a | Archive mode (recursive, preserve attributes) |
| --info=PROGRESS2 | Show detailed transfer progress |
| --info=STATS3 | Show comprehensive statistics |

### Long-running Transfer Support

- Async execution enabled
- Maximum runtime: 12 hours
- Status polling interval: 60 seconds