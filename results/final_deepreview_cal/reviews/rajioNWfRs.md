Now I have all the information I need. Let me write the consolidated review.

**Calibration Summary:**

**Round 1 bracket:** 5.5 – 7.0

**All retrieved anchors:**

| Anchor | Score | Round | Comparison to TNT |
|--------|-------|-------|-------------------|
| 1MHgMGoqsH | 3.00 | R1 | Unrelated topic (MPC for training) |
| 4ymHtDAlBv | 2.33 | R1 | Unrelated (text classification RNN) |
| igZ5PlRB0t | 3.00 | R1 | Unrelated (local learning) |
| It4KL6XnPq | 3.00 | R1 | Unrelated (RL memory) |
| s1kyHkdTmi | 7.00 | R1 | Learned transformer memory, stronger generality demonstration |
| bC50ZOyPQm | 5.00 | R1 | RNN adaptation of transformers, weaker experiments |
| TvGPP8i18S | 6.25 | R1 | Hierarchical memory compression, similar scope and quality |
| UU9Icwbhin | 4.75 | R1 | RetNet, overclaimed, missing baselines — TNT is stronger |
| Tzh6xAJSll | 7.60 | R1 | Unrelated (associative memory theory) |
| E4Fk3YuG56 | 8.50 | R1 | Unrelated (cross-entropy optimization) |
| nGiGXLnKhl | 8.00 | R1 | Unrelated (vision RWKV) |
| PdaPky8MUn | 8.00 | R1 | Unrelated (initialization for long-context models) |
| E34AlVLN0v | 6.00 | R2 | Parallelizing non-linear models, weaker experiments, stronger theory |
| OujTnpmAZG | 5.50 | R2 | Unrelated (spiking neural networks) |
| xwKt6bUkXj | 6.75 | R2 | Unrelated (RNN timescales) |
| 7iuFxx9Ccx | 6.00 | R2 | Unrelated (test-time training resource efficiency) |
| CNL2bku4ra | 5.25 | R2 | Unrelated (test-time training on nearest neighbors) |
| 4wk2eOKGvh | 6.50 | R2 | Unrelated (test-time ensemble) |
| 0vtftmYQGV | 5.75 | R2 | Unrelated (sparse test-time adaptation) |

The closest topical anchors are E34AlVLN0v (6.00, parallelizing non-linear sequential models) and TvGPP8i18S (6.25, MELODI hierarchical memory). TNT has stronger empirical evaluation than E34AlVLN0v and comparable quality to MELODI but with an unsupported generality claim. TNT is clearly stronger than RetNet (4.75) and READ (5.00), and weaker than the Evolved Universal Transformer Memory (7.00) which demonstrated cross-modality transfer. Final score: **6.0**.

---

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
// List only reasonable points. Rank by severity.
// Not every paper has weaknesses at every tier. Leave a tier empty (or write "None") if nothing qualifies.

### Fatal
// Errors that invalidate the paper's core claims or results.
// Examples: fundamentally flawed methodology, unsupported central claim, incorrect proofs, data fabrication concerns.
// Most papers have none. Leave empty if none apply.

### Major
// Issues that a reviewer would weigh against acceptance, and that the authors should fully resolve in a rebuttal.
// Examples: missing critical baseline, overclaimed scope unsupported by experiments, significant methodological gap.
// Not every paper has major weaknesses. Do not invent them to fill this section.

- weakness 1 — why it matters
- weakness 2 — why it matters

### Minor
// Issues worth the authors' attention but unlikely to change an accept/reject decision.
// Examples: addressable in rebuttal, limited scope of one experiment, unclear phrasing of a claim, missing ablation that would strengthen but not invalidate.

- weakness 1 — why it matters

### Trivial
// Small issues the authors should fix but that carry no weight in evaluation.
// Examples: typos, minor notation inconsistencies, suboptimal figure choices, small presentation issues.

- weakness 1

## Nice-to-Haves
- suggestion that would improve but is not a core flaw

## Removed Points
Include something like this "These points are flagged to be removed, treat them with caution"
Weaknesses that are removed keep the details of the S/W just in case they are useful 

## Novel Insights
One paragraph synthesizing genuinely novel observations.
If no genuinely novel insight emerges from the reviews beyond the paper's own contributions, write
"None beyond the paper's own contributions."

## Suggestions
- specific actionable suggestion

DO differentiate between papers of varying quality clearly.

Do evaluate the paper on these axis using language first.
Originality, importance of research question addressed, whether the claims are well supported, soundness of experiments, clarity of writing, and value to the research community

## Score and Decision
After you finish writing a review, assign a score to the review. 

