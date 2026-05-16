Here is my consolidated meta-review.

---

## Summary

This paper proposes FIRM (Focused In-distribution Representation Modeling), a multi-positive contrastive loss for anomaly detection. The key idea is to encourage compact clustering of in-distribution (ID) representations by treating all ID samples in a minibatch as positives for each other, while preserving diversity among synthetic outliers by keeping a single-positive strategy for them. Experiments on CIFAR-10/100, Fashion-MNIST, and Cats-vs-Dogs show that FIRM outperforms NT-Xent and SupCon under controlled conditions, and achieves competitive or state-of-the-art results when compared with prior methods on standard benchmarks and unlabeled multiclass OOD detection tasks.

---

## Strengths

1. **Well-motivated and principled objective design.** FIRM is a clean, intuitive modification to contrastive learning that directly addresses known limitations of NT-Xent (excessive intraclass variance) and SupCon (forcing outlier collapse) for anomaly detection. The loss landscape visualization (Figure 1) provides mechanistic grounding showing that FIRM's minima lie in regions of high ID similarity and low outlier similarity, while NT-Xent and SupCon each collapse one of these axes.

2. **Controlled ablation studies isolate the loss function's impact.** Table 4 directly compares NT-Xent, SupCon (binary), SupCon (multiclass), and FIRM under identical conditions (same encoder, scoring, outlier sources). FIRM consistently yields the highest AUROC and AULC across all four datasets, with relative improvements over NT-Xent ranging from ~11% to ~20%. This is the strongest evidence for the paper's central claim, as it eliminates confounding factors from different training pipelines.

3. **Strong empirical performance across benchmarks.** On CIFAR-10, FIRM with outlier exposure achieves 97.9% mean AUROC, substantially outperforming prior contrastive methods such as DROC (93.3%) and CSI (94.3%). Similar gains are observed on CIFAR-100 (83.4% vs. DROC 73.1%) and Fashion-MNIST (97.7% vs. CSI 94.9%). The method also generalizes effectively to unlabeled multiclass OOD detection (Table 3), setting competitive results on LSUN, ImageNet, and other OOD benchmarks.

4. **Robustness across scoring methods.** FIRM maintains strong performance whether using cosine similarity to k-NN ($s_{\text{con}}$), rotation ensembles ($s_{\text{shift}}$), or full ensembles with crops ($s_{\text{ens}}$). On CIFAR-10, FIRM $s_{\text{con}}$ (94.1%) already surpasses CSI $S_{\text{shift}}$ (94.3%), demonstrating that the learned representations are not brittle to the choice of detector.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Missing variance estimates in result tables.** The paper states (line 103) that results are averaged over five runs with standard deviation, but Table 1 and Table 4 appear to report only point estimates without standard deviations. Without these, readers cannot judge whether reported improvements are statistically significant. This is the single most consequential weakness in the paper — adding standard deviation bars (or confidence intervals) to all tables reporting the paper's own results is necessary for the claims to be properly assessed.

2. **Uncontrolled heterogeneity in inter-paper comparisons (Table 1).** Table 1 compares FIRM against numbers taken from prior papers (DROC, CSI, etc.). While the paper uses ResNet-18 throughout, other factors that can strongly affect AUROC — training epochs, batch size, temperature, the $k$ for nearest-neighbor scoring, data augmentation pipelines, and training protocols for the projection head — are not guaranteed to match. For example, CSI uses $k=1$ for $s_{\text{con}}$ and $k=10$ for ensemble scores, while FIRM is reported with $k=5$ (Table 1 caption). This weakens the headline claim of superiority. The controlled ablation in Table 4 partially mitigates this concern, but the paper should either reproduce the strongest baselines under identical conditions or explicitly discuss which hyperparameters differ and why the gap cannot be explained by those differences.

3. **Incomplete experimental details in the main text.** The paper does not report basic training specifications such as the number of epochs, learning rate schedule, optimizer, batch size, temperature ($\tau$), or the specific augmentation transformations used for ID and synthetic outlier samples. While the appendix may contain these, the main text should at minimum summarize the key settings for reproducibility.

### Trivial

1. **The term "AULC" is introduced (Table 4 caption, line 129) without definition.** The reader needs to know exactly how this metric is computed and what it is intended to measure beyond the standard final AUROC.

2. **The choice of $k=5$ for the primary detection score $s_{\text{con}}$ is not justified.** The paper uses $k=1$ in the ablation studies (Table 4) but $k=5$ in the main results (Table 1 caption). A brief justification for this choice would help.

3. **The text contains a minor reference inconsistency.** Line 113 says "Similar trends are observed in other datasets (Tables 1 (a), (b), and (c))" while Cats-vs-Dogs results appear in panel (d). The surrounding discussion does cover Cats-vs-Dogs, so this is simply a typographical oversight.

---

## Nice-to-Haves

- **A dedicated Limitations section.** The paper ends with a generic conclusion. A few sentences on sensitivity to the quality of synthetic outliers, to the homogeneity of the ID distribution, or to the choice of $k$ would strengthen scientific honesty and provide practical guidance.
- **A brief analysis of when the multi-positive strategy might hurt**, e.g., if the ID is highly multimodal (as in the unlabeled multiclass OOD setting) or if batch sizes are very small.
- **An explanation for why ensemble scores ($s_{\text{shift}}, s_{\text{ens}}$) do not improve over $s_{\text{con}}$ on Fashion-MNIST and Cats-vs-Dogs.** The paper notes this behavior (line 113) but offers no comment — a short hypothesis would make the presentation more complete.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about CutPaste/NSA mention without defect detection experiments.** The paper mentions CutPaste and NSA as examples of synthetic outlier generation techniques but explicitly states (line 39) "our focus is not on comparing these synthetic outlier generation techniques" and scopes the paper to semantic anomaly detection. This does not create an unfulfilled expectation; the paper is clear about its scope. (Rule: REMOVE weakness based on misreading or evaluating against wrong class of expectations.)

- **Criticism about missing appendix content.** The reviewer notes that experimental details "may be in the appendix." The parser strips appendix sections from all papers. The paper states it follows established methodologies from prior works. This criticism reflects a known artifact of the review format, not an author error. (Rule: REMOVE weaknesses about missing appendix/proofs/content stripped by the parser.)

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Add standard deviations (or confidence intervals) to all tables reporting the paper's own results** (Tables 1 and 4). This is the single highest-priority fix.
2. **Provide a short hyperparameter summary table in the main text** listing epochs, batch size, temperature $\tau$, optimizer settings, and augmentation details for each dataset.
3. **For Table 1, either reproduce the strongest baselines (DROC, CSI) under FIRM's own training conditions, or clearly enumerate which hyperparameters differ across methods and argue that the differences cannot explain the observed performance gap.** The controlled ablation in Table 4 already provides strong evidence, so this would further strengthen the headline claims.
4. **Define AULC explicitly** and explain what additional information it provides beyond final AUROC.
5. **Add a brief justification for $k=5$ vs $k=1$** in the detection score section.

---

## Score and Decision

This paper makes a solid, well-motivated incremental contribution. The FIRM loss is a simple but effective modification to contrastive learning for anomaly detection, and the controlled ablation studies provide strong internal validation. The weaknesses are all fixable — missing variance estimates and incomplete hyperparameter reporting are presentation issues rather than structural flaws. The uncontrolled confounds in the inter-paper comparison are partially mitigated by the controlled ablation, and the core contribution remains convincing. The paper is clearly written and the code is provided.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>