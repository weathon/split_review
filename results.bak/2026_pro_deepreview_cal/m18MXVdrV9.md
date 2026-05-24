Now I have a clear picture. Let me compose the final review.

## Summary

INFO-SEDD proposes a method for estimating mutual information and entropy on high-dimensional discrete data by extending the diffusion-based MI estimation framework (MINDE) to discrete state spaces via Continuous Time Markov Chains (CTMCs). The key insight is applying Dynkin's formula to relate the KL divergence between two discrete distributions to an integral over score function ratios of CTMC processes sharing the same generator. By using sparse absorbing transition matrices, a single score model trained on the joint distribution suffices for computing marginal scores, enabling scalable MI estimation. The method is evaluated on synthetic benchmarks, text summarization, and genomics tasks including motif discovery.

## Strengths

- **Genuinely novel extension of diffusion-based MI estimation to discrete data.** The paper adapts the MINDE framework (originally for continuous SDEs) to CTMCs over discrete state spaces. This directly addresses a recognized gap: existing neural MI estimators overwhelmingly target continuous distributions, forcing practitioners to use "embedding tricks" that break down in high dimensions. The connection via Dynkin's formula is a natural and elegant transfer of the continuous approach.

- **Strong empirical performance on synthetic benchmarks with ground truth.** Table 1 shows INFO-SEDD achieving near-exact MI estimates (e.g., 9.92 ± 0.12 for ground truth MI=10 at D=10; 20.02 ± 0.21 for MI=20, D=20) while all competing neural estimators (GAN-DIME, HD-DIME, SMILE, MINE, NWJ, MINDE) show large errors or collapse as MI and dimensionality grow. This is a decisive result.

- **Clever absorbing-state design enables a single model for joint and marginal scores.** By choosing an absorbing forward process (Equation 6), the method computes marginal scores from a model trained only on the joint distribution. This eliminates the need for separate training runs and is what makes the sliding-window motif discovery in Section 4.3 scalable — competing estimators would require retraining for each window position.

- **Compelling real-world applications demonstrating practical utility.** The TATA-BOX motif discovery result (Figure 5) is particularly striking: the MI profile peaks precisely at the known TATA-BOX location (-39 to -26 relative to TSS), and the method accomplishes this with a single trained model. The text summarization model selection analysis (Table 2) shows that INFO-SEDD-C MI estimates correlate well with human consistency judgments (Pearson r=0.740, Kendall τ=0.505), outperforming variational competitors.

- **Seamless integration with pretrained discrete diffusion backbones.** The method is demonstrated using off-the-shelf MDLM-SMALL (text) and CADUCEUS (genomics) models with minimal architectural changes, lowering the barrier to adoption.

## Weaknesses

### Fatal

None.

### Major

