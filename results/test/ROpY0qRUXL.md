Now I have a thorough understanding of the paper and can verify the reviewer's claims. Let me write the final consolidated review.

## Summary

This paper explores whether LoRA modules can be merged in closed form by aligning outputs across modules. It identifies that jointly solving for both low-rank matrices A and B yields an indeterminate system, and proposes **LORM** — an alternating optimization strategy where one matrix is frozen and the other is merged via closed-form RegMean-derived equations. The method is applied to Federated Class-Incremental Learning (FCIL), with both spatial aggregation (across clients per round) and temporal aggregation (across tasks). Empirical results on CIFAR-100, ImageNet-R, and EuroSAT across multiple heterogeneity levels show strong performance.

## Strengths

1. **Principled closed-form merging of LoRA modules.** The paper derives closed-form equations (Eq. B and Eq. A, Section 3.1) for merging LoRA matrices by fixing one matrix and solving the regression objective for the other. This is a principled advancement beyond simple averaging, and the alternating optimization strategy (Section 3.2) is a sensible way to resolve the otherwise indeterminate joint system.

2. **Strong empirical results.** The method achieves top Final Average Accuracy across most settings in the in-domain evaluation (CIFAR-100, ImageNet-R) and surpasses competitors by a significant margin on the out-of-domain EuroSAT dataset, directly supporting the claim of state-of-the-art performance in most settings.

3. **Ablation studies validate design choices.** The ablation in Section 4.3 shows that the alternating strategy outperforms training only the B matrix, and that applying RegMean for temporal merging further boosts performance. The ablation also isolates the contribution of simply using LoRA (vs. full fine-tuning) from the contribution of the closed-form merging strategy.

4. **Communication efficiency from alternating optimization.** By transmitting only one low-rank matrix per communication round (instead of both), the alternating procedure reduces communication overhead compared to transmitting the full LoRA module.

## Weaknesses

### Major

- **Contradiction between claimed diagonal-only Gram matrix transmission and the actual equations.** The paper states twice (Section 3.3, lines 120 and 122) that *only the diagonal* of the Gram matrix is communicated, citing both privacy and efficiency benefits. However, **Eq. (B)** (line 92–93) requires the full matrix products $\sum \mB_i \mA \mX_i\mX_i^\top$ and $\mA \sum \mX_i\mX_i^\top \mA^\top$, and **Eq. (A)** (line 97) requires $\sum \mX_i\mX_i^\top$ and its inverse. None of these operations can be computed from only the diagonal. Furthermore, the methodology description in Section 3.2 (line 103) says clients send the full $\mX_i\mX_i^\top$ to the server, directly contradicting the later claim about diagonal-only transmission. This is an internal contradiction: either the method uses full Gram matrices (as the equations and Section 3.2 imply), in which case the privacy/efficiency claims about diagonal transmission are false and the "obfuscation" argument is overstated (full Gram matrices can reveal distributional information especially for early layers); or a diagonal approximation is used, in which case the derivations in Eqs. (A) and (B) are incorrect as written. Either way, the technical description is unreliable on this critical point. **The equations require the full Gram matrix.** This must be resolved before the paper can be taken at face value.

### Minor

- **Convergence analysis is thin.** The claim of faster convergence (Section 4.2) is supported by a single plot (Figure convergence) for the first task of ImageNet-R with $\beta=0.05$. Convergence rate depends on task difficulty, data heterogeneity, and round count. Stronger evidence would require plots across multiple tasks/datasets or quantitative comparison (e.g., rounds to reach a threshold accuracy).

- **Memory cost of temporal aggregation is not discussed.** Section 3.2 (line 112) states that the server stores task-specific residuals $\Delta\mW^t$ and Gram matrices $\mX^t\mX^{t\top}$ for all $T$ tasks. This grows linearly with the number of tasks, yet this memory cost is not discussed in the efficiency or limitations sections.

