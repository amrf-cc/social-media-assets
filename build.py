#!/usr/bin/env python3
"""No-op build step for the social asset host.

The manager runs `build.py` before publishing and requires BUILD_OK in the
output. This repo serves raw files, so there is nothing to generate.
"""

print("BUILD_OK")
