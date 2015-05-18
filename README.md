# ansible-testing
Python module to help test Ansible, specifically ansible modules

## Current Tests

1. `main()` at the bottom of the file (warning)
1. Module includes `from ansible.module_utils` imports
1. `module_utils` imports at the bottom
1. Invalid `module_utils` import
1. Try/Except `HAS_` expression (warning)
1. Has DOCUMENTATION and is valid YAML
1. Has EXAMPLES
1. Has RETURN (warning)
