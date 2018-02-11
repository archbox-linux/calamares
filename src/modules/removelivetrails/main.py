#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import libcalamares


def run():
    """
    Remove live environment trails from target system
    """
    try:
        # run script from archbox installer
        libcalamares.utils.check_target_env_call(["/opt/archbox/include/remove_trails.sh"])

    except subprocess.CalledProcessError as e:
        libcalamares.utils.debug("Cannot remove trails. "
                                 "Exit code "
                                 "{}.".format(e.returncode))
    return None
