Thank you — now I have a thorough understanding of the paper and all reviewer claims. Let me compile the final review after cross-checking each point against the actual paper text.

---

## Summary

This paper derives generalization bounds for Kolmogorov–Arnold Networks (KANs) under two regimes: (1) activation functions expressed as linear combinations of basis functions (Section 2.2, Theorems 1–2), and (2) activation functions lying in a low-rank Reproducing Kernel Hilbert Space (Section 2.3, Theorem 3). The bounds scale with interpretable quantities such as Lipschitz constants and l₁-norms of coefficient matrices, avoid combinatorial parameters outside logarithmic factors, and accommodate unbounded loss functions via a truncation argument. Numerical experiments on simulated and real data track one component of the basis-function bound against excess loss during training.

## Strengths

- **First rigorous generalization bounds for KANs.** As the paper notes in Section 1.1, "there is currently no recent research focusing on quantifying the complexity of KANs." Theorems 1–2 provide covering-number-based bounds for KANs with general basis-function representations, filling a genuine gap in the literature. The bounds are technically sound extensions of the covering-number approach from Anthony & Bartlett (1999) and Bartlett et al. (2017), adapted to the KAN structure where activations are learnable functions on edges rather than fixed nonlinearities on nodes.

- **Novel low-rank RKHS analysis with practical connection to fine-tuning.** Theorem 3 (thm-main3) and its variants provide generalization bounds for KANs with activation functions in a low-rank Matérn RKHS. Remark 1 (rm1) explicitly connects this to LoRA-style fine-tuning, observing that if a pre-trained activation is fine-tuned with a low-rank update, the theory applies. This connection is genuinely new — the paper states "the results for KANs with a low-rank structure in Section 3.2 appear to be new, and we are not aware of comparable results for MLPs in the recent literature."

- **Bounds handle unbounded loss functions.** Unlike many prior bounds that require boundedness (e.g., the ramp loss in Bartlett et al. 2017), Theorem 2 (thm-main2) and Corollary 1 cover squared loss, Huber loss, pinball loss, and other regression losses via a truncation argument (Assumption 4). This is a meaningful technical improvement over comparable MLP bounds.

- **Bound complexity depends on interpretable quantities, not combinatorial parameters.** The bound depends on l₁-norms of coefficient matrices, Lipschitz constants, and basis-function Lipschitz constants — not on the raw number of nodes or edges outside logarithmic factors. This provides a concrete, interpretable complexity measure for KANs.

## Weaknesses

### Fatal
None.

### Major

1. **Empirical validation tests only a normalized component of one bound, not the full bound, and oversells empirical scope.** The experiments track a single term proportional to \((\prod \rho_j)^{2/3} \sum (B_i c_i)^{2/3}\) (which is proportional to \(\tilde{\alpha}\)), not the full bound from Theorem 2. The full bound includes sample-size-dependent terms, moment constants, and probability parameters. Showing that one *component* correlates with excess loss is weaker than validating the full bound. Furthermore, the abstract states "These bounds are empirically investigated" — implying both the basis-function and low-rank RKHS bounds — but the low-rank bound (Section 2.3) receives no empirical testing whatsoever. Its practical relevance therefore rests entirely on theoretical reasoning. While the theory is a genuine contribution, this gap between presentation and execution is significant.

