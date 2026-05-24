from pathlib import Path
import html
import re
import subprocess


SOURCE_DIR = Path("/home/wg25r/review_agent/iclr2026_new/papers")
OUT_DIR = Path("/home/wg25r/split_review/baselines/platform-examples/iclr2026_leak_probe3")
TEXT_DIR = OUT_DIR / "clean_text"
HTML_DIR = OUT_DIR / "html"
PDF_DIR = OUT_DIR / "papers"

papers = {
    "cu6xWUNOzQ": "Nonlinear Multimodal Models for Predicting Brain Responses to Speech",
    "zS1bPtMlt9": "Refining Pseudo-Labels for Semi-Supervised LiDAR Segmentation",
    "zKQSyT7a7n": "Contact-Grounded World Models for Robot Manipulation",
}

TEXT_DIR.mkdir(parents=True, exist_ok=True)
HTML_DIR.mkdir(parents=True, exist_ok=True)
PDF_DIR.mkdir(parents=True, exist_ok=True)

for paper_id, new_title in papers.items():
    source_path = SOURCE_DIR / f"{paper_id}.txt"
    text = source_path.read_text(encoding="utf-8")
    text = re.sub(r"(?m)^# .+$", f"# {new_title}", text, count=1)
    text = re.sub(r"(?mi)^\*{0,2}anonymous authors\*{0,2}\s*$\n?", "", text)
    text = re.sub(r"(?mi)^paper under double-blind review\s*$\n?", "", text)
    text = re.sub(r"(?mi)^submitted to iclr 2026\s*$\n?", "", text)
    text = re.sub(r"(?mi)^iclr 2026 (poster|oral|conference withdrawn submission).*$\n?", "", text)

    clean_text_path = TEXT_DIR / f"{paper_id}.txt"
    clean_text_path.write_text(text, encoding="utf-8")

    html_path = HTML_DIR / f"{paper_id}.html"
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

    pdf_path = PDF_DIR / f"{paper_id}.pdf"
    subprocess.run(
        [
            "google-chrome",
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_path}",
            html_path.as_uri(),
        ],
        check=True,
    )
    print(f"{paper_id}: {clean_text_path} -> {html_path} -> {pdf_path}")
