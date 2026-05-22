Now I have sufficient calibration data. Let me compile my final review.

**Bracket analysis:**
- Round 1 bracket: roughly 4.5–6.0
- Round 2 anchors:
  - "AQOT" (4.50): heuristic active learning, limited novelty, rejected — our paper is stronger
  - "Flip-flopped Samples" (5.25): well-theorized active learning, accepted — our paper has weaker theory but more novel application domain
  - "Diffusion Active Learning for CT" (6.0): similar generative+AL combination, but with cleaner presentation — our paper is weaker
- Final placement: ~5.0. Between the 4.5 and 5.25 anchors, closer to 5.25 in ambition but held back by presentation/theory gaps.

Now let me write the review.

---

Let me first organize the verified weaknesses and strengths from cross-checking the paper:

**Strengths (verified):**
1. Novel direction: active learning for flow matching (generative) models — under-explored area
2. Theory-motivated query strategies (Q_D, Q_A) derived from piecewise-linear analysis framework
3. Four-dataset evaluation including 3 real shape-design tasks
4. Q_D consistently outperforms baselines on diversity (Fig 4a)
5. Data-centric querying decoupled from generative model retraining — practical advantage
6. Ablation study validates multi-term Q_D design (Fig 9)
7. Hybrid strategy for tunable diversity-accuracy trade-off

**Weaknesses (verified):**
1. Q_A is missing from Figure 4, the central comparison figure — the paper claims Q_A yields highest accuracy but the comparison figure only shows Q_D, Random, Coreset, Committee, and Anchor
2. Piecewise-linear assumptions are stated as hypothesis but the abstract claims "rigorous theoretical characterization" — gap between claims and delivery
3. RBF label predictor accuracy/performance never evaluated; sensitivity of query strategies to prediction errors not studied
4. Lemma 2 and error bound (Eq 5) stated without proof in main text
5. Diversity metric uses simple pairwise distance rather than proper Vendi score, substitution not justified
6. Limited implementation details: RBF architecture, hyperparameter choices
7. No convergence verification reported for the 4M-step training

**Removed/Demoted harsh critic points:**
- ω contradiction: the paper text (line 187) is self-consistent with the equation; the parser-generated figure description may be wrong. Demote to a note about verification needed.
- "No empirical evidence of condensation": the paper frames this as a hypothesis. Keep as a limitation of the theory but not a fatal flaw.
- "Closed-form solution invoked without verification": this is the framework assumption, not a missing verification. Remove.
- Full dataset baseline missing: the paper mentions this in text but doesn't show it in plots. Minor point.
- Hyperparameter sensitivity analysis: minor/nice-to-have.
- Missing code/data descriptions: standard for submissions; remove.

Now let me write the final review.## Summary

This paper presents a pilot study on active learning for conditional flow matching models in shape design. The authors propose a piecewise-linear neural network analysis framework to derive how individual data points influence a flow matching model's diversity and accuracy, yielding two query strategies: Q_D (diversity-oriented, selects points with labels similar to existing ones) and Q_A (accuracy-oriented, selects points with labels farthest from the current set), plus a weighted hybrid. Experiments on one synthetic and three real shape-design datasets (airfoil, flying wing, starship) show Q_D consistently outperforms discriminative active learning baselines on diversity, and the hybrid strategy enables a tunable trade-off.

## Strengths

- **Novel problem framing.** Active learning for generative models — specifically flow matching — is genuinely under-explored. The paper takes a principled approach rather than naively porting discriminative AL strategies, which distinguishes it from prior work that uses generative models only as tools for discriminative AL.

- **Theory-motivated strategy design.** The derivation connecting dataset composition to generation diversity (Eq. 3, the combinatorial product argument in §2.3) and accuracy (Eq. 5, the error-bound argument in §2.4) provides a coherent narrative for why Q_D and Q_A should work. The strategies follow transparently from the framework rather than being post-hoc heuristics.

- **Consistent diversity gains across diverse tasks.** Figure 4a shows Q_D achieving the highest diversity across all four datasets — synthetic, airfoil, flying wing, and starship — over multiple query iterations, outperforming Random, Coreset, Committee, and Anchor methods. Qualitative results (Figs. 3, 5, 6, 8) provide visual confirmation of the diversity advantage.