Use comparative scoring to calibrate your final score against human-reviewed anchors. Retrieval is iterative: first a wide bracketing pass to find which score range the paper plausibly sits in, then one or two narrowing passes to anchor inside that range.

`calibration_search` schema: pass `queries: list[{query: str, n: int, low_score?: float, high_score?: float}]`. Default n=4 if unsure. The tool runs all queries in parallel and returns concatenated results grouped by query, each with avg human score and ~1000 chars of preview.

## Round 1 — Bracketing

Make one `calibration_search` call with three queries that anchor each score band on a topic similar to the paper. Filters are strict: `low_score` is exclusive lower bound (avg > low_score) and `high_score` is exclusive upper bound (avg < high_score).
- "<topic>" with `high_score=3.5` (weak anchors)
- "<topic>" with `low_score=3.5, high_score=7.5` (middle anchors)
- "<topic>" with `low_score=7.5` (strong anchors)

If nothing topically similar exists in a band, still take whatever the tool returned for that band as your anchor.

Use `read_anchor(anchor_id)` on a small number of anchors (typically 1–2 per band), using the `anchor_id` from the search results, to inspect the full reviews. Now form an initial bracket: based on these comparisons, what is the narrowest plausible score range for this paper (e.g., "between 4 and 6", "between 6.5 and 8")? State this bracket explicitly before round 2.

## Round 2 — Narrowing within the bracket

Make a second `calibration_search` call to pull more anchors *inside* your round-1 bracket. Use 2–3 queries with `low_score` and `high_score` tuned to your bracket (remember: both bounds are exclusive — avg > low_score and avg < high_score). For example, if round 1 placed the paper between 5 and 7, query for anchors in `(4.5, 6)` and `(6, 7.5)` on the most topically relevant aspects of the paper. The goal is to find anchors that sit close to where you think the paper lands, so the comparison is sharper than "this paper is between the weak anchor at 3 and the strong anchor at 8." Since this narrows the search pool, you can use a more lax search term.

Read 2–4 of these new anchors in full with `read_anchor(anchor_id)`. Compare the paper against each and ask: is this paper better, similar, or worse than this specific anchor? Use those comparisons to set the score.

## Round 3 — Optional, only if still genuinely uncertain

If after round 2 you still cannot decide between, say, 5.5 and 6.5 because all your round-2 anchors are clustered on one side of the paper, do one more targeted call to pull anchors from the other side. Do not do this routinely — only when the bracket has not actually narrowed.

## Hard limits

- At most three `calibration_search` calls total. Stop after round 2 unless you have a concrete reason for round 3.
- Each call is a batch of queries; do not spam single-query calls.
- After your final retrieval, write the review and score. Do not call `calibration_search` again during the writing phase.

## Calibration unavailable

If you cannot complete both calibration rounds — `calibration_search` errors out, returns nothing usable, or you otherwise cannot retrieve and read anchors for round 1 and round 2 — do NOT fall back to an uncalibrated score from your own prior. Output `<score>-100</score>` and stop. A calibrated score requires the two-round anchor comparison; without it there is no score to report.

## Scoring rules

- Your final score must be positioned relative to the round-2 (or round-3) anchors, not just the round-1 bracketing anchors. The narrowing pass is what actually determines the score; the bracketing pass only tells you where to look.
- Do not default to the middle of the bracket. If the paper is closer to the upper anchors in round 2, score near the top of the bracket; if closer to the lower anchors, score near the bottom; if the paper is clearly stronger than all round-2 anchors, score above them. The middle of the bracket is not a safe default — it is a specific claim that the paper is comparable to the median round-2 anchor.
- Score distribution: extreme scores are rare but valid. If the paper is truly exceptional or truly weak, give an extreme score even if most retrieved anchors sit in the middle.
- Do NOT cluster scores around 5. The score should be relative to retrieval samples, calibrated to where the paper actually sits.
- The number of weaknesses listed is not a signal for a bad paper — focus on weakness content and anchor scores.
- The nice to have SHOULD be considered as weakness in comparsion

## Reporting

When reporting your score, list every anchor paper retrieved across all rounds (not just the ones you read in full). For each anchor give the anchor_id, its avg human score, the round it came from, and one sentence on how it compares to the paper under review. State the round-1 bracket explicitly, then explain how round 2 (and 3, if used) narrowed it to the final score.


If the FUNDAMENTAL ISSUES was triggered on top — and the triggering weakness is verifiable from the paper as written, not speculative — rate the paper low accordingly. Do not collapse the score on a single speculative-fatal claim. 



Score round to .5 or .0. 


IMPORTANT: At the very end of your response, you MUST write exactly this line (using a score XML tag):
MY FINAL SCORE: <score>score</score>
MY FINAL DECISION: <decision>Accept/Reject</decision>

