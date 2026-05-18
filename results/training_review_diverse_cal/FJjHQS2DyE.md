Now I have a thorough understanding of the paper, the reviews, and have verified the relevant claims against the text. Let me now produce the final consolidated review.

---

## Summary

This paper proposes Conditional Adversarial Support Alignment (CASA) for unsupervised domain adaptation under label shift. The key idea is to align the *conditional* supports of feature distributions (given class labels) rather than the marginal supports as done in prior work (ASA). The authors derive a novel target risk bound based on Conditional Symmetric Support Divergence (CSSD, Theorem 1), and propose a practical training scheme using pseudo-labels and an entropy-conditioning filter to approximate CSSD minimization. Experiments on three benchmark datasets under simulated label shift show consistent improvements over 12 baselines, with CASA achieving the highest average accuracy on 11 of 15 transfer tasks.

## Strengths

1. **Novel and well-motivated conditional support alignment formulation.** The paper identifies a genuine limitation of marginal support alignment (ASA) — that aligning marginal feature supports can be insufficient when label distributions shift — and introduces CSSD to explicitly align class-conditioned supports. Figure 1 provides clear intuition. This is a principled extension of the support alignment direction in UDA.

2. **Novel theoretical target risk bound (Theorem 1).** The paper derives an upper bound on target risk that incorporates CSSD, grounded in the Integral Measure Discrepancy framework. Lemma 1 shows how IMD can be bounded by CSSD. While the comparison to the marginal SSD bound (Remark 2) reveals a trade-off rather than strict dominance, the bound itself is a valid and useful theoretical contribution that justifies the CSSD approach.

3. **Consistent and practically meaningful empirical gains.** Across three datasets (USPS→MNIST, STL→CIFAR, VisDA-2017) and five label-shift levels, CASA achieves the highest average accuracy in 11/15 tasks. Under the most severe shift (α=0.5), CASA outperforms the second-best method by 3.6%, 1.6%, and 0.7% on the three datasets respectively. The method is also competitive under no label shift, unlike several label-shift-specific baselines.

4. **Principled proxy for CSSD via joint support alignment (Proposition 1).** The equivalence between conditional support divergence and joint support divergence (over Z⊗Ŷ) provides theoretical grounding for the practical objective without requiring explicit label distribution estimation as in importance-weighting approaches.

5. **Ablation study confirming the contribution of each loss component.** The text reports that removing any of ℒ_align, ℒ_ce, or ℒ_v degrades performance across different label shift levels, verifying that all designed losses contribute to robustness.

## Weaknesses

### Fatal
None.

### Major

1. **Pseudo-label confound in the central empirical comparison.** The key empirical claim is that conditional support alignment (CSSD) outperforms marginal support alignment (SSD). However, CASA uses pseudo-labels + entropy conditioning to estimate class membership, while ASA — the closest marginal-support baseline — does not use pseudo-labels. This means the observed improvement could be partially (or entirely) due to the pseudo-label signal rather than the conditional nature of the alignment. The comparison against IWCDAN (which also uses pseudo-labels for conditional *distribution* alignment) provides partial control, but does not isolate the specific question of CSSD vs SSD with matched pseudo-label usage. An ASA variant augmented with the same pseudo-labeling scheme (ASA+pl) is the cleanest missing baseline. Without it, the paper's central empirical claim that "conditional support alignment is more robust than marginal support alignment" is not fully disentangled from "pseudo-labels help." This is an addressable gap, but it weakens the evidence for the core contribution in the current submission.

2. **Minimal discussion of why related conceptually close methods underperform.** PCT (prototype-based alignment) is conceptually related to conditional alignment — it aligns class-level prototypes — but the paper reports results without any analysis of why CASA outperforms it. A brief discussion of the relationship and key differences would strengthen the paper's positioning and help the reader understand where the improvement comes from.

### Minor

1. **The theoretical comparison between CSSD and SSD bounds is a trade-off, not a resolution.** Remark 2 correctly identifies that one term in the CSSD bound is larger than its SSD counterpart while another is smaller, concluding there is a "trade-off." The paper is transparent about this, but it means the theory provides motivation rather than a guarantee that CSSD is strictly preferable to SSD. The empirical results carry the weight that the theory cannot settle. The paper would benefit from either identifying a specific condition under which the CSSD bound is tighter, or being more explicit that the theoretical contribution is the CSSD bound itself (which justifies the approach), not the comparison to SSD.

2. **Proposition 1's ideal-case equivalence overstates the proxy guarantee.** The proposition states that D^c_supp(P^S_{Z|Y},P^T_{Z|Y}) = 0 iff D_supp(P^S_{Z,Ŷ},P^T_{Z,Ŷ}) = 0, conditional on P^S(Ŷ=y)>0 and P^T(Ŷ=y)>0. The text describes this as demonstrating that the joint support divergence "can be used to estimate" the conditional divergence. However, the equivalence depends on Ŷ being sufficiently accurate — if pseudo-labels are noisy, joint alignment with Ŷ does not imply conditional alignment with true labels. The paper uses entropy conditioning to mitigate this, which is reasonable, but the proposition itself is presented without this caveat. Rephrasing it as a motivating approximation in the ideal case (where Ŷ≈Y) would be more accurate.

