# src/airoh/utils.py
import os
import shutil
from pathlib import Path
from invoke import task

@task
def setup_env_python(c, reqs="requirements.txt"):
    """
    Set up Python environment by installing from a requirements file.
    """
    if not os.path.exists(reqs):
        raise FileNotFoundError(f"⚠️ Requirements file not found: {reqs}")

    print(f"🐍 Installing Python requirements from {reqs}...")
    c.run(f"pip install -r {reqs}")

def clean_folder(dir_name, label=None):
    """
    Remove an entire directory recursively. Use with caution!!!
    """
    label = label or dir_name
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
        print(f"💥 Removed {label} at {dir_name}")
    else:
        print(f"🫧 Nothing to clean: {label}")

@task
def run_figures(c, notebooks_path=None, figures_base=None):
    """
    Run figure notebooks, skipping any that already have output folders.
    Notebooks directory and output location pulled from invoke.yaml.
    """
    import pathlib as lib

    notebooks_path = Path(notebooks_path or c.config.get("notebooks_dir", "code/figures"))
    figures_base = Path(figures_base or c.config.get("figures_dir", "output_data/Figures"))

    if not notebooks_path.exists():
        print(f"⚠️ Notebooks directory not found: {notebooks_path}")
        return

    notebooks = sorted(notebooks_path.glob("*.ipynb"))

    if not notebooks:
        print(f"⚠️ No notebooks found in {notebooks_path}/")
        return

    for nb in notebooks:
        fig_name = nb.stem
        fig_output_dir = figures_base / fig_name

        if fig_output_dir.exists():
            print(f"✅ Skipping {nb.name} (output exists at {fig_output_dir})")
            continue

        print(f"📈 Running {nb.name}...")
        c.run(f"jupyter nbconvert --to notebook --execute --inplace {nb}")

    print("🎉 All figure notebooks processed.")
