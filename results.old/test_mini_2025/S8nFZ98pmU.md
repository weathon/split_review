Now I'll write the final consolidated review.

---

## Summary

This paper proposes a meta-learning framework for dynamical systems that uses contrastive learning to infer system-specific embeddings from unlabeled trajectory observations, then uses those embeddings for forecasting. Key contributions include an Element-wise Square Ratio Loss (ESRL) with covariance regularization to avoid dimensional collapse, a local linear least-square feature extractor for vector-based systems, and a Spatially Adaptive Linear Modulation (SALEM) module for conditioning PDE forecasters on learned embeddings. The framework is evaluated on three vector-based ODE systems (spring-mass, 2D/4D Lotka-Volterra) and two grid-based PDE systems (incompressible flow, Gray-Scott reaction-diffusion).

## Strengths

1. **Unsupervised system embedding without labeled coefficients**: The paper demonstrates that contrastive learning can extract meaningful system embeddings from raw trajectory observations, without access to true physical coefficients or fine-tuning on new systems. This is a genuinely different setting from prior meta-learning work (LEADS, CAMEL, DyAd) that requires labeled coefficients or few-shot adaptation. The paper explicitly discusses this distinction in Section 6.2.

2. **ESRL with covariance regularization is well-motivated and ablation-supported**: The proposed loss in Equation (1) directly addresses dimensional collapse by operating element-wise rather than on vector distances. The covariance regularizer (Equation 3) further prevents correlated dimensions. Table 4 shows that removing the covariance regularizer (line 3) degrades performance across all three vector-based systems, and replacing ESRL with Info-NCE or Triplet loss (lines 5-6) leads to substantially larger errors (e.g., Info-NCE on LV(4D): 22.4e-2 vs ESRL: 8.31e-2). This provides clear evidence that the loss design is critical.

3. **SALEM outperforms conditioning baselines on grid-based systems**: The proposed SALEM module (Section 4.4) combines learned embeddings with spatial coordinates to modulate ResNet feature maps. Across all six grid-based settings in Tables 2-3, ResNet+SALEM achieves the lowest or tied-lowest MSE. It also provides training stability where competitors fail — FiLM produces NaN in the buoyancy & supply rate experiment and DyAN fails in the Gray-Scott kill rate and feed & kill rate experiments.

4. **Comprehensive evaluation across diverse dynamical systems**: The paper tests on three vector-based systems and two PDE systems with multiple coefficient variations, providing breadth that supports the framework's generality.

## Weaknesses

### Major

1. **The "standard training" baseline does not isolate the benefit of contrastive learning.** For vector-based systems (Table 1), the baseline is an MLP trained with only the system state *x* as input — it has no access to any system-specific information at all. The proposed method, in contrast, uses an encoder that processes a trajectory segment to produce a system embedding, which is then concatenated with *x* as input to the forecaster. The comparison conflates two effects: having any system-specific information (regardless of how it is obtained) versus the specific benefit of contrastive learning. A fairer baseline would use the same encoder+forecaster architecture but train the encoder with a different objective (e.g., a simple reconstruction/autoencoding loss, or a supervised objective if coefficients were available). Without such a control, the results in Table 1 demonstrate that "having a system embedding helps," which is unsurprising, but do not cleanly demonstrate that *contrastive learning* is the crucial ingredient.

2. **Statistical evidence for grid-based improvements is weak.** In Tables 2-3, several comparisons between SALEM and DyAN/FiLM show heavily overlapping standard deviations. For example, incompressible fluid (buoyancy): DyAN 9.51e-2 ± 2.21e-2 vs SALEM 9.06e-2 ± 2.77e-2; Gray-Scott (feed & kill rate): FiLM 4.56e-3 ± 1.82e-3 vs SALEM 3.81e-3 ± 2.22e-3. No statistical significance tests are reported. While SALEM consistently has the lowest point estimate, the overlapping intervals mean the claim of "substantial enhancement" is not statistically supported for these individual comparisons. The main evidence for SALEM's advantage instead rests on (a) training stability (fewer NaN failures) and (b) consistent rank ordering, which is meaningful but weaker than what is claimed.