3. **The positivity assumption on pseudo-label class proportions may fail under extreme label shift.** The proposition requires P^S(Ŷ=y) > 0 and P^T(Ŷ=y) > 0 for all y. Under severe label shift (α=0.5), the target may have near-zero probability for some classes, and the entropy-conditioning filter could produce no pseudo-labeled samples for that class, violating the assumption. This is a practical concern worth discussing or addressing.

4. **The inf_{h∈H^r²} ℒ_S(h)+ℒ_T(h) term in Theorem 1 is assumed small but not discussed.** This "ideal joint risk" term is common in DA bounds, but the paper does not comment on how small it needs to be for the bound to be informative, nor whether the optimization procedure implicitly reduces it. This is a standard gap in adaptation theory but deserves at least an acknowledgment.

### Trivial
None.

## Nice-to-Haves

- A sensitivity study of the entropy conditioning threshold used for pseudo-label filtering would increase confidence in the method's robustness.
- A sensitivity plot for the four loss weights (λ_align, λ_y, λ_ce, λ_v) across a reasonable range would strengthen the practical contribution.

## Removed Points

These points were flagged during review but have been removed for the following reasons:

- **Criticism about missing standard deviations / confidence intervals.** The table is included via `\input{figures/big_table_with_variance}` — the filename itself indicates variance is reported. The reviewer's inability to see the table is a parser limitation.
- **Criticism about missing reproducibility details** (architectures, hyperparameters, optimization settings). Implementation details are conventionally placed in the supplementary material, which the parser strips from all papers. These details exist in the original submission.
- **Criticism that Proposition 1 is "questionable."** The proposition is mathematically valid under its stated conditions (P(Ŷ=y)>0, well-defined distance). The practical concern about pseudo-label accuracy is real and is addressed above as a minor weakness about framing, but the proposition itself is not mathematically flawed.

## Novel Insights

The most interesting observation that emerges from the reviews — beyond the paper's own contributions — is the unresolved tension between theoretical grounding and practical evaluation in support alignment under label shift. The paper transparently shows that its CSSD bound involves a trade-off with the SSD bound (one term larger, one term smaller), yet the empirical results consistently favor CASA. This suggests the real advantage may not come from a uniformly tighter bound, but rather from the fact that conditioning on classes imposes a useful inductive bias — forcing the alignment to respect class structure — even when the bound analysis cannot prove dominance. The pseudo-label confound underscores a broader challenge in this sub-area: methods designed for label shift almost unavoidably incorporate label estimates (pseudo-labels, importance weights, or prototype assignments), making it difficult to isolate which component (the alignment objective vs. the label estimation mechanism) drives improvement. A controlled comparison that matches the auxiliary machinery across baselines would substantially clarify the source of gains.

## Suggestions

1. **Add an ASA+pl baseline.** Augment ASA (marginal support alignment) with the same pseudo-labeling and entropy-conditioning scheme used in CASA. If CASA still outperforms ASA+pl, the claim that CSSD > SSD (conditional > marginal) is strongly supported. If performance is similar, the contribution is better described as "support alignment benefits from pseudo-labels," which is a different (and less novel) message. Either outcome is informative and would improve the paper.

2. **Sharpen the theoretical narrative.** Be explicit that the CSSD bound (Theorem 1) justifies aligning conditional supports as a *valid* approach (i.e., reducing CSSD provably reduces the target risk bound), without claiming it is provably tighter than the SSD bound. Let the empirical evidence speak to the comparative advantage. This would avoid overclaiming while preserving the theoretical contribution.

3. **Acknowledge the pseudo-label accuracy assumption in Proposition 1.** Add a sentence clarifying that the equivalence holds when pseudo-labels are sufficiently accurate (which the entropy conditioning aims to ensure), and that the proposition is best understood as a theoretical motivation for the proxy objective.

4. **Add a brief analysis comparing CASA to PCT.** Since both methods incorporate class structure during alignment, explaining why CASA's support-based approach differs from PCT's prototype-based approach would help readers place the contribution.

## Score and Decision

The paper proposes a reasonable and well-motivated extension of support alignment to the conditional case, with a novel theoretical risk bound and consistent experimental improvements. The main weakness — a confound between conditional alignment and pseudo-label usage in the comparison to ASA — is real but addressable, and the method's superiority over IWCDAN (which also uses pseudo-labels) partially mitigates it. The theoretical contribution is incremental but solid, and the writing is clear. With the pseudo-label confound properly addressed, this would be a solid paper.

**MY FINAL SCORE:** <pineapple>6.0</pineapple>
**MY FINAL DECISION:** <orange>Accept</orange>