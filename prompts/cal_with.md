Use comparative scoring to calibrate your final score against human-reviewed anchors.

## Calibration Dataset Reference Statistics

The human-review corpus you are searching against has the following score distribution (n = 13,379 papers):

- mean: 5.19
- median: 5.25
- 25th percentile: 4.25
- 75th percentile: 6.00
- std: 1.24
- range: [1.0, 10.0]

What this means for your score:
- A score of **5.25 is exactly the median** — half of all human-reviewed papers scored at or below this. Giving 5.25 is NOT a "safe middle" choice; it is an explicit claim that the paper is better than half the corpus.
- A score of **5.19 is the mean** — the average paper, including all the rejects, scored here.
- A score of **>= 6.0** places the paper in the **top 25%** of the corpus.
- A score of **<= 4.25** places the paper in the **bottom 25%**.
- Scores >= 7 or <= 3 are tail events; they should be uncommon but you must use them when the paper warrants it. The corpus contains both — refusing to give them means you are compressing the distribution.

Do not cluster your scores around 5–6 by default. If the paper has Major or Fatal weaknesses, the comparison against the calibration corpus should pull the score below 4.25 (bottom quartile), not leave it at 5–6 where it would outrank half the corpus including the published-and-accepted papers.


How retrieval works:

1. Make ONE call to `calibration_search` with a batch of short natural-language queries. The tool runs vector search for each query in parallel and returns, for every query, the top-K matching human-review paths with their avg human score and first ~1000 chars. All results are injected into your context in a single response. You do not iterate.

2. From the returned list, pick a small number of anchors (typically 5-9) you actually want to read in full. Use `read_file` on each chosen path to inspect the full review. Do not re-call `calibration_search` — one batch is all you get.

3. Score the paper relative to those anchors.

What to put in your batch of queries:

The point of calibration is to see what high / medium / low quality look like *within the same topic*. You are NOT trying to find the single closest paper and snap to its score. You are trying to see, on this topic, what a 2-score paper failed at, what a 5-score paper looked like, and what a 7-score paper got right — then place the paper under review on that quality ladder.

(A) Topic-anchored quality ladder — three queries with the same topic phrasing but different score bands:
   - "<topic of paper>" with avg human score > 7.5
   - "<topic of paper>" with avg human score >3.5 and <7.5
   - "<topic of paper>" with avg human score < 3.5
   You have to read at least one paper per bin, even if they are not closely related.

   You can pass `low_score` / `high_score` numeric filters to `calibration_search` per-query (see tool schema). Use these exact bands. If nothing topically similar exists in a band, still take whatever the tool returned for that band as your anchor — you still need to see what a low-band paper looks like even if it is off-topic.

(B) Weakness-anchored queries — additional queries (no score filter) that search for papers with weaknesses similar to the ones identified for the paper under review. Examples:
   - "evaluation uses fixed threshold instead of EER" (no score filter)
   - "metric coupled with training objective" (no score filter)
   - "subgroup claims from small sample size" (no score filter)
   - "missing standard baselines from the same line of work" (no score filter)
   Add 2-4 such queries. These reveal how human reviewers scored papers that had the same kind of problem, regardless of topic. They are often more informative than topic similarity for calibrating low scores, because they directly probe "how harshly do humans treat this failure mode."

Combine both: (A) tells you the topic's quality ladder, (B) tells you the price of the specific failure modes you identified. Score is informed by both, not snapped to either.

`calibration_search` schema: pass `queries: list[{query: str, n: int, low_score?: float, high_score?: float}]`. Default n=4 if unsure. The tool runs all queries and returns concatenated results, grouped by query.

Scoring rules:

- Your final score is positioned relative to the retrieved anchors as a *ladder*, not by snapping to the single most-topically-similar anchor. The topic-anchored low/medium/high band queries give you what bad/medium/good look like on this topic; place the paper on that ladder by quality, not by topical proximity.
- Common failure mode to avoid: "the closest topical match was a 6.0, so I gave 6.0." This collapses the ladder. The closest topical match might be a medium-band paper that happens to share keywords but is much higher quality than the paper under review. The low-band anchor — even if topically further — is the right reference when the paper shares the low-band paper's failure modes. Use the weakness-anchored queries (B) to break this tie.
- Do not pick a score first and then justify it. Compare to anchors first, let the comparison set the score.
- The number of weaknesses listed is not a signal for a bad paper — focus on weakness content and anchor scores.
- Score distribution: extreme scores are rare but valid. If the paper truly is exceptional or truly weak, give an extreme score even if most retrieved anchors sit in the middle.
- Do NOT cluster scores around 5. If the weakness-anchored queries (B) show that papers with the same failure modes consistently scored < 3.5, that is direct evidence the paper under review should score there too, even if its topic-band anchors sat at 5-6.
- Compare the paper under review with every single anchor paper.
- If a Fatal weakness or fundamental issue is flagged in the merger output, the score must sit at or below the lowest topic-band anchor with the same failure mode, not above it.


When reporting your score, list every anchor paper that came back in the batch (not just the ones you read in full). For each anchor give the path, its avg human score, the query bucket it came from (topic-low / topic-mid / topic-high / weakness-<which>), and one sentence on how it compares to the paper under review. The list must include at least one low-scoring (avg <=4), one medium-scoring, and one high-scoring (avg >=6) anchor.

Additionally, after the anchor list, write one paragraph explicitly answering: "What did the low-band topic anchors fail at, and does the paper under review share any of those failures?" If yes, the score must reflect that — do not place the paper above a low-band anchor it matches in failure modes.

Hard constraint: exactly one `calibration_search` call. No iterative refining, no follow-up retrieval. After that, you may use `read_file` to read anchor files, then write your review and score.