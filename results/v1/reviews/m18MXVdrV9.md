Now I have all the information needed to write a comprehensive, calibrated review. Let me assemble it.

## Summary

This paper introduces INFO-SEDD, a method for estimating KL divergences, mutual information (MI), and entropy on high-dimensional discrete data by leveraging score functions from Continuous Time Markov Chains (CTMCs) used in discrete diffusion models. The key idea is to express MI as a KL divergence and approximate it via an integral over the diffusion path of score-function ratios, computed from a single model trained with an absorbing-state diffusion process. The method is evaluated on synthetic benchmarks, text summarization (consistency tests and model selection), and genomics (consistency tests and TATA-box motif discovery), where it generally outperforms embedding-based neural MI estimators.

## Strengths

1. **Strong synthetic results in the high-MI regime.** Table 1 shows INFO-SEDD recovering true MI values of 10-50 with errors of 0.2-2.2 nats and low standard deviation across 10 seeds, while every competing estimator (GAN-DIME, HD-DIME, KL-DIME, MINDE, MINE, NWJ, SMILE) exhibits substantially larger bias, variance, or both. This is the paper's cleanest evidence that the method works.

2. **Effective use of absorbing-state diffusion to avoid training separate models.** The insight that an absorbing-state transition matrix allows a single jointly-trained model to provide both joint and marginal scores (Equation 6, Appendix A.3) is a genuine practical contribution. This eliminates the need for separate score networks for the joint and product-of-marginals distributions, which would double the compute.

3. **Compatibility with pretrained discrete diffusion models in real applications.** The text experiments use MDLM-SMALL and the genomics experiments use CADUCEUS with minimal architectural changes, demonstrating that INFO-SEDD can be dropped into existing discrete diffusion pipelines. This is a meaningful practical advantage over methods that require learned embeddings.

4. **Concrete downstream application showing biological validity.** The TATA-box motif discovery experiment (Figure 5) uses INFO-SEDD-J with sliding-window masking to produce an MI profile that peaks precisely in the known TATA-box region (-39 to -26 relative to TSS) in *Arabidopsis thaliana* promoters. This demonstrates a task where INFO-SEDD's ability to estimate MI between subsets of variables from a single trained model is uniquely convenient.

## Weaknesses

### Major

1. **The theoretical derivation in Section 2.2 is presented in a confusing and apparently incorrect manner.** Equation (2) states `KL[p0∥q0] = E[log(p0/q0)(X_T)]` without justification — the expectation is over X_T ~ p_T, not X_0 ~ p_0, so this equality does not hold as written. The text then states "We omit the term E[log(p0/q0)(X_0)], as both p0 and q0 converge to π (Lou et al., 2024)" — this reverses the direction of convergence (it is p_T, q_T that converge to π, not p0, q0). The relationship between the Dynkin formula application and the desired KL is therefore unclear from the main text. While a correct derivation likely exists (analogous to Girsanov-based formulas in the continuous diffusion literature, e.g., Song et al. 2021, Franzese et al. 2023), the paper does not provide a self-contained derivation or clearly cite one, making it impossible for a reader to verify the estimator's correctness from the paper as written. This is a serious exposition problem because the entire method hinges on this derivation.

2. **The text consistency test reveals a substantial positive bias at ρ=0 that is not adequately addressed.** When ρ=0 (summaries randomly paired with texts), true MI should be zero, yet INFO-SEDD-J reports ~100 nats (Figure 1, log scale). INFO-SEDD-C is somewhat lower but still far from zero. The paper mentions this only in passing ("INFO-SEDD-C obtains MI estimates closer to zero than the joint variant") without quantifying the bias, explaining its origin, or discussing whether it reflects a fundamental limitation. Competing methods like KL-DIME report near-zero values at ρ=0. The reference lines (256ρ, 303ρ) pass through zero, so the claim of "closely matching the empirical derivation" is misleading at low ρ. This bias directly concerns the method's claimed consistency.

3. **No synthetic experiment with known ground truth in the low-MI or zero-MI regime.** The synthetic benchmarks in Table 1 all have MI ≥ 10. While the genomics consistency test (Figure 4) operates at low MI (~0-0.6 nats), the reference used there is itself an approximation (classifier-based), and the paper does not include a controlled synthetic experiment with known MI near zero where the ground truth is exact. Without this, it is unclear whether the ρ=0 bias in the text experiment reflects a general limitation of the method or a text-domain-specific artifact.

### Minor

4. **Classical discrete MI estimators (plug-in, shrinkage, James-Stein) are mentioned in the introduction but never included in experiments.** The paper motivates the need for a new method by noting that classical discrete estimators degrade with dimensionality, but never demonstrates this failure on the synthetic data. Including even one classical estimator (e.g., the plug-in estimator discretized at the token level) would strengthen the narrative that existing discrete methods fail and a new approach is needed.

5. **Correlation values in Table 2 are reported without error bars, confidence intervals, or p-values.** With only 15 data points (models), the reported Pearson correlations (e.g., 0.740 for INFO-SEDD-C vs. consistency) have substantial uncertainty. The paper should report at least a bootstrap confidence interval or p-value to allow the reader to assess the reliability of these comparisons.

6. **No computational cost comparison.** The paper claims scalability and efficiency but does not report training time, GPU hours, or inference cost for INFO-SEDD vs. any competitor. Since training a discrete diffusion model (MDLM-SMALL, CADUCEUS) requires non-trivial compute, the practical trade-off between accuracy and cost is unclear to a practitioner.

### Trivial

7. The paper says "We omit the term E[log(p0/q0)(X_0)], as both p0 and q0 converge to π" — this statement is factually wrong about which distributions converge. It should read "as both p_T and q_T converge to π."

