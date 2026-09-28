"""
Criterion 4 — measure chunk quality.

criteria.md asks three things of the chunks that `chunker.py::split_documents`
produces:

  1. At least 95% end on '.', '!' or '?'
  2. No chunk is under 100 characters
  3. 100% of chunks from the nine town guides contain the town's name

`run_eval.py` measures criteria 1-3, which depend on retrieval and the model.
This measures criterion 4, which depends only on the chunker, so it needs no
API calls and gives the same answer every time.

Run it with:  python check_chunks.py
"""

import config
from chunker import split_documents
from ingest import load_documents

# The nine town guides and the town each one is about. The other five
# documents in the corpus (accessibility, eating, regional_transport,
# seasons, walking) are region-wide and are not expected to name a town.
TOWN_GUIDES = {
    "guide_brightwater.md": "Brightwater",
    "guide_corry_vale.md": "Corry Vale",
    "guide_elder_ness.md": "Elder Ness",
    "guide_givens_mill.md": "Givens Mill",
    "guide_halden_bay.md": "Halden Bay",
    "guide_kestrelford.md": "Kestrelford",
    "guide_marchwood.md": "Marchwood",
    "guide_pellew_sands.md": "Pellew Sands",
    "guide_thornby_wells.md": "Thornby Wells",
}

MIN_CHARS = 100


def report(corpus: str | None = None) -> None:
    """Print the three criterion 4 numbers, plus the chunks that fail."""
    chunks = split_documents(load_documents(corpus or config.CORPUS))
    total = len(chunks)

    ends_clean = [c for c in chunks if c.text.rstrip().endswith((".", "!", "?"))]
    too_short = [c for c in chunks if len(c.text) < MIN_CHARS]
    town_chunks = [c for c in chunks if c.source in TOWN_GUIDES]
    named = [c for c in town_chunks if TOWN_GUIDES[c.source].lower() in c.text.lower()]

    pct_clean = 100 * len(ends_clean) / total
    pct_named = 100 * len(named) / len(town_chunks)

    print(f"{total} chunks, produced by {chunks[0].produced_by}\n")

    print("1. Chunks ending on . ! or ?")
    print(f"   {len(ends_clean)}/{total} = {pct_clean:.1f}%   target >= 95%")
    print(f"   {'MET' if pct_clean >= 95 else 'MISSED'}\n")

    print(f"2. Chunks under {MIN_CHARS} characters")
    print(f"   {len(too_short)}   target 0")
    print(f"   {'MET' if not too_short else 'MISSED'}")
    for c in too_short:
        print(f"     {c.label}  ({len(c.text)} chars)  {c.text.splitlines()[0][:60]!r}")
    print()

    print("3. Town-guide chunks naming their town")
    print(f"   {len(named)}/{len(town_chunks)} = {pct_named:.1f}%   target 100%")
    print(f"   {'MET' if pct_named == 100 else 'MISSED'}")
    missing = [c for c in town_chunks if c not in named]
    print(f"   {len(missing)} chunks do not name their town, for example:")
    for c in missing[:5]:
        print(f"     {c.label}  {c.text.splitlines()[0][:60]!r}")


if __name__ == "__main__":
    report()
