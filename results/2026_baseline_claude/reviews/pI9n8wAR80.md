## Summary
CoLA (Co-Calibrated Logit Adjustment) is a method for Long-Tailed Semi-Supervised Learning (LTSSL) that addresses two under-studied limitations of Logit Adjustment (LA): (1) naive frequency counting overestimates head-class prevalence due to sample redundancy, causing over-suppression; (2) the optimal overall LA scaling strength τ is highly sensitive to the class distribution yet treated as a fixed hyperparameter in prior work. CoLA introduces DDDE, which uses the effective rank of per-class feature matrices to measure redundancy-adjusted class sizes, and LMC, which meta-learns τ on a proxy validation set constructed to match the estimated unlabeled distribution. The method achieves state-of-the-art on CIFAR-10/100-LT, STL-10-LT, and SIN-127 across five distinct unlabeled distribution scenarios.

---

## Strengths

- **Well-diagnosed problems with empirical validation.** Figure 1(a) clearly shows how sample redundancy inflates head-class estimates, and Figure 1(b) concretely demonstrates that the optimal τ is non-monotone in the imbalance ratio γ_l (e.g., τ∗ for γ_l=100 > τ∗ for γ_l=150 on CIFAR-10-LT). These motivating experiments ground both contributions in observable phenomena rather than abstract conjecture.

- **Principled use of effective rank for redundancy estimation.** Applying erank (Roy & Vetterli, 2007) as a proxy for the effective number of samples is a creative and theoretically grounded choice. It is computationally lightweight (SVD of a per-class feature matrix), interpretable as the exponentiated Shannon entropy of the singular value spectrum, and does not require explicit clustering or distance-based deduplication.

- **Strong, consistent empirical improvements.** CoLA is best in all 10 distribution-dataset combinations on CIFAR-10/100-LT (Table 1), all 4 settings on STL-10-LT (Table 2), and both resolutions on SIN-127 (Table 3). Margins over the runner-up on the harder CIFAR-100-LT dataset exceed 1 pp in nearly every case, which is meaningful given the competitive baseline pool.

- **Thorough ablation with clear decomposition.** Table 4 isolates DDDE and LMC, and demonstrates their interaction: (a) fixed τ gives inconsistent results across datasets; (b) LMC with noisy frequency-counting underperforms CoLA, showing that DDDE is a prerequisite for LMC to work well; (c) DDDE alone over frequency counting already narrows the gap. Table 5 directly measures distribution estimation error and confirms DDDE is more accurate than NWGMA and MCA.

- **Theoretical link between distribution estimation and pseudo-label quality.** Proposition 1 formally ties DDDE accuracy to the tightness of the generalization bound for τ∗, providing a theoretical motivation for the co-design philosophy. The convexity analysis (in the appendix) guarantees a unique global minimum for the LMC objective.

---

## Weaknesses

### Fatal
None.

### Major

1. **Proposition 1 is generic domain-adaptation theory, not LTSSL-specific.** The bound is a straightforward application of importance-weighted ERM (covariate shift, Shimodaira 2000), with Rademacher complexity controlling the richness of ℋ_τ. Since τ is a single scalar, ℋ_τ is a one-dimensional family and its Rademacher complexity trivially converges to zero quickly. Proposition 1 does not quantitatively distinguish DDDE from frequency counting, nor does it give guidance on how large the proxy set V needs to be relative to K or the imbalance ratio. The theoretical contribution would be substantially strengthened by bounding the discrepancy term |R̂_{𝒟_v,w} − R̂_{𝒟_v}| explicitly in terms of the estimation error of DDDE.

2. **LMC is applied as a single one-time calibration, not an adaptive update.** Figure 2 shows that τ∗ is fixed after approximately epoch 200 (a warm-up driven by ACR). Because the pseudo-label distribution continues to evolve after this point, the static τ∗ may be suboptimal in later training stages, particularly under distribution shift. The paper does not analyze sensitivity to the epoch at which LMC is triggered, nor does it consider online updates to τ during training.

### Minor

1. **Warm-up stage inherits ACR's τ initialization without sensitivity analysis.** During the warm-up, τ is set according to ACR's heuristic. How CoLA's final performance depends on warm-up length or ACR's specific τ during that phase is not analyzed. If ACR's warm-up produces systematically worse feature representations, DDDE (which runs on those features) would inherit the damage.

2. **DDDE is computed only on high-confidence samples (confidence > ρ).** In early training, when the model is most biased, few high-confidence samples exist (especially for tail classes), so the erank estimates could be unreliable for the classes where correction matters most. The paper does not report erank estimates over training epochs to show stability.

3. **The improvement on CIFAR-100-LT in Table 5 is modest.** The L₂ distance improvements of DDDE over NWGMA range from 0.0024 to 0.0072 on CIFAR-100-LT. It is unclear whether such small differences in distribution estimation accuracy drive the 1+ pp accuracy gains; an additional sensitivity plot relating estimation error to final performance would strengthen the causal story.

### Trivial
None worth mentioning.

---

## Nice-to-Haves

- A plot of τ∗ found by LMC across different distribution types and imbalance ratios would corroborate Figure 1(b) and confirm that LMC discovers the non-trivial sensitivity the paper claims.
- An online/periodic variant of LMC that re-estimates τ throughout training (e.g., every 50 epochs) would address the static-calibration concern and potentially yield further gains.
- A breakdown of per-class accuracy (head vs. tail) before and after DDDE correction would make the over-suppression fix more visually concrete.

---

## Novel Insights

The most genuinely novel insight is the empirical finding that the optimal overall LA scaling τ is non-monotone in the labeled imbalance ratio γ_l—a counter-intuitive result that undermines all methods treating τ as a monotone function of the imbalance ratio or as a fixed hyperparameter. This insight, combined with the demonstration that class-wise and overall LA components interact bidirectionally (an inaccurate distribution estimate corrupts τ∗, and a mistuned τ wastes a good distribution estimate), motivates a co-design framework that is principled rather than heuristic. The use of effective rank as a redundancy-corrected sample count is also a transferable idea with broader applicability beyond LTSSL.

---

## Suggestions

- Provide an analytical or empirical bound on how DDDE's reduction in L₂ distribution error translates into a reduction in the discrepancy term |R̂_{𝒟_v,w} − R̂_{𝒟_v}| in Proposition 1.
- Test whether periodic re-calibration of τ (e.g., every 25 epochs after warm-up) improves over the single-shot calibration, especially in settings where the pseudo-label distribution changes rapidly.
- Report head/medium/tail accuracy breakdown to confirm that DDDE specifically corrects head-class over-suppression rather than uniformly shifting performance.
- Conduct a study on the computational overhead of erank computation (SVD per class per epoch) at scale, especially for SIN-127 with 127 classes.

---

## Score and Decision

CoLA is a focused, well-motivated contribution that identifies two concrete, underexplored problems in LA-based LTSSL and proposes principled solutions for both. The experimental validation is thorough, the ablation is convincing, and the empirical improvements are consistent and meaningful. The main limitations—generic theory and static τ calibration—are real but do not invalidate the core claims. This is a solid, ready-to-publish paper for the LTSSL community.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>