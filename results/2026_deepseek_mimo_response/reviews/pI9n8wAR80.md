Now let me write the final review output:

## Summary
This paper proposes CoLA (Co-Calibrated Logit Adjustment), a framework for Long-Tailed Semi-Supervised Learning (LTSSL) that co-designs the class-wise and overall components of Logit Adjustment. CoLA introduces DDDE (De-Duplicated Distribution Estimation), which uses effective rank of class representations to produce redundancy-aware class distribution estimates, and LMC (Logit Meta-Calibration), which meta-learns the optimal overall adjustment strength τ on a proxy validation set constructed to mirror the estimated distribution. The paper provides a generalization bound linking both components and demonstrates SOTA performance across 4 benchmarks with 6 distribution types.

## Strengths
- **DDDE using effective rank is novel and well-motivated**: Rather than naively counting pseudo-label frequencies, DDDE computes the effective rank (exponential entropy of normalized singular value spectrum) of each class's representation matrix (Eq. 3-4). Table 5 demonstrates DDDE achieves lower L₂ distance to the true distribution than MCA and NWGMA across all 10 tested scenarios, providing concrete evidence of superior estimation quality.

- **Empirical demonstration that optimal τ is dataset-dependent (Figure 1b)**: The paper shows the optimal overall adjustment strength does not monotonically increase with imbalance ratio — e.g., on CIFAR-10-LT, the optimal τ for γ_l=100 is greater than for γ_l=150. This directly motivates the need for adaptive rather than fixed τ selection.

- **Ablation validates bidirectional co-dependency (Table 4)**: The ablation shows (a) no single fixed τ consistently outperforms others across datasets (τ=2 best for CIFAR-10-LT, τ=1 better for CIFAR-100-LT), (b) LMC without DDDE (w/o D-L) is consistently suboptimal because poor distribution estimation misguides the learned τ, and (c) the full co-designed system achieves best results in all 10 settings. This validates the paper's central thesis that the two components must be co-designed.

- **Comprehensive experimental evaluation**: CoLA is tested on 4 benchmarks (CIFAR-10-LT, CIFAR-100-LT, STL-10-LT, SIN-127) with 6 distribution types and compared against 20+ methods across 6 categories. All use FixMatch backbone for fairness. STL-10-LT includes unknown distributions and OOD samples. CoLA achieves best or near-best across all settings, with particularly strong gains on CIFAR-100-LT (>1pp over runner-up in most cases).

- **Theoretical grounding (Proposition 1)**: The generalization bound decomposes target risk where the discrepancy term |R̂_{D_v,w} − R̂_{D_v}| directly measures proxy-target distribution match, providing principled support for why accurate DDDE improves LMC. Convexity analysis (Appendix F) guarantees convergence of τ optimization.

## Weaknesses

### Fatal
None.

### Major
- **Ambiguity between log and linear LA formulations at inference**: The paper motivates the problem using the standard logarithmic post-hoc LA (Eq. 1: z_y − τ · log P̂(y)), but the LMC meta-learning objective optimizes τ using a linear penalty: σ(z − τ · p) (Eq. on line 97, p = P̂(y)). The paper acknowledges this deviation (line 99) citing Mor & Carmon (2025) and justifies it for numerical stability. However, it never explicitly states which formulation is used at inference time when τ* generates pseudo-labels on unlabeled data. If the log form from Eq. 1 is used, τ* was optimized for a different objective. If the linear form is used, this should be stated explicitly. The intent seems to be the linear form at both meta-learning and inference, but this needs to be clarified. Resolution: either (a) explicitly state the linear formulation is used at inference, or (b) meta-learn τ for the log formulation directly.

- **Missing ablation variant: DDDE + fixed τ**: Table 4 includes (a) no DDDE + fixed τ ∈ {1,2,4}, (b) LMC without DDDE (w/o D-L), and (c) full model (w/ D-L), but omits DDDE + fixed τ. Without this variant, DDDE's individual contribution is confounded with the τ-selection mechanism. Table 5 shows DDDE's superior distribution estimation, but adding DDDE + fixed τ would cleanly isolate whether better distribution estimation alone improves pseudo-labels even without adaptive τ, directly validating or challenging the co-design thesis.

### Minor
- **SIN-127 results lack standard deviations (Table 3)**: The margins over the best baseline are small — 0.52% at 32×32 (24.18 vs 23.66) and 1.21% at 64×64 (37.49 vs 36.28). Without standard deviations, statistical significance is unclear.

- **Cold-start problem for erank on tail classes**: DDDE computes erank on high-confidence pseudo-labeled samples (confidence > ρ). During early training with heavy head-class bias, m_y for tail classes may be very small — potentially fewer than d (the representation dimension), making Z_y rank-deficient. The paper assumes Z_y is full-rank (line 77) but does not discuss mitigations for this cold-start issue. A brief discussion of safeguards (minimum sample thresholds, smoothing) would strengthen the paper.

- **Theoretical bound addresses classifier risk, not pseudo-label quality directly**: Proposition 1 bounds the expected risk of classifier h_τ, but τ is used in practice for pseudo-label generation, not for final classification. The connection is indirect: better pseudo-labels → better training → better classifier. The paper acknowledges this (line 132-133) but the theoretical-practical link is imprecise.

