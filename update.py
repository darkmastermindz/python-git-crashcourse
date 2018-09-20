#!/usr/bin/env python
from subprocess import call

# Update Git submodules
call(["git", "submodule", "update"])