- **Ablation validates Q_D design.** Figure 9 demonstrates that all three terms in Eq. 4 (label similarity, entropy, data-space distance) contribute positively to diversity, with the data-space distance term being the dominant factor. This justifies the multi-term construction empirically.

- **Practical decoupling of querying from model training.** The query strategies operate on the dataset via an RBF label predictor rather than requiring repeated flow matching model retraining — a pragmatic design choice for annotation-budget-constrained settings.

## Weaknesses

### Major

- **Q_A missing from the central comparison figure.** Figure 4 — the paper's primary quantitative comparison across iterations — shows only Q_D, Random, Coreset, Committee, and Anchor. The text (line ~167) claims "Q_A yields the highest accuracy," but this claim is not supported by the figure intended to compare methods across iterations. Q_A's accuracy is shown only in per-condition qualitative figures (Figs. 5, 6, 8), which report point estimates for individual conditions. The systematic accuracy comparison of Q_A against all baselines across query iterations is absent from the paper's main evidentiary display. This is a significant evidential gap for one of the paper's two core proposed strategies.

- **Gap between theoretical framework claims and delivery.** The abstract claims a "rigorous theoretical characterization," but the core analysis rests on the hypothesis that the trained flow matching network behaves as a piecewise-linear interpolator (stated explicitly as a hypothesis in §2.2). The condensation literature cited (Luo et al., 2021; Xu et al., 2025) is not shown to apply to flow matching with continuous conditions under the paper's specific architecture and training regime. The extension from the clean 1D analysis (§2.3) to the general Q_D formulation (Eq. 4) relies on heuristic surrogates (minimum Euclidean distance as a proxy for label equality, cluster-entropy as a proxy for the product-of-counts argument) whose connection to the 1D insight is not analytically justified. Lemma 2 — which underpins the error bound (Eq. 5) motivating Q_A — is stated without proof or even a proof sketch in the main text. These gaps mean the strategies, while well-motivated by the framework, are not *derived* from verified mechanistic understanding in the sense the paper claims.

### Minor

- **RBF label predictor unevaluated.** Both Q_D and Q_A rely on an RBF network to predict labels of unlabeled points. The predictor's accuracy and the sensitivity of query selections to prediction errors are never characterized. Since the theoretical analysis assumes knowledge of label relationships, errors in the RBF predictions could cause the strategies to select suboptimal points.

- **Diversity metric substitution not justified.** The diversity score (Eq. 8) is described as a "custom variant of the Vendi score" but computes a simple average pairwise Euclidean distance rather than the eigenvalue-based Vendi score. This discards distributional information (a few extreme points can dominate the mean), and no evidence is provided that this simplified metric correlates with meaningful diversity in shape design.

- **No convergence verification.** The flow matching model is trained for a fixed 4M steps. Whether training actually converged is not reported or discussed.

### Trivial

- The ω direction in Figure 7: the paper text (line 187) states "a larger ω prioritizes diversity," consistent with Eq. 7 (Q_hybrid = ω Q_D + (1−ω) Q_A). The parser-generated figure description reports the opposite trend. While this is likely a parser artifact, the authors should verify the figure's correctness and ensure consistency.

## Nice-to-Haves

