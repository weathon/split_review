"""
Claude Agent SDK merger for main.py.
Used when MERGER_MODEL starts with 'claude_sdk:'.
"""
from __future__ import annotations

import os
import random
import time
import numpy as np
import pickle
from pathlib import Path
from rank_bm25 import BM25Okapi
from openai import OpenAI
import dotenv
dotenv.load_dotenv()

from paths import DATASETS_DIR, prompt_path as _prompt_path
_position_mode = False
HUMAN_REVIEW_DIR = str((DATASETS_DIR / "deepreview_13k_calibration").resolve())

# ── Build indexes (mirrors tools.py) ──────────────────────────────────
_bm25_db: dict = {}
_or_client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY"))

def _ensure_indexes():
    global _bm25_db, _vectors, _filenames
    if _bm25_db:
        return
    all_files = []
    all_file_paths = []
    for root, _, files in os.walk(HUMAN_REVIEW_DIR):
        for fname in files:
            if fname.endswith(".txt") or fname.endswith(".md"):
                fpath = os.path.join(root, fname)
                with open(fpath, "r", errors="replace") as fh:
                    content = fh.read()
                if content.strip():
                    all_files.append(content)
                    all_file_paths.append(fpath)
    tokenized = [doc.split(" ") for doc in all_files]
    _bm25_db["bm25"] = BM25Okapi(tokenized)
    _bm25_db["files"] = all_file_paths

    from paths import ensure_hf_file
    _emb_path = ensure_hf_file("human_reviews_embeddings_deepreview.pkl")
    _idx_path = ensure_hf_file("human_review_score_index_deepreview.pkl")
    with open(_emb_path, "rb") as f:
        db = pickle.load(f)
    _bm25_db["filenames"] = list(db.keys())
    _bm25_db["vectors"] = np.array(list(db.values()))

    with open(_idx_path, "rb") as f:
        _bm25_db["score_index"] = pickle.load(f)


