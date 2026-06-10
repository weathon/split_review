## Summary

This paper proposes Goodie, a hybrid framework for node classification on graphs with partially observed features. It combines Label Propagation (structure branch) and Feature Propagation (feature branch) via a learned scalar attention mechanism, and introduces a pseudo-label contrastive learning loss (PseudoCon) that weights positive pairs by their label-source reliability (ground-truth > mixed > pseudo-only). The paper claims this is the first approach to explicitly and adaptively combine LP and FP embeddings.

## Strengths

- **Adaptive Structure-Feature Attention validated by attention-score trends.** Figure 6 (referenced in text) shows that the attention coefficient on features monotonically increases as more features become available and decreases when features are scarce, directly confirming the claimed automatic weighting behavior (Section 4.2, Eq. 6–7). This is concrete evidence that the mechanism works as designed.

- **Principled three-tier weighting for pseudo-label contrastive learning.** The PseudoCon loss (Eq. 9–10) assigns weights 1, ỹ, and ỹᵢ·ỹₚ to strong/neutral/weak positive pairs, producing the clean inequality chain (Eq. 11): Weak < Neutral ≤ Strong. This is a well-motivated extension of supervised contrastive learning to the semi-supervised setting with pseudo-labels, going beyond a naive application of SupCon.

- **Scalable prototype-based variant reduces contrastive cost from O(N²) to O(|C|²).** The class-prototype formulation (Eq. 12–13) incorporates pseudo-label uncertainty through weighted prototype aggregation, enabling the method to scale to larger graphs like OGBN-Arxiv.

- **Thorough ablation isolating each component.** The text describes ablation studies comparing the attention mechanism against Random, Sum, Mean, and Concat alternatives (Figure 5) and PseudoCon against variants without contrastive learning or with standard SupCon (Figure 7), providing evidence that each proposed component contributes.

- **Motivation grounded in an empirical observation.** Figure 1 demonstrates the core motivating pattern (structure-based models outperform GNN-based models when features are scarce, with the trend reversing when features are abundant) rather than relying on intuition alone.

## Weaknesses

### Fatal
None.

### Major

- **Link prediction is claimed but never evaluated.** Section 3's problem statement explicitly includes link prediction as a task: "we aim to learn a GNN-based decoder, encoder, and classifier that works well on node classification and link prediction." Section 5 describes link prediction split settings (following GCNMF, using GAE). However, **no link prediction results — tables, figures, or discussion — appear anywhere in the paper.** All experimental reporting (Section 5.1, Table 2, Table 3, Figure 8) is exclusively about node classification. This is not a parser artifact; it is a structural gap between the claimed scope and the presented evidence. The method's components (LP logits, FP imputed features, contrastive learning) interact differently under a link prediction decoder, and the reader cannot assess whether Goodie works for this task.

- **Section 5.3 (Sensitivity Analysis) is completely empty.** The heading "5.3 SENSITIVITY ANALYSIS" appears at line 292 with no text, figures, or discussion before "6 CONCLUSION" at line 296. Analysis of key hyperparameters λ (PseudoCon weight), τ (temperature), K (number of LP/FP iterations), D (hidden dimension) — directly relevant to the method's practical utility — is promised but entirely absent.

- **The prose reports almost no concrete numerical results.** The text provides essentially one specific number: a "0.7~4.8% drop" from full features to 100% missing (Table 2). All accuracy values, standard deviations, baseline comparisons, and improvement margins reside in image-only tables and figures (Table 2, Table 3, Figure 5, 6, 7, 8). The prose relies on qualitative statements ("generally performs well," "outperforms those GNN-based models," "survives better than") without anchoring to specific numbers. While the original PDF would render the images, the text itself does not allow a reader to assess the strength of the evidence from the prose alone — a significant presentation gap for a venue requiring self-contained arguments.

### Minor

