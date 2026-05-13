## Summary
The paper extends Jenner et al. (2024)'s mechanistic interpretability analysis of Leela Chess Zero's policy network to longer horizons (5- and 7-move tactical puzzles), introduces a digit-based notation for partitioning puzzles by square-overlap structure, and adapts board corruption to two-branch puzzles. It claims Leela looks ahead up to seven moves with context-dependent, time-translation-invariant circuits (notably L12H12), and considers multiple move sequences simultaneously.

## Strengths
- **Time-translation-invariant AAC pattern in L12H12.** Patching the 3rd-, 5th-, and 7th-move "C" square produces strong effects only when the prefix matches ...AAC (vs. weak for ...ACC, moderate for ...ABC). This is a non-trivial, genuinely new mechanistic claim (Fig. 2 in body, with 7-move extension in appendices).
- **Useful notation (Section 2.4).** The $s_1 s_2 \cdots s_n$ square-overlap notation disentangles puzzle categories that Jenner et al. bundled together ("bundles the higher move squares ... into the third move square results"), making subset effects legible. Genuinely reusable bookkeeping.
- **Head specialization by tactical context.** Cleanly separates L12H12 (checkmate / M-prefix) from L12H17 (non-checkmate / N-prefix, AABCD with D=A) and L13H3 (AABCD with B=C or C=D), instead of treating "long-range head" as monolithic.
- **Two-branch corruption methodology.** Adapting Jenner's contrastive corruption to puzzles with two near-equiprobable continuations is a sensible methodological extension.
- **Honest probing-vs-causal framing in Section 2.3.** The paper explicitly notes that probing reflects encoding, not causal use ("probing can identify information that is encoded but not necessarily used").

## Weaknesses

### Fatal
None. The contributions are real even if incremental.

### Major
- **Probe baselines are insufficient for the headline 7-move claim.** The only control for the 7-move probing accuracy (Fig. 3, set 1123456) is a random-model probe. There is no probe-on-input / layer-0 / linear-classifier-on-raw-board baseline. Since principal-variation moves are heavily constrained by the starting position, much of the "7-move information" may be trivially decodable from the board encoding. Without that control, the "up to seven moves" headline rests on a baseline that does not rule out the most obvious confound.
- **7-move patching evidence is only in the appendix; the main body shows 5-move patching.** The conclusion explicitly hedges ("Based on Fig. 2 and Appendices B and E, we *hypothesize* ..."), yet the abstract/intro/conclusion assert the 7-move capability firmly. The causal evidence carried by the body does not match the strength of the headline.
- **Alternative-move generalization is shown for a single puzzle set.** Figure 6 in the main body illustrates 123425 only; broader analysis is deferred to appendices. A single puzzle set is anecdote, not evidence that "the model considers multiple move sequences" generally — at minimum the body should aggregate over the 609-puzzle pool.

### Minor
- **Zero ablation is used without justification or sensitivity check.** Zero ablation pushes activations off-distribution and is the weakest causal intervention; several head-role assignments depend on it. A brief comparison with mean/resample ablation would strengthen the head specialization claims.
- **No per-puzzle-set sample sizes reported.** Only "sets with more than 50 puzzles are considered." With 5- and 7-digit partitions of 22k/2.2k pools, several subset claims (L12H17 on AABCA, L13H3 patterns, M112 vs. N112) are made over potentially small cells, with no significance tests or multiple-comparison correction.
- **Probing-vs-lookahead conflation in places.** Although Section 2.3 acknowledges the distinction, Section 3 and the conclusion still slide between "encoded in residual stream" and "the model looks ahead." A patching test on probe-identified directions would resolve this.
- **Incremental delta over Jenner et al. (2024).** Same checkpoint, same 22k dataset, same toolset. Genuine new contribution boils down to the notation, the longer horizon, and the two-branch corruption.

### Trivial
- The conclusion restates findings ("considers multiple move sequences simultaneously") more firmly than the body's hedged language ("hypothesize," "appears to") warrants.

## Nice-to-Haves
- Head-to-head replication on Jenner et al.'s 3-move puzzles, showing what is replication vs. new.
- Adversarial puzzles that break the AAC structural cue, to test whether L12H12's pattern-matching is genuinely about the AAC structure rather than co-occurring tactical features.
- Per-set puzzle count tables.

## Removed Points
*These points are flagged to be removed; treat them with caution.*
- **"Compute / probe architecture / partition details are missing."** Standard reproducibility nitpick; the paper reports compute (2 days, RTX 3070Ti) and uses Jenner et al.'s public dataset and model. Implementation details likely sit in the appendix that the parser strips.
- **"The paper never isolates a phenomenon Jenner et al. couldn't have claimed by re-bucketing."** Overstated: the time-translation-invariant AAC finding across 3/5/7 moves and the L12H12 vs. L12H17 vs. L13H3 specialization are not in Jenner et al. and require the longer-horizon data.
- **Strength: "complementary interpretability techniques avoid blind spots."** Generic; dropped.
- **Strength: "advances our understanding of look-ahead."** Generic.

## Novel Insights
The time-translation invariance of L12H12's response to ...AAC patterns across the 3rd, 5th, and 7th moves is the most genuinely novel observation: it suggests a single pattern-matching circuit that fires on a *structural* cue (same square targeted twice with an intervening opponent move) regardless of the move's temporal position. If robust to non-AAC confounds, this would be a more interesting finding than the "seven moves" headline.

## Suggestions
- Train probes on the raw board / layer-0 activations as a baseline; report the gap between this and mid-layer probes as the actual evidence of internal computation.
- Move 7-move patching results into the main body (replace or supplement Fig. 2 with a 7-move panel).
- Aggregate the alternative-move analysis across all qualifying sets in the 609 pool; report effect-size distribution.
- Test sensitivity of head-role claims to zero vs. mean vs. resample ablation.
- Reframe the abstract/intro/conclusion around the AAC-pattern circuit (the strongest finding) rather than the 7-move depth claim.
- Report per-set puzzle counts and apply at minimum a multiple-comparison correction for subset-level claims.

## Axis Evaluation
- **Originality:** Moderate. Notation + longer horizon + two-branch corruption are real but incremental atop Jenner et al.
- **Importance:** Mechanistic interpretability of planning in a strong game-playing net is a worthwhile, active area.
- **Claim support:** Uneven. The AAC pattern claim is well-supported; the 7-move depth and "multiple sequences" claims are stated more strongly than the body's causal evidence justifies.
- **Soundness of experiments:** Mostly sound but with a notable missing probe baseline, single-set alt-move illustration in body, and unjustified zero ablation.
- **Clarity:** Generally clear; notation in Section 2.4 is dense.
- **Value to community:** Real — the notation and the AAC finding are reusable; the methodology for two-branch corruption is transferable.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>