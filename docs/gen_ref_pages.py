"""Generate the code reference pages and navigation.

Recursively search through the project, then write Markdown files with the module paths and organise them appropriately.
Directly relies on the `mkdocs-gen-files` and `mkdocs-literate-nav` packages. Additional configuration allowed by
`mkdocs-section-index`.
"""

from pathlib import Path

import mkdocs_gen_files

nav = mkdocs_gen_files.Nav()
SOURCE: Path = Path(__file__).parents[1]
DOC_INJECTION_PATH: Path = Path("reference")
SUMMARY_PATH: Path = DOC_INJECTION_PATH / "SUMMARY.md"

for path in sorted(SOURCE.rglob("my_project/**/*.py")):
    module_path = path.relative_to(SOURCE).with_suffix("")
    doc_path = path.relative_to(SOURCE).with_suffix(".md")
    full_doc_path = DOC_INJECTION_PATH / doc_path

    parts = module_path.parts

    if parts[-1] == "__init__":
        parts = parts[:-1]
        doc_path = doc_path.with_name("index.md")
        full_doc_path = full_doc_path.with_name("index.md")
    elif parts[-1] == "__main__":
        continue

    nav[parts] = doc_path.as_posix()

    with mkdocs_gen_files.open(full_doc_path, "w") as fd:
        ident = ".".join(parts)
        fd.write(f"::: {ident}")

    mkdocs_gen_files.set_edit_path(full_doc_path, path)

with mkdocs_gen_files.open(SUMMARY_PATH, "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())
