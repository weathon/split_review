Now I have all the comparisons I need. Let me finalize the review.

**Comparison summary across rounds:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| Driving by the Rules (MapDR) | 5.00 | R1 | OMMP-Bench is stronger: clearer motivation, more systematic empirical evidence |
| ESDMotion | 5.25 | R2 | OMMP-Bench is clearly stronger: fewer misleading claims, better experimental design |
| RedMotion | 5.33 | R1 | OMMP-Bench is stronger: clearer novelty, better experimental rigor |
| BEV Uncertainty Benchmark | 5.40 | R2 | OMMP-Bench is stronger: more impactful problems identified |
| TAO-Amodal | 6.00 | R2 | OMMP-Bench is comparable or slightly stronger: more analytical depth |
| SmartPretrain | 6.75 | R2 | Slightly below: SmartPretrain has broader model support and SOTA results |
| RouteFormer | 6.67 | R1 | Comparable level of contribution |
| SEPT | 7.00 | R1 | Below: SEPT has SOTA results on major benchmarks |
| PMR | 7.00 | R2 | Below: PMR has larger scale data contribution and multi-modality |

**Round 1 bracket:** 5.5 – 7.0
**Round 2 narrowed bracket:** 5.75 – 6.5
**Final score:** 6.0

The paper is clearly above the 5.0–5.5 reject range and below the 7.0 strong-accept range. The lack of variance reporting (the main substantive weakness) and the mild Table 1 confound keep it from being higher, but the diagnostic value and systematic empirical approach push it above the borderline.

---

## Summary
This paper identifies three protocol-level problems in the emerging field of online-map-based motion prediction: (1) inappropriate dataset splits that create a train-validation gap under two-stage training, (2) a perception-range mismatch between online mapping models and motion prediction requirements, and (3) non-discriminative evaluation metrics that overrepresent easy static agents or evaluate only the ego vehicle. It proposes OMMP-Bench with a new spatially-disjoint data split, refined agent-grouped metrics, and a simple baseline that uses raw image features via deformable attention to provide out-of-range agents with environmental context. The paper's primary contribution is a corrected evaluation protocol that disentangles these confounds for the field.

## Strengths
- **Empirically grounded diagnosis of the train-validation gap**: Table 1 provides within-group evidence (Split 2 vs Split 1 on the same eval set; Split 4 vs Split 3 on the same eval set) showing that training the map model on data overlapping with motion training data harms motion prediction. Figure 4 quantifies the spatial overlap problem (87% in default vs 5% in proposed split), giving a concrete geometric explanation.
- **Clear two-table demonstration of the range mismatch**: Table 2 shows online mapping mAP collapses from 0.164 (30×60m) to 0.002 (100×100m). Table 3 shows ground-truth maps at longer range improve motion prediction (minADE 0.6154 → 0.6003). Together these establish that range matters for prediction quality and current map models cannot deliver it.
- **Granular metrics expose static-agent dominance**: Table 6 shows static agents have near-zero error (minADE 0.002) while far non-ego agents have minADE 0.6997 — over 300× higher. This directly justifies excluding static agents and stratifying by distance.
- **Effective and simple boundary-free baseline**: The deformable-attention baseline consistently improves far-agent prediction across all model combinations in Table 7. With MapTRv2-CL+HiVT, far non-ego minADE drops from 0.6999 (base) to 0.6274 (img), while prior methods `unc` and `bev` degrade far-agent performance (0.7071 and 0.7242).
- **Comprehensive cross-method benchmarking**: Table 7 evaluates 24 model-method combinations (2 map models × 2 motion models × 4 methods) across three agent categories (ego, close, far), providing dense evidence for benchmark design choices.
- **Actionable map-element ablation**: Table 5 isolates the contribution of individual map element types, showing centerlines alone nearly match the full set, providing practical guidance for the online mapping community.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **No variance reporting**: No standard deviations, confidence intervals, or significance tests are reported across any of the 7 tables. For a benchmark paper that aims to set evaluation standards, this is a notable omission. Some differences between methods are modest (e.g., img minADE 0.6163 vs bev 0.6287 in Table 4, ~2% relative), and the proposed validation set contains only 86 scenes, making scene-composition effects a real concern. The reader cannot assess whether reported differences are reliable.
- **Table 1 headline comparison confounds training protocol with evaluation set**: The paper's main textual comparison is Split 1 (proposed split, eval on Motion Val) vs Split 3 (default split, eval on nuScenes Val), which differ in both the training protocol and the evaluation data. The within-group comparisons (Split 2 vs 1, Split 4 vs 3) do support the claim, but the paper should acknowledge this confound explicitly rather than relying on the cross-protocol comparison as the primary headline evidence.
- **Some claims about degradation are weakly supported**: The paper states that `unc` and `bev` methods "show performance drops when predicting close non-ego agents compared to base method." For MapTRv2-CL+HiVT, base gets 0.5585 on close non-ego while unc gets 0.5682 — a ~1.7% difference that could easily be noise (especially without error bars). The directional observation that methods improving ego prediction do not necessarily help other agents is valid, but claims of actual degradation on close agents are overstated given the magnitude of differences.

