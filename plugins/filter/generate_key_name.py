import re
import hashlib
import uuid
from ansible.errors import AnsibleFilterError

DOCUMENTATION = '''
---
filter: generate_key_name
description: >
    Generates a unique SSH key name based on the target host and key type.
    The key name is sanitized to remove invalid characters and includes a hash for uniqueness.
parameters:
  - target_host:
      description: The target host name or IP address.
      required: true
      type: str
  - key_type:
      description: >
          The type of SSH key to generate. Must be one of: 'rsa', 'ed25519', 'ecdsa', 'dsa'.
      required: false
      type: str
      default: ed25519
returns:
    description: >
        A sanitized key name in the format: id_<key_type>_<sanitized_host>_<hash>.
    type: str
    sample: id_ed25519_example_com_a1b2c3d
'''

def generate_key_name(target_host, key_type='ed25519'):
    """
    Generate a unique SSH key name based on target host and UUID.
    
    Args:
        target_host (str): The target host name/IP
        key_type (str): Type of SSH key. Must be one of: 'rsa', 'ed25519', 'ecdsa', 'dsa'
    
    Returns:
        str: A sanitized key name in format: id_keytype_hostname_hash
    
    Raises:
        AnsibleFilterError: If an invalid key type is provided
    """
    # Valid SSH key types
    valid_key_types = ['rsa', 'ed25519', 'ecdsa', 'dsa']
    
    # Validate key type
    if key_type.lower() not in valid_key_types:
        raise AnsibleFilterError(f"Invalid key type. Must be one of: {', '.join(valid_key_types)}")
    
    # Validate target host is not empty or whitespace
    if not target_host or not target_host.strip():
        raise AnsibleFilterError("target_host cannot be empty or contain only whitespace")
    
    # Sanitize the target host name (remove non-alphanumeric chars)
    safe_host = re.sub(r'[^a-zA-Z0-9]+', '_', target_host).strip('_')
    
    # Generate UUID-based hash
    unique_id = str(uuid.uuid4())
    hash_obj = hashlib.sha256(unique_id.encode())
    short_hash = hash_obj.hexdigest()[:7]
    
    # Combine all parts with 'id_' prefix (SSH key naming convention)
    return f"id_{key_type.lower()}_{safe_host}_{short_hash}"

class FilterModule(object):
    '''Custom filters for key name generation'''
    
    def filters(self):
        return {
            'generate_key_name': generate_key_name
        }