- A sensitivity analysis of α, β, γ weights in Eq. 4, or of the ω parameter in Eq. 7.
- Comparison of selections made with ground-truth labels vs. RBF-predicted labels to quantify sensitivity to prediction errors.
- Full-dataset performance shown on the same figures to contextualize absolute gains.
- Empirical verification that the trained model approximates piecewise-linear behavior (e.g., measuring deviation from linearity on interpolated conditions).

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"No empirical evidence that the model condenses to piecewise-linear"** — The paper frames this as a hypothesis, not a proven fact. The criticism is partially valid (the abstract overclaims) and is retained in moderated form as a Major weakness.
- **"ω definition contradiction is a fatal error"** — The parser-generated figure description contradicts the paper text, but the paper text itself (line 187, Eq. 7) is internally consistent. This is likely a parser artifact, not an author error. Demoted to Trivial.
- **"Closed-form solution invoked without verification"** — The paper uses the closed-form FM solution explicitly as part of the analytical framework; verifying that the trained network matches it would be circular (the framework *assumes* it). Removed.
- **"The diversity metric may be measuring a proxy" and "could confounders be controlled?"** — Generic sweep criticisms without concrete anchors in the paper. Removed.
- **"Full dataset baseline missing from plots"** — The paper mentions full-dataset performance in text. Moved to Nice-to-Haves.
- **"Missing code, hyperparameter search, data descriptions"** — Standard submission-level limitations; hyperparameter search falls under reproducibility nitpicks per instructions. Removed (code/descriptions) or moved to Nice-to-Haves (sensitivity analysis).
- **"Missing formal statement and proof sketch of Lemma 2"** — Retained within the Major weakness about the theory-practice gap, since this directly affects whether Eq. 5 is substantiated.

## Novel Insights

The paper's central insight — that in a piecewise-linear flow matching regime, label-identical data promotes combinatorial sample diversity while label-diverse data bounds generation error — provides a clean dataset-level explanation for the diversity-accuracy trade-off that is typically studied at the model or training level. Even if the piecewise-linear assumption is strong, this decomposition of dataset influence into two antagonistic forces is conceptually useful and could inform dataset design beyond the active learning setting.

## Suggestions

- Add Q_A to Figure 4 (or a companion figure) showing accuracy across iterations alongside all baselines. This is the single highest-impact fix.
- Include a proof sketch or at minimum a clear statement of Lemma 2's assumptions in the main text, so Eq. 5 is not entirely unsubstantiated.
- Report the RBF predictor's held-out accuracy and discuss how prediction errors might affect query selections.
- Consider a simple experiment verifying the piecewise-linear behavior on a small subset, or at minimum acknowledge the gap between the hypothesized framework and the actual trained model more prominently.

## Score and Decision

**Originality:** The paper tackles a genuinely under-explored problem (active learning for generative flow matching models) and proposes theory-motivated strategies rather than heuristic adaptations. The diversity-accuracy decomposition from dataset composition is a fresh perspective.

**Importance:** Active learning for generative models in simulation-heavy domains (shape design, medical imaging) is practically important. The decoupled querying design has pragmatic value.

**Claim support:** The diversity claims are well-supported by Figure 4a and qualitative figures. The accuracy claims for Q_A are weakened by the absence from Figure 4. The theoretical framework overstates its rigor relative to what is delivered.

**Soundness:** The experimental methodology is adequate in scope (4 datasets, multiple baselines, ablation) but has gaps: Q_A missing from the central comparison, unevaluated RBF predictor, unjustified diversity metric simplification. The theory is well-motivated but rests on unverified assumptions.

**Clarity:** The paper is generally well-written and the flow from theory to strategy design is easy to follow. However, key mathematical objects (Lemma 2, the extension from 1D to general label space) are presented without sufficient substantiation.

**Value to community:** The dataset-centric perspective on diversity-accuracy in generative models and the practical query strategies provide a foundation for future work, even if the current theoretical framework needs further validation.

**Anchor comparisons:**
- "AQOT" (4.50, rejected): heuristic AL with limited novelty — our paper is clearly stronger in originality and scope.
- "Querying Easily Flip-flopped Samples" (5.25, accepted): well-theorized AL with rigorous proofs — our paper has weaker theory but a more novel application domain (generative models vs. classification).
- "Diffusion Active Learning for CT" (6.00, rejected): similar generative+AL scope, cleaner presentation — our paper is weaker due to the Figure 4 omission and theory gaps.
- "Flow Matching for Posterior Inference" (4.20, rejected): similar FM application with theory gaps — our paper has more complete experiments.

**Round 1 bracket:** 4.5–6.0. **Round 2 narrowing:** The paper sits above AQOT (4.50) and below "Diffusion Active Learning for CT" (6.0), most comparable to "Flip-flopped Samples" (5.25) in overall contribution level, but held back by the Q_A Figure 4 omission and the theory-claim gap. Final score: **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>