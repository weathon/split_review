Here is my final consolidated review.

---

## Summary

This paper introduces INFO-SEDD, a method for estimating mutual information (MI), KL divergences, and entropy for high-dimensional discrete data using score functions from discrete diffusion models (CTMCs). The core idea uses Dynkin's formula to connect KL divergence to score ratios, and an absorbing-state diffusion to extract marginal scores from a single joint model. The method is validated on synthetic benchmarks with known ground truth, text summarization (consistency + model selection), genomics (consistency + motif discovery), and Ising model entropy estimation, consistently outperforming baselines that rely on embedding discrete data into continuous spaces.

## Strengths

- **Theoretically grounded and original approach**: The derivation connecting KL divergence to score ratios via Dynkin's formula (Eq. 2→4→5) is mathematically coherent, and the use of absorbing-state diffusion to obtain marginal scores from a single joint model (Eq. 6) is both clever and practically important. A consistency bound (Eq. 7) decomposes error into estimation error and exponentially vanishing truncation bias.

- **Superior performance on high-dimensional, high-MI synthetic benchmarks**: Table 1 shows INFO-SEDD producing estimates closest to ground truth (e.g., 9.92±0.12 for true MI=10, D=10) with low variance, while competing methods (MINE, NWJ, SMILE, KL-DIME, HD-DIME, GAN-DIME, MINDE) degrade substantially as MI and dimensionality increase (e.g., INFO-SEDD 47.77 vs. next best 17.27 for MI=50, D=50).

- **Consistency on real-world data with strong practical validation**: In the text summarization consistency test (Figure 1), INFO-SEDD variants follow the theoretically expected linear trend (≈256–303 nats), while competitors saturate. The model selection experiment (Table 2) shows INFO-SEDD-C achieves Pearson correlation of 0.740 with human consistency judgments—the highest among all methods. In genomics, the method accurately localizes the TATA-box motif (Figure 5) with minimal engineering, and enables sliding-window MI profiles without separate training runs per window.

- **Versatility across domains with minimal domain-specific changes**: The same core method is demonstrated on synthetic data, text summarization, DNA sequence analysis, and Ising model entropy (Appendix D), all using standard pretrained discrete diffusion backbones (MDLM, CADUCEUS) without ad-hoc embedding procedures.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **"Empirical MI estimate" in Figure 1 is undefined.** The gray curve labeled "Empirical MI estimate" closely tracks INFO-SEDD and is used as a de facto reference for consistency, but the main text never states how it is computed (e.g., plug-in estimator, specific binning strategy, bias correction). While the paper provides entropy-rate-derived bounds (256–303 nats) for the expected slope, the empirical curve itself is unattributed. This undermines the strength of the consistency validation, as a reader cannot assess whether the agreement is meaningful or coincidental. This should be clarified either in the main text or the figure caption.

- **Derivation from Eq. (2) to Eq. (4) via Dynkin's formula is too compressed in the main text.** The paper states "combined with Equation (3), the KL divergence can be conveniently approximated as" and presents Eq. (4) without showing which function *f* is differentiated or how the backward operator yields the specific integrand. The full derivation is deferred to the appendix. While not a validity concern, this makes it difficult for readers to gauge which terms are exact and which are approximated without consulting the supplementary material. Adding one intermediate equation showing the application of Dynkin's formula to *f(a,t) = log(p_t(a)/q_t(a))* would substantially improve self-containedness.

- **Synthetic data generation process is described only at a high level in the main text.** The paper says "full details are in Appendix C.1" and describes the data as "two vectors X and Y sampled from their respective discrete distributions" with "known mutual information." The generative model, the relationship between D and MI, and whether the data respects the factorized assumptions of the diffusion are not explained in the main text. Given that the synthetic results (Table 1) are the strongest quantitative evidence for the method's accuracy, a brief description in the main body would help readers assess whether the benchmark is genuinely challenging or potentially tailored to the method's strengths.

### Trivial
- The constants *C₁, C₂* in the theoretical bound (Eq. 7) are introduced but never instantiated or discussed. An empirical check varying *T* to observe the truncation bias would strengthen the theoretical claims but is not required for acceptance.
- The paper does not discuss computational cost or training time relative to baselines, which would help practitioners assess practical trade-offs.

