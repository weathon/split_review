# %%
import re
import os
from pathlib import Path
import time

log_path = Path("../results/pipeline.log")
file = log_path.read_text(encoding="utf-8")

prompts = []
for block in file.split("\n" + "=" * 60 + "\n"):
    if not block.strip():
        continue

    paper_match = re.search(r"^Paper: (.+)$", block, re.MULTILINE)
    merger_input_match = re.search(
        r"--- Merged Inputs ---\n\n(.*?)\n--- Merged Review ---",
        block,
        re.DOTALL,
    )
    if paper_match is None or merger_input_match is None:
        raise RuntimeError(f"could not parse log block:\n{block[:1000]}")

    paper_path = paper_match.group(1).strip()
    prompts.append(
            f"Here is the paper being reviewed (extracted from PDF — formatting "
            f"artifacts are parser issues, not paper problems).\n\n"
            f"Paper path: {os.path.abspath(paper_path)} — use read_file (which reads the whole file by default; do not pass start_line/end_line unless you specifically need a slice) or grep_file to read it.\n\n"
            f"Here are the inputs:\n\n{merger_input_match.group(1).strip()}\n\n"
            f"Now produce the final consolidated review following your instructions. "
            f"Remember: many of the harsh critic's points may be nonsensical or overly "
            f"picky — cross-check everything against the actual paper before including it."
    )

with open("../prompts/merger.md", "r") as f:
    raw = f.readlines()

with open("../prompts/timeline.md", "r") as f:
    timeline = f.read().replace("{{CURRENT_DATE}}", time.strftime("%Y-%m-%d"))


kept = [line for line in raw if not line.lstrip().startswith("&&")]
text = "".join(kept)
text = text.replace("{{CALIBRATION_INSTRUCTION}}", "Assign a score based solely on your assessment of the paper's quality after review. ")
text = text + "\n\n" + timeline


# %%
