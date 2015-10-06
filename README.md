# ansible-testing
Python module to help test or validate Ansible, specifically ansible modules

## Current Validations

### Modules

#### Errors

1. Interpreter line is not `#!/usr/bin/python`
1. `main()` not at the bottom of the file
1. Module does not include `from ansible.module_utils.basic import *`
1. `module_utils` imports at the top (excluding whitelisted `module_utils`)
1. Invalid `module_utils` import
1. Missing `DOCUMENTATION` or invalid YAML
1. Missing `EXAMPLES`
1. Invalid Python Syntax
1. Tabbed indentation
1. Use of `sys.exit()`
1. Missing GPLv3 license header in module
1. Powershell module missing `WANT_JSON`
1. Powershell module missing `REPLACER_WINDOWS`

#### Warnings

1. Whitelisted `module_utils` imports at the top
1. Try/Except `HAS_` expression missing
1. Missing `RETURN`
1. `import json` found

#### Notes

1. `module_utils` imports not at bottom may be error or warning depending on the import.

### Module Directories (Python Packages)

1. Missing `__init__.py`
