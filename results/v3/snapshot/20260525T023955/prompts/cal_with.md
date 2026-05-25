Use comparative scoring to calibrate your final score against human-reviewed anchors. Retrieval is iterative: a wide bracketing pass to find which score range the paper plausibly sits in, then one or two narrowing passes to anchor inside that range.

`calibration_search` schema: pass `queries: list[{query: str, n: int, low_score?: float, high_score?: float}]`. Default n=4 if unsure. The tool runs all queries in parallel and returns concatenated results grouped by query, each with avg human score and ~1000 chars of preview. `low_score` is an exclusive lower bound (avg > low_score); `high_score` is an exclusive upper bound (avg < high_score).

## Round 1 — Bracketing

Make one `calibration_search` call covering both:

(A) Topic-anchored quality ladder — three queries with the same topic phrasing but different score bands:
   - "<topic of paper>" with `high_score=3.5` (weak band)
   - "<topic of paper>" with `low_score=3.5, high_score=7.5` (middle band)
   - "<topic of paper>" with `low_score=7.5` (strong band)

If nothing topically similar exists in a band, still take whatever the tool returned for that band — you still need to see what each band looks like.

(B) Weakness-anchored queries — 2–4 queries (no score filter) probing how human reviewers scored papers with the same kind of failure mode as the paper under review. Examples:
   - "evaluation uses fixed threshold instead of EER"
   - "metric coupled with training objective"
   - "subgroup claims from small sample size"
   - "missing standard baselines from the same line of work"

The point of (A) is to see what bad/medium/good look like *within the topic*. The point of (B) is to see what the corpus does with the specific failure modes you identified, regardless of topic. Together they prevent two failure modes: (a) snapping to the closest topical match by keyword similarity, (b) ignoring the price of a real flaw because nearby topical anchors were stronger papers.

Use `read_file` on a small number of anchors (typically 1–2 per topic band, plus 1–2 from weakness queries) to inspect full reviews. Then form an initial bracket: based on these comparisons, what is the narrowest plausible score range for this paper (e.g., "between 4 and 6", "between 6.5 and 8")? State this bracket explicitly before round 2.

## Round 2 — Narrowing within the bracket

Make a second `calibration_search` call to pull more anchors *inside* your round-1 bracket. Use 2–3 queries with `low_score` and `high_score` tuned to your bracket. For example, if round 1 placed the paper between 5 and 7, query for anchors in `(4.5, 6)` and `(6, 7.5)` on the most topically relevant aspects. Since this narrows the search pool, you can use a more lax topical term.

Round 2 does NOT discard the round-1 anchors. The low-band topic anchors and weakness-anchored hits from round 1 stay in your comparison set throughout round 2. If the paper shares concrete failures with a round-1 low-band anchor scored at 2.5, that anchor remains the relevant comparison even when round-2 pulled in nicer-looking 5–6 neighbors. Round 2 sharpens within the bracket; it does not relocate the bracket upward.

Read 2–4 of these new anchors in full with `read_file`. Compare the paper against each: is this paper better, similar, or worse than this specific anchor? Use those comparisons together with the retained round-1 anchors to set the score.

Before writing the score, answer in 2–3 sentences: **"What did the round-1 low-band anchors and weakness-anchored hits fail at, and does the paper under review share any of those failures?"** If yes, the score must reflect that, not just the round-2 narrowed neighbors. This step happens BEFORE the score is decided, not in the final report.

## Round 3 — Optional, only if still genuinely uncertain

If after round 2 you still cannot decide between, say, 5.5 and 6.5 because all round-2 anchors clustered on one side of the paper, do one more targeted call to pull anchors from the other side. Do not do this routinely — only when the bracket has not actually narrowed.

## Hard limits

- At most three `calibration_search` calls total. Stop after round 2 unless you have a concrete reason for round 3.
- Each call is a batch of queries; do not spam single-query calls.
- After your final retrieval, write the review and score. Do not call `calibration_search` again during the writing phase.

## Scoring rules

- Final score is positioned relative to the combined anchor set: round-1 anchors (both topic bands and weakness queries) plus round-2 narrowed anchors. Round 2 sharpens within the bracket but does not replace round-1 evidence.
- Round-2 anchors are by construction closer in score than round-1 anchors, so the paper will often look "comparable" to round-2 neighbors. This is an artifact of the narrowed search range, not evidence that the paper deserves a middle-of-bracket score. Resist the pull toward the round-2 median.
- Do not pick a score first and then justify it. Compare to anchors first, let the comparison set the score.
- Place the paper on the quality ladder by quality, not by topical proximity. The closest topical anchor might be a medium-band paper that shares keywords but is much higher quality than the paper under review. When the paper shares the failure modes of a lower-band anchor — even if topically further or outside the round-2 bracket — that lower-band anchor is the right reference. The weakness-anchored queries (B) and round-1 low-band anchors override topical proximity.
- The number of weaknesses listed is not a signal for a bad paper — focus on weakness content and anchor comparisons.
- Extreme scores are rare but valid. If the paper is truly exceptional or truly weak, give an extreme score even if most retrieved anchors sit in the middle.
- Do not cluster scores around 5. If the weakness-anchored queries (B) show that papers with the same failure modes consistently scored < 3.5, that is direct evidence — score accordingly even if topic-band or round-2 anchors sat at 5–6. The weakness-anchored evidence is not a tiebreaker; it is a primary signal that overrides "but the topical neighbors looked similar."
- If a Fatal weakness or fundamental issue is flagged in the merger output, the score must sit at or below the lowest anchor with the same failure mode. Round-2 narrowing does not override this — if the bracket excluded that anchor, the bracket was wrong and the score must drop below the bracket.
- If the paper shares 2+ Major weaknesses with any low-band anchor (<= 3.5), the score must be within 1.0 of that anchor's score regardless of where round-2 neighbors sat.
- The "nice to have" items should be weighed as minor weaknesses in anchor comparisons, not ignored.

## Reporting

List every anchor paper retrieved across all rounds (not just the ones you read in full). For each anchor give the path, its avg human score, the round and query bucket it came from (round1-topic-low / round1-topic-mid / round1-topic-high / round1-weakness-<which> / round2 / round3), and one sentence on how it compares to the paper under review.

State the round-1 bracket explicitly, then explain how round 2 (and 3, if used) narrowed it to the final score. After the anchor list, write one short paragraph answering: "What did the low-band anchors fail at, and does the paper under review share any of those failures?" If yes, the score must reflect that.
