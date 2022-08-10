from pathlib import Path

from toml import load

try:
    pyproject_toml_path: str = str(Path(__file__).resolve().parent / "pyproject.toml")
    config = load(pyproject_toml_path)["moboard"]
except FileNotFoundError:
    print(
        "File 'pyproject.toml' not found in same directory as config.py. This error is fatal,"
        " please fix."
    )
    raise