- **The KL divergence derivation in Section 2.2 lacks rigor and contains unjustified steps.** Equation (2) begins with `KL[p̂₀ ∥ q̂₀] = E[log(p̂₀/q̂₀)(X̂_T)]` — this replaces the initial state X̂₀ with the terminal state X̂_T inside the density ratio without any justification. It is not obvious why the KL divergence between initial distributions should equal an expectation of the log-ratio of initial densities evaluated at a terminal state of a stochastic process. The subsequent transformation to `E[log(p̂_T/q̂_T)(X̂_T)]` is also stated without derivation. The application of Dynkin's formula is then described only verbally; the intermediate steps connecting Dynkin's formula to the integral expression in Equation (4) are absent. Most problematically, the paper states "We omit the term E[log(p̂₀/q̂₀)(X̂_0)], as both p̂₀ and q̂₀ converge to π" — this statement is confusing as written: E[log(p̂₀/q̂₀)(X̂_0)] *is* the KL divergence being estimated, not a residual to be discarded, and the distributions p̂₀, q̂₀ themselves do not "converge"; it is the evolved distributions p̂_T, q̂_T that converge to π. While the underlying idea (relating KL to an integral over the forward process via Dynkin's formula, exploiting the fact that KL(p̂_T ∥ q̂_T) → 0 as T → ∞) is conceptually sound — and the empirical results strongly suggest the estimator works — the exposition does not constitute a trustworthy derivation. This matters because the paper's core intellectual contribution rests on this derivation being correct. **The authors should provide a complete, step-by-step derivation in the rebuttal or revision, explicitly handling all boundary terms and justifying each equality.**

### Minor

- **The text consistency test relies on an unverified linearity assumption.** The paper assumes MI grows linearly with scrambling probability ρ (i.e., I(ρ) ≈ ρ · I₀), justified by reference entropy-rate estimates from the literature (Takahira et al., 2016; Cover and King, 1978). While this is a reasonable order-of-magnitude approximation, the exact relationship for a mixture distribution ρ·p_{XY} + (1−ρ)·p_X p_Y is not exactly linear in MI. The test remains informative but would be stronger with a semi-synthetic validation where ground-truth MI is known.

- **Monte Carlo integration procedure is underspecified.** Equation (5) describes an integral over continuous time estimated by sampling t uniformly in [0, T] and simulating the forward process. The paper does not analyze the bias or variance introduced by this finite-sample approximation, does not report the number of integration steps used, and provides no ablation over the truncation horizon T. These practical details affect reproducibility and the reliability of reported estimates.

- **The theoretical bound (Equation 7) provides limited insight.** The bound decomposes error into a score-approximation term and an exponentially decaying truncation bias, but the constants C₁, C₂ are not connected to any data or model properties. The bound mainly formalizes the intuition that better score models and longer horizons reduce error — useful but not deep.

### Trivial

- The paper states that details of how ground-truth MI is constructed for synthetic experiments are in Appendix C.1, and algorithmic pseudocode for the estimator variants is in Appendix B. These are standard appendix material; no issue.

## Nice-to-Haves

- A comparison of computational cost (training time, inference time, memory) relative to competitors would help practitioners assess the practical trade-offs of using INFO-SEDD over simpler embedding-based estimators in lower-dimensional settings.
- The consistency tests could be strengthened by constructing a semi-synthetic setup (e.g., using a tractable generative model of text with known MI) rather than relying on literature entropy-rate estimates and the linearity approximation.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic claim: "The derivation is structural/fatal and invalidates the paper's entire contribution."** → Removed as overstated. While the derivation is indeed sketchy (retained as Major), the underlying idea is conceptually sound (Dynkin's formula applied to log-density ratios of CTMCs) and follows a clear lineage from MINDE's Girsanov-based approach. The empirical results on synthetic data with known ground truth provide independent evidence that the estimator works correctly. This is a presentation/rigor problem, not a mathematical impossibility.

- **Harsh critic claim: "Details of synthetic ground-truth construction and genomics algorithms are in missing appendix."** → Removed per hard rules. The parser strips appendices; they exist in the original submission.

- **Harsh critic claim: "The motif discovery procedure is not described with sufficient detail."** → Removed. The paper describes the sliding window approach (Section 4.3, "we use a sliding window of length L and mask the DNA sequence outside this window"), which is sufficient for the main text. Algorithmic details belong in the appendix.

- **Strength Finder: "This paper addressed an important problem" and similar generic framing.** → Removed as superficial. These are statements about problem importance, not concrete strengths of the paper's execution.

- **Strength Finder: "Robustness to varying support size" without qualification.** → Kept but noted as appendix material.

## Novel Insights

The most interesting insight from synthesizing these reviews is that INFO-SEDD's absorbing-state trick (Equation 6) — which allows a single joint-distribution score model to yield marginal scores — solves a practical scaling problem that has no analogue in the continuous (MINDE) setting. In continuous diffusion, marginalization requires either separate models or architectural workarounds. The discrete absorbing process makes this fall out naturally from the mathematics, which is an elegant property specific to the CTMC formulation and a genuine conceptual contribution beyond simply "porting MINDE to discrete data."

## Suggestions

- Rewrite Section 2.2 with a complete, self-contained derivation. Start from `KL(p̂₀ ∥ q̂₀) = E_{X∼p̂₀}[log(p̂₀/q̂₀)(X)]`, use the forward CTMC evolution, apply Dynkin's formula to `f(x,t) = log(p̂_t/q̂_t)(x)`, explicitly handle the boundary terms (showing that the terminal boundary vanishes as T → ∞), and derive Equation (4) step by step.
- Report the number of Monte Carlo time samples and the horizon T used in experiments, and include a brief ablation over these parameters.
- For the text consistency test, either derive the exact MI–ρ relationship or acknowledge it as approximate and discuss the error.

## Score and Decision

**Round 1 bracket:** Based on the initial retrieval, the paper sits between INFO-Net (5.75, rejected) and the discrete diffusion convergence paper (7.00, accepted). The closest comparison is MINDE (6.50, accepted), which INFO-SEDD directly extends. Initial bracket: **5.5–7.0**.

**Round 2 narrowing:** Retrieved anchors at 5.60 (f-DIME, rejected), 5.75 (InfoNet, rejected), 6.00 (Scalable Discrete Diffusion Samplers, accepted), 6.25 (DDPP, accepted), 6.50 (MINDE, accepted; Discrete Guidance, accepted), 6.60 (SEDD, rejected), 7.00 (Convergence paper, accepted).

INFO-SEDD is stronger than InfoNet (5.75) and comparable to DDPP (6.25) in terms of empirical breadth and practical impact. It is slightly below MINDE (6.50) — MINDE's reviewers praised its "solid, detailed derivation," whereas INFO-SEDD's derivation has the gap identified above. However, INFO-SEDD's empirical results are arguably broader and more applied than MINDE's benchmark-focused evaluation. The derivation weakness pulls the score down from what would otherwise be a clear 6.5-level paper.

**Final comparison:** Better than DDPP (6.25) in terms of originality and empirical breadth; slightly below MINDE (6.50) due to the derivation gap. Comparable to the Discrete Guidance paper (6.50) which had similar strengths (practical CTMC application, diverse experiments) and weaknesses (some reviewers found it incremental, presentation issues). I assign **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>