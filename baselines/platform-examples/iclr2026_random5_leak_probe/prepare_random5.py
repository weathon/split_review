from pathlib import Path
import csv
import html
import json
import re
import subprocess
import sys


sys.path.insert(0, "/home/wg25r/review_agent")
from fetch_iclr import download_pdf, get_or_client, pdf_to_markdown


root = Path("/home/wg25r/split_review/baselines/platform-examples/iclr2026_random5_leak_probe")
original_pdf_dir = root / "original_pdfs"
raw_submit_dir = root / "raw_original_submit" / "papers"
raw_markdown_dir = root / "raw_markdown"
clean_text_dir = root / "edited_submit" / "clean_text"
html_dir = root / "edited_submit" / "html"
edited_pdf_dir = root / "edited_submit" / "papers"

for folder in [original_pdf_dir, raw_submit_dir, raw_markdown_dir, clean_text_dir, html_dir, edited_pdf_dir]:
    folder.mkdir(parents=True, exist_ok=True)

papers = [
    {
        "paper_id": "BxGrZFfTp5",
        "avg_score": "6.00",
        "decision": "Reject",
        "scores": "6 4 8",
        "title": "L4Dog: Towards BEV Perception for Quadruped Robots in Complex Urban Scenes",
        "new_title": "BEV Perception for Legged Robots in Urban Environments",
    },
    {
        "paper_id": "aUsx1G6RVQ",
        "avg_score": "6.00",
        "decision": "Reject",
        "scores": "6 6 4 8",
        "title": "FLOYDNET: A LEARNING PARADIGM FOR GLOBAL RELATIONAL REASONING",
        "new_title": "Neural Global Reasoning over Relational Structures",
    },
    {
        "paper_id": "NvhXAt1I2Q",
        "avg_score": "6.00",
        "decision": "Reject",
        "scores": "6 8 4",
        "title": "VTBench: Comprehensive Benchmark Suite Towards Real-World Virtual Try-on Models",
        "new_title": "Benchmarking Virtual Try-On Models for Practical Deployment",
    },
    {
        "paper_id": "yYPQvuaHkc",
        "avg_score": "6.00",
        "decision": "Reject",
        "scores": "4 8 4 8",
        "title": "Decomposed Attention FredFormer: Large Time-series Prediction Model for Satellite Orbit Prediction",
        "new_title": "Decomposed Attention Models for Satellite Orbit Forecasting",
    },
    {
        "paper_id": "iutupTjoZo",
        "avg_score": "6.00",
        "decision": "Reject",
        "scores": "8 4 4 8",
        "title": "WaMo: Wavelet-Enhanced Multi-Frequency Trajectory Analysis for Fine-Grained Text-Motion Retrieval",
        "new_title": "Multi-Frequency Motion Analysis for Text-to-Motion Retrieval",
    },
]

notes = {row["paper_id"]: row for row in json.load(open("/home/wg25r/review_agent/iclr2026_new/all_notes.json"))}
client = get_or_client()

with open(root / "selected.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["paper_id", "avg_score", "decision", "scores", "title", "new_title", "pdf_url"])
    writer.writeheader()
    for paper in papers:
        note = notes[paper["paper_id"]]
        row = dict(paper)
        row["pdf_url"] = note["pdf_url"]
        writer.writerow(row)

for paper in papers:
    paper_id = paper["paper_id"]
    original_pdf = download_pdf(client, paper_id, original_pdf_dir)
    raw_submit_pdf = raw_submit_dir / f"{paper_id}.pdf"
    raw_submit_pdf.write_bytes(original_pdf.read_bytes())

    raw_md_path = raw_markdown_dir / f"{paper_id}.txt"
    if raw_md_path.exists():
        markdown = raw_md_path.read_text(encoding="utf-8")
    else:
        markdown = pdf_to_markdown(original_pdf)
        raw_md_path.write_text(markdown, encoding="utf-8")

    text = markdown
    text = re.sub(r"(?m)^\{\d+\}-+\s*$\n?", "", text)
    text = re.sub(r"(?m)^# .+$", f"# {paper['new_title']}", text, count=1)
    text = re.sub(r"(?mi)^\*{0,2}anonymous authors\*{0,2}\s*$\n?", "", text)
    text = re.sub(r"(?mi)^paper under double-blind review\s*$\n?", "", text)
    text = re.sub(r"(?mi)^under review as a conference paper at iclr \d{4}\s*$\n?", "", text)
    text = re.sub(r"(?mi)^submitted to iclr \d{4}\s*$\n?", "", text)
    text = re.sub(r"(?mi)^iclr \d{4} (poster|oral|conference withdrawn submission).*$\n?", "", text)
    text = re.sub(r"(?mi)^accepted as.*$\n?", "", text)
    text = re.sub(r"(?mi)^rejected.*$\n?", "", text)
    text = re.sub(r"(?m)^\s*\d{3}\s*$\n?", "", text)
    text = re.sub(r"(?m)^-\s*\d{3}\s*$\n?", "", text)
    text = re.sub(r"(?m)^(\s*)\d{3}\s+", r"\1", text)
    text = re.sub(r"(?m)^\*\*\d{3}(?:\s+\d{3})*\*\*\s*", "", text)
    text = re.sub(r"\n{4,}", "\n\n\n", text).strip() + "\n"

    clean_text_path = clean_text_dir / f"{paper_id}.txt"
    clean_text_path.write_text(text, encoding="utf-8")

    html_path = html_dir / f"{paper_id}.html"
    html_path.write_text(
        f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>{html.escape(paper['new_title'])}</title>
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
    edited_pdf = edited_pdf_dir / f"{paper_id}.pdf"
    subprocess.run(
        [
            "google-chrome",
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            "--no-pdf-header-footer",
            f"--print-to-pdf={edited_pdf}",
            html_path.as_uri(),
        ],
        check=True,
    )
    print(f"{paper_id}: raw={raw_submit_pdf} edited={edited_pdf}")