## Nice-to-Haves
- An ablation study varying the time horizon *T* to empirically verify the exponentially vanishing truncation bias predicted by Eq. (7).
- Sensitivity analysis for the choice of *T* and the noise schedule σ(t), providing practical guidelines for users.
- Brief discussion of scenarios where the method might be less effective (e.g., very small support sizes where absorbing-state dynamics are less efficient).

## Removed Points
These points from the input reviews were removed or demoted for the following reasons:

- *Criticism that synthetic data construction might favor INFO-SEDD*: The paper explicitly defers to Appendix C.1 for details, which is standard conference practice. The concern is speculative rather than a documented bias. This is already captured under the milder "high-level description only" point above.
- *Criticism about missing related work*: Per the hard rules, I cannot confirm whether related works exist or not, and the paper's citation coverage appears adequate.
- *Formatting/typo nitpicks*: Removed per hard rules as parser artifacts.
- *Strength Finder's generic strengths* (e.g., "the paper addresses an important problem"): Removed as superficial and not specific to the paper's contributions.
- *Criticism that the theoretical bound is not empirically validated*: Demoted to Nice-to-Have, as deriving and stating the bound is already a meaningful theoretical contribution.

## Novel Insights
The key insight that emerges from synthesizing the reviews is that INFO-SEDD's practical advantage is not merely accuracy but **structural efficiency**: by using absorbing-state diffusion, marginal scores can be extracted from a single joint model (Eq. 6), eliminating the need to train separate models for the joint and product-of-marginals distributions. This design choice turns what would be a computational bottleneck into a scalability feature, particularly for the sliding-window motif discovery task where alternative methods would require per-window retraining. The paper's downstream applications (model selection via MI correlation with human metrics, motif discovery without per-window training) concretely demonstrate that the method's value extends beyond benchmark numbers into practical scientific workflows.

## Suggestions
1. **Define the "Empirical MI estimate"** in Figure 1 — state how it is computed (e.g., plug-in estimator over token co-occurrence matrices, with any bias corrections applied). This single clarification would substantially strengthen the consistency validation.
2. **Add one intermediate equation** in Section 2.2 showing Dynkin's formula applied to *f(a,t) = log(p_t(a)/q_t(a))* so readers can trace the integrand in Eq. (4) without consulting the appendix.
3. **Include a 2–3 sentence description** of the synthetic data generative process in Section 4.1 to help readers evaluate the benchmark's difficulty and fairness.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Searched three bands:
- Weak (high_score<3.5): Papers about diffusion with avg scores ~3.0 — INFO-SEDD is clearly far above these.
- Middle (3.5<score<7.5): **MINDE** (6.50, the continuous counterpart), **f-DIME** (5.60, variational MI estimator), **InfoNet** (5.75, feed-forward MI estimator).
- Strong (low_score>7.5): Diffusion papers at 8.0 — INFO-SEDD is below these top-tier papers due to presentation gaps.

**Round 1 bracket:** 5.0–7.5.

**Round 2 (Narrowing):** Searched within (5, 8):
- **MINDE** (6.50) — Directly comparable: same approach but for continuous data. INFO-SEDD is stronger: tackles a harder problem (discrete), has more extensive real-world validation (human evaluation + genomics + Ising models), and the literature gap is more significant.
- **Convergence of Score-Based Discrete Diffusion Models** (7.00) — Theory-only discrete diffusion paper. INFO-SEDD has weaker theoretical depth but far stronger empirical validation and practical impact.
- **Steering Masked Discrete Diffusion Models** (6.25) — Strong empirical validation including wet-lab. INFO-SEDD has comparable breadth across domains.
- **Discrete Diffusion Samplers** (6.00) — Combinatorial optimization. Less directly comparable.

**Final calibration:** INFO-SEDD sits between MINDE (6.50) and the stronger 7.0+ papers. It is stronger than MINDE due to tackling discrete data (a harder and more underserved problem) and more extensive real-world applications. It is slightly below pure theory+wet-lab papers at 7.5+ due to presentation gaps (undefined empirical estimate, compressed derivation). Score: **7.0**.

### Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>