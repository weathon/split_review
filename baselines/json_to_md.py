import json, glob, os

SRC_DIRS = [
    "/home/wg25r/split_review/baselines/consolidated_reviews_2025/v1_DeepReviewer_7B_TXT",
    "/home/wg25r/split_review/baselines/consolidated_reviews_2025/v1_DeepReviewer_14B_TXT",
]

for src in SRC_DIRS:
    dst = src + "_MD"
    os.makedirs(dst, exist_ok=True)
    n = 0
    for fn in sorted(glob.glob(os.path.join(src, "*.json"))):
        with open(fn) as f:
            d = json.load(f)
        r = d["results"][0]
        paper_id = d["file"].replace(".txt", "")
        for rev in r["reviews"]:
            out_path = os.path.join(dst, f"{paper_id}_reviewer{rev['reviewer_id']}.md")
            with open(out_path, "w") as f:
                f.write(rev["text"].strip() + "\n")
            n += 1
        meta_path = os.path.join(dst, f"{paper_id}_meta.md")
        m = r["meta_review"]
        meta_lines = [
            f"# {paper_id} — Meta Review",
            "",
            f"- Model: {d['model_type']} {d['model_size']}",
            f"- Decision: {r['decision']}",
            f"- Rating: {m.get('rating')}",
            f"- Soundness: {m.get('soundness')}",
            f"- Presentation: {m.get('presentation')}",
            f"- Contribution: {m.get('contribution')}",
            "",
            "## Summary", "", (m.get("summary") or "").strip(), "",
            "## Strengths", "", (m.get("strengths") or "").strip(), "",
            "## Weaknesses", "", (m.get("weaknesses") or "").strip(), "",
            "## Suggestions", "", (m.get("suggestions") or "").strip(), "",
            "## Questions", "", (m.get("questions") or "").strip(), "",
            "## Full Content", "", (m.get("content") or "").strip(), "",
        ]
        with open(meta_path, "w") as f:
            f.write("\n".join(meta_lines))
        n += 1
    print(f"wrote {n} files to {dst}")
