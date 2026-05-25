from agents import Agent, Runner, function_tool
import os

from paths import DATASETS_DIR, ensure_hf_file

_position_mode = os.getenv("POSITION_MODE", "").strip().lower() in ("1", "true", "yes")
_calibration_env = os.getenv("CALIBRATION_SET", "deepreview").strip().lower()
if _position_mode:
    if _calibration_env not in ("", "deepreview", "position"):
        raise ValueError(
            f"POSITION_MODE is set but CALIBRATION_SET={_calibration_env!r}; "
            "these are mutually exclusive (unset CALIBRATION_SET or POSITION_MODE)."
        )
    CALIBRATION_REVIEW_DIR = str((DATASETS_DIR / "neurips_position_human_review").resolve())
    _embeddings_path = ensure_hf_file("human_reviews_embeddings_position.pkl")
    _score_index_path = ensure_hf_file("human_review_score_index_position.pkl")
    _calibration_set = "position"
elif _calibration_env in ("2025", "iclr2025"):
    CALIBRATION_REVIEW_DIR = os.path.expanduser("~/review_agent/human_reviews")
    _embeddings_path = os.path.expanduser("~/review_agent/new/human_reviews_embeddings.pkl")
    _score_index_path = os.path.expanduser("~/review_agent/new/human_review_score_index.pkl")
    _calibration_set = "iclr2025"
elif _calibration_env in ("2026", "iclr2026"):
    CALIBRATION_REVIEW_DIR = os.path.expanduser("~/review_agent/human_reviews_2026")
    _embeddings_path = os.path.expanduser("~/review_agent/new/human_reviews_embeddings_2026.pkl")
    _score_index_path = os.path.expanduser("~/review_agent/new/human_review_score_index_2026.pkl")
    _calibration_set = "iclr2026"
elif _calibration_env in ("ai_cal", "ai-cal"):
    CALIBRATION_REVIEW_DIR = str((DATASETS_DIR / "ai_review_cal").resolve())
    _embeddings_path = str((DATASETS_DIR / "human_reviews_embeddings_ai_cal.pkl").resolve())
    _score_index_path = str((DATASETS_DIR / "human_review_score_index_ai_cal.pkl").resolve())
    _calibration_set = "ai_cal"
elif _calibration_env in ("", "deepreview"):
    CALIBRATION_REVIEW_DIR = str((DATASETS_DIR / "deepreview_13k_calibration").resolve())
    _embeddings_path = ensure_hf_file("human_reviews_embeddings_deepreview.pkl")
    _score_index_path = ensure_hf_file("human_review_score_index_deepreview.pkl")
    _calibration_set = "deepreview"
else:
    raise ValueError(
        f"Unknown CALIBRATION_SET={_calibration_env!r}; expected one of "
        "'deepreview', '2025', '2026', 'ai_cal' (or unset)."
    )

PAPERS_DIR = os.path.expanduser(os.environ["PAPERS_DIR"]) if os.environ.get("PAPERS_DIR") else None

from rank_bm25 import BM25Okapi
from openai import OpenAI
import dotenv
dotenv.load_dotenv()

or_client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY"))
# ── Build Index ────────────────────────────────────────────────
import time
print(f"Indexing calibration corpus '{_calibration_set}' from {CALIBRATION_REVIEW_DIR} ...")
start = time.time()
database = {}
for path in [CALIBRATION_REVIEW_DIR]:
    all_files = []
    all_file_paths = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt") or file.endswith(".md"):
                with open(os.path.join(root, file), "r", errors="replace") as f:
                    all_files.append(f.read())
                    all_file_paths.append(os.path.join(root, file))

    tokenized_corpus = [doc.split(" ") for doc in all_files if doc.strip()]
    if not tokenized_corpus:
        print(f"  Skipping {path} (no files found)")
        continue
    bm25 = BM25Okapi(tokenized_corpus)
    database[path] = {"files": all_file_paths, "bm25": bm25}
    
