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
import struct

def compile_python27_compatible(src_file, dst_file):
    """
    Compile Python source to Python 2.7 compatible bytecode
    """
    # Try to use py_compile with Python 2.7 magic number
    try:
        # Read source code
        with open(src_file, 'r') as f:
            source_code = f.read()
        
        # Compile to Python 3 bytecode first
        code = compile(source_code, src_file, 'exec')
        
        # Create directory if needed
        os.makedirs(os.path.dirname(dst_file), exist_ok=True)
        
        # Write with Python 2.7 magic number (0x03f30d0a)
        with open(dst_file, 'wb') as f:
            # Python 2.7 magic number
            f.write(b'\x03\xf3\r\n')
            # Timestamp (4 bytes)
            f.write(struct.pack('<L', 0))
            # Marshal the code object
            import marshal
            marshal.dump(code, f)
            
    except Exception as e:
        print("Warning: Could not create Python 2.7 compatible bytecode: %s" % e)
        print("Falling back to standard py_compile...")
        py_compile.compile(src_file, dst_file)

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
    
    # Compile Python source (Python 2.7 compatible bytecode)
    src_file = "src/mod_helloworld.py"
    dst_file = os.path.join(build_dir, "res/scripts/client/gui/mods/mod_helloworld.pyc")
    
    print("Compiling %s -> %s" % (src_file, dst_file))
    compile_python27_compatible(src_file, dst_file)
    
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