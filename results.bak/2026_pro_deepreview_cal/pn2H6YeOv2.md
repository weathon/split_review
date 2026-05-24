Now I have enough information to write the consolidated review. Let me compile my analysis.

---

## Summary
PI-CCA proposes a replay-free continual learning method for vision-language models that preserves cross-modal generalization by explicitly maintaining CCA (Canonical Correlation Analysis) geometry. The core idea is to summarize image-text alignment with a compact "certificate" capturing the top-k canonical spectrum and subspace, then regularize training to match this certificate using only mini-batch statistics. The method achieves state-of-the-art results among replay-free methods across four VL-CL benchmarks (MTIL, X-TAIL, VLCL, ConStruct-VL) and includes a prompt-invariance mechanism for robustness to phrasing variations.

## Strengths
- **Strong SOTA results across four diverse benchmarks with thorough baselines.** Tables 1–2 show PI-CCA leading on MTIL Avg (76.8), X-TAIL Avg (68.1), VLCL I2T R@1 (48.6), and ConStruct-VL FA (75.2) with the lowest AF (2.7), outperforming strong replay-free baselines including C-CLIP, DIKI, RAIL, and even the synthetic-replay method GIFT. The evaluation spans classification, retrieval, and structured-concept matching.
- **Clean ablation validates the core design.** Table 3 demonstrates that removing either the spectral term (λ₁=0, −2.5 MTIL Avg) or the subspace term (λ₂=0, −2.2 MTIL Avg) causes the largest performance drops, confirming that both canonical correlations and subspace angles are necessary for retention.
- **Prompt-invariance loss demonstrably reduces sensitivity to phrasing.** Figure 4 shows that with L_pi, degradation slopes under increasing perturbation strength are visibly flatter for both ID and OOD templates, with +2.44 p.p. gain at s=1.0.
- **Practical efficiency with constant memory.** The Pareto analysis (Figure 2) identifies a knee configuration (k=64, h=256) achieving high performance with <6 GB peak memory and <100 ms per step, making the approach practically deployable.
- **Task-order robustness demonstrated.** Figure 5 shows narrow IQRs (76.0–77.4 MTIL Avg) across 20 shuffled orders, ruling out order-dependent lucky outcomes.

## Weaknesses

### Fatal
None.

### Major
- **Figure 3 correlation coefficients (r=1.00, ρ=1.00) are not credible as reported.** Two of four panels in the geometry→performance correlation analysis report Pearson r=1.00 and Spearman ρ=1.00, and the other two report r=0.99, ρ=1.00. The paper's own caption describes "realistic scatter," which directly contradicts perfect correlation. While the sweep across hyperparameter configurations (certificate size, EMAs, invariance strength, etc.) could produce strong correlations, perfect values with zero residual variance are implausible given multiple perturbation sources, random seeds, and optimization stochasticity. The paper's text (§4.3) describes the trends more modestly ("larger angle/spectral drifts generally imply larger drops"), suggesting the annotated values may be a rendering error rather than fabrication. Nevertheless, as presented, the correlation evidence — which the paper uses to argue that preserving CCA geometry *causes* retention — is unreliable. This weakens the paper's central conceptual claim about the causal role of alignment-geometry drift, though it does not undermine the main empirical results (Tables 1–2, Table 3) which stand independently.

### Minor
- **Table 1 lacks variance estimates.** The main classification results (MTIL and X-TAIL) are reported without error bars, standard deviations, or confidence intervals. Margins over the next-best replay-free method are modest (+1.6 on MTIL Avg, +0.7 on X-TAIL Avg over DIKI/RAIL), and without variance information the reader cannot assess whether these differences are statistically meaningful. Table 2 does report ± values, and Figure 5 demonstrates robustness across task orders, which partially mitigates this concern.
- **The "invariants rather than proxy signals" framing slightly overclaims.** The method is ultimately a regularizer on sketched projector distances; while more geometrically principled than similarity-distribution matching, it still optimizes a loss rather than guaranteeing invariance. The abstract's "optimizing alignment invariants rather than proxy signals" promises a stronger causal mechanism than what is empirically established, especially given the concerns with Figure 3.

### Trivial
- Backbone and hyperparameter details (CLIP variant, LoRA rank, learning rates) are deferred to the stripped appendix. While standard practice, specifying the CLIP backbone in the main text would aid readability.

