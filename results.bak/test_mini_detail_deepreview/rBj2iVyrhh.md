Now I have a good understanding of the calibration landscape. Let me write my consolidated review.

**Round 1 Bracket**: Low ~2.33-3.33, Mid ~4.33-6.33, High ~8.0. This paper clearly falls in the middle band.

**Round 2 Narrowing**: Comparing against anchors like the accepted 6.33 paper (which has stronger theory and cleaner presentation) and the 5.5-6.0 papers (which have similar profiles with some presentation/rigor issues), I place this paper at 5.5. It has genuine novelty and strong results but is held back by several presentation inconsistencies and one methodological underspecification.

---

## Summary

This paper proposes Classifier-Constrained Alternating Training (CCAT) to address modality imbalance in multimodal learning. The key idea is to pretrain a shared classifier with a modality-contribution regularization term, then freeze it during alternating encoder updates (adding modality-specific LoRA adapters) to prevent dominant modalities from biasing decision boundaries. A sample-level secondary update mechanism targets severely imbalanced samples. Experiments on CREMA-D, Kinetic-Sound, and MVSA show consistent improvements, with particularly large gains on Kinetic-Sound (+6.76%).

## Strengths

1. **Novel two-stage framework with a well-motivated classifier-centric design (Section 3.2–3.3, Algorithm 1)**: The core idea of freezing a balanced classifier during alternating training is a clean and principled solution to a real limitation of existing alternating training methods like MLA. Combining this with modality-specific LoRA adapters (to handle the distribution mismatch between fused and unimodal features) and sample-level secondary updates creates a systematic pipeline that addresses imbalance at both dataset and sample levels.

2. **Strong ablation study confirming each component's contribution (Table 2)**: The ablation systematically removes classifier freezing, alternating training, secondary updates, and LoRA modules. Each component positively contributes, with the largest drop from removing classifier freezing (85.89% → 82.80% on CREMA-D). This provides clear evidence that the full framework is more than the sum of well-tuned pieces.

3. **Large and consistent empirical gains (Table 1)**: CCAT achieves +6.76% on Kinetic-Sound (79.29% vs. 72.53% for LFM) — a substantial improvement — and +1.92% on MVSA. The improvement on the weaker unimodal performance (e.g., Video on CREMA-D: 73.79% vs. 68.01% for MLA) shows that the method genuinely boosts the underperforming modality.

4. **Hyperparameter analysis with grid search (Table 3, Figure 4)**: The paper reports grid search results for LoRA rank *r* and imbalance threshold *β* across all three datasets, showing that optimal values differ by dataset and that performance is reasonably stable near the optimum. This provides useful practical guidance.

## Weaknesses

### Fatal
None.

### Major

1. **Underspecified contribution score computation during the alternating training stage (Section 3.3, Algorithm 1 line 10)**: The paper states that during alternating training, contribution scores *cᵢᵐ* are computed "following the same decision-level fusion used in the inference stage." However, the mutual information formula (Eq. 5) requires a fused feature ***f*ᵢ** to compute MI(**z*ᵢᵐ***, *f*ᵢ*). Under decision-level fusion (averaging unimodal logits), there is no explicit fused feature vector defined. The paper does not specify what *f*ᵢ is during this stage, nor how MI is estimated from unimodal logits or decision-level outputs. This is not a fatal flaw — a reasonable reader can infer the general intent — but the mechanism is underspecified enough that the results relying on it cannot be fully evaluated without clarification.

### Minor

2. **Numeric inconsistencies in Figure 1 and the abstract**: The text on line 80 states that MLA "reduces initial contribution disparity (1.00 → 0.92)," but the table embedded in Figure 1 shows MLA Modality A at 0.90 (not 0.92) at epoch 100, giving a disparity of 0.80 (not 0.08). Additionally, the abstract reports a gain of "+1.35% on CREMA-D," but Table 1 shows the best baseline (LFM, 83.62) to CCAT (85.89), which is a gain of +2.27%. While neither error invalidates the core claim, they suggest sloppy finalization and erode confidence in the reported numbers.

3. **Missing standard deviations (Table 1)**: All main results are reported as averages over three seeds without standard deviations. On MVSA, the gap between CCAT (80.73%) and MMPareto (78.81%) is only 1.92%, and without variance information it is impossible to assess whether this gap is statistically significant. This is a standard reporting expectation for empirical papers.

4. **Missing comparison with SMLV (Section 2 vs. Section 4.1)**: The paper cites Sample-level Modality Valuation (SMLV, Zhou et al. 2025b) in the related work as a method that "addresses intrinsic data imbalance via per-sample modality contribution quantification" — which is conceptually the most directly related baseline to CCAT's sample-level secondary update. Yet SMLV is absent from the experimental comparison. Including it would strengthen the paper's positioning.

5. **Theoretical connection is motivational rather than rigorous (Section 3.1)**: The derivation showing the similarity between class and modality imbalance uses implicit coefficients *γ₁, γ₂* that are described as "learned modality utilization coefficients" but are not formally connected to any specific model parameters. The analysis provides a useful intuition but does not constitute a formal theoretical framework as claimed in Contribution (i).