## Nice-to-Haves
- Brief summary of computational overhead in the main text (SVD per class per epoch for DDDE + inner optimization for LMC), rather than only referencing Appendix H.
- Empirical comparison of linear vs. log LA formulation in the meta-learning objective to validate the design choice.
- Discussion of cold-start safeguards for erank computation.

## Removed Points
These points are flagged to be removed, treat them with caution:
- "Appendix J is not available" — The appendix exists in the original submission; it was stripped by the parser. This is not an author error. The paper explicitly references per-setting results in Appendix J (line 182).
- Any claims about missing appendices, proofs, or supplementary material — these are parser artifacts, not author errors.
- "Missing related works" — Cannot verify external works not present in the paper.

## Novel Insights
The paper's core novel insight is that the class-wise and overall components of Logit Adjustment are bidirectionally dependent: the optimal overall adjustment strength τ varies non-intuitively with the estimated class distribution (Figure 1b), and accurate distribution estimation (DDDE) is a prerequisite for meaningful meta-learning of τ (LMC). This "co-calibration" philosophy — that adjusting one component without simultaneously adapting the other is suboptimal — is validated both theoretically (Proposition 1) and empirically (Table 4). The use of effective rank as a redundancy-aware proxy for effective sample size in representation space is a genuinely novel contribution to distribution estimation in imbalanced settings.

## Suggestions
- Explicitly state whether the linear or log LA formulation is used at inference time for pseudo-label generation.
- Add the DDDE + fixed τ ablation row to cleanly isolate individual component contributions.
- Add standard deviations to SIN-127 results in Table 3.
- Discuss cold-start behavior of erank when m_y is small, including any practical mitigations.

## Calibration Report

### Anchors Retrieved

**Round 1 (bracketing):**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| RwiUmrEHgR | 3.00 | 1 | Cost-sensitive loss for long-tail. Much weaker contribution and evaluation than CoLA. |
| 2aebB2mf0q | 3.00 | 1 | Semi-supervised infrared detection. Unrelated domain, weak. |
| E0UsEIRBQ8 | 3.00 | 1 | Semi-supervised underwater detection. Weak contribution. |
| rwdeKOdAwY | 3.00 | 1 | Multimodal retrieval. Unrelated domain. |
| zLHP6QDWYp | 3.80 | 1 | Open-world LTSSL. Very relevant topic but limited novelty, outdated baselines. Clearly weaker than CoLA. |
| OeKp3AdiVO | 6.25 | 1 | Classifier re-training for long-tailed. Similar scope but CoLA addresses harder LTSSL with more comprehensive evaluation. |
| II81zQUS1x | 5.67 | 1 | MLA theoretical justification. Narrow contribution, limited experiments. CoLA is clearly more comprehensive. |
| u1yvEwYfK9 | 5.67 | 1 | Label shift correction. Different focus, was rejected. |
| 25kAzqzTrz | 8.00 | 1 | Theory of FixMatch generalization. Stronger theoretical paper but different focus. CoLA is not at this level. |
| RvUVMjfp8i | 8.00 | 1 | SSL in open environments. Stronger evaluation framework paper. |
| zl0HLZOJC9 | 8.00 | 1 | Learning to defer. Unrelated. |
| uAFHCZRmXk | 8.00 | 1 | Modality gap in VLMs. Unrelated. |

**Round 2 (narrowing):**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| HvkXPQhQvv | 6.00 | 2 | Semi-supervised model evaluation. Different focus. |
| AEi2wyAMyb | 5.33 | 2 | Bi-level optimization for pseudo-labeling. Relevant but weaker contribution. |
| 85G2t3yklD | 6.67 | 2 | DiffMatch for semi-supervised segmentation with imbalance. Well-received, different domain but similar theme. CoLA is comparable. |
| 3GurO0kRue | 6.50 | 2 | Subpopulation imbalance. Different but related topic. |
| GySIAKEwtZ | 6.50 | 2 | FeatRecon for long-tailed. Comparable scope but CoLA addresses harder LTSSL with more baselines. |
| vM94dZiqx4 | 7.00 | 2 | Long-tailed adversarial training. Strong contribution but different focus. CoLA is slightly below. |
| LW55JrLYPg | 6.67 | 2 | Long-tailed object detection. Different task. |

### Score Positioning
Round 1 bracket: **5.5–7.0**. CoLA is clearly above the reject-level anchors (3.0–3.8) and the weaker accept at 5.67. Round 2 narrowed to **6.0–7.0**. CoLA is comparable to the 6.50 anchor (FeatRecon — similar theoretical-empirical structure, but CoLA addresses harder LTSSL with more comprehensive evaluation) and slightly below the 7.0 anchor (long-tailed adversarial training — a cleaner contribution without the log/linear ambiguity). CoLA's log/linear ambiguity and missing ablation prevent it from reaching 7.0+. The final score of **6.5** positions CoLA as a solid, well-evaluated contribution with clear novelty in the DDDE component and strong empirical validation, held back by the methodological ambiguity around the LA formulation used at inference and a missing ablation variant.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>