### Minor

1. **"Explicit physical significance" is an overstatement.** The abstract claims the embeddings "carry explicit physical significance." The evidence in Figure 3 shows that for the linear spring-mass system, the learned embedding is a rotated/scaled version of the true coefficients (a linear transformation — any sufficiently flexible encoder could achieve this). For the nonlinear Lotka-Volterra system, the paper itself concedes the embedding only "loosely correlates" and has a "complex, non-linear relationship." No analysis establishes what individual embedding dimensions encode in physical terms. The claim should be toned down to reflect what is actually shown: the learned embedding correlates with underlying parameters, with the strength of correlation depending on system linearity.

2. **Ablation comparison of loss functions is not fully controlled.** Table 4 compares ESRL+reg (with covariance regularizer) against Info-NCE and Triplet *without* the covariance regularizer. The covariance regularizer is known to benefit contrastive learning generally (Bardes et al., 2021). This means the comparison confounds the effect of the ESRL loss function with the effect of the regularizer — Info-NCE+reg and Triplet+reg would be needed to attribute the improvement specifically to ESRL. The paper's claim that "conventional contrastive loss functions... result in a significant increase in prediction error" (Section 6.1) is technically true of the table as shown, but the conflated comparison weakens the strength of the conclusion.

### Trivial

- The normalization variable *M* in Equation (1) is described only as "the number of anchor points for normalization purpose" without a precise definition of how it is computed from the summation indices. Clarifying this would improve reproducibility.
- In Table 3, DyAN produces NaN in the "kill rate" column and N/A in "feed & kill rate" — the footnote explains these, but a brief note on whether this is systematic or due to hyperparameter choices would help interpretation.

## Nice-to-Haves

- The paper correctly scopes out comparison to LEADS/CAMEL due to different problem settings (Section 6.2). However, it would be interesting to see whether the learned embeddings can be plugged into those frameworks' forecasters to improve performance even when coefficients are available — the paper notes this compatibility but does not test it.
- A diagnosis of why SALEM avoids the NaN training failures that affect DyAN and FiLM would strengthen the practical relevance of the contribution.

## Removed Points

The following points from the input reviews are removed or downgraded with justification:

- **"Zero-shot" terminology complaint** — Removed. The paper clarifies that "zero-shot" means "does not require adaptation to new systems or explicit labelling of system-specific coefficients" (Section 1, line 29). This is a standard usage in meta-learning for methods that require no gradient-based fine-tuning. The method does use a short observed trajectory as context, which is analogous to a support set in few-shot learning, but the paper's terminology is defensible and not misleading.
- **Missing comparison to LEADS/CAMEL** — Removed. The paper explicitly explains why this comparison is not applicable (different problem settings requiring labeled coefficients or fine-tuning). This is appropriate scope scoping.
- **Missing model architecture details / data generation details** — Removed. These are standard appendix items, the appendix is stripped by the parser, and the instruction prohibits penalizing missing appendix content.
- **Missing related works** — Removed. I cannot verify their existence.
- **"M" not precisely defined in Eq. 1** — Demoted to Trivial (not a structural issue).
- **Barlow Twins citation** — Removed. The paper cites Bardes et al. (2021) which is the appropriate reference for the covariance regularizer.
- **Local feature extractor hurts LV(4D)** — Removed as a weakness. The paper acknowledges this, and the extractor helps on 2/3 systems; the difference on LV(4D) (7.73e-2 vs 8.31e-2) is within overlapping error bars. A component does not need to help on every single test case to be a reasonable default.
- **Hyperparameter sensitivity beyond λ** — Removed (appendix content).
- **Generic strengths about "important problem"** — Removed from strengths list; kept only evidence-grounded strengths.
- **"NaN needs explanation"** — Demoted from standalone point to a brief note in Trivial, since the paper already has a footnote explaining NaN/N/A.

## Novel Insights