### Trivial
- The figure caption for Figure 1 says "Ours lines show a more pronounced imbalance" when the data clearly shows Ours has *less* imbalance (disparity 0.30 vs. MLA's 0.80). The intended meaning (more pronounced *correction* of imbalance) is clear from context but the wording is wrong.
- No sensitivity analysis for the regularization coefficient *λ* (set to 0.001).

## Nice-to-Haves
- An experiment on a tri-modal dataset (or even a synthetic tri-modal setup) would strengthen the claim of generalization beyond two-modality scenarios.
- A comparison of training time or FLOPs against MLA would help contextualize the computational trade-off of the two-stage pipeline.

## Removed Points

- **"Figure 1 inconsistency is a fatal credibility issue"**: While the numeric discrepancy is real, it does not invalidate the figure's core message (CCAT achieves more balanced contributions than MLA). The reviewer overstates severity.
- **"The baseline comparison may be unfair"**: The reviewer speculates about different evaluation protocols without evidence. The paper describes using the same encoder architecture (ResNet18) across methods, and the large gap between Concat (18.68% video) and MLA (68.01% video) is expected behavior for a weak modality under vanilla fusion vs. a dedicated balancing method.
- **"The class/modality imbalance connection lacks rigor"**: This is downgraded to minor. The paper uses this as motivation, not as a formal proof, and the reviewer's criticism that *γ₁, γ₂* are not formally defined is noted but does not threaten the main contribution.
- **"Strengths about 'important problem' and 'addressed an important question'"**: Generic strengths that lack specific evidence are removed.

## Novel Insights

The most interesting observation that emerges from cross-referencing the reviews is that CCAT's largest relative improvement (+6.76% on KS vs. +1.35-2.27% on CREMA-D and +1.92% on MVSA) occurs on the dataset where the baseline LFM (72.53%) leaves the most room for improvement. This suggests that classifier-constraining may be most impactful when the starting imbalance is severe, and that on already well-balanced datasets the gains are more modest. The paper does not explore this relationship explicitly, but it is a natural hypothesis for future work.

## Suggestions

1. Clarify how fused features *f*ᵢ are obtained under decision-level fusion for the sample-level contribution computation in the alternating training stage.
2. Correct the numeric errors: (a) the "1.00 → 0.92" claim about MLA in the Figure 1 discussion, and (b) the "+1.35%" CREMA-D gain in the abstract to "+2.27%".
3. Report standard deviations for all main results.
4. Add SMLV to the experimental comparison if feasible, or explicitly state why it was excluded.

## Score and Decision

**Round 1 bracketing**: The weak anchors (scores ~2.3–3.3) are papers with fundamental flaws or very limited scope. The strong anchors (score 8.0) are polished papers with rigorous theoretical or empirical contributions. This paper sits squarely in the middle band (4.3–6.3).

**Round 2 narrowing**: Compared against accepted papers at 6.0–6.33 (e.g., the test-time adaptation paper at 6.0, the contrastive multimodal learning paper at 6.25), CCAT has a more novel core idea and stronger empirical results on KS, but is held back by presentation inconsistencies (Figure 1, abstract) and an underspecified algorithmic component. Compared against rejected papers at 4.33–5.5, CCAT has a clearer contribution and more convincing ablations. The closest comparable anchor is the "Towards Holistic Multimodal Interaction" paper (avg 5.50) which similarly has interesting ideas but is weakened by experimental rigor issues — CCAT is slightly stronger empirically due to the large KS gain and clean ablation.

**Final baseline anchors** (all rounds):

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| a4O528mek9 | 3.00 | 1 | Much weaker; generic multi-modal method with no clear novelty |
| YrxhSkfHh0 | 3.33 | 1 | Much weaker; method of limited significance |
| gNoqEdT2wO | 2.33 | 1 | Much weaker; benchmark with limited scope |
| lNtio1tdbL | 3.00 | 1 | Much weaker; unrelated topic (model merging) |
| BZWssJoYEv | 5.50 | 1 | Similar; has theoretical framing but weaker empirical results |
| ul1cjLB98Y | 5.25 | 1,2 | Comparable; purely theoretical paper, CCAT is stronger empirically |
| 5BXWhVbHAK | 6.33 | 1,2 | Slightly stronger; accepted with cleaner theory and presentation |
| Pa6SiS66p0 | 4.33 | 2 | Weaker; narrower scope (continual learning with missing modalities) |
| XTwwtlEfTF | 4.50 | 2 | Weaker; narrower scope (missing modalities) |
| 1L52bHEL5d | 6.00 | 2 | Slightly stronger; accepted with thorough experiments |
| Pe3AxLq6Wf | 6.25 | 2 | Slightly stronger; accepted, mixed reviews on theory |
| VeSsiD0DP9 | 5.75 | 2 | Comparable; hallucination benchmark, different domain |

**Final score**: 5.5. The paper has a genuinely novel contribution and strong empirical results, particularly on Kinetic-Sound, but is weakened by several presentation inconsistencies and one methodological underspecification that need to be resolved.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>