- **Computational cost of Gram matrix computation not addressed.** Computing $\mX_i\mX_i^\top$ for every linear layer, every client, every round requires forward-passing all local examples through every layer and forming $k \times k$ matrices (where $k$ is the feature dimension). For ViT-B/16 with 12 attention blocks and 768-dimensional features, this is non-negligible. The paper does not discuss this overhead relative to the efficiency claims.

- **Baseline fairness on EuroSAT could be better isolated.** The ablation (Section 4.3, line 155) shows that simply using LoRA with FedAvg gives a *large* improvement on EuroSAT but no effect on ImageNet-R. The main results table includes many baselines that do not use LoRA (EWC, LwF, DER++, L2P, CODA-Prompt, FisherAvg, RegMean, CCVR). While PLoRA (a LoRA-based FCIL competitor) is included and outperformed, a direct "LoRA + FedAvg + ACE" control in the main results table would help cleanly decompose the gain attributable to closed-form merging vs. the gain from using LoRA at all. The ablation provides this breakdown in a figure but it is not in the primary comparison table.

### Trivial

- The paper's "state-of-the-art" claim is appropriately qualified (Section 4.2, line 144: "across all settings except for one"), so this is not a substantive weakness. However, the framing could be tightened for precision.

## Nice-to-Haves

- A brief discussion of whether the alternating optimization objective decreases monotonically or jointly optimizes a consistent objective would strengthen the methodology section. The current treatment is empirical.
- Formal definition of Final Average Accuracy (FAA) in the main text (currently only in appendix) would improve readability.
- A discussion of why the Gram matrix, even in full form, provides meaningful privacy protection vs. raw input transmission, especially given concerns about data reconstruction from Gram matrices of early layers.

## Removed Points

- **Strength about "only the diagonal of the Gram matrix is communicated" (from Strength Finder):** Removed because it conflicts with a verified weakness — the equations require the full Gram matrix, and the methodology description on line 103 says the full matrix is sent.
- **Strength about "privacy preservation by diagonal-only transmission":** Same reason as above.
- **Criticism that derivations are "relegated to the appendix":** Removed per instructions — the parser strips appendix sections; these exist in the original submission.
- **Criticism about missing related works:** Removed per instructions — I cannot independently verify existence of missing works.
- **Formatting/style nitpicks:** Removed per instructions — formatting artifacts are parser issues, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviewer's observation that the Gram matrix claim contradicts the equations is the only genuinely novel finding not present in the original paper. The strength finder and other review content largely recapitulate what the paper itself claims.

## Suggestions

1. **Resolve the Gram matrix contradiction.** The equations (Eq. B, Eq. A, Eq. regmean_cl) all require the full Gram matrix $\mX_i\mX_i^\top$. If the implementation indeed uses the full matrix, correct Sections 3.3 and 3.4 to reflect this, and discuss the privacy implications honestly (e.g., note that Gram matrices leak some distributional information but are less revealing than raw inputs). If a diagonal approximation is actually used, provide the modified equations and evaluate the approximation error empirically — though this would likely degrade results significantly.

2. **Add a "LoRA + FedAvg + ACE" baseline to the main results table.** The ablation study already provides this breakdown for two settings; including it in the primary comparison table would cleanly separate the benefit of LoRA from the benefit of closed-form merging.

3. **Expand convergence analysis.** Provide convergence curves for at least one more dataset/heterogeneity level, or report rounds-to-threshold accuracy quantitatively.

4. **Discuss the memory and computational costs of storing task-specific Gram matrices and computing them for every layer.** This is relevant to the practical applicability of the method.

## Score and Decision

The paper presents a genuinely novel approach (closed-form merging of LoRA via alternating optimization) with strong empirical results. However, the critical internal contradiction about Gram matrix communication undermines the technical description — the paper claims diagonal-only transmission while the equations require the full matrix, and the methodology description says the full matrix is sent. This must be fixed. The other issues (thin convergence analysis, missing cost discussions, baseline decomposition) are addressable.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>