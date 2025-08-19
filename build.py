#!/usr/bin/env python
"""
Build script for WoT Hello World mod
Compiles Python source and packages the mod
"""

import os
import sys
import py_compile
import subprocess
import shutil

def main():
    print("Building WoT Hello World mod...")
    
    # Create build directory
    build_dir = "build"
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    os.makedirs(build_dir)
    
    # Copy structure
    shutil.copytree("res", os.path.join(build_dir, "res"))
    shutil.copy("meta.xml", build_dir)
    
    # Compile Python source
    src_file = "src/mod_helloworld.py"
    dst_file = os.path.join(build_dir, "res/scripts/client/gui/mods/mod_helloworld.pyc")
    
    print("Compiling %s -> %s" % (src_file, dst_file))
    py_compile.compile(src_file, dst_file)
    
    # Package mod
    mod_file = "antoinekm.helloworld.wotmod"
    if os.path.exists(mod_file):
        os.remove(mod_file)
    
    print("Packaging %s" % mod_file)
    cmd = ["7z", "a", "-tzip", "-mm=Copy", mod_file, "-r"]
    cmd.extend([os.path.join(build_dir, "*")])
    
    result = subprocess.run(cmd, cwd=".", capture_output=True, text=True)
    if result.returncode != 0:
        print("Error packaging mod: %s" % result.stderr)
        return 1
    
    print("Mod built successfully: %s" % mod_file)
    return 0

if __name__ == "__main__":
    sys.exit(main())