---

My FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>## Summary

This paper introduces TNT (Two-stage Non-linear Training), a training paradigm for deep memory modules (e.g., Titans, TTT) that decouples training efficiency from inference performance. The key ideas are: (1) a hierarchical memory architecture where a global memory handles large chunks for long-range context while multiple parallel local memories process sequence shards independently via periodic state resets; (2) a Q-K Projection mechanism that resolves a domain mismatch between memory compression and retrieval; and (3) a two-stage process where Stage 1 maximizes throughput and Stage 2 briefly fine-tunes local memories with smaller chunk sizes for accuracy. On 150M-parameter Titans models trained on 10B tokens, TNT achieves up to 17× training speedup while improving perplexity and reasoning accuracy over baseline Titans.

## Strengths

- **Periodic local memory reset enables context parallelism for non-linear deep memory modules.** The paper identifies a fundamental limitation: deep memory modules (Titans, TTT) cannot parallelize across chunks due to non-linear recurrences. By resetting local memory states to a shared learnable initial state at segment boundaries (Eq. 6), TNT breaks the sequential dependency and allows all sequence shards to be processed in parallel. This is a genuine architectural insight, validated by linear runtime scaling in Figure 4 (TNT runtime stays nearly constant as sequence length increases from 2K to 32K, while Titans and standard attention grow quadratically).

- **Two-stage training cleanly resolves the chunk-size dilemma.** Challenge 3 (Figure 2) shows that deep memory modules are over-specialized to their pre-training chunk size — using a smaller chunk at inference degrades performance. Stage 2 fine-tuning with smaller chunk sizes recovers and even improves accuracy with only ~5% additional compute (Table 2: perplexity drops from 23.13 to 23.09, reasoning accuracy reaches 40.9%). This is a practical solution to a problem the paper identifies and motivates well.

- **Comprehensive ablation study validates each design choice.** Table 3 systematically decomposes the contribution of each component: removing global memory increases perplexity from 21.04 to 25.60; removing Q-K projection increases it to 22.01; adding more local memories progressively improves performance. The clear attribution of each component's impact strengthens confidence in the architecture.

- **Empirical evaluation includes both training speed and model quality on 150M-parameter models.** The experiments cover time-to-quality (Table 1), downstream performance on language modeling and reasoning tasks (Table 2), and runtime scaling (Figure 4), providing a reasonably comprehensive picture for this model scale.

## Weaknesses

### Major

1. **Generality is claimed but only demonstrated on one architecture.** The abstract states "Evaluated on Titans and TTT models," but TNT is only instantiated on Titans — TTT appears exclusively as a baseline (Table 2). The paper claims TNT is a "general training paradigm applicable to any deep memory module" (Section 4) and mentions Atlas as another example, but provides no experiments on TTT, Atlas, or any other deep memory architecture. While the method is architectural and likely general, the evidence does not support the breadth of the claim.

2. **Parameter accounting across model variants is not documented.** All models are labeled "150M params" in Table 2, suggesting parameter count is controlled when adding local memory modules. However, the paper never explains *how* this is achieved — e.g., whether hidden dimensions are reduced, layers are removed, or the fast-weight sub-networks are shared. Each local memory module adds a separate deep sub-network (fast weights). Without knowing the mechanism, the accuracy improvement from TNT (23.13 vs. 25.07 PPL) could partially reflect increased capacity rather than the training paradigm itself. The authors should state explicitly how total parameters are kept constant.

### Minor

3. **Stage 2 fine-tuning protocol is underspecified.** The paper says "only the local memory modules are adapted" with a smaller chunk size, but does not state the number of fine-tuning steps, learning rate schedule, whether the global memory is frozen, or which specific Stage 1 checkpoint is used as the starting point. This makes the 5% compute claim (Table 4, referenced but appendix-stripped) difficult to verify and the protocol non-reproducible as written.

4. **No variance or error bars reported.** Perplexity and accuracy numbers in Table 2 are reported as point estimates without standard deviations or multiple seeds. Some differences are small (e.g., Stage 2 C_L={2,4,8,16} achieves 23.09 vs. Stage 1 C_L={4,8,16,32} at 23.13) and could be within noise. Given 150M models trained on 10B tokens, single-seed reporting is a meaningful omission.

5. **The Q-K Projection's effect is not analyzed beyond perplexity.** The ablation shows a ~1 PPL benefit from the projection, but the paper does not analyze what the projection actually does — e.g., does it collapse queries to a low-dimensional subspace, does it make local memory behave more like attention, or is it compensating for a fundamentally flawed training objective? The mechanism is introduced as a core contribution (Section 4.1.2) but treated as a black box in evaluation.

