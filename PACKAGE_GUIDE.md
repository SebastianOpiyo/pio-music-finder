# Pio Music Finder Package Management Guide

## Using pyproject.toml

Your project now uses `pyproject.toml` for modern Python package management. Here's how to use it:

## Installation Options

### 1. Install with basic dependencies only:
```bash
pip install -e .
```

### 2. Install with specific feature sets:
```bash
# Audio processing capabilities
pip install -e ".[audio]"

# Audio analysis features
pip install -e ".[analysis]"

# Music recognition services
pip install -e ".[recognition]"

# Lyrics fetching capabilities
pip install -e ".[lyrics]"

# Development tools
pip install -e ".[dev]"

# Install everything
pip install -e ".[all]"
```

### 3. Common combinations:
```bash
# For development with all features
pip install -e ".[all,dev]"

# For production with core features
pip install -e ".[audio,analysis,recognition]"
```

## Package Structure

```
pio-music-finder/
├── pyproject.toml          # Project configuration
├── README.md              # Project documentation
├── main.py               # Entry point
├── src/                  # Source code
│   └── pio_music_finder/ # Package modules
├── tests/               # Test files
└── docs/               # Documentation
```

## Development Workflow

1. **Create virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

2. **Install in development mode:**
   ```bash
   pip install -e ".[dev]"
   ```

3. **Run tests:**
   ```bash
   pytest
   ```

4. **Format code:**
   ```bash
   black .
   ```

5. **Type checking:**
   ```bash
   mypy src/
   ```

## Building and Distribution

```bash
# Build the package
pip install build
python -m build

# Upload to PyPI (requires account)
pip install twine
twine upload dist/*
```

## Key Benefits of pyproject.toml

- **Single configuration file** for all project settings
- **Optional dependencies** for different use cases
- **Modern Python packaging** standards (PEP 518, 621)
- **Tool configuration** in one place (black, pytest, mypy)
- **Better dependency resolution** than requirements.txt