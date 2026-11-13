from pathlib import Path
import importlib.util

PROJECT_NAME = "AI Documentary Studio"

FOLDERS = [
    "assets",
    "assets/music",
    "assets/images",
    "assets/fonts",
    "scripts",
    "audio",
    "scenes",
    "exports",
]

def setup_project():
    print(f"\n=== {PROJECT_NAME} ===")

    for folder in FOLDERS:
        Path(folder).mkdir(parents=True, exist_ok=True)

    print("\nProject folders created.")

    packages = [
        "moviepy",
        "PIL",
        "numpy",
        "edge_tts",
    ]

    print("\nChecking dependencies:")

    for package in packages:
        installed = importlib.util.find_spec(package) is not None
        status = "Installed" if installed else "Missing"
        print(f"{package}: {status}")

    print("\nStudio setup complete!")

if __name__ == "__main__":
    setup_project()
