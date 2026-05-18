Now I have a thorough understanding of the paper and all the claims. Let me write the final consolidated review.

## Summary

This paper introduces a contextual biasing method for ASR that replaces WFST-based search with a vectorized implementation of the Knuth-Morris-Pratt (KMP) string matching algorithm applied during beam search. The method operates on token sequences directly, tracking partial matches of biasing phrases and adding score bonuses incrementally. It supports both on-the-fly rescoring and shallow fusion, can be extended with prefix (carrier phrase) boosting, and is designed to be TPU-friendly through vectorization. Without introducing trainable parameters, KMP biasing achieves 50–77% relative WER reductions on biasing test sets and yields further gains when combined with model-based biasing (NAM).

## Strengths

- **Large WER reductions without additional model parameters.** On the With-Prefix test set, KMP biasing (shallow fusion, F=4096) reduces WER from 9.6% to 2.4% for B=150, and from 20.9% to 4.8% on Without-Prefix (Table 1). These represent relative reductions of 75% and 77%, respectively, with no new trainable parameters.

- **Complementarity with model-based biasing (NAM).** Combining KMP biasing with NAM yields additive gains. On With-Prefix (B=150), NAM alone achieves 1.5% WER, while NAM + KMP (fusion, F=50) achieves 0.9%—a 40% relative improvement (Table 2). On Contact-Tag, the combination drops WER from 3.8% (NAM alone) to 3.4%.

- **Efficient handling of prefix-based biasing.** The proposed prefix-boosting method (§2.4) avoids the combinatorial explosion of concatenating prefixes with biasing phrases (which would create O(CB) extra patterns) by maintaining separate states for prefixes and biasing phrases with O(C+B) complexity. This is validated in Table 2, where adding prefix boosting further reduces WER.

- **Rigorous algorithmic exposition with complexity bounds.** The paper provides pseudocode for all key subroutines (Algorithms 1–3) and explicitly states time complexities for each operation (e.g., O(γ̄KB) per step for OTF rescoring). This level of detail supports reproducibility and informed deployment decisions.

## Weaknesses

### Fatal

None.

### Major

- **No empirical evidence of TPU efficiency.** The paper's central design motivation is that it is a "TPU-friendly" alternative to WFST-based biasing, with "careful considerations on memory footprint and efficiency on TPUs by vectorization" (abstract, §1). Yet the paper provides zero runtime measurements — no wall-clock time, no throughput comparisons (with or without biasing), no latency numbers, and no comparison to a WFST-based baseline on any hardware. The complexity analysis (O(γ̄KB), etc.) is necessary but not sufficient to substantiate the claim. Since the motivation for avoiding FSTs is precisely that they are "inherently sparse" and therefore inefficient on TPUs (line 32), the reader needs to see that the proposed alternative is actually efficient in practice. This is a structural gap: it leaves the paper's main practical proposition unsubstantiated, even though the accuracy results are strong.

### Minor

- **Out-of-domain degradation is under-analyzed.** On the Anti-Biasing test set (B=3000), WER degrades from 1.7% to 2.3% for shallow fusion (Table 1) — a 35% relative increase. The paper describes this as "not degrading… by much" (line 341), but provides no analysis of whether this degradation is uniform across utterance types, whether it concentrates on utterances with acoustic similarity to biasing phrases, or whether a confidence-based gating mechanism could mitigate it. The practical cost in production (where most traffic is out-of-domain) is unclear.

- **No experimental comparison to WFST-based biasing.** The paper positions itself as an alternative to WFST-based approaches (the standard inference-time method) but never compares against one experimentally. Without such a comparison, the reader cannot assess the relative accuracy of the method against the approach it seeks to replace. Adding a CPU-based WFST baseline (or explaining why it is infeasible on this model) would significantly strengthen the paper's positioning.

- **Hyperparameter robustness is not shown.** Only the best δ, s, and λ values are reported, with a brief remark that WER first drops, plateaus, then rises as δ increases. No sensitivity curves, confidence intervals, or analysis of how much performance changes when parameters deviate from the optimum are provided. This matters because these parameters must be tuned per use case and per B.

