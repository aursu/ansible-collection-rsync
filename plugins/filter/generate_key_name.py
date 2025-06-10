from ansible.errors import AnsibleFilterError
import re
import hashlib
import uuid

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
