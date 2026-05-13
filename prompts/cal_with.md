Use comparative scoring to calibrate your final score against human-reviewed anchors.

How retrieval works (classic RAG, one-shot):

1. Make ONE call to `calibration_search` with a batch of 4-8 short natural-language queries. The tool runs vector search for each query in parallel and returns, for every query, the top-K matching human-review paths with their avg human score and first ~1000 chars. All results are injected into your context in a single response. You do not iterate.

2. From the returned list, pick a small number of anchors (typically 3-6) you actually want to read in full. Use `read_file` on each chosen path to inspect the full review. Do not re-call `calibration_search` — one batch is all you get.

3. Score the paper relative to those anchors.

What to put in your batch of queries:
- 1-2 queries by topic of the paper under review (e.g. "privacy attacks on face recognition").
- 2-3 queries by the paper's specific strength/weakness patterns (e.g. "overclaim strong experiments", "novel framing missing baselines"). Do NOT restrict by score for these.
- 3 queries that anchor each score band on a topic similar to the paper:
   - "<topic> with avg human score >= 6" (high band)
   - "<topic> with avg human score around 5" (medium band)
   - "<topic> with avg human score <= 4" (low band)
  You can pass `low_score` / `high_score` numeric filters to `calibration_search` per-query (see tool schema). Use these exact bands. If nothing topically similar exists in a band, still take whatever the tool returned for that band as your anchor.

`calibration_search` schema: pass `queries: list[{query: str, n: int, low_score?: float, high_score?: float}]`. Default n=4 if unsure. The tool runs all queries and returns concatenated results, grouped by query.

Scoring rules:

- Your final score must be positioned relative to the retrieved anchors. If anchors with similar strengths got 7s, and anchors with similar weaknesses got 3s, your score lives in that range.
- Do not pick a score first and then justify it. Compare to anchors first, let the comparison set the score.
- Retrieval is noisy. Use the center of the anchor cluster, weighted by topical similarity. Move outside the cluster only if the paper clearly beats or falls below most anchors.
- The number of weaknesses listed is not a signal for a bad paper — focus on weakness content and anchor scores.
- Score distribution: extreme scores are rare but valid. If the paper truly is exceptional or truly weak, give an extreme score even if most retrieved anchors sit in the middle.

&& IMPORTANT: Do NOT be afraid to be harsh/nice if the retrieved anchors support it.

When reporting your score, list every anchor paper that came back in the batch (not just the ones you read in full). For each anchor give the path, its avg human score, and one sentence on how it compares to the paper under review. The list must include at least one low-scoring (avg <=4), one medium-scoring, and one high-scoring (avg >=6) anchor.

Hard constraint: exactly one `calibration_search` call. No iterative refining, no follow-up retrieval. After that, you may use `read_file` to read anchor files, then write your review and score.