2. **The normalization procedure weakens the correlation evidence.** The paper normalizes "so that the maximum value of the complexity measure is equal to the last value of the excess loss" (Section 4). This is a data-dependent scaling that forces alignment at one point. While the *shape* of the curves across training epochs can still be informative, this normalization makes visual correlation claims substantially less convincing. Combined with the absence of any quantitative correlation measure (e.g., Spearman's \(\rho\)), error bars, or multiple random seeds, the central empirical claim of "tight correlation" is not robustly supported.

3. **No experimental comparison against alternative complexity measures.** The experiments do not compare the proposed complexity measure against any baselines — e.g., VC dimension estimates, Rademacher complexity of comparable MLPs, spectral-norm-based MLP bounds, or even simpler baselines like parameter count. Without such comparison, it is impossible to judge whether the KAN-specific bound captures something distinctive that simpler measures miss, or whether the observed correlation is generic to any monotonically evolving quantity during training.

### Minor

- **Experimental details are insufficient for replication.** The numerical section specifies neither the learning rate, optimizer variant (SGD with/without momentum?), batch size, number of basis functions, type of basis (B-spline? polynomial? which degree?), nor how the spectral norm \(\|A\|_\sigma\) in Remark 4 was estimated to bound the Lipschitz constants. These are standard details even for theory papers with supporting experiments.

- **The low-rank bound's exponent can be extremely large for high-dimensional inputs.** Proposition 4 and Theorem 3 contain terms of the form \((\tilde{b} \prod \rho_j / \epsilon)^{(d_{i-1}/\nu) \vee 1}\). For the CIFAR-10 experiment with \(d_0 = 1000\) and moderate smoothness \(\nu\), this exponent is \(1000/\nu\), which could make the bound vacuous. The paper does not discuss practical values of \(\nu\) or characterize regimes where this bound is meaningful.

- **The paper would benefit from a small number of baseline comparisons** (e.g., plotting the same complexity measure for a randomly-wired KAN, or comparing against parameter count) to establish that the *specific* form of \(\tilde{\alpha}\) matters beyond being a generic complexity proxy.

### Trivial
None.

## Nice-to-Haves
- A scatter plot of the predicted bound vs. actual test risk across different KAN configurations (width, depth, basis type) rather than only across training epochs.
- An ablation showing that removing components of \(\tilde{\alpha}\) (e.g., the \(B_i^{2/3}\) or \(\rho_j\) factors) weakens the correlation.
- A non-vacuous numerical evaluation of the *full* bound (including all terms) for at least one small dataset, to demonstrate feasibility.

## Removed Points
These points are flagged to be removed, treat them with caution:

1. **"The paper never actually compares the final bounds to analogous MLP bounds under comparable assumptions."** — The paper explicitly states at line 250: "In Section \ref{sec-add-discuss}, we compare this bound with a corresponding bound for MLPs in \cite{bartlett2017spectrally}." This section was in the appendix, which the parser strips from all papers. Per the instructions, criticisms about missing appendix content are removed.

2. **"Reproducibility crisis" and "no learning rate, optimizer variant, batch size..."** — While the experiments are indeed sparse on details, the "reproducibility crisis" framing is overly theatrical for a theory paper with illustrative experiments. The missing details are noted as a minor weakness above rather than a major crisis.

3. **"The constants C', C'', s, s' appear but their interpretation is left entirely to the appendices."** — These constants are defined in Assumption 4 (as4) directly in the main paper: \(\mathbb{E}[G^s(\mathbf{x},y)] < C' < \infty\) and \(\mathbb{E}[B^{s'}(y_i)] < C'' < \infty\). They are not left to the appendices.

4. **"The bound on \(\|\boldsymbol{\Psi}(\mathbf{0})\|_2\) is reasonable but its effect on the final bound is not discussed."** — The bound explicitly incorporates \(C = \max_l C_l\) into the definition of \(\tilde{\alpha}\) (line 217–221), and the special case \(C=0\) is explicitly computed, showing the term's effect.

5. **"The Lipschitz constant \(\rho_l\) may scale with the number of input nodes \(d_{i-1}\) in a way not explicitly bounded."** — Remark 4 provides an explicit upper bound \(\rho^* \le \|A\|_\sigma c_l \sqrt{b_l}\) for the basis-function case, accounting for this structure.

## Novel Insights
None beyond the paper's own contributions. The reviews did not surface any insight about the paper that is not already stated in the paper's own analysis and discussion.

## Suggestions

1. **Revise the abstract and discussion to accurately scope the empirical contribution.** Replace "These bounds are empirically investigated" with "The basis-function bound is empirically investigated" or similar. This small change would eliminate the most significant disconnect between claims and evidence.

2. **Add basic experimental rigor:** report results from at least 3–5 random seeds with error bars or band plots, and report a simple quantitative correlation measure (Spearman \(\rho\)) between the complexity measure and excess loss. This would substantially strengthen the empirical support without requiring new experiments.

3. **Add one baseline comparison** — even plotting parameter count or the spectral norm of the first layer's coefficient matrix against excess loss — to demonstrate that \(\tilde{\alpha}\) captures something non-trivial.

4. **Discuss the practical regime for the low-rank bound.** A paragraph characterizing when \(\nu\) and \(d_{i-1}\) make the bound non-vacuous would help readers understand the low-rank result's applicability.

## Score and Decision

The paper makes a genuine theoretical contribution: it provides the first generalization bounds for KANs, including a novel low-rank RKHS analysis with a clean connection to fine-tuning. The technical derivations appear sound and the bounds are interpretable. The experimental section, however, is substantially weaker than the paper's language suggests — it tests only a normalized component of one bound, lacks baselines and error bars, and the low-rank bound receives no empirical validation. This gap between presentation and evidence is the paper's primary weakness.

The paper is above the acceptance threshold for a theoretical contribution with illustrative experiments, but the authors should address the experimental overselling and strengthen the empirical analysis in a revision.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>