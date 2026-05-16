Now I have a thorough understanding of the paper and can verify the reviewer claims. Let me compose the final consolidated review.

## Summary

This paper proposes a two-step test-time adaptation (TTA) framework for graph neural networks. First, it adapts BN layer statistics (mean and variance) via a data-driven weighting factor computed from JS divergence between activation distributions, combined with a learnable mask matrix for selective dimension-wise adjustment. Second, it refines BN scale/shift parameters using a joint energy-based model with entropy-based and confidence-based pseudo-label filtering. Experiments across seven datasets and three backbone architectures show consistent improvements over seven TTA baselines.

## Strengths

1. **Novel two-step BN adaptation decomposition**: The paper correctly identifies that prior TTA methods adjust only BN statistics (μ, σ²) while leaving γ, β unchanged, which may be suboptimal when statistics shift significantly. Splitting adaptation into BNSA (statistics) then BNPA (parameters) is a principled structural contribution, validated by the ablation where removing either step degrades performance (Section 3, Table 2).

2. **Data-driven weighting via JS divergence**: Instead of a fixed or grid-searched α, the method computes per-dimension weights from the JS divergence between training and test activation distributions (Eq. 3–4). This provides a principled, instance-specific adaptation weight without manual tuning. The ablation confirms that replacing this with a fixed weight harms performance (Section 4.2).

3. **Learnable mask for selective adaptation**: The differentiable mask matrix M (via Gumbel-Max trick) enables per-dimension control over which BN statistics to adjust, going beyond uniform weighting. The ablation (Table 2) and the model collapse analysis on FB-100 (Fig. 3) support its effectiveness.

4. **Strong empirical breadth**: The method achieves best or second-best accuracy on 7 datasets × 3 backbone architectures, with notable margins (e.g., +2.84% on Cora with GCN, +2.60% on Elliptic with GraphSAGE). The evaluation covers diverse distribution shifts (covariate, class-prior, full-distribution) and both transductive and inductive settings.

5. **Systematic ablation**: Table 2 isolates each component (A, M, SGLD selection, entropy/confidence filtering, removal of either main step), showing consistent degradation when any is removed. This validates the design choices incrementally.

## Weaknesses

### Fatal
None.

### Major

1. **Computational feasibility of the α computation is unaddressed (Eq. 4)**: Equation 4 defines α^{(i,d)} as the average JS divergence over **all pairs** of training and test instances: (1/(|D_tr|·|D_te|)) Σ Σ JS(P_m||P_n). For datasets like OGB-Products (2.4M nodes) or OGB-Arxiv (170K nodes), a literal pairwise computation would be O(|D_tr| × |D_te| × L × D), which is prohibitive. The paper mentions storing "a small histogram matrix" (line 29) and computing P_m only at the final training epoch (line 107), which hints at a practical approximation (e.g., aggregated histograms), but the paper never explains how Eq. 4 is actually implemented in practice. This is the most significant gap: the method description and the implementation are inconsistent, and a reader cannot determine whether the proposed approach is tractable on the very datasets used in the experiments. The authors should clarify the practical computation (e.g., aggregated histograms per dimension, minibatch approximation) and report runtime comparisons.

2. **Calibration claims are unsupported by quantitative evidence**: The paper claims improved calibration in the abstract, contribution list (line 27), Section 3.2 motivation, Section 4.2 (line 255), and conclusion, yet reports **no calibration metric** (ECE, reliability diagrams, or similar) anywhere in the visible text. The EBM component is motivated largely by calibration improvement (lines 161, 255), but the only support provided is a mention of "Section 4.4" (line 255) which is absent from the extracted text. Without a calibration evaluation, this central claim is unsubstantiated. The authors should report ECE or a comparable metric on at least a subset of datasets.

### Minor

