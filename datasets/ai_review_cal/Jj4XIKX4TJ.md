- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 5, 6, 8, 6
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes SO(3)-Averaged Flow, a new flow-matching training objective that integrates over all rotations of molecular conformers during training (avoiding the need for explicit rotational alignment), combined with reflow and distillation to straighten flow trajectories for few-step generation. The method is evaluated on GEOM-QM9 and GEOM-Drugs, using a compact 4.7M-parameter NequIP-based architecture.

## Strengths

1. **Faster convergence of Averaged Flow training (strongest empirical result).** Figure 2 shows that on a 300-molecule GEOM-Drugs subset, the model trained with Averaged Flow consistently achieves higher COV-R and lower AMR-R across training epochs than both conditional OT and Kabsch-aligned flow. After 68 epochs, Averaged Flow surpasses the other objectives trained for 100 epochs on several metrics. This directly supports the core claim that Averaged Flow accelerates training.

2. **Parameter efficiency with competitive performance.** The model uses only 4.7M parameters, yet on GEOM-Drugs it outperforms MCF-S (~3× more parameters) on precision metrics (COV-P 55.3% vs. 53.4%, AMR-P 0.830 Å vs. 0.844 Å). On QM9, the paper reports that AvgFlow outperforms all baselines on COV-R and nearly matches the AMR-R of ET-Flow-SS. This demonstrates that the approach can compete with much larger transformer-based models.

3. **Few-step generation enabled by reflow/distillation.** On QM9, the paper states that AvgFlow$_{\text{Reflow}}$ (2 ODE steps) and AvgFlow$_{\text{Distill}}$ (1 step) achieve higher COV-R than other models, demonstrating that reflow+distillation preserves generation quality at very few sampling steps. On Drugs, AvgFlow$_{\text{Reflow}}$ outperforms all cheminformatics tools and GeoMol on all metrics.

4. **Honest and informative ablation of step-count necessity.** Figure 3 systematically compares AvgFlow and AvgFlow$_{\text{Reflow}}$ across 1–100 ODE steps, showing that without reflow, performance collapses below 5 steps (0% coverage at 1 step), while reflow maintains quality down to 2 steps. The paper openly acknowledges that AvgFlow (without reflow) is better when $N_{\text{step}} \ge 10$. This analysis provides clear, actionable guidance on when reflow is beneficial.

5. **Substantial wall-clock speed advantage.** Table 3 reports that AvgFlow$_{\text{Reflow}}$ generates each conformer on GEOM-Drugs in 2.68 μs—21–50× faster than MCF variants and 48× faster than torsional diffusion—while achieving competitive or better precision metrics against those methods.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Abstract overstates "match performance" without sufficient nuance.** The abstract claims the model "can match the performance of strong transformer baselines." While this holds on QM9 (where reflow models achieve higher COV-R than baselines), on Drugs the reflow model has a clear recall gap (COV-R 53.48 vs. MCF-L 57.26) and higher AMR-R (1.226 vs. 1.180), as honestly reported in Table 2. The paper's own text notes "the model's performance drops after reflow especially for the precision metrics." The central claim should be qualified to reflect that reflow trades off some recall/precision quality on larger molecules for dramatic speed gains, and that the strongest quality results come from the multi-step AvgFlow model (~19 steps). This is a framing issue, not a methodological flaw — the paper reports the numbers faithfully.

2. **Sampling time comparison lacks sufficient methodological detail for fair assessment.** The paper acknowledges that "the major speed-up... is due to the JAX implementation and less number of parameters," which is transparent. However, the comparison does not specify: (a) whether equivalent batch sizes were used for all methods, (b) whether the baseline implementations (PyTorch MCF, torsional diffusion) were re-run in the same environment or numbers were taken from papers, and (c) how "per conformer" timing handles multi-conformer-per-molecule amortization effects. Since the dramatic speed advantage (21–50×) is central to the practical contribution, these details (likely deferred to the appendix, which was stripped during parsing) should be summarized in the main text.

3. **Reflow performance degradation mechanism acknowledged but not addressed.** The paper correctly identifies that reflow-generated $X_1'$ may drift from the data distribution and that filtering low-RMSD couplings could help, but this filtering is not implemented or ablated. As a result, the precision drop on Drugs is stated as a limitation but not mitigated, weakening the otherwise strong contribution of the reflow pipeline.

### Trivial
None.

## Nice-to-Haves

