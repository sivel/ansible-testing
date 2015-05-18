# ansible-testing
Python module to help test Ansible, specifically ansible modules

## Current Tests

### Modules

1. Interpreter line is `#!/usr/bin/python`
1. `main()` at the bottom of the file
1. Module includes `from ansible.module_utils` imports
1. `module_utils` imports at the bottom (warning)
1. Invalid `module_utils` import
1. Try/Except `HAS_` expression (warning)
1. Has `DOCUMENTATION` and is valid YAML
1. Has `EXAMPLES`
1. Has `RETURN` (warning)
1. `import json` found (warning)
1. Python syntax error

#### Notes

1. I would like to find a way to error for some `module_utils` imports that do not appear at the bottom

### Module Directories (Python Packages)

1. Missing `__init__.py`
