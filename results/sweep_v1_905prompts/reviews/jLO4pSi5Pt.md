Now I have sufficient calibration data. Let me write the final consolidated review.

## Summary

This paper formulates and tackles a new problem: long-tailed test-time adaptation (LT-TTA) for Vision-Language Models. It identifies two VLM-specific failure modes (text-induced tail erosion and modality-bias amplification) and proposes L-TTA, combining three co-designed mechanisms — Synergistic Prototypes (DPs + EPs), Rebalancing Shortcuts (RSs) with a class re-allocation loss, and Balanced Entropy Minimization (BEM). Experiments span 15 datasets across OOD, cross-domain, and corruption benchmarks under three imbalance ratios (10, 20, 50), with consistent improvements in both accuracy and macro-F1 over 12 baselines.

## Strengths

1. **First principled study of VLM-specific failure modes in long-tailed TTA.** The paper identifies two problems—Text-induced Tail Erosion and Modality-bias Amplification (Figure 1b)—that go beyond what generic LT or TTA methods consider. The components (SyPs, RSs, BEM) are explicitly designed to counter these problems, giving the method a clear motivation.

2. **Consistent SOTA across an extensive evaluation suite.** Tables 1–3 report results on 15 datasets, three benchmarks (OOD, cross-domain, corruption), and three imbalance ratios (10, 20, 50), with 12+ baselines. L-TTA outperforms the next best method on nearly all settings. On the OOD average at imb=10, it improves over DPE by +1.5% accuracy and +3.6% macro-F1. The gains are largest at the most imbalanced settings.

3. **Ablation confirms each component contributes.** Table 6 shows that removing either DP or EP drops macro-F1 by ~3–4%, removing RS hurts by ~0.7–1%, and adding BEM yields a further ~0.6–0.7% gain. This demonstrates the synergy the paper claims.

4. **Generality across backbones.** Table 5 reports consistent gains on ViT-L/14, ViT-H/14, SigLIP-L/16, and MetaCLIP-BigG (~1.5% Acc, ~1.8% Mac. on average), showing the approach works beyond the default ViT-B/16.

5. **Favorable efficiency.** Table 4 shows L-TTA achieves 1.45h runtime and 1.89G memory (similar to lightweight methods like DPE and TDA) while producing the highest harmonic mean on LT-CDB (67.20 vs. 66.31 for DPE).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Undefined notation in BEM formulation.** In Equation (9), the term $\tilde{\mathbb{P}}$ is used but never explicitly defined. From context it is clear that $\tilde{\mathbb{P}} = \sigma(z)$ (the original softmax predictions), but this should be stated directly. The paper would also benefit from stating the assumptions behind Propositions 1–2 in the main text rather than deferring all theoretical support to the appendix.

2. **Inconsistent and ambiguous hyper-parameter for hyper-class vectors.** Implementation details state $K=0.3$, but $K$ is described as the number of hyper-class vectors, an integer quantity. The ablation section uses $b$ (from 0.2 to 1.0) and reports $K=0.2$ as best, which contradicts the default $K=0.3$. This suggests $K$ is actually a scaling factor (e.g., $K\times C$ or a proportion), but the paper is not clear. This ambiguity harms reproducibility.

3. **No error bars or variance estimates.** The paper reports five-run averages in Tables 1–3 but no standard deviations. Given the synthetic long-tailed sampling, variance may be non-negligible, and confidence intervals would help assess significance.

### Trivial

1. The EP update in Equation (5) uses $(N_{c,s}^{\text{EP}} - \phi_c)$ as a weighting factor, which is non-standard for an EMA. While the formulation is mathematically valid, its relationship to a standard momentum update could be clarified with a brief note.

## Nice-to-Haves

- The paper could compare against a simple "reweighted entropy" baseline (e.g., applying TPT or DPE with class-weighted or logit-adjusted entropy) to more directly attribute gains to the specific BEM design rather than to any class-imbalance correction. This would strengthen the claim that the exact form of BEM matters, but its absence does not invalidate the paper's contributions since extensive ablations already isolate BEM's role.

- A brief analysis of what the EP prototypes actually capture (e.g., nearest-neighbor visualization or t-SNE of stored features) would help readers understand why the unusual update rule works. The empirical ablation already shows EP helps substantially, so this is a nice-to-have rather than a requirement.

- A discussion of sensitivity to early inaccurate class-prior estimates would be welcome, since the method updates $\pi$ online from pseudo-labels.

## Removed Points

