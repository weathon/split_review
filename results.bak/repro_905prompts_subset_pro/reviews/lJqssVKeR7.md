Now I have all the information I need. Let me compose the final review.

## Summary
This paper proposes HiSo, a federated optimization method that accelerates zeroth-order (ZO) training by incorporating a global diagonal Hessian approximation into a scalar-only communication framework. The key insight is that the diagonal preconditioner can be reconstructed from the same gradient scalars already communicated, incurring zero additional communication cost. The paper provides theoretical convergence rates showing dimension-free and Lipschitz-constant-free behavior under a "well-approximated Hessian" condition, and extends the analysis to multiple local steps — a setting the prior DeComFL framework could not handle. Empirically, HiSo achieves 1.4–5.4× faster convergence than DeComFL on LLM fine-tuning benchmarks (SST-2, QQP, SQuAD) across OPT models from 125M to 2.7B parameters.

## Strengths
- **Strong theoretical contribution**: The paper proves the first convergence rate for ZO-FL that is independent of both model dimension $d$ and Lipschitz constant $L$ under the well-approximated Hessian and low-effective-rank conditions (Corollary 1). The extension to $\tau > 1$ local steps (Corollary 3) resolves an open question from DeComFL, which could not provide a dimension-free rate in that setting. Theorem 1 itself does not require the well-approximated condition, giving a clean separation between unconditional and conditional results.

- **Elegant integration of preconditioning into scalar-only FL**: The diagonal Hessian approximation is updated via an exponential moving average of squared ZO updates (Eq. 12), which can be reconstructed from the same scalar values already used for gradient communication. This means HiSo achieves curvature-aware updates while transmitting exactly the same per-round data as vanilla ZO-SGD — a genuinely clever design that directly answers the paper's motivating research question.

- **Clear empirical gains over the state-of-the-art ZO-FL baseline**: Table 2 reports round counts needed to match DeComFL's best accuracy, showing 1.4–5.4× reductions across all model sizes and tasks, with corresponding 29%–80% communication savings. Table 3 further shows HiSo consistently achieves the highest accuracy among ZO baselines while maintaining the lowest communication cost in almost all settings.

- **Honest presentation of limitations**: The paper explicitly acknowledges in footnotes that the Hessian update resembles RMSProp (footnote 2) and that "Hessian-informed" means the update approximates preconditioning direction, not that the full Hessian is computed (footnote 1). The theoretical corollaries are clearly marked as conditional on the well-approximated assumption, with the remark that if $H_r$ fails to approximate the Hessian, performance degenerates to DeComFL (Section 5.2).

- **Generalized scalar-only framework**: Algorithm 1 provides a clean abstraction that decouples scalar-only communication from vanilla ZO-SGD, enabling future work to plug in other optimization algorithms without breaking the communication budget.

## Weaknesses

### Fatal
None.

### Major
- **LLM experiments do not specify data partitioning across clients.** The paper's motivating scenario is collaborative fine-tuning over privacy-sensitive data, where non-IID data distributions are the standard challenge in federated learning. The MNIST experiment (Section 6, Fig. 5) explicitly uses a non-IID Dirichlet partition ($\alpha = 1$), but the LLM experiments (SST-2, QQP, SQuAD) only state "6 clients in total, and 2 clients are uniformly sampled in each round" with no mention of how data are split. If the LLM splits are random/IID, the practical significance of the federated results is weakened — readers cannot assess whether HiSo's gains persist under data heterogeneity, which is the regime that truly motivates federated learning. This should be clarified and ideally tested under non-IID partitions.

### Minor
- **No direct empirical validation that the learned $H$ captures Hessian structure.** The paper's core branding is "Hessian-informed," yet the update rule for $H$ (Eq. 12: EMA of squared ZO updates) is structurally identical to an RMSProp-style adaptive scaling rule. The paper is transparent about this (footnote 2), but the gap between the "Hessian" label and what is demonstrated remains. The long-tail distribution of $H$ values (Fig. 5, right) is consistent with a low-effective-rank Hessian but is equally consistent with many non-curvature weighting schemes. A small-scale experiment where the true Hessian diagonal can be computed (e.g., logistic regression) and compared against the learned $H$ would substantially strengthen the central claim. As the paper notes, additional evidence is deferred to Appendix F.7.2, which is not available for review.

- **The "P = 5" parameter is undefined in the main text.** In the LLM task setup (line 314), the paper states "We set P = 5 for all ZO methods" without defining what $P$ represents. In the ZO optimization literature this typically refers to the number of perturbation directions, but it must be explicitly defined for reproducibility. This is particularly important since the number of queries directly affects both convergence and communication cost.

### Trivial
- The abstract states HiSo provides "strong empirical evidence that Hessian information acts as an effective accelerator," which slightly overstates what is shown — the evidence supports that the preconditioner accelerates convergence, but does not directly establish the preconditioner as Hessian in nature. The paper itself acknowledges this distinction in footnotes and remarks; the abstract could be more precisely aligned.

## Nice-to-Haves
- A comparison against an adaptive ZO method that uses per-coordinate scaling without the Hessian framing (e.g., a scalar-only ZO-RMSProp baseline) would help readers isolate whether the gains come specifically from the diagonal preconditioning update rule or from adaptive scaling more generally. The current comparison against DeComFL (no preconditioning) shows that *some form* of preconditioning helps, but does not distinguish between different preconditioning strategies.

