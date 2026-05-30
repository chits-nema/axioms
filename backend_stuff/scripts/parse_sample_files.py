from __future__ import annotations

from pathlib import Path

from app.services.file_parser import ParserError, parse_file


SAMPLE_DIR = Path(__file__).resolve().parents[1] / "app" / "storage" / "uploads" / "samples"


def main() -> None:
    if not SAMPLE_DIR.exists():
        raise SystemExit("No samples found. Run: python scripts/create_sample_files.py")

    for path in sorted(SAMPLE_DIR.iterdir()):
        if not path.is_file():
            continue

        print(f"\n=== {path.name} ===")
        try:
            parsed = parse_file(path)
        except ParserError as exc:
            print(f"ParserError: {exc}")
            continue

        print(f"extension: {parsed.extension}")
        print(f"text_chars: {len(parsed.text)}")
        print(f"pages: {len(parsed.pages)}")
        print(f"tables: {len(parsed.tables)}")
        if parsed.warnings:
            print(f"warnings: {' | '.join(parsed.warnings)}")

        preview = parsed.text[:700].replace("\n", " ")
        print(f"preview: {preview}")

        for table in parsed.tables:
            print(f"table {table.label}: {len(table.rows)} rows")
            if table.rows:
                print(f"first row: {table.rows[0]}")


if __name__ == "__main__":
    main()