3. **Non-parametric density estimation method is unspecified**: The paper repeatedly mentions "non-parametric density estimation" to obtain P_m and P_n (line 95) and "a small histogram matrix" to store distributions (line 29), but never specifies the technique (e.g., equal-width histogram with how many bins? KDE with what kernel/bandwidth?). This matters because the granularity of the density estimate directly affects the JS divergence values and thus α. The per-dimension estimation also assumes feature independence (each dimension's histogram is computed separately), which is likely violated in high-dimensional GNN embeddings — this is not discussed.

4. **Several hyperparameters are introduced without values or sensitivity analysis**: Gumbel temperature τ (Eq. 5), SGLD step size δ and step count T (Eq. 13), entropy threshold τ_e, probability thresholds τ_c^1 and τ_c^2 (Eq. 19–20), contrastive loss temperature (Eq. 7), KL penalty λ (Eq. 8), and the number of decay steps k (Eq. 9) are all defined as variables without numerical guidance. While some of these may appear in a stripped appendix, the main text should provide at least the values used or a reference to a specific appendix section.

5. **Baseline adaptation to graph data is not explained**: a-BN and DUA were originally designed for image classifiers with BN layers where batch statistics are computed over image batches. The paper does not state how these baselines were adapted to GNNs (e.g., do statistics aggregate over nodes or graphs? What constitutes a "batch" for node-level predictions?). Since BN operates differently in graph settings, this omission weakens the reproducibility of the comparison.

6. **No limitations discussion**: The conclusion (Section 5) is four sentences and does not acknowledge any limitations — such as the added computational cost of SGLD sampling, the dependence on histogram-based density estimates, the need to access training activation distributions, or the sensitivity to the introduced thresholds. The paper would be strengthened by a brief limitations paragraph.

### Trivial
- Figure 1 caption reads "Batch normalization parameter adaptation and batch normalization parameter adaptation" — clearly a duplicate; it should reference "statistic adaptation" for part (a) and "parameter adaptation" for part (b).
- The Gumbel-Max trick formulation in Eq. 5 uses sigmoid((log δ − log(1−δ) + B)/τ), which is the Gumbel-Softmax for Bernoullis, but the standard notation is typically softmax over two classes. This is workable but could confuse readers familiar with the standard formulation.

## Nice-to-Haves

- **Runtime comparison**: Given the added complexity (SGLD sampling, contrastive learning for the mask, density estimation), a wall-clock time comparison with baselines would help readers assess the practical cost-benefit trade-off.
- **Comparison with simpler ablated baselines**: The ablation removes one component at a time. An additional baseline using "BNSA-only with uniform α" (no JS divergence weighting) would more cleanly isolate the contribution of the data-driven α.
- **Transductive vs. inductive distinction**: The paper could clarify how the method handles transductive (e.g., Cora) vs. inductive (e.g., OGB-Products) settings, since the availability of test nodes during training differs.

## Removed Points

These points were raised by reviewers but removed after cross-checking against the paper:

- **"Incoherent mask learning description / circularity"** (Harsh Critic #2): The paper's description of mask learning (lines 111–137) is coherent: the mask M (through A⊙M) is applied in the forward pass via Eq. 6, then the KL divergence is between original model predictions (p) and mask-adjusted model predictions (q). There is no circularity — the mask parameters B are optimized via standard gradient-based learning on loss L_BNSA. The critic's confusion appears to stem from a misreading. The description could be clearer, but it is not "incoherent" or "impossible to implement."

- **"Grammatically broken sentence" about BN theory**: The sentence "BN demonstrates strong empirical performance. However, a comprehensive theoretical understanding of its underlying mechanisms is acknowledged" (line 81) is grammatically correct and logically conveys that there is no consensus on why BN works. This is a nitpick.

- **"No error bars" claim**: The paper states results are averaged over 10 runs (line 229, 239). The table (Table 1) is an image stripped by the parser, and it likely contained standard deviations. This is a parser artifact.

- **"EBM loss not obviously tied to calibration"**: The JEM formulation (Eq. 10–14) is a well-known approach from Grathwohl et al. (2020) explicitly designed to improve calibration through joint energy modeling. Whether one agrees with the philosophy is a matter of taste, not a weakness of the paper — though the paper should indeed support the calibration claim with metrics (see Major weakness #2).

- **"Dataset/domain breadth" complaints**: Demanding the paper cover additional graph domains, methods, or tasks beyond its stated scope (7 datasets, 3 backbones, 7 baselines) is scope creep. The existing evaluation is already substantial.

## Novel Insights

The harsh critic identifies two important tensions that the paper does not fully resolve: (1) the JS divergence-based α computation as written is intractable for large datasets, and the gap between the formal definition (pairwise sums) and a tractable implementation (aggregated histograms) needs explicit bridging; (2) the calibration motivation for the EBM component runs ahead of the evidence — the paper leans heavily on calibration as a justification but provides only accuracy results. These are genuinely insightful observations that point to specific, fixable gaps rather than fundamental flaws.

The strength finder's observation that the mask's effectiveness "extends beyond accuracy improvements" (line 255) hints at calibration benefits that Section 4.4 (stripped) apparently explores, but without it, the paper's own evidence for this claim is invisible to the reader.

## Suggestions

1. **Clarify the α computation**: Replace Eq. 4 or add a paragraph explaining the practical implementation. If aggregated histograms are used, state this explicitly and explain whether the JS divergence is computed between the aggregated training histogram and per-test-batch histograms, or some other approximation. Add a runtime breakdown showing the method is tractable on OGB-Products/Arxiv.

2. **Add calibration metrics**: Report Expected Calibration Error (ECE) or reliability diagrams for the proposed method vs. top baselines on at least 2–3 datasets. This is necessary to substantiate the claimed calibration improvement, which is a core motivation for the EBM component.

3. **Specify the density estimation method**: Name the technique (e.g., equal-width histograms with M bins) and state how bins are set. Discuss (or at least acknowledge) the per-dimension independence assumption.

4. **Include a limitations paragraph or table**: Acknowledge the added computational cost of SGLD, the dependence on histogram granularity, and any sensitivity to the introduced thresholds (τ_e, τ_c^1, τ_c^2). This would significantly strengthen the paper's scientific rigor.

5. **Add a pseudocode algorithm**: A one-page algorithm box showing the exact flow — (a) compute A from JS divergence, (b) optimize B via contrastive + KL loss, (c) derive M*, (d) decay statistics via Eq. 9, (e) optimize γ, β via L_BNPA — would immediately resolve any remaining clarity concerns about the two-step process and the mask learning.

## Score and Decision

This paper presents a well-motivated framework with a novel decomposition of BN adaptation for GNN TTA, supported by strong empirical results across diverse settings. The core contributions are real and the evaluation is extensive. The major weaknesses — the unaddressed computational gap in Eq. 4 and the unsupported calibration claims — are fixable with clarifications and additional analysis. The method description, while not "incoherent" as the harsh critic claimed, could be significantly improved with a pseudocode or more explicit implementation details. The paper is above the acceptance threshold but should address these issues before publication.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>