6. **The 17× speedup figure is partly an artifact of baseline choice.** The headline speedup compares TNT C_L=64 against Titans C=8 (the slowest and most accurate Titans configuration). This is a fair comparison (highest accuracy baseline), but the paper also shows TNT C_L=64 is only 3.7× faster than Titans C=64 (same chunk size: 4.18/1.12 hrs). The 17× figure is valid but should be presented alongside same-chunk-size comparisons to give a complete picture of the speed-accuracy Pareto frontier.

### Trivial

- The paper says TNT runtime "scales linearly with sequence length" (Section 5.2) which would be more precisely described as "scaling sub-linearly" or "remaining nearly constant per token." The fixed-tokens-per-batch experimental design means runtime is roughly constant across sequence lengths, which is better than linear — but the phrasing "linear" is slightly imprecise.

## Nice-to-Haves

- An analysis of inference-time efficiency would be useful. Stage 2 fine-tunes to chunk size 1, which could be slow during inference since the local memory updates per token. The paper's focus is training efficiency, but practical deployment also depends on inference speed.
- A sensitivity analysis of the local segment length S_L (currently 2048 or 4096) and the number of local memories N would help users understand the speed-accuracy Pareto frontier for these new hyperparameters.

## Removed Points

These points were raised in the input reviews but are removed or weakened after verification:

- **"Parameter count table must be stated"** (Harsh Critic) — Actually, Table 2 header does state "150M params" for all models. The issue is the *mechanism* is undocumented, not that it's missing. Moved to Major #2 (reformulated).
- **"Q-K Projection d×d matrix is expensive"** (Harsh Critic) — The paper explains it is maintained as a running sum with constant-size state, making it efficient. The critic's 2.4M parameter calculation assumes specific dimensions not stated in the paper. Removed as speculative.
- **"Global memory should also use Q-K projection"** (Harsh Critic) — The paper explicitly justifies applying it only locally: "its fine-grained nature makes it more sensitive to the mismatch." This is a design choice, not an inconsistency.
- **"The target loss 3.20 is arbitrary"** (Harsh Critic) — Target loss thresholds are standard in time-to-quality comparisons. Removed as a nitpick.
- **"Figure 2 shows the mismatch problem"** (Harsh Critic requested removal as a criticism) — This is evidence FOR the paper's motivation, not a weakness. Removed.
- **Strength Finder claim "Evaluated on Titans and TTT models"** — This repeats the paper's own overclaim and is inaccurate (TNT was only instantiated on Titans). Removed.
- **Strength Finder strengths about "important problem" and generic praise** — Removed per filtering rules. Only concrete, evidenced strengths retained.

## Novel Insights

None beyond the paper's own contributions. The observation that periodic state resets can enable context parallelism for non-linear deep memory modules, combined with the Q-K projection to fix compression-retrieval mismatch, is a novel contribution that is well-articulated in the paper.

## Suggestions

1. **Document parameter accounting explicitly.** Add a table or paragraph stating: "All models use 150M total parameters. When TNT adds N local memory modules (each with hidden dimension d_m), this is compensated by [reducing the number of layers / reducing hidden dimension / sharing weights across local memories]." This single addition would remove the largest concern about the accuracy comparison.

2. **Add at least one non-Titans instantiation.** A single experiment applying TNT to TTT (or another deep memory module) on one benchmark would substantiate the generality claim and significantly strengthen the paper.

3. **Report Stage 2 fine-tuning details.** Specify the number of optimization steps, learning rate schedule, and whether the global memory is updated or frozen during Stage 2.

4. **Include error bars for key results.** Even 2-3 seeds with standard deviations for the main perplexity numbers in Table 2 would address the noise concern.

5. **Add a Pareto plot showing speed vs.** accuracy for different TNT configurations and baseline Titans configurations, to give a complete picture of the trade-off space.

**Calibration Report:**
- Round 1 bracket: 5.5 – 7.0
- Round 2 narrowed via comparison to closely related anchors: E34AlVLN0v (6.00, parallelizing non-linear sequential models — TNT has stronger experiments); TvGPP8i18S (6.25, MELODI hierarchical memory — comparable quality); UU9Icwbhin (4.75, RetNet — TNT is stronger); bC50ZOyPQm (5.00, READ — TNT is stronger); s1kyHkdTmi (7.00, Evolved Universal Transformer Memory — TNT demonstrates less generality).
- TNT is clearly stronger than the 4.75–5.00 anchors and sits alongside the 6.00–6.25 anchors. Its unsupported generality claim and undocumented parameter accounting prevent it from reaching the 7.00 level. Final score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>