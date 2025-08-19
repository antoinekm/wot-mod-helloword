# WoT Hello World Mod

A simple "Hello World" mod for World of Tanks that demonstrates basic mod loading and functionality.

## Features

- Displays greeting message in game logs
- Reads player name from data file
- Demonstrates proper WoT mod structure

## Installation

1. Download the `.wotmod` file from releases
2. Place it in your `World_of_Tanks/mods/[version]/` directory
3. Start the game

## Development

### Requirements

- Python 2.7 (for compilation to .pyc)
- 7-Zip (for packaging)

### Building

```bash
# Compile Python to bytecode
python2.7 -c "import py_compile; py_compile.compile('src/mod_helloworld.py', 'build/mod_helloworld.pyc')"

# Package mod
7z a -tzip -mm=Copy antoinekm.helloworld.wotmod meta.xml res/
```

### Structure

```
├── meta.xml              # Mod metadata
├── res/
│   ├── mods/
│   │   └── antoinekm.helloworld/
│   │       └── data/
│   │           └── name.txt    # Player name data
│   └── scripts/
│       └── client/
│           └── gui/
│               └── mods/
│                   └── mod_helloworld.pyc  # Compiled mod script
```

## License

MIT License