- "The Corruption Benchmark only uses gaussian noise": The paper explicitly states that 16 corruption types are in Appendix J. The appendix is stripped by the parser and exists in the original submission. This is a parser artifact, not a paper deficiency.

- "Missing baseline: reweighted version of existing TTA": While a reasonable suggestion, the paper already compares against 12+ baselines and ablates each component individually. A reweighted baseline would be informative but is not required to validate the core claims; the paper's ablation study (Table 6) already separates the contribution of BEM from the prototypes and shortcuts.

- "EP may add noise instead of enriching tail classes": This is speculative. The ablation in Table 6 empirically demonstrates that EP improves performance by ~3–4% macro-F1. The concern is not borne out by the evidence.

- "Efficiency comparison not fully controlled": The paper does not claim a perfectly controlled comparison; it reports facts (runtime, memory, HM) and notes which methods are training-free. This is standard practice and not a flaw.

- "Propositions deferred to appendix": Common practice in conference papers due to space constraints. Not a weakness per se, though the main text could state the key assumptions.

- "The paper should test on other VLM architectures": Already done in Table 5 (SigLIP, MetaCLIP).

- "Figure 1(b) is presented as evidence without a proper controlled experiment": The figure is a motivating illustration, not a controlled experiment. The paper's actual evidence comes from the extensive Tables 1–3.

- "BEM may be circular / poorly specified": $\tilde{\mathbb{P}}$ is inferable from context as $\sigma(z)$. The reviewer's concern about circularity is not substantiated by the actual equations.

- Various formatting/style nitpicks and complaints about content relegated to the appendix are removed per protocol.

## Novel Insights

The paper's key insight — that VLM test-time adaptation under long-tailed streams suffers from two distinct VLM-specific failure modes (text-induced erosion and modality-bias amplification) that generic LT-TTA methods cannot address — is genuinely novel. The design of Exclusionary Prototypes that update *all* classes from every view (not just the predicted class) is an elegant solution to the tail-class under-representation problem. The idea of penalizing confident classes in the entropy gradient via a prediction-confidence-weighted logit adjustment (BEM) is also a clean adaptation of standard logit-adjustment ideas to the unique unsupervised, single-epoch setting of TTA.

## Suggestions

1. Define $\tilde{\mathbb{P}}$ explicitly after Eq. (9): "where $\tilde{\mathbb{P}} = \sigma(z)$ are the original softmax predictions."
2. Clarify whether $K$ (the number of hyper-class vectors) is a raw count or a proportion of $C$, and reconcile the implementation default ($K=0.3$) with the ablation finding ($K$ = 0.2 best).
3. Add standard deviations or confidence intervals to the main tables.
4. State the core assumptions of Propositions 1–2 in the main text (even if proofs remain in the appendix) so readers can assess the theoretical claims without cross-referencing.

## Score and Decision

**Round-1 bracket**: After reading the paper and retrieving calibration anchors in three bands (weak: ~2.5–3.0, middle: ~4.4–7.0, strong: 8.0), I placed this paper in the middle band (3.5–7.5).

**Round-2 narrowing**: I retrieved anchors within (4.5, 6.5) and (6.0, 7.5). The most relevant anchors are:

| Anchor | Score | Decision | Comparison |
|---|---|---|---|
| DOTA (yD2JMeKumt) | 6.0 | Reject | Similar TTA+prototype approach but distribution estimation is unclear; L-TTA has stronger experiments and clearer motivation. L-TTA is clearly better. |
| BLG (BUDxvMRkc4) | 4.67 | Reject | Long-tailed CLIP but not TTA; limited novelty. L-TTA is substantially stronger. |
| BEM Multi-label (75PhjtbBdr) | 6.25 | Accept | Similar paper structure (new TTA sub-problem + tailored loss); L-TTA has more comprehensive experiments but comparable overall quality. L-TTA is slightly stronger. |
| RLCF (kIP0duasBb) | 6.67 | Accept | Broad task coverage but incremental technical contribution. L-TTA has clearer novelty and comparable experimental rigor. Similar tier. |
| "Entropy is not Enough" (9w3iw8wDuE) | 7.0 | Accept | Stronger theory but narrower empirical scope. L-TTA is weaker on theory but broader empirically. Slightly below. |

L-TTA sits between the 6.25 (BEM multi-label) and 6.67 (RLCF) anchors — it is stronger than the former in experimental breadth and comparable to the latter in overall rigor. The paper's weaknesses are presentation/clarity issues rather than fundamental flaws, and the empirical contribution is substantial. I therefore assign **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>