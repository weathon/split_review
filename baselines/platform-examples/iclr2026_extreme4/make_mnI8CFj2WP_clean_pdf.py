from pathlib import Path
import html
import re
import subprocess
import sys


sys.path.insert(0, "/home/wg25r/review_agent")
from fetch_iclr import pdf_to_markdown


paper_id = "mnI8CFj2WP"
new_title = "Autoregressive Modeling Across Scales for 3D Generation and Understanding"
root = Path("/home/wg25r/split_review/baselines/platform-examples/iclr2026_extreme4")
pdf_path = root / "original_pdfs" / f"{paper_id}.pdf"
raw_md_path = root / "raw_markdown" / f"{paper_id}.txt"
clean_md_path = root / "clean_text" / f"{paper_id}.txt"
html_path = root / "html" / f"{paper_id}.html"
clean_pdf_path = root / "papers" / f"{paper_id}.pdf"

for folder in [raw_md_path.parent, clean_md_path.parent, html_path.parent, clean_pdf_path.parent]:
    folder.mkdir(parents=True, exist_ok=True)

if raw_md_path.exists():
    markdown = raw_md_path.read_text(encoding="utf-8")
else:
    markdown = pdf_to_markdown(pdf_path)
    raw_md_path.write_text(markdown, encoding="utf-8")

text = markdown
text = re.sub(r"(?m)^\{\d+\}-+\s*$\n?", "", text)
text = re.sub(r"(?m)^# .+$", f"# {new_title}", text, count=1)
text = re.sub(r"(?mi)^\*{0,2}anonymous authors\*{0,2}\s*$\n?", "", text)
text = re.sub(r"(?mi)^paper under double-blind review\s*$\n?", "", text)
text = re.sub(r"(?mi)^under review as a conference paper at iclr \d{4}\s*$\n?", "", text)
text = re.sub(r"(?mi)^submitted to iclr \d{4}\s*$\n?", "", text)
text = re.sub(r"(?mi)^iclr \d{4} (poster|oral|conference withdrawn submission).*$\n?", "", text)
text = re.sub(r"(?m)^\s*\d{3}\s*$\n?", "", text)
text = re.sub(r"(?m)^-\s*\d{3}\s*$\n?", "", text)
text = re.sub(r"(?m)^(\s*)\d{3}\s+", r"\1", text)
text = re.sub(r"(?m)^\*\*\d{3}(?:\s+\d{3})*\*\*\s*", "", text)
text = re.sub(r"\n{4,}", "\n\n\n", text).strip() + "\n"
clean_md_path.write_text(text, encoding="utf-8")

html_path.write_text(
    f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>{html.escape(new_title)}</title>
  <style>
    @page {{ margin: 0.65in; }}
    body {{ font-family: "Times New Roman", serif; font-size: 10.5pt; line-height: 1.25; }}
    pre {{ white-space: pre-wrap; overflow-wrap: anywhere; font-family: inherit; }}
  </style>
</head>
<body>
<pre>{html.escape(text)}</pre>
</body>
</html>
""",
    encoding="utf-8",
)

subprocess.run(
    [
        "google-chrome",
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",
        f"--print-to-pdf={clean_pdf_path}",
        html_path.as_uri(),
    ],
    check=True,
)

print(f"raw_markdown={raw_md_path}")
print(f"clean_text={clean_md_path}")
print(f"clean_pdf={clean_pdf_path}")
