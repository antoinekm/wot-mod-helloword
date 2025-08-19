"""
Hello World mod for World of Tanks
Test mod to verify mod loading works correctly
"""

def init():
    """
    Mod initialization function.
    Called by World of Tanks when the game starts up.
    """
    try:
        import ResMgr
        
        # Try to read name from data file
        vfs_path = 'mods/antoinekm.helloworld/data/name.txt'
        vfs_file = ResMgr.openSection(vfs_path)
        
        if vfs_file is not None and ResMgr.isFile(vfs_path):
            name = str(vfs_file.asString).strip()
        else:
            name = "Unknown"
        
        # Print to python.log
        print('[HELLOWORLD] Hello %s!' % name)
        print('[HELLOWORLD] Mod initialized successfully!')
        
    except Exception as e:
        print('[HELLOWORLD] Error during init: %s' % str(e))
        print('[HELLOWORLD] Simple Hello World!')

def fini():
    """
    Mod deinitialization function.
    Called by World of Tanks when the game shuts down.
    """
    try:
        import ResMgr
        
        vfs_path = 'mods/antoinekm.helloworld/data/name.txt'
        vfs_file = ResMgr.openSection(vfs_path)
        
        if vfs_file is not None and ResMgr.isFile(vfs_path):
            name = str(vfs_file.asString).strip()
        else:
            name = "Unknown"
        
        print('[HELLOWORLD] Bye bye %s!' % name)
        
    except Exception as e:
        print('[HELLOWORLD] Error during fini: %s' % str(e))
        print('[HELLOWORLD] Goodbye!')

# Also try immediate execution for testing
print('[HELLOWORLD] Module imported successfully!')