- Ablation of the exponential timestep distribution parameter $\lambda = -1.2$ (Eq. 10). The motivation is stated but no comparison to uniform sampling or other $\lambda$ values is provided.
- Statistical significance measures (confidence intervals or error bars) for Figure 2 and Figure 3, particularly since they report averages over a 300-molecule subset.
- Reporting the number of conformers generated per molecule (fixed $k$ or 2× ground truth, as in prior work) to aid comparability.
- An explicit algorithmic pseudocode for the Averaged Flow training step, showing how the SO(3) integral (Mohlin et al., 2020) integrates into the forward/backward pass.

## Removed Points

The following criticisms from the inputs were evaluated against the paper text and removed:

**1. "The Averaged Flow derivation is insufficiently specified for reproducibility" (Harsh Critic, Critical Issue #2).** The paper provides: the decomposition over group orbits (Eq. 2), the specific form for conformer generation (Eqs. 5–7), the final expression $u_t(x_t) = ([\partial_\alpha \log Z_t(x_t,\alpha)]_{\alpha=0} - x_t)/(1-t)$, reference to the closed-form SO(3) integral from Mohlin et al. (2020), the loss function (Eq. 8), and the practical approximation (sampling one conformer per epoch). The mathematical derivation is sufficiently specified for a main body. OCR artifacts in the rendered Eq. 8 (repeated terms) are parser-level issues and not present in the original submission. The appendix (stripped by the parser) would contain additional implementation details. This does not constitute a weakness of the paper as submitted.

**2. "The reflow model underperforms MCF on QM9" (implied by Harsh Critic's numerical comparison).** The paper text explicitly states that "AvgFlow$_{\text{Reflow}}$ and AvgFlow$_{\text{Distill}}$ achieve higher COV-R than other models" on QM9. The specific numbers cited by the critic (88.52 COV-R for reflow vs. 96.36 for ET-Flow-SS) contradict the paper's own textual summary and cannot be verified from the image table. The paper's textual description is the authoritative source for its claims.

**3. "No analysis of number of conformers per molecule" (Harsh Critic).** A minor missing detail that falls under nice-to-have; prior work often uses 2× ground truth, and this is standard practice.

**4. Several generic/general-area criticisms** from the Harsh Critic (e.g., "the evaluation lacks rigor" implied in section-by-section notes about specific missing items) that lack a concrete anchor in the paper content.

## Novel Insights

The most interesting synthesis emerging from the reviews is that the paper's empirical contribution has two distinct regimes with very different strength profiles. **Regime 1 (multi-step, $N_{\text{step}} \ge 10$):** the main Averaged Flow model converges faster and achieves state-of-the-art or near-SOTA quality, demonstrating that symmetry-averaged training objectives are a genuine improvement over rotational alignment or conditional OT. **Regime 2 (few-step, $N_{\text{step}} < 5$):** reflow is necessary but introduces a precision-quality gap on larger molecules (Drugs) not seen on smaller molecules (QM9), suggesting that the distribution shift from reflow-generated couplings scales with molecular complexity. This contrast is not highlighted in the paper but is the most actionable insight: Averaged Flow alone is a clear win for quality-oriented use cases, while the reflow pipeline requires further work (e.g., the proposed coupling filtering) to close the quality gap on drug-sized molecules.

## Suggestions

1. **Tone down the abstract's blanket claim.** Replace "match the performance of strong transformer baselines" with a more precise statement: e.g., "on GEOM-QM9 our model matches or exceeds transformer-based baselines in coverage, and on GEOM-Drugs it achieves competitive precision with far fewer parameters and generation steps, though with some reduction in recall after reflow."

2. **Provide a short algorithmic summary of Averaged Flow training** (2–3 lines of pseudocode or a step list) in the main text to mitigate the dense notation. This would also address reproducibility concerns without relying on the appendix.

3. **Add a brief paragraph to the sampling time comparison** (Section 4.5) specifying the hardware, batch size, framework, and whether baseline numbers were measured in the same environment. Even a single sentence like "All methods were benchmarked on an NVIDIA A100 GPU with batch size X, using the authors' public implementations where available" would resolve the fairness question.

4. **Implement the proposed filtering of reflow couplings** as an additional ablation, or acknowledge it as a clear limitation if it remains unimplemented. The paper already identifies the fix — demonstrating it (or showing the effort fails) would substantially strengthen the reflow contribution.