print("Indexing complete. Time taken: {:.2f}s".format(time.time() - start))


import numpy as np
with open(_embeddings_path, "rb") as f:
    import pickle
    db = pickle.load(f)

filenames = list(db.keys())
vectors = np.array(list(db.values()))

# Per-file avg human score (basename -> float). Used to pre-filter candidates
# by score range before BM25/vector ranking.
with open(_score_index_path, "rb") as f:
    _score_index: dict[str, float] = pickle.load(f)


# ── Tools ────────────────────────────────────────────────────────────
_PAPERS_DIR_HOLDER = {"dir": PAPERS_DIR}


def set_papers_dir(path: str):
    """Set the directory holding {paper_id}.txt files (per-benchmark, runtime)."""
    _PAPERS_DIR_HOLDER["dir"] = os.path.abspath(path)


def _paper_path(paper_id: str) -> str:
    papers_dir = _PAPERS_DIR_HOLDER["dir"]
    if papers_dir is None:
        raise RuntimeError("PAPERS_DIR not set (env PAPERS_DIR or set_papers_dir())")
    for ext in (".txt", ".md"):
        cand = os.path.join(papers_dir, f"{paper_id}{ext}")
        if os.path.isfile(cand):
            return cand
    return os.path.join(papers_dir, f"{paper_id}.txt")


@function_tool
def read_paper(paper_id: str) -> str:
    """Read the full text of the paper under review, by its id (no path, no extension)."""
    path = _paper_path(paper_id)
    print(f"  [read_paper] {paper_id} -> {path}")
    if not os.path.isfile(path):
        return f"ERROR: paper '{paper_id}' not found at {path}"
    with open(path, "r", errors="replace") as f:
        return f.read()


@function_tool
def grep_paper(paper_id: str, pattern: str) -> str:
    """Search the paper under review (by id) for a regex pattern. Returns matching lines with line numbers."""
    import re
    path = _paper_path(paper_id)
    print(f"  [grep_paper] {paper_id} pattern='{pattern}'")
    if not os.path.isfile(path):
        return f"ERROR: paper '{paper_id}' not found at {path}"
    matches = []
    try:
        with open(path, "r", errors="replace") as fh:
            for i, line in enumerate(fh, 1):
                if re.search(pattern, line):
                    matches.append(f"{i}: {line.rstrip()}")
    except Exception as e:
        return f"ERROR: {e}"
    return "\n".join(matches) if matches else "No matches found."


@function_tool
def read_anchor(anchor_id: str) -> str:
    """Read the full text of a human-review calibration anchor, by the id returned from search_file."""
    path = os.path.join(CALIBRATION_REVIEW_DIR, f"{anchor_id}.md")
    print(f"  [read_anchor] {anchor_id} -> {path}")
    if not os.path.isfile(path):
        return f"ERROR: anchor '{anchor_id}' not found at {path}"
    with open(path, "r", errors="replace") as f:
        return f.read()


EXCLUDED_PAPER_IDS: set[str] = set()


def set_excluded_paper_ids(ids) -> None:
    """Exclude these paper IDs (basename without extension) from calibration search results.

    Used so that papers being scored in the current benchmark run are not also
    retrieved as calibration anchors for themselves.
    """
    EXCLUDED_PAPER_IDS.clear()
    EXCLUDED_PAPER_IDS.update(ids)
    print(f"  [calibration] excluding {len(EXCLUDED_PAPER_IDS)} test paper id(s) from calibration search")


def _is_excluded(basename: str) -> bool:
    if not EXCLUDED_PAPER_IDS:
        return False
    pid = basename.rsplit(".", 1)[0]
    return pid in EXCLUDED_PAPER_IDS


