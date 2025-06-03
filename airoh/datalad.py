# src/airoh/datalad.py
from invoke import task
import os

@task
def get_data(c, name):
    """
    Ensure a Datalad subdataset is installed and retrieved.

    Parameters:
        name (str): Name of the dataset as defined in invoke.yaml under 'datasets'.
    """
    datasets = c.config.get("datasets", {})
    if name not in datasets:
        raise ValueError(f"❌ Dataset '{name}' not found in invoke.yaml under 'datasets'.")

    path = datasets[name]
    print(f"📦 Checking dataset '{name}' at: {path}")

    if not os.path.exists(path):
        print(f"📥 Installing subdataset '{name}'...")
        c.run(f"datalad install --recursive {path}")

    print(f"📥 Retrieving data for '{name}'...")
    c.run(f"datalad get {path}")
    print("✅ Done.")

@task
def import_archive(c, url, archive_name=None, target_dir=".", drop_archive=False):
    """
    Download a remote archive (e.g. from Zenodo) and extract its content with Datalad.

    Parameters:
        url (str): URL to the archive (e.g. .zip, .tar.gz)
        archive_name (str): Optional filename (default: basename of URL)
        target_dir (str): Directory to extract into (default: current dir)
        drop_archive (bool): Whether to drop the original archive from annex after extraction
    """
    archive_name = archive_name or os.path.basename(url)
    archive_path = os.path.join(target_dir, archive_name)

    print(f"🌐 Downloading archive: {url}")
    c.run(f"datalad download-url -O {shlex.quote(archive_path)} {shlex.quote(url)}")

    print(f"📦 Extracting archive content into {target_dir}...")
    c.run(f"datalad add-archive-content --delete --extract {shlex.quote(archive_path)} -d {shlex.quote(target_dir)}")

    if drop_archive:
        print(f"🧹 Dropping archive from annex: {archive_path}")
        c.run(f"datalad drop {shlex.quote(archive_path)}")

    print("✅ Archive import complete.")