- **Matching restart prevents overlapping matches of different phrases.** When any biasing phrase is fully matched, matching restarts for all phrases (Algorithm 2, line 153). This means a hypothesis containing two different biasing phrases (e.g., "call John and text Mary") would only receive a bonus for the first. The paper states this is intentional ("we are not interested in overlapping matches," line 122) and the test sets contain utterances with at most one biasing entity, so this does not affect reported results. However, the limitation is not discussed, and it may affect generalization to use cases with multiple biasing entities per utterance.

### Trivial

None.

## Nice-to-Haves

- A comparison of WER as a function of δ for at least one setting (visualized as a sensitivity curve) to help practitioners assess tuning difficulty.
- An ablation comparing the linear incremental scoring function to alternatives (e.g., a constant bonus per full match) to verify that the incremental formulation drives the gains.
- Analysis of how results vary with beam size K (the paper uses K=8 throughout).

## Removed Points

These points were raised by reviewers but are removed or downgraded per the review guidelines:

- **"Scoring function is extremely simple"** — The paper explicitly acknowledges this (line 169: "It is future work to explore more sophisticated scoring functions") and the function is appropriate for the voice search use case with short phrases (max 16 tokens). This is acknowledged scope, not a weakness.
- **"Prefix boosting tested with only three prefixes"** — The paper states "It is future work to conduct full-fledged experiments with more complex prefixes" (line 396-397). The experiments adequately validate the mechanism; more prefixes would not change the conclusion about the method. This is scope the paper already acknowledges.
- **"Strength: TPU-friendly alternative"** (from Strength Finder) — This claimed strength conflicts with the verified major weakness that no empirical TPU efficiency evidence is provided. The design considerations exist but are not validated. Per guidelines, when a strength and weakness disagree, the weakness wins.

## Novel Insights

The key insight that emerges from the reviews is that the paper's strongest contribution is decoupled from its headline claim: the KMP-based biasing algorithm delivers large and consistent WER improvements regardless of whether one cares about TPU efficiency. Even if the TPU-friendliness claim were set aside entirely, the method stands on its own as a clean, parameter-free, and well-specified inference-time biasing technique that complements model-based approaches. The vectorization strategy for running KMP-style matching across thousands of phrases in parallel is a genuine algorithmic contribution that could find use beyond ASR (e.g., in other sequence transduction tasks with discrete constraints). The reviews also surface that the paper could be strengthened more by narrowing its claimed scope than by expanding experiments: if the TPU efficiency claim were softened or deferred to future work, the remaining claims would be fully supported by the evidence.

## Suggestions

1. **Provide runtime measurements.** The single highest-leverage improvement is to report wall-clock time or throughput for each variant (OTF rescoring, shallow fusion with various F) on the same TPU hardware, ideally comparing against a reasonable implementation of WFST-based shallow fusion (even on CPU). This directly substantiates the central claim of TPU-friendliness.

2. **Analyze the out-of-domain degradation more deeply.** Explore whether degradation concentrates on certain utterance types, or whether a simple confidence-based gating mechanism could reduce it. This would increase the practical credibility of the method.

3. **Add a WFST experimental comparison, or explain its absence.** Even a brief note that WFST-based biasing is not compatible with the current model/hardware stack (which itself supports the motivation) would help.

4. **Include hyperparameter sensitivity analysis.** A plot of WER vs. δ for one representative setting would give readers a sense of the plateau width and tuning difficulty.

5. **Discuss the matching restart limitation** explicitly and note that it is not a concern for the single-phrase-per-utterance test setup but may matter in other deployments.

## Score and Decision

This paper presents an elegant algorithmic contribution — adapting the KMP algorithm for ASR biasing with vectorized multi-phrase matching — and backs it with strong WER results on large-scale data. The accuracy improvements are substantial and the complementarity with model-based biasing is clearly demonstrated. However, the paper's central narrative frames the method as a "TPU-friendly" alternative to WFST-based biasing, yet provides zero empirical evidence of efficiency. This is a structural gap in the evidence for the claimed contribution, not a minor omission. The paper would be strengthened considerably by adding runtime measurements and a WFST baseline comparison, and the out-of-domain degradation needs more careful treatment. The core idea is worth publishing, and the accuracy results are compelling, but the paper does not fully support its own framing.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>