def _search_file_impl(query: str, n: int, mode: str, low_score: float = -1.0, high_score: float = 11.0) -> str:
    """Search human reviews, optionally filtered by the reviewer avg-score range.

    Args:
        query: search query.
        n: number of top results.
        mode: 'vector' for semantic similarity, 'bm25' for keyword matching.
        low_score: include only papers with avg score > low_score (default -1.0).
        high_score: include only papers with avg score < high_score (default 11.0).

    Filtering is applied FIRST by score range, THEN ranking (BM25/vector) runs
    over the filtered subset. Use this to anchor calibration to a specific
    score band (e.g. low_score=7, high_score=10 for strong papers).

    Each result gives an `anchor_id`; pass it to read_anchor to read the full review.
    """
    print(f"  [search_file] query='{query}' mode='{mode}' n={n} score=({low_score}, {high_score})")
    if mode == "bm25":
        bm25 = list(database.values())[0]["bm25"]
        files = list(database.values())[0]["files"]
        allowed_idx = [
            i for i, p in enumerate(files)
            if low_score < _score_index.get(os.path.basename(p), -1.0) < high_score
            and not _is_excluded(os.path.basename(p))
        ]
        if not allowed_idx:
            return "No files in that score range."
        tokenized_query = query.split(" ")
        doc_scores = bm25.get_scores(tokenized_query)
        allowed_sorted = sorted(allowed_idx, key=lambda i: doc_scores[i], reverse=True)[:n]
        results = []
        for idx in allowed_sorted:
            file_path = os.path.abspath(files[idx])
            anchor_id = os.path.basename(file_path).rsplit(".", 1)[0]
            rel = doc_scores[idx]
            avg = _score_index.get(os.path.basename(file_path), -1.0)
            with open(file_path, 'r', errors='replace') as f:
                content = f.read()
            results.append(f"anchor_id: {anchor_id}\navg_score: {avg:.2f}  bm25: {rel:.2f}\n first 1000 chars:\n{content[:1000]}\n")
        return "\n---\n".join(results) if results else "No relevant files found."
    elif mode == "vector":
        allowed_mask = np.array([
            low_score < _score_index.get(fn, -1.0) < high_score and not _is_excluded(fn)
            for fn in filenames
        ])
        if not allowed_mask.any():
            return "No files in that score range."
        query_embedding = or_client.embeddings.create(
            model="google/gemini-embedding-001",
            input=query,
            encoding_format="float"
        )
        query_vector = np.array(query_embedding.data[0].embedding)
        similarities = vectors @ query_vector.T
        masked = np.where(allowed_mask, similarities, -np.inf)
        top_indices = masked.argsort()[-n:][::-1]
        results = []
        for idx in top_indices:
            if not np.isfinite(masked[idx]):
                break
            fn = filenames[idx]
            anchor_id = fn.rsplit(".", 1)[0]
            file_path = os.path.abspath(os.path.join(CALIBRATION_REVIEW_DIR, fn))
            rel = similarities[idx]
            avg = _score_index.get(fn, -1.0)
            with open(file_path, "r", errors="replace") as file_handle:
                content = file_handle.read()
            results.append(f"anchor_id: {anchor_id}\navg_score: {avg:.2f}  sim: {rel:.2f}\n first 1000 chars:\n{content[:1000]}\n")
        return "\n---\n".join(results) if results else "No relevant files found."
    else:
        return "ERROR: Invalid search mode. Use 'bm25' or 'vector'."


@function_tool
def search_file(query: str, n: int, mode: str, low_score: float = -1.0, high_score: float = 11.0) -> str:
    """Search human reviews, optionally filtered by the reviewer avg-score range.

    Args:
        query: search query.
        n: number of top results.
        mode: 'vector' for semantic similarity, 'bm25' for keyword matching.
        low_score: include only papers with avg score > low_score (default -1.0).
        high_score: include only papers with avg score < high_score (default 11.0).

    Filtering is applied FIRST by score range, THEN ranking (BM25/vector) runs
    over the filtered subset. Use this to anchor calibration to a specific
    score band (e.g. low_score=7, high_score=10 for strong papers).

    Each result gives an `anchor_id`; pass it to read_anchor to read the full review.
    """
    return _search_file_impl(query, n, mode, low_score, high_score)
