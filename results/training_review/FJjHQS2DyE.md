Here is my final consolidated review:

---

## Summary

This paper proposes Conditional Adversarial Support Alignment (CASA), an extension of marginal support alignment (ASA) that aligns class-conditional feature supports for unsupervised domain adaptation under label shift. The authors derive a novel target risk bound based on conditional symmetric support divergence (CSSD), design a training objective motivated by this bound (source cross-entropy + target entropy minimization + VAT + joint support alignment via pseudo-labels), and report consistent empirical gains over strong baselines on USPS→MNIST, STL→CIFAR, and VisDA-2017 across multiple label-shift severities.

---

## Strengths

- **Clear and well-motivated extension.** The paper identifies a genuine limitation of marginal support alignment (ASA) — that aligning marginal supports can still misalign class-conditional supports — and proposes a natural fix. Figure 1 provides an effective intuitive illustration of why this matters under label shift, and the framing is grounded in concrete failures of prior approaches.

- **Consistent empirical gains across datasets and shift levels.** Across three benchmark datasets, CASA achieves the highest average accuracy and outperforms the second-best method by margins of 4.1% (USPS→MNIST), 1.8% (STL→CIFAR), and 1.0% (VisDA-2017) in average per-class accuracy. Under severe label shift (α=0.5) the margins are 3.6%, 1.6%, and 0.7% respectively. These gains are reported across 15 transfer tasks (5 per dataset), lending credibility to the claim.

- **Theoretical bound connecting conditional support alignment to target risk.** Theorem 1 provides a new target risk bound that explicitly incorporates CSSD, extending the prior IMD-based theory (Dhouib et al. 2022) to the conditional setting. Remark 3.2 provides a thoughtful analysis of the trade-off between the marginal SSD bound and the conditional CSSD bound, showing that while the per-class distance term may be larger, the sup-norm term is smaller — a genuinely non-trivial theoretical observation.

- **Empirical validation of the core mechanism.** The 2D visualization experiment (Figure 2) shows that CASA achieves lower CSSD (0.02) than ASA (0.05) and CDAN (0.13), with corresponding accuracy improvements (99% vs 93% vs 85%). The paper notes that Wasserstein distance does not correlate with accuracy in the same way, directly validating the motivation for using support divergence rather than distribution divergence.

- **Avoids explicit label distribution estimation.** Unlike IWCDAN/IWDAN which require estimating target label proportions, CASA's joint support alignment via pseudo-labels avoids this potentially brittle step — a practical advantage that is backed by its superior performance over IWCDAN (3.6% higher average accuracy on STL→CIFAR).

---

## Weaknesses

### Fatal
None.

### Major

- **Gap between the theoretical bound and the actual training objective.** Theorem 1 bounds target risk as the sum of source-guided uncertainty, CSSD, Σ(qₖδₖ + pₖγₖ), and the ideal joint risk term. The optimization (Eqs. 12–15) only minimizes source-guided uncertainty and CSSD (via a proxy). The terms Σ(qₖδₖ + pₖγₖ) and the ideal joint risk are "assumed to be small" (line 178) without theoretical or empirical justification. Under the label shifts the paper targets, these terms may not be negligible — if class-conditional supports overlap, δₖ and γₖ need not be small, and if the optimal joint hypothesis incurs non-trivial error on both domains, the ideal joint risk can be large. Furthermore, the bound relies on per-class localized hypothesis spaces H^𝐫¹, H^𝐫², but the algorithm does not enforce any such localization — it trains on the full hypothesis space without per-class source risk constraints. This severs the claimed link that the training process is "precisely based on the proposed target risk bound" (line 50). This is the paper's most significant weakness and limits the strength of its theoretical contribution.

### Minor

