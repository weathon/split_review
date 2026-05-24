from pathlib import Path
import fitz


root = Path("/home/wg25r/split_review/baselines/platform-examples/iclr2026_random5_leak_probe")
source_dir = root / "original_pdfs"
out_dir = root / "redacted_original_submit" / "papers"
out_dir.mkdir(parents=True, exist_ok=True)

papers = {
    "BxGrZFfTp5": "BEV Perception for Legged Robots in Urban Environments",
    "aUsx1G6RVQ": "Neural Global Reasoning over Relational Structures",
    "NvhXAt1I2Q": "Benchmarking Virtual Try-On Models for Practical Deployment",
    "yYPQvuaHkc": "Decomposed Attention Models for Satellite Orbit Forecasting",
    "iutupTjoZo": "Multi-Frequency Motion Analysis for Text-to-Motion Retrieval",
}

for paper_id, new_title in papers.items():
    src = source_dir / f"{paper_id}.pdf"
    dst = out_dir / f"{paper_id}.pdf"
    doc = fitz.open(src)
    page = doc[0]
    page.add_redact_annot(fitz.Rect(100, 22, 330, 44), fill=(1, 1, 1))
    page.add_redact_annot(fitz.Rect(95, 68, 530, 186), fill=(1, 1, 1))
    page.apply_redactions()
    page.insert_textbox(
        fitz.Rect(108, 72, 504, 150),
        new_title,
        fontsize=14,
        fontname="helv",
        align=1,
        color=(0, 0, 0),
    )
    doc.set_metadata({"title": new_title, "author": "redacted", "creator": "split_review leak probe"})
    doc.save(dst, garbage=4, deflate=True)
    doc.close()
    print(f"{paper_id}: {dst}")