## Nice-to-Haves
- An ablation comparing the sketched projector-distance loss against a simpler feature-moment matching regularizer would help isolate the specific benefit of the CCA subspace formulation.
- A variant using a fixed pre-continual covariance matrix (instead of streaming EMA) could clarify how much retention comes from the statistical accumulation of second-order moments versus the certificate losses themselves.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **"EMA covariances as implicit replay" (Harsh Critic):** REMOVED. Accumulating second-order statistics (covariance matrices) is fundamentally different from storing or replaying data samples. The "replay-free" terminology in continual learning refers to the absence of stored exemplars, not the absence of any aggregated statistics. This criticism reflects a misunderstanding of standard CL terminology.
- **"The phrase promises a stronger causal connection than the experiments establish — the method is still a regulariser on the features" (Harsh Critic):** PARTIALLY RETAINED, downgraded to Minor. The paper does slightly overclaim, but the distinction between geometric invariants and proxy signals is real and substantive — the method directly constrains canonical spectra and subspaces rather than matching similarity distributions or logits.
- **"Without [backbone details], the paper cannot be evaluated for compute requirements" (Harsh Critic):** REMOVED. Backbone details are standard appendix material; their absence from the main text is a trivial formatting issue, not an evaluation barrier.
- **"The code is not released during review" (Harsh Critic):** REMOVED per hard rules — code release status is not a valid criticism.
- **Strength: "This paper addressed an important problem" (Strength Finder):** REMOVED as generic/superficial — not grounded in a specific, verifiable contribution.

## Novel Insights
The paper's reframing of forgetting in VL-CL as alignment-geometry drift (quantified via canonical correlations and subspace angles) is genuinely novel and productive. Rather than treating the CCA decomposition as merely diagnostic (as prior work has done with SVCCA/CKA), PI-CCA operationalizes it as a training objective, which is a conceptual step forward. The insight that a compact random-sketch certificate can serve as a constant-memory proxy for the full CCA geometry is practically valuable. The observation that averaging sketched projectors across prompt perturbations eliminates sign/rotation ambiguity without Procrustes alignment is a neat technical trick.

## Suggestions
- **Correct or verify Figure 3.** The authors should re-check the correlation computation and figure annotations. If the true Pearson r values are in the 0.8–0.95 range (still very strong), report them honestly with the actual scatter visible. If the annotated values are correct, explain how perfect correlation arises from the experimental design (e.g., if each point represents a deterministic sweep without re-seeding) and acknowledge this as a limitation of the analysis rather than a strength.
- **Add variance to Table 1.** Report ±std or confidence intervals across at least 3 seeds for the MTIL and X-TAIL results. This would substantially strengthen the paper's primary empirical claim.
- **Tone down the causal language.** Replace "optimizing alignment invariants rather than proxy signals" with language that accurately reflects what the method does: constraining CCA geometry through a regularized objective, which correlates with (but does not provably cause) retention.

## Score and Decision

### Calibration Anchors Used

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| C-CLIP | sb7qHFYwBc | 6.50 | R1/R2 | Direct baseline; PI-CCA outperforms it on all benchmarks with better methodology and evaluation |
| PROOF | k9NYnsC4Mq | 5.67 | R1/R2 | Weaker VL-CL method with inference mismatch issues; PI-CCA substantially stronger |
| TiC-CLIP | TLADT8Wrhn | 6.25 | R3 | Related domain; PI-CCA has stronger results and more principled approach |
| Elastic Feature Consolidation | 7D9X2cFnt1 | 7.00 | R3 | Unimodal CL with strong methodology; comparable rigor but different domain |
| Budgeted Online CL | dOAkHmsjRX | 7.50 | R3 | Different domain; higher score reflects strong theoretical+empirical package with fewer concerns |

### Round 1 Bracket: 6.0–7.5

### Score Justification
PI-CCA is clearly stronger than C-CLIP (6.50), the most directly comparable anchor — it has better results, a more principled geometric approach, more comprehensive evaluation (four benchmarks plus Pareto, task-order, and prompt-invariance analyses), and outperforms C-CLIP as a direct baseline. However, it falls short of the 7.50-level unimodal CL papers because the Figure 3 correlation issue raises genuine concerns about evidential rigor on the paper's central conceptual claim, and the lack of variance reporting on the primary results table is a notable omission for a paper making SOTA claims. The paper lands above Elastic Feature Consolidation (7.00) in contribution novelty (multimodal CL + CCA geometry is more novel than second-order feature consolidation) but shares similar empirical rigor concerns. **Score: 7.0.**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>