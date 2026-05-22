Now I have all the information needed. Let me compose the final consolidated review.

---

## Summary

This paper identifies two interrelated limitations of Logit Adjustment (LA) for long-tailed semi-supervised learning: (1) naive frequency counting overestimates head-class prevalence due to sample redundancy, causing over-suppression, and (2) existing methods treat the overall adjustment strength τ as a fixed hyperparameter, ignoring its sensitivity to the estimated distribution. CoLA addresses these by (a) DDDE, which estimates the unlabeled class distribution via the effective rank of per-class feature matrices to account for redundancy, and (b) LMC, which meta-learns τ on a proxy validation set resampled to match the DDDE-refined distribution. A generalization bound connects the two components. Experiments across CIFAR-10/100-LT, STL-10-LT, and SIN-127 with six distribution types show consistent but modest (1–3 pp) improvements over prior methods.

## Strengths

- **Consistent SOTA across diverse distribution shifts**: Table 1 shows CoLA achieves the highest accuracy on all five distributions on both CIFAR-10-LT and CIFAR-100-LT, outperforming every prior method including strong LA-based baselines. On the more challenging CIFAR-100-LT, margins exceed one percentage point in nearly all settings.

- **Ablation evidence that both components are necessary**: Table 4 compares the full CoLA against variants lacking DDDE (w/o D-L) and variants using a fixed τ (w/o D-τ). In every distribution on both datasets, removing either component degrades performance, directly supporting the paper's central claim that class-wise and overall adjustment must be co-designed.

- **Clear empirical motivation for adaptive τ**: Figure 1(b) demonstrates that the optimal overall adjustment strength varies non-monotonically with the imbalance ratio and number of classes, showing that a fixed hyperparameter is insufficient. This observation directly grounds the paper's core claim.

- **Scalability to challenging real-world scenarios**: Tables 2–3 show CoLA achieves SOTA on STL-10-LT (unknown/OOD unlabeled distribution) and SIN-127 (large-scale, 127 classes), demonstrating applicability beyond small controlled benchmarks.

- **Theoretical generalization bound linking DDDE and LMC**: Proposition 1 provides a PAC-style bound that connects distribution-estimation accuracy (DDDE) to the quality of the meta-learned τ (LMC) through a discrepancy term, formalizing why the co-design is principled.

## Weaknesses

### Major

- **Missing ablation comparing the linear LA term against the standard log form.**  
  The paper replaces the standard `−τ log P(y)` with `−τ · P(y)`, justifying this as avoiding numerical instability and overly aggressive penalization (Section 4.2, citing Mor & Carmon 2025). However, no experiment isolates whether the reported gains come from the proposed framework or from this specific design choice. Since the linear term fundamentally changes how adjustment scales with class frequency — tail classes receive proportionally much smaller penalties — an ablation comparing linear vs. log LA within the same CoLA pipeline is essential to attribute the improvements correctly.

- **DDDE's robustness for tail classes and early-training instability is not analyzed.**  
  DDDE builds feature matrices from pseudo-labeled samples above confidence threshold ρ. Tail classes will have very few such samples in early training, making the singular value spectrum noisy. The paper measures L₂ estimation error only over the final 8 epochs (Table 5), which avoids early-stage instability. While Figure 2 shows pseudo-label accuracy over all epochs, there is no epoch-wise analysis of DDDE's distribution estimate quality, no sensitivity analysis w.r.t. the threshold ρ, and no discussion of the edge case where a tail class has zero or very few confident pseudo-labeled samples (making the feature matrix degenerate). The warm-up phase mitigates this partially but its sufficiency is not demonstrated.

### Minor

- **The meta-learning procedure on a resampled proxy set may overfit when the labeled set is small.**  
  The proxy set D_v is constructed by rejection-sampling from the labeled set D_l to match the estimated unlabeled distribution. When tail classes have very few labeled samples (e.g., ~15), resampling repeatedly selects the same few samples, producing a very small proxy set. The paper does not report the typical size of D_v or analyze the variance of the learned τ across seeds, leaving a methodological gap in assessing reliability.

- **The theoretical bound is standard and does not leverage the specific structure of CoLA.**  
  Proposition 1 is a standard importance-weighted Rademacher bound. It treats any h_τ and does not exploit the specific structure of the logit-adjusted classifier. The bound's form highlights the importance of DDDE (via the discrepancy term), but it does not explain why the meta-learned τ should outperform a fixed heuristic — it only guarantees generalization if the discrepancy is small.

