# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Alexander Ursu

"""
Ansible filter plugin that returns the default SSH home directory
or .ssh directory for a given SSH user. For user 'root' it returns '/root/.ssh',
for any other user it returns '/home/<user>/.ssh'.
"""

from ansible.errors import AnsibleFilterError

DOCUMENTATION = r'''
---
name: ssh_dir
author: Alexander Ursu <alexander.ursu@gmail.com>
version_added: "1.0"
short_description: Returns default SSH directory path for a given user
description:
  - This filter returns the full SSH directory path (e.g. /root/.ssh or /home/username/.ssh)
    depending on the provided user name.
  - If the user is C(root), the result is C(/root/.ssh).
  - For all other users, the result is C(/home/<user>/.ssh).
options:
  _input:
    description: The user name to derive the SSH directory path from.
    required: true
    type: str
seealso:
  - name: Ansible filters
    description: General filter plugin reference
    link: https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_filters.html
'''

EXAMPLES = r'''
- name: Get SSH directory for default root user
  ansible.builtin.debug:
    msg: "{{ 'root' | ssh_dir }}"
  # => /root/.ssh

- name: Get SSH directory for non-root user
  ansible.builtin.debug:
    msg: "{{ 'backup' | ssh_dir }}"
  # => /home/backup/.ssh

- name: Use ssh_dir to define ssh_path in defaults
  vars:
    ssh_user: backup
    ssh_dir: "{{ ssh_user | ssh_dir }}"
'''

RETURN = r'''
_raw:
  description: The SSH directory path corresponding to the user
  type: str
  examples:
    - "/root/.ssh"
    - "/home/deploy/.ssh"
'''

def ssh_dir(user):
    """Returns the default SSH directory path for a given user."""
    if not isinstance(user, str) or not user.strip():
        raise AnsibleFilterError("Invalid SSH user: must be a non-empty string")
    
    home_dir = "/root" if user == "root" else f"/home/{user}"
    return f"{home_dir}/.ssh"

class FilterModule(object):
    """SSH path helpers"""
    def filters(self):
        return {
            'ssh_dir': ssh_dir,
        }
