"""
Resample ../human_reviews to flatten the score distribution.

- Backs up ../human_reviews to ../human_reviews.bak.
- Backs up ./human_reviews_embeddings.pkl to ./human_reviews_embeddings.pkl.bak.
- Parses the '- Scores:' line from each review to get per-paper avg score.
- Bins by rounded avg_score; per-bin target = K + alpha * (count - K), capped at count.
- Writes the resampled files back to ../human_reviews (originals preserved in .bak).
- Filters the embeddings pkl to the resampled paper_ids.
"""
from __future__ import annotations

import os
import pickle
import random
import shutil
from collections import defaultdict
from pathlib import Path

HR_DIR = Path("../human_reviews").resolve()
HR_BAK = Path("../human_reviews.bak").resolve()
PKL = Path("./human_reviews_embeddings.pkl").resolve()
PKL_BAK = Path("./human_reviews_embeddings.pkl.bak").resolve()

K_UNIFORM = 363       # floor per main bin
ALPHA_MIX = 0.3       # fraction of original excess to mix in above K
SEED = 42


def parse_avg_score(path: Path) -> float | None:
    with open(path) as f:
        head = [next(f, "") for _ in range(15)]
    score_line = next((l for l in head if l.startswith("- Scores:")), None)
    if not score_line:
        return None
    nums_str = score_line.split(":", 1)[1].strip()
    try:
        nums = [float(x.strip()) for x in nums_str.split(",") if x.strip()]
    except ValueError:
        return None
    return sum(nums) / len(nums) if nums else None


def main():
    rng = random.Random(SEED)

    assert HR_DIR.exists(), f"{HR_DIR} does not exist"
    assert PKL.exists(), f"{PKL} does not exist"

    # Backups
    if HR_BAK.exists():
        print(f"[skip] {HR_BAK} already exists — not overwriting")
    else:
        print(f"Backing up {HR_DIR} -> {HR_BAK} (this copies ~17k files)")
        shutil.copytree(HR_DIR, HR_BAK)
    if PKL_BAK.exists():
        print(f"[skip] {PKL_BAK} already exists — not overwriting")
    else:
        print(f"Backing up {PKL} -> {PKL_BAK}")
        shutil.copy2(PKL, PKL_BAK)

    # Bin all review files by rounded avg_score
    bins: dict[int, list[str]] = defaultdict(list)
    skipped = 0
    for fn in sorted(os.listdir(HR_BAK)):
        if not fn.endswith(".md"):
            continue
        avg = parse_avg_score(HR_BAK / fn)
        if avg is None:
            skipped += 1
            continue
        bins[round(avg)].append(fn)
    print(f"\nBinned {sum(len(v) for v in bins.values())} reviews ({skipped} skipped).")
    for k in sorted(bins.keys()):
        print(f"  bin {k}: {len(bins[k])}")

    # Per-bin targets
    print(f"\nResampling with K={K_UNIFORM}, alpha={ALPHA_MIX}")
    keep: set[str] = set()
    for k in sorted(bins.keys()):
        count = len(bins[k])
        if count <= K_UNIFORM:
            target = count  # keep all in small bins
        else:
            target = int(K_UNIFORM + ALPHA_MIX * (count - K_UNIFORM))
            target = min(target, count)
        rng.shuffle(bins[k])
        picked = bins[k][:target]
        keep.update(picked)
        print(f"  bin {k}: {count} -> {len(picked)}")

    print(f"\nTotal kept: {len(keep)}")

    # Clear current HR_DIR and write the resampled subset (from the backup)
    # Note: HR_DIR and HR_BAK are separate copies now — HR_DIR still has the full 17k.
    print(f"\nWriting resampled subset to {HR_DIR}")
    # Delete files not in keep set
    removed = 0
    for fn in os.listdir(HR_DIR):
        if fn.endswith(".md") and fn not in keep:
            (HR_DIR / fn).unlink()
            removed += 1
    print(f"  removed {removed} files from {HR_DIR}")
    remaining = sum(1 for f in os.listdir(HR_DIR) if f.endswith(".md"))
    print(f"  remaining: {remaining}")

    # Filter embeddings pkl
    print(f"\nFiltering embeddings pkl")
    with open(PKL_BAK, "rb") as f:
        db = pickle.load(f)
    filtered = {k: v for k, v in db.items() if k in keep}
    print(f"  original entries: {len(db)}")
    print(f"  filtered entries: {len(filtered)}")
    missing_in_pkl = keep - set(db.keys())
    if missing_in_pkl:
        print(f"  WARN: {len(missing_in_pkl)} kept reviews have no embedding in pkl")
    with open(PKL, "wb") as f:
        pickle.dump(filtered, f)
    print(f"  wrote filtered pkl to {PKL}")


if __name__ == "__main__":
    main()