- **Edge cases of DDDE are not discussed.**  
  When m_y < d (tail class has fewer confident pseudo-labels than feature dimensions), the full-rank assumption for Z_y still holds in the sense that rank ≤ m_y, but the erank is bounded above by m_y, which is small. The paper does not discuss this regime or how the method behaves when erank values for tail classes are near their theoretical minimum.

### Trivial

None.

## Nice-to-Haves

- An epoch-wise plot of DDDE's L₂ estimation error (not just final-8-epoch average) would strengthen the claim that the estimator is stable throughout training.
- Reporting the typical size of the proxy validation set D_v and the learned τ values across seeds would address overfitting concerns.
- A brief discussion of the m_y < d regime for tail classes in DDDE would improve completeness.

## Removed Points

These points from the inputs were removed because they are factually incorrect, duplicate, or violate the review rules:

1. **"The linear LA term is introduced without explanation"** (Harsh Critic): The paper *does* provide an explanation in Section 4.2: "This linear term, as opposed to the logarithmic one, avoids potential numerical instability and overly aggressive penalization for classes with very small estimated probabilities." The request for an ablation is valid and retained above; the claim of "no explanation" is factually wrong.

2. **"ADELLO comparison mentioned only in appendix"** (Harsh Critic): The paper states in Section 6.2.2 that the comparison is in Appendix I. The appendix exists in the original submission; this is a page-limit artifact.

3. **"TRAS performs ~59% on CIFAR-10-LT, the paper does not comment on why"** (Harsh Critic): This is a minor observation about a baseline, not a weakness of the proposed method.

4. **"The erank is sensitive to m_y so it may reintroduce frequency bias"** (Harsh Critic): The erank is a measure of effective sample size — classes with more samples *should* have larger erank values if the samples are redundant; if they are not redundant, erank grows sub-linearly. This is by design, not a bug. After normalization, tail classes with few but non-redundant samples get appropriately small effective counts. The critic's scenario would produce a frequency bias only if head-class erank grew proportionally to m_y (i.e., no redundancy detected), which is precisely the signal the method is designed to avoid.

## Novel Insights

None beyond the paper's own contributions. The core insight — that class-wise and overall LA should be co-designed rather than treated independently — is already stated clearly in the paper.

## Suggestions

1. Add an ablation comparing `−τ · p` (linear) vs. `−τ · log p` (log) within the same CoLA pipeline on at least two distributions and one dataset. This directly addresses the most significant evidential gap.
2. Add an epoch-wise plot of DDDE's L₂ estimation error (not just the final-8 average), with error bands, to demonstrate stability throughout training.
3. Report the size of D_v and the distribution of learned τ∗ values over seeds for a representative setting.
4. Discuss the edge case where a tail class has fewer confident pseudo-labeled samples than feature dimensions (m_y < d).

## Score and Decision

### Calibration summary

**Round 1 — Bracketing** (query: "long-tailed semi-supervised learning logit adjustment"):
- **Weak band** (score < 3.5): anchors at 3.00, 2.50, 3.00, 2.67 — clearly below this paper.
- **Middle band** (3.5–7.5): SCAD (4.50, Poster), DyTrim (4.00, Poster), BiAL (4.00, Reject), SLN (5.00, Reject). CoLA is meaningfully stronger than SCAD and DyTrim: it has two independently-motivated novel components, does not rely on external pre-trained models, provides a theoretical bound linking its components, and evaluates more distribution types. Initial bracket: **4.5–7.0**.
- **Strong band** (> 7.5): anchors at 8.00–8.50 on unrelated topics (RL, rotation estimation, text-to-3D). CoLA does not reach this tier.

**Round 2 — Narrowing** (queries: "logit adjustment co-design meta-learning" 4.5–6.0 and "effective sample size distribution estimation" 6.0–7.5):
- ALA (5.33, Poster, different topic — multimodal debiasing): a solid accepted paper with a clear but incremental contribution.
- GUIDE (6.50, Poster, LTR not SSL): stronger expert-diversity framework but not directly comparable.
- CoLA sits above the SCAD/DyTrim level (4.0–4.5) but below the GUIDE tier (~6.5). The missing ablation and limited tail-class analysis prevent it from reaching higher; the consistent SOTA and clean co-design framework keep it clearly above 4.5.

**Decision**: The round-2 narrowing places CoLA between the 4.5 anchor (SCAD) and the 6.5 anchor (GUIDE), closer to 5.5 given the modest gains and missing analyses. Final score: **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>