- Including non-IID data splits for the LLM tasks and discussing how performance varies with heterogeneity would substantially increase the practical value of the empirical evaluation.

- The accuracy vs. communication trade-off could be discussed more explicitly: HiSo saves orders of magnitude in communication compared to first-order methods but loses several accuracy points (e.g., 90.34% vs 92.86% on OPT-1.3B SST-2). A brief discussion of when this trade-off is worthwhile would help practitioners.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh Critic: "The Hessian-informed claim is not supported and the algorithm is mischaracterised."** REMOVED as a standalone fatal criticism because the paper explicitly addresses this in footnotes 1 and 2 — it acknowledges the RMSProp connection and clarifies that "Hessian-informed" refers to approximating the Hessian preconditioning direction. The theoretical corollaries are explicitly conditional. This concern is downgraded and partially retained as a Minor weakness above (lack of direct Hessian validation).

- **Harsh Critic: "Comparisons do not isolate the effect of Hessian-informed preconditioning" and demand for a ZO-FedAdam baseline.** PARTIALLY REMOVED. The paper already compares against DeComFL (no preconditioning), which isolates the effect of adding preconditioning. The demand for a "ZO-RMSProp without Hessian framing" baseline is circular since HiSo *is* the RMSProp-style method. Moved to Nice-to-Haves as a suggestion for isolating the diagonal preconditioning mechanism specifically.

- **Harsh Critic: "The meaning of P = 5 is not defined, a critical omission for reproducibility."** This is valid but not "critical" — it's a clarity issue. Retained as Minor.

- **Harsh Critic: "Appendix is not provided, so I cannot check missing derivations."** REMOVED per the hard rule against criticizing missing appendix. The parser strips appendices from all papers.

- **Harsh Critic: "The accuracy remains far below first-order methods. The trade-off is not discussed."** PARTIALLY REMOVED as a weakness target. This is inherent to ZO methods and expected. Moved to Nice-to-Haves.

- **Harsh Critic: "The paper provides no derivation linking the expectation of this update to any curvature quantity."** REMOVED. The paper does provide a derivation in Section 4.1 (Eqs. 5-9) showing that the expected update follows a Newton-style direction when $H_r$ approximates the Hessian. The update rule itself (Eq. 12) is an EMA of squared updates, whose connection to curvature is through the standard RMSProp/Adam intuition, which the paper cites.

- **Strength Finder: "Performance remains competitive with first-order methods."** SOFTENED. The accuracy gap to first-order methods is 2-4 points on some tasks, which is significant. The strength is retained in the main review with appropriate qualification.

## Novel Insights
The paper's theoretical framework decomposes the ZO gradient variance bound through a "whitening" lens (Eq. 16), showing that a well-approximated diagonal Hessian preconditioner can reduce the variance from $\mathcal{O}(Ld)$ to $\mathcal{O}(\zeta)$ where $\zeta$ is a dimension-free "low whitening rank." This provides a plausible theoretical explanation for why ZO methods often converge faster in practice than their worst-case $\mathcal{O}(d)$ bounds would predict — an observation that has been noted empirically but not formally explained in the FL setting. The generalization of DeComFL's analysis to $\tau > 1$ local steps without reintroducing dimension dependence is also a genuine theoretical advance.

## Suggestions
- Define $P$ explicitly in the main text (e.g., "number of perturbation directions per ZO gradient estimate").
- Specify the data partitioning strategy for all LLM experiments. If IID splits were used, either add non-IID results or explicitly discuss this as a limitation.
- Consider running a small-scale validation (e.g., on a toy network or logistic regression) where the true Hessian diagonal is computable, to directly assess whether the learned $H$ correlates with curvature.

## Score and Decision

**Calibration summary:**

Round 1 bracket: The paper is clearly stronger than the weak anchors (1.67–3.25) and the DeComFL baseline paper at 6.25. It is below the 7.5+ strong-theory anchors. Initial bracket: **6.0–7.5**.

Round 2 narrowing:
- **DeComFL (omrLHFzC37, 6.25)**: HiSo is a direct improvement over this paper, adding preconditioning, stronger theory (τ > 1 support), and 1.4–5.4× empirical speedup. HiSo is clearly stronger.
- **FRLoRA (e0rQRMUhs, 6.60)**: Both papers address federated LLM fine-tuning but with different techniques. FRLoRA had novelty concerns (similarity to FlexLoRA, Chain of LoRA) and limited non-IID testing. HiSo has cleaner novelty relative to its baseline (DeComFL) and more honest framing, but weaker heterogeneity evaluation. These are comparable in overall quality.
- **FedDA (kjn99xFUF3, 6.00)**: Adaptive methods for FL, different domain. HiSo has better empirical validation and clearer practical motivation.

HiSo extends DeComFL with a genuine contribution (curvature-aware scalar-only FL), provides clean theory including the first τ > 1 analysis, and shows strong empirical speedups. The main weaknesses are the unspecified LLM data partitioning and lack of direct Hessian validation, but both are acknowledged limitations rather than hidden flaws. The paper is honestly framed throughout.

Final score: **7.0**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>