def _make_merger_mcp_server(paper_dir: str, no_cal: bool = False):
    from claude_agent_sdk import create_sdk_mcp_server, tool

    if not no_cal:
        _ensure_indexes()
    allowed_paths = [paper_dir, HUMAN_REVIEW_DIR]

    def _check_path(path: str) -> str | None:
        resolved = os.path.abspath(path)
        if any(resolved.startswith(ap) for ap in allowed_paths):
            return None
        return f"ERROR: Access denied. Path '{resolved}' is not under any allowed directory: {allowed_paths}"

    @tool(
        "read_file",
        "Read lines from a file. Returns lines numbered start_line to end_line (1-based). If end_line is 0, reads to EOF.",
        {"abs_path": str, "start_line": int, "end_line": int},
    )
    async def _read_file(args: dict) -> dict:
        time.sleep(random.uniform(0.5, 1.5))  # Simulate latency
        abs_path = args["abs_path"]
        start_line = args.get("start_line", 1) or 1
        end_line = args.get("end_line", 0) or 0
        print(f"  [claude:read_file] {abs_path} lines {start_line}-{end_line or 'EOF'}")
        err = _check_path(abs_path)
        if err:
            return {"content": [{"type": "text", "text": err}], "is_error": True}
        try:
            with open(abs_path, "r", errors="replace") as fh:
                lines = fh.readlines()
            selected = lines[max(0, start_line - 1):end_line if end_line > 0 else len(lines)]
            text = "".join(f"{start_line + i}: {line}" for i, line in enumerate(selected))
            return {"content": [{"type": "text", "text": text}]}
        except FileNotFoundError:
            return {"content": [{"type": "text", "text": f"ERROR: File not found: {abs_path}"}], "is_error": True}

    @tool(
        "grep_file",
        "Search a single file for a substring pattern. Returns matching lines with line numbers.",
        {"pattern": str, "abs_path": str},
    )
    async def _grep_file(args: dict) -> dict:
        import re as _re
        pattern = args["pattern"]
        abs_path = args["abs_path"]
        print(f"  [merger:grep_file] pattern='{pattern}' in '{abs_path}'")
        err = _check_path(abs_path)
        if err:
            return {"content": [{"type": "text", "text": err}], "is_error": True}
        if not os.path.isfile(abs_path):
            return {"content": [{"type": "text", "text": f"ERROR: '{abs_path}' is not a file."}], "is_error": True}
        matches = []
        try:
            with open(abs_path, "r", errors="replace") as fh:
                for i, line in enumerate(fh, 1):
                    if _re.search(pattern, line):
                        matches.append(f"{i}: {line.rstrip()}")
        except Exception as e:
            return {"content": [{"type": "text", "text": f"ERROR: {e}"}], "is_error": True}
        text = "\n".join(matches) if matches else "No matches found."
        return {"content": [{"type": "text", "text": text}]}

    @tool(
        "search_file",
        "Search human reviews, optionally filtered by avg reviewer score. Args: query, n, mode ('bm25' or 'vector'), low_score (default 0), high_score (default 10). Filtering by score range is applied FIRST, then BM25/vector ranks over the filtered subset — use this to anchor calibration to a specific score band.",
        {"query": str, "n": int, "mode": str, "low_score": float, "high_score": float},
    )
    async def _search_file(args: dict) -> dict:
        time.sleep(random.uniform(0.5, 1.5))  # Simulate latency
        query = args["query"]
        n = args.get("n", 5)
        mode = args.get("mode", "vector")
        low_score = float(args.get("low_score", 0.0) or 0.0)
        high_score = float(args.get("high_score", 10.0) if args.get("high_score") is not None else 10.0)
        print(f"  [merger:search_file] query='{query}' n={n} mode='{mode}' score=[{low_score}, {high_score}]")
        score_index = _bm25_db.get("score_index", {})
        if mode == "bm25":
            bm25 = _bm25_db["bm25"]
            files = _bm25_db["files"]
            allowed_idx = [
                i for i, p in enumerate(files)
                if low_score <= score_index.get(os.path.basename(p), -1.0) <= high_score
            ]
            if not allowed_idx:
                return {"content": [{"type": "text", "text": "No files in that score range."}]}
            tokenized_query = query.split(" ")
            doc_scores = bm25.get_scores(tokenized_query)
            allowed_sorted = sorted(allowed_idx, key=lambda i: doc_scores[i], reverse=True)[:n]
            results = []
            for idx in allowed_sorted:
                fpath = os.path.abspath(files[idx])
                rel = doc_scores[idx]
                avg = score_index.get(os.path.basename(fpath), -1.0)
                with open(fpath, "r", errors="replace") as fh:
                    content = fh.read()
                results.append(f"{fpath}\navg_score: {avg:.2f}  bm25: {rel:.2f}\nfirst 1000 chars:\n{content[:1000]}\n")
            text = "\n---\n".join(results) if results else "No relevant files found."
        else:
            vectors = _bm25_db["vectors"]
            filenames = _bm25_db["filenames"]
            allowed_mask = np.array([
                low_score <= score_index.get(fn, -1.0) <= high_score for fn in filenames
            ])
            if not allowed_mask.any():
                return {"content": [{"type": "text", "text": "No files in that score range."}]}
            query_embedding = _or_client.embeddings.create(
                model="google/gemini-embedding-001",
                input=query,
                encoding_format="float",
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
                fpath = os.path.abspath(os.path.join(HUMAN_REVIEW_DIR, fn))
                rel = similarities[idx]
                avg = score_index.get(fn, -1.0)
                with open(fpath, "r", errors="replace") as fh:
                    content = fh.read()
                results.append(f"{fpath}\navg_score: {avg:.2f}  sim: {rel:.2f}\nfirst 1000 chars:\n{content[:1000]}\n")
            text = "\n---\n".join(results) if results else "No relevant files found."
        return {"content": [{"type": "text", "text": text}]}

    tools = [_read_file, _grep_file]
    if not no_cal:
        tools.append(_search_file)
    return create_sdk_mcp_server(
        name="merger_fs",
        version="1.0.0",
        tools=tools,
    )


with open(_prompt_path("cal_with.md"), "r") as _f:
    CAL_INSTRUCTION_WITH = _f.read()

with open(_prompt_path("cal_without.md"), "r") as _f:
    CAL_INSTRUCTION_WITHOUT = _f.read()


CALIBRATION_SUBAGENT_PROMPT = """You are a retrieval helper for the main merger agent. The main agent sends you a retrieval request (e.g. "find papers on face recognition privacy with high scores" or "find papers with weakness: unfair baseline comparison"), and you return a concise list of matching paper reviews.

You have these tools (all under the mcp__merger_fs__ namespace):
- search_file(query, n, mode, low_score=0, high_score=10): BM25 or vector search over human reviews, pre-filtered by the reviewer avg-score range. mode='vector' or 'bm25'. Set low_score/high_score to anchor to a band (e.g. low_score=7 for strong papers, high_score=3 for weak ones).
- read_file(abs_path, start_line, end_line): read lines from a human review file.
- grep_file(pattern, abs_path): substring search inside a single file.

Workflow:
1. Run 1-3 search_file calls to find candidate reviews matching the request. Use vector search for semantic queries and bm25 for literal keyword matches.
2. Optionally skim promising candidates with read_file to confirm they match (especially to verify score/decision if the request specifies a score range).
3. Return a list of matching papers. For each: the absolute file path and ONE sentence describing why it matches (the key weakness/strength/topic/score that makes it relevant).

Output format (strict):
- <abs_path>: <one-sentence reason, mentioning human score and decision if known>
- <abs_path>: <one-sentence reason>
...

Constraints:
- Return 3-8 papers, not more.
- Do not produce a review, do not give calibration advice, do not compare the retrieved papers to the paper under review. The main agent handles all reasoning — you just retrieve.
- Keep the whole response under 300 words.
- Cap yourself at 6 tool calls total.
- Search exactly for what the main agent asked. Do not broaden or narrow the request on your own.
"""


def _make_calibration_subagent():
    from claude_agent_sdk import AgentDefinition

    return AgentDefinition(
        description="Retrieval helper for calibration anchors. Accepts a free-form retrieval request (e.g. 'find papers with weakness X' or 'find papers scored 7+ on topic Y') and returns 3-8 paper paths each with a one-sentence summary. Does not do calibration reasoning — just retrieves.",
        prompt=CALIBRATION_SUBAGENT_PROMPT,
        tools=[
            "mcp__merger_fs__search_file",
            "mcp__merger_fs__read_file",
            "mcp__merger_fs__grep_file",
        ],
        model="haiku",
    )


async def _run_claude_sdk_query(
    *,
    label: str,
    model_id: str,
    system_prompt: str,
    user_prompt: str,
    allowed_tools: list[str],
    mcp_servers: dict | None = None,
    agents: dict | None = None,
    max_turns: int = 30,
) -> tuple[str, dict]:
    """
    Generic single-turn-style Claude SDK runner. Captures cost/usage from
    ResultMessage and returns (text, usage dict).
    """
    from claude_agent_sdk import (
        ClaudeSDKClient,
        ClaudeAgentOptions,
        AssistantMessage,
        TextBlock,
        ResultMessage,
        RateLimitEvent,
    )

    print(f"  [{label}] starting Claude Agent SDK ({model_id}) ...")

    options = ClaudeAgentOptions(
        model=model_id,
        allowed_tools=allowed_tools,
        permission_mode="bypassPermissions",
        disallowed_tools=["Read", "Glob", "Grep", "Bash", "Edit", "Write"],
        mcp_servers=mcp_servers or {},
        max_turns=max_turns,
        cwd="/tmp",
        agents=agents,
    )

    full_prompt = f"{system_prompt}\n\n---\n\n{user_prompt}"

    result_text = ""
    sdk_usage: dict = {
        "model": model_id,
        "session_id": None,
        "total_cost_usd": None,
        "num_turns": None,
        "duration_ms": None,
        "duration_api_ms": None,
        "usage": None,
        "rate_limit": None,
    }
    time.sleep(random.uniform(20, 40))  # Simulate latency

    async with ClaudeSDKClient(options=options) as sdk_client:
        await sdk_client.query(full_prompt)
        async for message in sdk_client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        result_text += block.text
            elif isinstance(message, ResultMessage):
                sdk_usage["session_id"] = message.session_id
                sdk_usage["total_cost_usd"] = message.total_cost_usd
                sdk_usage["num_turns"] = message.num_turns
                sdk_usage["duration_ms"] = message.duration_ms
                sdk_usage["duration_api_ms"] = message.duration_api_ms
                sdk_usage["usage"] = message.usage
            elif isinstance(message, RateLimitEvent):
                info = message.rate_limit_info
                sdk_usage["rate_limit"] = {
                    "status": info.status,
                    "type": info.rate_limit_type,
                    "utilization": info.utilization,
                    "resets_at": info.resets_at,
                    "overage_status": info.overage_status,
                    "overage_resets_at": info.overage_resets_at,
                }

    if not result_text.strip():
        raise RuntimeError(f"[{label}] Claude Agent SDK returned empty output")

    print(f"  [{label}] done — {model_id} (Claude Agent SDK)")
    return result_text, sdk_usage


async def run_harsh_claude_sdk(model_id: str, harsh_prompt_user: str, paper_dir: str, system_prompt: str) -> tuple[str, dict]:
    """
    Run the Harsh Critic via Claude Agent SDK with only read_file (so it can
    read the paper from disk instead of receiving it inline).
    """
    mcp_server = _make_merger_mcp_server(paper_dir, no_cal=True)
    return await _run_claude_sdk_query(
        label="Harsh Critic",
        model_id=model_id,
        system_prompt=system_prompt,
        user_prompt=harsh_prompt_user,
        allowed_tools=["mcp__merger_fs__read_file"],
        mcp_servers={"merger_fs": mcp_server},
        max_turns=15,
    )


async def run_merger_claude_sdk(model_id: str, merger_prompt: str, paper_dir: str, no_cal: bool = False) -> tuple[str, dict]:
    """
    Run the merger agent via Claude Agent SDK.
    Returns (final merged review text, usage dict with cost/tokens/turns).
    """
    _merger_prompt_file = _prompt_path("merger.md")
    with open(_merger_prompt_file, "r") as f:
        system_prompt = f.read()
    system_prompt = system_prompt.replace(
        "{{PAPER_ACCESS_INSTRUCTION}}",
        "The paper path is provided in the user message. Use read_file to read the paper and verify reviewer claims directly.",
    )
    cal_instruction = CAL_INSTRUCTION_WITHOUT if no_cal else CAL_INSTRUCTION_WITH
    system_prompt = system_prompt.replace("{{CALIBRATION_INSTRUCTION}}", cal_instruction)

    mcp_server = _make_merger_mcp_server(paper_dir, no_cal=no_cal)

    # Main merger only gets read_file/grep_file. Calibration retrieval is
    # delegated to the calibration_search subagent (invoked via Task) so its
    # many search/read tool results don't accumulate in the main merger's
    # context — only the subagent's short paper-list response does.
    allowed_tools = [
        "mcp__merger_fs__read_file",
        "mcp__merger_fs__grep_file",
    ]
    agents = None
    if not no_cal:
        allowed_tools.append("Task")
        agents = {"calibration_search": _make_calibration_subagent()}

    return await _run_claude_sdk_query(
        label="Merger",
        model_id=model_id,
        system_prompt=system_prompt,
        user_prompt=merger_prompt,
        allowed_tools=allowed_tools,
        mcp_servers={"merger_fs": mcp_server},
        agents=agents,
        max_turns=30,
    )