## Nice-to-Haves

- A synthetic experiment with true MI = 0 (independent X and Y) and MI = 0.5-2 (weak dependence) would directly address the low-MI concern and complement the strong high-MI results in Table 1.
- Adding a standard plug-in MI estimator (using the same tokenization as INFO-SEDD, before any embedding) as a baseline in Table 1 would demonstrate the failure mode of classical discrete estimators and strengthen the motivation.

## Removed Points

The following points from the reviewer inputs were removed under the filtering guidelines:

- *Criticism about the backward operator definition.* The definition used in the paper is a correct statement of the generator acting on a function in the context of Dynkin's formula for CTMCs. The notation is non-standard but internally consistent.
- *Claim that "the paper does not discuss the bias at all."* The paper does note that INFO-SEDD-C is closer to zero than INFO-SEDD-J at ρ=0 (line 144). The concern is that this discussion is insufficient, not absent.
- *Formatting and style nitpicks.*
- *Reproducibility concerns about undisclosed hyperparameters.* The paper provides extensive appendices with experimental details (though the appendix text was stripped during parsing).
- *Missing related works.* The paper cannot be penalized for not citing papers with which the reviewer has familiarity but whose existence cannot be verified.
- *Concerns about the MINDE baseline.* The paper includes MINDE as a competitor; the reviewer's criticism that MINDE is not included is incorrect.
- *The claim that INFO-SEDD "does not work" at low MI.* The genomics experiment (Figure 4) actually shows good performance at low MI (0-0.6 nats) for INFO-SEDD-C, so the claim of failure is unsubstantiated.
- *Overstatement about uniqueness in conclusion.* Generic overclaiming in a conclusion section is a common weakness of many papers and not specific enough to elevate.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Rewrite Section 2.2.** Provide a clean, step-by-step derivation that clearly states the starting point (the chain rule of KL divergences through the forward process), references a known Girsanov-type formula for CTMCs or provides the Dynkin argument correctly, and makes explicit which boundary terms are dropped and why. The current text confuses readers and undermines confidence in the method.

2. **Quantify and explain the ρ=0 bias.** Report the actual INFO-SEDD estimates at ρ=0 in the text, discuss why INFO-SEDD-J and INFO-SEDD-C differ, and provide experimental analysis (e.g., does the bias decrease with longer T? better convergence of the score model?).

3. **Add a synthetic zero-MI condition.** Extend the synthetic benchmark to include MI = 0 (independent marginals) and a small MI (e.g., 1-2 nats) to demonstrate that the method can distinguish independence from weak dependence, using known ground truth.

4. **Add at least one classical discrete MI baseline to the synthetic experiments.** A simple plug-in estimator (with appropriate bias correction) would visually demonstrate the dimensionality problem mentioned in the introduction.

5. **Report confidence intervals for the correlations in Table 2** and note the small sample size (n=15).

## Calibration Anchors

The following anchors were retrieved in the calibration search. All are from the same human-review corpus (n=13,379).

| Anchor | Avg Score | Query Bucket | Comparison to Paper Under Review |
|--------|-----------|-------------|----------------------------------|
| MINDE (0kWd8SJq8d) | 6.50 | Topic-mid | Continuous diffusion MI estimator; cleaner theoretical derivation (Girsanov); accepted; paper under review is weaker in theoretical exposition but addresses discrete data |
| Discrete Diffusion Convergence (pq1WUegkza) | 7.00 | Topic-mid | Theoretical analysis of discrete diffusion convergence; accepted; stronger theory than paper under review |
| f-DIME (KC2MViQASx) | 5.60 | Topic-mid | f-divergence MI estimator with derangements; rejected despite solid theory; weaker empirical evaluation than paper under review |
| InfoNet (PyHRUMxKbT) | 5.75 | Topic-mid | Feed-forward MI estimator; rejected; comparable empirical scope |
| NF-DoE (vgQmK5HHfz) | 4.83 | Weakness (MI estimation) | Normalizing flow MI estimator; rejected; derivation concerns similar to paper under review |
| FKEE (5sPgOyyjG5) | 3.00 | Topic-low | Diffusion-based expectation estimator; rejected; weaker empirical validation |
| SymmetricDiffusers (EO8xpnW7aX) | 8.00 | Topic-high | Discrete diffusion for permutations; accepted; significantly stronger theoretical and empirical contribution |

**What did the low-band anchors fail at?** The low-band topic anchors (FKEE, DFITE, DynamicsDiffusion, all at 3.00) shared common failure modes: weak or missing experimental validation, unclear connection between claimed contribution and empirical results, and incomplete theoretical justification. The paper under review does not share the weakest of these failure modes — its synthetic experiments are solid and its real-world applications are meaningful. However, it does share the low-band anchors' problem of a derivation that is presented in a way that prevents verification of the central claim (the FKEE paper had a similar issue with its Feynman-Kac derivation). This shared failure mode prevents the paper from reaching the 6+ range where MINDE and the discrete diffusion theory papers sit. The paper is clearly stronger than the 3.0-level anchors (which lacked meaningful experiments entirely) but weaker than the 6.5-level MINDE paper, which had a cleaner theoretical justification and more thorough experimental protocol.

**Score determination:** Positioned relative to the anchors: below MINDE (6.50) due to weaker theoretical presentation and unaddressed ρ=0 bias; above NF-DoE (4.83) due to stronger empirical validation and real-world applications; comparable to f-DIME (5.60) in terms of overall quality but with different strength/weakness profiles. The two Major weaknesses (derivation clarity and ρ=0 bias) are substantive enough to prevent acceptance but not so severe as to place the paper in the 3-4 range.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>