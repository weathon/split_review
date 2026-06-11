Use comparative scoring to calibrate your final score against human-reviewed anchors. Retrieval is iterative: first a wide bracketing pass to find which score range the paper plausibly sits in, then one or two narrowing passes to anchor inside that range.

`calibration_search` schema: pass `queries: list[{query: str, n: int, low_score?: float, high_score?: float}]`. Default n=4 if unsure. The tool runs all queries in parallel and returns concatenated results grouped by query, each with avg human score and ~1000 chars of preview.

Before any `calibration_search` call, first finish filtering the Harsh Critic and Strength Finder inputs into a draft review. Then call `draft_review` exactly once with that draft. The draft should include the kept strengths, kept weaknesses with severity tiers, removed points, novel insights, and suggestions. Do not include calibration anchors or a final calibrated score in this draft. After `draft_review` returns, start Round 1.

## Round 1 — Bracketing

Make one `calibration_search` call with a couple queries that anchor each score band on a topic similar to the paper. Filters are strict: `low_score` is exclusive lower bound (avg > low_score) and `high_score` is exclusive upper bound (avg < high_score).
- "<topic>" with `high_score=2.5` (strong reject anchors) ~3 papers
- "<topic>" with `low_score=2.5, high_score=4.5` (weak anchors) ~3 papers
- "<topic>" with `low_score=4.5, high_score=6.1` (middle anchors) ~3 papers
- "<topic>" with `low_score=6.0, high_score=7.5` (middle anchors) ~3 papers
- "<topic>" with `low_score=7.5` (strong anchors) ~3 papers

The strong reject paper is used as a matching template: what kind of papers will be strong rejected. If current paper match, strong reject it. 

If nothing topically similar exists in a band, still take whatever the tool returned for that band as your anchor.

Use `read_file` on a small number of anchors (typically 1–2 per band) to inspect the full reviews. Now form an initial bracket: based on these comparisons, what is the narrowest plausible score range for this paper (e.g., "between 4 and 6", "between 6.5 and 8")? State this bracket explicitly before round 2.

## Round 2 — Narrowing within the bracket

Make a second `calibration_search` call to pull more anchors *inside* your round-1 bracket. Use 2–3 queries with `low_score` and `high_score` tuned to your bracket (remember: both bounds are exclusive — avg > low_score and avg < high_score). For example, if round 1 placed the paper between 5 and 7, query for anchors in `(4.5, 6)` and `(6, 7.5)` on the most topically relevant aspects of the paper. The goal is to find anchors that sit close to where you think the paper lands, so the comparison is sharper than "this paper is between the weak anchor at 3 and the strong anchor at 8." Since this narrows the search pool, you can use a more lax search term.

&& Hint: you usually over estimate the paper's quality for low quality papers and under estimate quality for high papers. Thus, artificially lower your bracket for 1-2 points for papers lower than 5 and raise the bracket for 1-2 points for paper >5. and widen it for 1-2 points if it sits in middle. 

Read 2–4 of these new anchors in full with `read_file`. Compare the paper against each and ask: is this paper better, similar, or worse than this specific anchor? Use those comparisons to set the score.

## Hard limits

- At most three `calibration_search` calls total. Stop after round 2 unless you have a concrete reason for round 3.
- Each call is a batch of queries; do not spam single-query calls.
- After your final retrieval, write the review and score. Do not call `calibration_search` again during the writing phase.

## Scoring rules

- Your final score must be positioned relative to the round-2 (or round-3) anchors, not just the round-1 bracketing anchors. The narrowing pass is what actually determines the score; the bracketing pass only tells you where to look.
- Do not default to the middle of the bracket. If the paper is closer to the upper anchors in round 2, score near the top of the bracket; if closer to the lower anchors, score near the bottom; if the paper is clearly stronger than all round-2 anchors, score above them. The middle of the bracket is not a safe default — it is a specific claim that the paper is comparable to the median round-2 anchor.
- Score distribution: extreme scores are rare but valid. If the paper is truly exceptional or truly weak, give an extreme score even if most retrieved anchors sit in the middle.
- Do NOT cluster scores around 5. The score should be relative to retrieval samples, calibrated to where the paper actually sits.
- The number of weaknesses listed is not a signal for a bad paper — focus on weakness content and anchor scores.
- The nice to have SHOULD be considered as weakness in comparsion

## Reporting

When reporting your score, list every anchor paper retrieved across all rounds (not just the ones you read in full). For each anchor give the path, its avg human score, the round it came from, and one sentence on how it compares to the paper under review. State the round-1 bracket explicitly, then explain how round 2 (and 3, if used) narrowed it to the final score.

Piror: You usually over estimate score, keep that in mind and act accordingly. 