### Trivial
- **Moving threshold lacks sensitivity analysis**: The threshold for classifying agents as "moving" (2 meters over 3 seconds, ~0.67 m/s) is quite permissive and may include near-stationary agents. The benchmark would benefit from analysis of how results vary with this threshold.
- **Table 5 omits key multi-element combinations**: The most informative combination — boundary + centerline, the two strongest single elements — is absent. This would reveal whether adding elements yields additive or redundant benefits.
- **The img method is under-specified in the main text**: Equation (1) is the entirety of the method description. How initial agent features are obtained, how aggregated features are fused into the motion model, and the dimensions involved are not described in the main body.

## Nice-to-Haves
- The image-feature baseline's gains on far agents significantly exceed the upper bound from perfect long-range GT maps, suggesting image features may contribute beyond merely filling missing map information (e.g., appearance cues about road geometry). Exploring this mechanism would strengthen the paper's diagnostic value.
- Reporting computational cost (inference latency or FLOPs) of the img baseline relative to base would help practitioners assess the cost-benefit tradeoff.
- A cross-protocol evaluation — training the motion model under the default protocol and evaluating on the proposed Motion Val set — would isolate the train-val gap more cleanly, though the within-group evidence is already present.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Split methodology not described** (from Harsh Critic): The critic notes the split construction methodology is vague. However, the critic acknowledges these details likely reside in Appendix A (stripped by the parser). Per rules, remove appendix-deferred criticisms.
- **Range mismatch conclusion not justified** (from Harsh Critic): The critic argues the leap from Table 3's GT-map gains to "current models cannot meet requirements" is not fully justified. However, the paper's logic combines Table 2 (mappers fail at long range) + Table 3 (long-range maps help) → current models can't deliver. This inference is reasonable; the criticism reads as speculative skepticism rather than an identified flaw.
- **Missing related works** (from Strength Finder / Harsh Critic): Per rules, do not flag missing related works.

## Novel Insights
The paper's most striking empirical finding is the asymmetry between improvements from prior methods (`unc`, `bev`) for ego vs. non-ego agents. Table 7 reveals that methods designed to improve ego prediction under the old protocol can actually degrade performance on far non-ego agents (e.g., MapTRv2-CL+HiVT far: unc 0.7071 vs base 0.6999; bev 0.7242 vs base 0.6999). This validates the paper's core methodological critique: optimizing for the old protocol's ego-only metrics can produce methods that regress on the actual task of predicting other vehicles' motion — a finding that would have remained hidden without the proposed benchmark.

## Suggestions
- Run multiple seeds (at least 3) on the main results in Table 7 and report standard deviations. With only 86 validation scenes, this is important for the benchmark's credibility and is directly addressable in rebuttal.
- Either run the cross-protocol evaluation or explicitly acknowledge the confound in Table 1 and rely on the within-group comparisons (Split 2 vs 1, Split 4 vs 3) as the primary evidence for the train-val gap claim.
- Add boundary+centerline combination to Table 5 to reveal additive vs. redundant effects.
- Tone down claims about degradation on close non-ego agents where differences fall within plausible noise range.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>