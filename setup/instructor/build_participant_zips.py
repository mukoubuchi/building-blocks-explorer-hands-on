"""Build localized workshop packages from an explicit, reviewed file list."""

from pathlib import Path
import argparse
import zipfile

ROOT = Path(__file__).resolve().parents[2]
FILES = ("README.md",)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    output = parser.parse_args().output
    output.mkdir(parents=True, exist_ok=True)
    for locale in ("en", "ja"):
        stem = f"building-blocks-explorer-workshop-{locale}"
        target = output / f"{stem}.zip"
        with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
            for name in FILES:
                source = ROOT / "setup" / "participant" / locale / name
                if source.is_symlink() or not source.is_file():
                    raise ValueError(f"Expected regular file: {source}")
                # Fixed metadata keeps packages reproducible across platforms.
                entry = zipfile.ZipInfo(f"{stem}/{name}", (2026, 9, 10, 0, 0, 0))
                entry.compress_type = zipfile.ZIP_DEFLATED
                entry.external_attr = 0o100644 << 16
                archive.writestr(entry, source.read_bytes())
            entry = zipfile.ZipInfo(f"{stem}/LICENSE", (2026, 9, 10, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, (ROOT / "LICENSE").read_bytes())
        with zipfile.ZipFile(target) as archive:
            assert archive.testzip() is None
            assert set(archive.namelist()) == {f"{stem}/{name}" for name in (*FILES, "LICENSE")}
        print(target)


if __name__ == "__main__":
    main()