- **Pseudo-label weighting has an unaddressed vulnerability when LP is confidently wrong.** The weight $w_{ip}$ depends entirely on the maximum softmax probability from the LP branch logits. If LP produces confident but incorrect predictions (which can occur on non-assortative graphs, when LP has not converged usefully, or when the labeled set is very small), the weighting scheme assigns high weight to demonstrably wrong pseudo-labels. The paper acknowledges that pseudo-labels "possess uncertainty" but addresses this only by down-weighting them relative to ground-truth labels; it does not consider the case where the *relative ordering* of confidence is misleading, nor does it provide any mechanism (e.g., confidence thresholding, entropy-based filtering, or consistency regularization) to discard unreliable pseudo-labels. This is a methodological gap that is not discussed or tested.

- **Structure-Feature Attention uses a single scalar per branch per node.** The attention mechanism (Eq. 5) projects the entire D-dimensional embedding onto one learned direction **a** to produce scalar coefficients α_{LP}, α_{FP}. This is a coarse mechanism — it cannot express that some feature dimensions should draw from LP while others draw from FP. The paper does not justify why scalar attention suffices or discuss whether an element-wise gating mechanism would be more appropriate.

- **The Concat baseline is not adequately analyzed in the ablation.** The ablation (Figure 5) shows Attention beats Concat, but Concat followed by a GNN classifier can learn any linear combination of the two embeddings. The paper's explanation — "its implicit way of reflecting still remains challenging" — is vague and does not clarify why the scalar attention mechanism is more expressive than what Concat + GNN can learn.

- **Computational cost is not reported.** Despite noting that full-batch PseudoCon is O(N²) and the scaled version reduces to O(|C|²), the paper reports no actual training times, memory usage, or convergence behavior for any configuration.

### Trivial
None.

## Nice-to-Haves

- Report concrete accuracy values with standard deviations in the prose for a representative subset of datasets and missing rates, so the central claims can be evaluated without consulting figures.
- Include a failure-mode analysis or synthetic experiment for the pseudo-label weighting scheme (e.g., randomly flipping labels to test robustness when LP is confidently wrong).
- Discuss or ablate whether scalar attention suffices vs. more expressive gating mechanisms.

## Removed Points

The following points from the input reviews are removed with justification:

- **Missing training hyperparameters (learning rate, optimizer, weight decay, epochs).** Per instructions, "undisclosed hyperparameters" as reproducibility nitpicks are removed.
- **Figure ordering issues / out-of-order references.** Likely a parser artifact; the original PDF ordering cannot be verified from the extracted text.
- **Claim that empirical observations recapitulate known work.** The paper presents these as motivation for the method, not as novel discoveries; the criticism overinterprets the framing.
- **"GNN-based decoder" language is inflated.** This is a subjective stylistic observation, not a technical weakness.
- **Strength Finder's generic or unsubstantiated strengths.** Strengths about "addressing an important problem" or that are purely sycophantic without specific evidence have been removed.
- **Strength Finder claim that conflicts with verified weakness.** Strength about "empirically demonstrated robustness" is kept but recontextualized with the caveat that the evidence is image-only.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Scope the paper to node classification only**, or deliver the link prediction results. If link prediction under missing features is not evaluated, remove it from the problem statement.
2. **Fill the empty Sensitivity Analysis section** with at minimum analysis of λ, τ, and K. This is expected experimental due diligence for a new method.
3. **Add a paragraph in the prose with representative accuracy numbers** (e.g., Goodie vs. best baseline at mr=0.9999 and mr=0 on Cora, CiteSeer, PubMed) so a reader can verify the central claim without consulting figures.
4. **Add a discussion of the pseudo-label confidence failure mode**, even if brief, and ideally a robustness test.

## Score and Decision

The paper addresses a well-motivated problem with a sensible method and preliminary ablation evidence. However, the submission in its current form has three structural and evidential issues that prevent acceptance: (1) link prediction is claimed in the problem statement but entirely unevaluated, (2) the promised sensitivity analysis is an empty heading with no content, and (3) the prose lacks virtually any concrete numerical results — all comparisons reside in image-only tables and figures that the text does not summarize numerically. These gaps are addressable in revision but make the current submission incomplete as a self-contained argument for a top venue. The core ideas are reasonable, and with substantial revision to fill these gaps the paper could become a strong contribution.

**Score: 3.0** — The paper has significant gaps in presentation and scope fulfillment that prevent acceptance in current form, though the core approach is sound.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>