The most interesting observation that emerges from the reviews is a methodological one: the paper's contrastive objective (ESRL) essentially replaces the classification-style softmax of Info-NCE with a per-dimension variance ratio, then adds a decorrelation regularizer. This combination is well-suited to dynamical systems where the embedding space is continuous (system coefficients vary on continua) rather than categorical. The ablation in Table 4 provides reasonably strong evidence that this design choice matters for this problem domain, even if the control is not perfect. The reviewer disagreement — where one sees "insufficient evaluation" and the other sees "clearly supported design choices" — highlights a tension between what the paper claims versus what it actually isolates experimentally.

## Suggestions

- **Fix the core baseline comparison.** Add a controlled baseline for vector-based systems: use the same encoder+forecaster architecture but train the encoder without contrastive learning (e.g., random initialization, or a simple reconstruction loss). This would isolate the benefit of the contrastive objective specifically.
- **Run significance tests or add more trials** for the grid-based experiments to determine whether SALEM's improvements over DyAN/FiLM are statistically significant.
- **Tone down the "explicit physical significance" claim** to something like "embeddings that correlate with underlying physical parameters" — the evidence supports correlation, not explicit encoding.
- **Add controlled ablations** testing Info-NCE+reg and Triplet+reg to cleanly separate the effect of the ESRL loss from the covariance regularizer.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing:**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Representation learning for financial time series forecasting | 1.80 | R1 | Far weaker, has fatal flaws in methodology |
| Contrastive Implicit Representation Learning | 2.33 | R1 | Far weaker, withdrawn paper |
| Ensemble Systems Representation for Function Learning | 3.00 | R1 | Weaker, unfocused contribution |
| From Appearance to Motion | 3.00 | R1 | Weaker, limited scope |
| **Discovering Physics Laws via Invariant Function Learning** | **5.00** | **R1** | **Comparable — similar dynamical systems domain, similar issues with evaluation strength and overclaiming** |
| Phase Transitions in Contrastive Learning | 4.33 | R1 | Weaker, mostly theoretical study with limited practical contribution |
| ConML: Universal Meta-Learning | 4.00 | R1 | Weaker, novelty concerns, limited evaluation |
| **Generalizing Dynamics Modeling (PDEDER)** | **5.25** | **R1** | **Comparable — similar domain, stronger data breadth but weaker technical novelty; both rejected** |
| Space and time continuous physics simulation | 7.60 | R1 | Much stronger, accepted spotlight with rigorous evaluation |
| ClimODE | 8.00 | R1 | Much stronger, accepted oral |

**Round 2 — Narrowing:**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| **Learning invariant representations of dynamical systems** | **6.00** | **R2** | **Stronger — accepted poster with theoretical grounding and more careful evaluation; this paper is below this bar** |
| Parametric Augmentation for Time Series Contrastive Learning | 6.60 | R2 | Stronger — accepted poster with solid empirical methodology |
| Stabilizing Contrastive RL | 7.25 | R2 | Much stronger, accepted spotlight |
| Unsupervised Zero-Shot RL via DVFB | 6.67 | R2 | Much stronger, accepted poster |

**Round 1 bracket**: I initially placed the paper between 4.0 and 6.0 based on comparison to the weak (<3.5) and middle (3.5-7.5) anchors.

**Round 2 narrowing**: The paper is clearly below "Learning invariant representations of dynamical systems" (6.00, Accept) — that paper has stronger theoretical grounding, cleaner evaluation, and more careful framing. It is comparable to "Discovering Physics Laws via Invariant Function Learning" (5.00, Reject) and "Generalizing Dynamics Modeling PDEDER" (5.25, Reject) — all have novel ideas in the dynamical systems space but evaluation weaknesses prevent acceptance. The paper under review has slightly better technical novelty than these comparators but shares the same class of evaluation issues (weak baselines, overlapping error bars, overclaiming).

**Final score**: The paper's core ideas (ESRL, SALEM, unsupervised system embedding for dynamics) are solid and address a worthwhile problem. However, the evaluation has two significant weaknesses: the main vector-based comparison does not isolate the effect of contrastive learning, and the grid-based comparisons lack statistical significance. Combined with overclaiming on interpretability, the paper does not meet the acceptance bar in its current form. A revision addressing the baseline comparison and toning down claims could make it a solid 6-level submission.

<score>5.0</score>
<decision>Reject</decision>
MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>