- **The distance function in the alignment loss is not specified.** In Eq. 13–14, the alignment loss uses a distance function *d* applied to discriminator outputs *d*(*r*(*s*(*x*)), {*r*(*s*(*x'*))}). The paper never states what this distance is (e.g., absolute difference? squared difference? minimal Euclidean distance to the set?). This ambiguity harms reproducibility, as the alignment loss is a core component of the method.

- **No analysis of pseudo-label quality under severe shift.** The method relies on pseudo-labels to estimate CSSD (Proposition 1), but provides no quantitative analysis of how accurate these pseudo-labels are, especially under severe label shift (α=0.5). Entropy conditioning is mentioned but its effect on pseudo-label quality is not empirically characterized. The reader cannot assess whether the method succeeds *because* of conditional support alignment or *despite* noisy pseudo-labels.

- **Hyperparameter details and baseline retuning unstated.** The paper reports results for a single hyperparameter setting (λ_align, λ_ce, λ_v) without sensitivity analysis. It also states "we adopt the experimental protocol of Garg et al. 2020" without clarifying whether baselines were re-tuned for fairness or scores taken from original papers. This makes it harder to assess whether the reported margins reflect algorithmic superiority or favorable hyperparameter choices.

### Trivial

- None beyond the issues already captured above.

---

## Nice-to-Haves

- A small-scale experiment measuring all components of the Theorem 1 bound (source-guided uncertainty, CSSD, Σ(qₖδₖ + pₖγₖ), ideal joint risk) and checking whether the bound correlates with actual target risk would substantially strengthen the theory-algorithm link.
- A hyperparameter sensitivity study (e.g., varying λ_align) would demonstrate robustness.
- Confusion matrices per domain and per class for each α level would reveal whether improvements are concentrated in certain classes.

---

## Removed Points

These points were raised in the reviews but are removed here because they are factually incorrect, reflect parser artifacts, or are not valid upon cross-checking with the paper.

1. *"Missing variance / standard deviation reporting"* — The paper's tables are included via `\input{figures/big_table_with_variance}`. The filename explicitly indicates variance is included. Since the parser strips input-included files, this criticism stems from an artifact, not the actual submission.

2. *"The remark comparing conditional and marginal bounds assumes supp(P^S_{Z|k}) ⊆ supp(P^S_Z) without discussing cases where subset relations are loose"* — The paper explicitly discusses this trade-off at lines 164–167, noting that Σ_k q_k δ_k ≤ δ precisely because of this subset relation, and that there is a trade-off between the distance term and the sup-norm term. The paper does discuss this.

3. *"VAT loss enforces local Lipschitzness but theory assumes 1-Lipschitz functions — mismatch not discussed"* — The paper explicitly acknowledges this at line 196: "we instead enforce the locally-Lipschitz constraint of the classifier, which is a relaxation of the global Lipschitz constraint." The mismatch is discussed.

4. *"Lemma 1 stated without proof (presumably in appendix)"* — The parser strips appendix sections; proofs exist in the original submission.

5. *"The comparison to CDAN could be expanded"* — This is scope creep; the paper already compares to CDAN empirically and is not required to isolate every theoretical difference.

---

## Novel Insights

The most interesting insight emerging across these reviews is the demonstration that support-based divergence can be more robust than distribution-based divergence under label shift *even when* the distance to per-class supports is theoretically larger than the distance to the marginal support. The paper's Remark 3.2 shows that this increased distance is compensated by a smaller sup-norm term (Σ qₖδₖ ≤ δ), creating a trade-off that can favor the conditional bound in practice. The visualization experiment confirms this: ASA achieves lower Wasserstein distance than CASA (0.63 vs 0.65) but higher CSSD (0.05 vs 0.02) and lower accuracy (93% vs 99%), demonstrating that Wasserstein distance is a misleading metric under label shift while CSSD correlates well with accuracy. This insight — that practitioners evaluating UDA methods under label shift should monitor CSSD rather than Wasserstein distance or MMD — is a practically useful takeaway beyond the paper's specific algorithmic contribution.

---

## Suggestions

1. **Acknowledge and discuss the theory-algorithm gap more transparently.** The paper currently claims the training process is "precisely based on" the bound, which overstates the connection. The ideal joint risk and Σ(qₖδₖ + pₖγₖ) terms are not controlled. A more honest framing — e.g., "the bound motivates the optimization objectives we choose, while the remaining terms are assumed to be small; we verify empirically that the overall approach works" — would be more accurate and would not diminish the contribution.

2. **Specify the distance function *d* used in the alignment loss (Eq. 13–14).** This is necessary for reproducibility. A brief sentence clarifying whether it is absolute difference, squared distance, or another metric would resolve the ambiguity.

3. **Add a small diagnostic experiment on pseudo-label accuracy.** A simple plot showing pseudo-label accuracy on the target domain across training iterations for different α values (e.g., α=10, 1.0, 0.5) would directly address concerns about whether the CSSD proxy is reliable under severe shift.

4. **Provide standard deviations for all main results.** If the tables already include them (as the filename suggests), this is already done — otherwise they should be added. This is standard practice and would allow readers to assess whether the reported margins (especially the modest 0.7% on VisDA-2017) are meaningful.

---

## Score and Decision

The paper makes a genuine contribution: the conditional support alignment idea is well-motivated, the theoretical bound provides new insight into the trade-off between conditional and marginal support alignment, and the empirical results are consistently positive. However, the gap between the theoretical claims and the actual training objective is a significant weakness — the paper overstates the connection between the bound and the algorithm. The missing specification of the distance function and lack of pseudo-label quality analysis are addressable in revision. The paper's core idea and empirical validation are strong enough to warrant acceptance, provided the authors address the theory-algorithm gap in their discussion.

**Originality:** 6/10 — Natural extension of ASA, but the theoretical trade-off analysis adds genuine novelty.
**Importance:** 7/10 — Label shift is an important and underexplored problem in UDA.
**Claims supported:** 6/10 — Empirical claims are well-supported; theoretical claims are somewhat overstated.
**Soundness:** 6/10 — Experiments are reasonable but missing some analyses; theory-algorithm link needs clarification.
**Clarity:** 8/10 — Well-written and clearly motivated.
**Value to community:** 7/10 — Practical method with consistently strong results and theoretical grounding.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>