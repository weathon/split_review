Now I have strong calibration. Let me produce the final consolidated review.

## Summary
This paper identifies three misconceptions in the emerging online-map-based motion prediction protocol: (1) inappropriate data splits causing a train-val gap in two-stage training, (2) perception range mismatch between mapping models (30×60m) and motion prediction (agents up to 100+ m), and (3) non-discriminative metrics that evaluate only the ego vehicle. It proposes OMMP-Bench with a spatially-disjoint three-way split, refined metrics evaluating moving non-ego agents split by distance, and an image-feature baseline using deformable attention to compensate for out-of-range agents. The paper provides compelling evidence that these issues are real and that the proposed fixes improve evaluation fidelity.

## Strengths
- **Clear identification and quantification of perception range mismatch.** Tables 2 and 3 convincingly show that extending MapTR's range from 30×60m to 100×100m collapses mAP (0.124 → 0.014), while having GT maps at extended range only marginally improves motion prediction (minADE 0.6154 → 0.6003). This cleanly demonstrates the bottleneck is online map quality, not range alone.
- **Refined metrics reveal previously hidden failure modes.** By evaluating Moving-Non-Ego agents split into Close/Far groups, Table 7 shows that methods improving ego prediction (e.g., MapUncertaintyPrediction) can degrade non-ego performance, and far-agent prediction is systematically worse — findings the old ego-only metrics would have masked.
- **Empirical demonstration and fix of the train-val gap.** Table 1 quantifies the gap: default split yields minADE 0.6839, the proposed three-way split yields 0.6308 (~7.8% improvement). Figure 4 documents that 87% of original validation data overlaps spatially with training data, reduced to 5% in the proposed split.
- **Actionable ablation of map element types.** Table 5 provides clear guidance: centerlines alone achieve second-best performance, all elements together work best — informing online mapping model design.
- **Image-feature baseline meaningfully addresses a practical gap.** The deformable-attention approach consistently reduces far-agent minADE (e.g., MapTRv2-CL+HiVT: 0.6999 → 0.6274, 12.7% improvement on Moving-Non-Ego-Far), validating the benchmark's core motivation.

## Weaknesses

### Fatal
None.

### Major
- **The close/far agent threshold is underspecified in the main paper.** Line 261 defines "close" and "far" only as "whether within the perception range of online mapping models," without stating the exact spatial threshold. Given that this split is central to the paper's refined metrics, readers need to know the precise distance used (presumably MapTR's 30×60m range from Section 3.3). This should be stated explicitly.
- **The unique benefit of the three-way split over simpler alternatives is not fully disentangled.** Table 1 shows Split 4 (nuScenes Train split into two halves, evaluated on original val set) achieves minADE 0.6373 vs. the proposed Split 1 at 0.6308 — a very small gap. Split 4 already eliminates the train-set familiarity issue without a three-way split and without sacrificing training data. The proposed split costs half the training data (367+397 scenes instead of ~700), but the incremental benefit over Split 4 is marginal (0.6308 vs 0.6373). The paper should explicitly discuss this trade-off rather than framing the proposed split as unequivocally superior.

### Minor
- **No variance or statistical significance reported.** The paper reports single-run metrics throughout. Given that some improvements are modest (e.g., 0.6287 → 0.6163 in Table 4), confidence intervals would help assess reliability.
- **The "misconception" framing slightly overstates the novelty of the train-val gap observation.** The fact that a second-stage model performs better on first-stage training-set outputs than on held-out outputs is a known property of cascaded systems. The paper's contribution is in quantifying it for this specific protocol and proposing a fix — which is valuable — but the framing as a "misunderstanding" is somewhat inflated.
- **Table 5 appears to have a formatting issue.** Rows 2 and 3 are both marked with the same checkmark pattern (Boundary only, ✗✓✗✗) but report different minADE values (0.6829 and 0.6558). If this is a parser artifact it should be clarified; if an error in the original it undermines the map element analysis.

### Trivial
- The paper states "87% of the validation data has overlap with training set" without explicitly stating that this statistic is from the paper's own spatial overlap analysis.

## Nice-to-Haves
- An ablation directly separating the two effects motivating the new split: (a) train-set familiarity vs. (b) spatial overlap removal. Split 4 partially addresses (a) but evaluates on the original val set. A clean ablation would clarify the marginal benefit of each correction.
- A discussion of how conclusions might generalize beyond nuScenes, since all existing work in this subfield is tied to one dataset (as the paper honestly acknowledges).
- Computational cost analysis for the image-feature baseline relative to base models.

## Removed Points
- Criticism about the benchmark being restricted to nuScenes: the paper explicitly acknowledges this limitation (lines 96-97).
- Claim that "evaluating only the ego vehicle is a methodological choice, not deliberate evasion": semantic nitpick that does not affect the paper's technical contribution.
- Reproducibility concern about missing appendix details: per instructions, appendices are stripped by the parser.
- Missing related works: removed per instructions (no external sources to verify).
- Claims about models/tools/benchmarks not existing: removed per instructions as all cited references are assumed to exist.

## Novel Insights
The observation that Split 4 achieves nearly comparable performance to the proposed split (0.6373 vs 0.6308) is genuinely useful: it suggests the main driver of the performance improvement may be eliminating the train-set familiarity gap rather than the spatial overlap removal. This helps clarify what the benchmark's split actually achieves. The refined metrics revealing that methods improving ego prediction can hurt non-ego prediction is another non-obvious finding — this would have been invisible under the old protocol and validates the benchmark's methodological contribution.

## Suggestions
- Explicitly state the close/far distance threshold in the main paper (e.g., "agents within the 30×60m range around the ego vehicle are classified as close; all others as far").
- Add a discussion comparing Split 1 and Split 4 in Table 1, explaining what each ablation buys and the trade-offs involved.
- Clarify the Table 5 row duplication issue.
- Report results with variance (e.g., over multiple seeds) for the key comparisons.
- Consider offering the new split as a complement to the existing protocol rather than a replacement, noting that each evaluates a different form of generalization.

**Calibration report:**

**Round 1 — Bracketing:** Low band (< 3.5): autonomous driving papers scoring 2.5-3.33 (clearly weaker than the paper under review). Mid band (3.5-7.5): ESDMotion (5.25), MapDR (5.00), BEV Uncertainty Benchmark (5.40, accepted), RedMotion (5.33), MotionBase (6.00). High band (> 7.5): papers scoring 8.00 (clearly stronger). The paper sits between 5.0 and 7.0.

**Round 2 — Narrowing:** The BEV Uncertainty Benchmark (5.40, accepted) is the closest topical anchor — a benchmark+method paper on autonomous driving. The paper under review has clearer motivation, more direct evidence, and more actionable findings, placing it above 5.40. ESDMotion (5.25) had incremental novelty concerns and was rejected. The paper under review is stronger. PMR (7.00) is a much larger-scale dataset effort with mixed reality, placing it higher. Final score: **6.0**, positioned between the accepted 5.40 benchmark and the 7.00 large-scale benchmark.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>