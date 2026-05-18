Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper proposes Spectral Contrastive Regression, a method for improving in-distribution (ID) and out-of-distribution (OOD) generalization in regression tasks. It introduces two loss components: (1) a relational contrastive loss (L_std) that minimizes the standard deviation of the ratio between feature distance and label distance across pairs, and (2) a spectral norm alignment loss (L_svd) that aligns the largest singular values of feature matrices from real and synthesized (C-Mixup augmented) distributions. Experiments on eight regression benchmarks show consistent state-of-the-art or near-SOTA results.

## Strengths

1. **Novel formulation of the feature-label proportion as a variable mapping.** Unlike prior work (RML) that assumes a constant proportion, the paper correctly notes this proportion varies across samples and proposes minimizing its standard deviation. This is a sound intuition that differs meaningfully from existing regression metric learning approaches.

2. **Consistent strong empirical results across diverse benchmarks.** The method achieves best or second-best results on all eight datasets spanning tabular, time-series, and image data (Tables 1–4), covering both ID and OOD settings. The MPI3D results (Tables 3–4) specifically show that spectral norm alignment outperforms Frobenius and nuclear norm alignment, providing concrete evidence for the design choice.

3. **Clean, practically-motivated loss design.** Both losses are simple to implement (add two terms to the MSE objective) and computationally inexpensive. The hyperparameter sensitivity analysis (Figure 2) provides practical guidance for deployment.

## Weaknesses

### Major

1. **Unsupported theoretical claims for L_std.** The paper builds Remarks 1 and 2 (label-distance order ⇔ feature-distance order) on the assertion that the regression function *p* is a "continuous bijection" with "homeomorphic label and feature distributions." Even if *p* is a homeomorphism, this preserves topological structure but does **not** imply the metric ordering equivalence stated in Remarks 1 and 2 — a homeomorphism can stretch distances non-uniformly. The attempt to justify Remark 2 via uniform continuity is also insufficient. Furthermore, the claim that L_std "constrains the predictor *p* as a Lipschitz continuous function" (line 135) is stated without derivation or proof; minimizing the standard deviation of d(f)/d(y) does not obviously yield Lipschitz continuity of *p* (which requires |y_i−y_j| ≤ L·‖f_i−f_j‖). These theoretical gaps mean the paper's motivation is overclaimed relative to what is actually established. This is a major weakness because the conceptual framing of the paper depends on this justification.

2. **Missing ablation of the fine-tuning (FT) strategy.** All experiments on the primary benchmarks (Tables 1–2) use the fine-tuning protocol (freezing the top of a C-Mixup pretrained network, finetuning only bottom layers and last block). While the baselines also use FT when possible (making comparisons fair), the paper never shows results *without* FT on these datasets. On MPI3D, where FT is *not* used, the gains appear more modest. Without an ablation that removes FT, it is difficult to isolate how much improvement comes from the proposed losses versus the careful FT schedule borrowed from prior work. Addressing this would substantially clarify the paper's contribution.

### Minor

3. **No standard deviations or confidence intervals reported.** Results are reported as means over 3 seeds with no measure of variance. Several reported improvements appear small (e.g., 0.626 vs. 0.627 on DTI RMSE, 0.486 vs. 0.501 on Crimes — though specific numbers could not be independently verified from table images). Without error bars, the reader cannot judge whether the improvements are statistically meaningful.

4. **Connection from Theorem 2 to L_svd is heuristic, not rigorous.** Theorem 2 bounds domain discrepancy by the difference in output Frobenius norms, and the paper notes that output Frobenius norms are bounded by terms involving the spectral norm of features (‖F‖₂). However, the bound involves products ‖F‖₂·‖W_i‖₂ + |b_i|, so minimizing |‖F_real‖₂ − ‖F_syn‖₂| does not directly control the bound. The paper describes this as "aligning the spectral norms can prevent the output scales from differing greatly," which is a reasonable intuition but not a formal theoretical connection. This weakness can be addressed by reframing L_svd as empirically motivated.

5. **t-SNE visualization provided for only one dataset (DTI).** The claim of "clearer" discriminative patterns is qualitative and limited to a single dataset, weakening its evidentiary value.

### Trivial

6. The introduction's claim that "existing regression methods overlook feature-level generalization" (line 8–9) is a rhetorical overstatement, as the paper itself cites and compares against RankSim (Gong et al., 2022) and FDS (Yang et al., 2021), which are feature-level methods. Minor framing issue.

## Nice-to-Haves

- An ablation study showing performance without FT on at least 2–3 datasets would cleanly separate the contribution of L_std/L_svd from the FT protocol.
- Individual ablations of L_std and L_svd on the main datasets (beyond the MPI3D norm comparisons) would strengthen attribution.
- Hyperparameter values (α, β) used for each dataset should be stated explicitly.

## Removed Points

- **DANN/CORAL criticism**: The reviewer claimed the MPI3D experiments include DANN and CORAL in ways requiring target-domain data. The paper's text (line 247–249) only mentions comparisons with RML, C-Mixup, and norm-based alignments (Nuclear, Frobenius). No DANN/CORAL references appear in the text, so this criticism is unverifiable from the paper content. **Removed — factual basis unclear.**
- **Linear layer assumption**: The reviewer called the linear optimal predictor assumption unrealistic. This is a standard theoretical simplification for building tractable bounds; many regression papers make similar assumptions. **Removed — scope creep.**
- **L_std variance denominator concern**: The reviewer questioned the N_b²−1 denominator. This is standard Bessel's correction for sample variance over all N_b² pairs. **Removed — standard practice.**
- **Sloppy λ(F) notation**: Concern about notation being "sloppy." This is a formatting/style nitpick. **Removed — formatting nitpick.**
- **Dominant direction concern**: The claim that aligning only the magnitude of the largest singular value "may not align the distributions" if dominant directions differ is speculative, not a specific identified flaw. **Removed — speculation.**
- **Strength about FT strategy**: The Strength Finder claimed the FT strategy as a paper strength, but this is borrowed directly from prior work (Kumar et al., 2022; Kirichenko et al., 2023) and is not a contribution of this paper. **Removed — not a claimed contribution.**

## Novel Insights

Beyond the paper's own contributions, the synthesis of the two reviews surfaces that the paper's empirical strength (consistent SOTA across benchmarks) and its theoretical weakness (overclaimed justification for L_std) exist in tension. The paper would be significantly stronger if it acknowledged L_std as a purely empirical regularization technique (with the intuitive motivation of smoothing the proportion map) rather than claiming formal Lipschitz or homeomorphism guarantees that do not follow from the presented reasoning. The spectral norm alignment for OOD regression is a genuinely novel and well-motivated idea, and the MPI3D comparison across norms provides the strongest direct evidence for the design.

## Suggestions

1. **Reframe the theoretical motivation for L_std.** Drop or substantially revise Remarks 1 and 2 and the Lipschitz claim. Replace with a simpler statement: "We minimize the std of d(f)/d(y) to encourage a more uniform proportion across samples, which we hypothesize improves generalization by reducing variance in the embedding space." This honest empirical framing is more defensible and still novel.
2. **Add an ablation without FT on 2–3 datasets** (e.g., Airfoil, Crimes, RCF-MNIST) to disentangle the contribution of FT from the proposed losses.
3. **Report standard deviations** across the three seeds for all main results.
4. **State hyperparameter α, β** used per dataset in the main paper (currently only in the sensitivity analysis for 2 datasets).
5. Provide the C-Mixup pretraining details (what data, what architecture) explicitly for reproducibility.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>