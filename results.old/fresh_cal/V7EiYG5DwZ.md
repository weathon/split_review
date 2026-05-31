Now I have all the information needed to verify the reviewer claims against the actual paper. Let me write the consolidated review.

## Summary

This paper introduces a probabilistic graphical model (PGM) perspective on transformer-based Sparse Mixture-of-Experts (SMoE), revealing that standard SMoE routing makes a conditional independence assumption across tokens' expert selections. To address the resulting routing fluctuation, the paper proposes Mutual-Inform SMoEs — two variants (Similarity-Inform and Attention-Inform) that allow tokens to influence each other's routing decisions via token-similarity or attention-derived weights. Theoretical analysis provides an entropy bound for the resulting routing distribution, and experiments on ImageNet classification and Wikitext-103 language modeling (including robustness benchmarks) show reduced fluctuation and improved performance relative to vanilla SMoE baselines.

## Strengths

- **Novel PGM derivation connecting attention and MoE.** Section 2 formally derives multihead attention as a 2-layer hierarchical mixture-of-experts regression (Equation 3) and attention-MoE as a 3-layer variant (Equation 4), revealing that standard SMoE's conditional independence assumption (\(\tilde{e}_i \perp\!\!\!\perp \tilde{e}_j \mid \tilde{\mathbf{X}}\)) is a structural limitation. This provides a principled motivation for the proposed mutual-inform methods and is a genuine theoretical contribution.

- **Direct empirical evidence of routing fluctuation reduction.** Figure 2 (Left) measures the proportion of tokens switching expert assignments between consecutive final training epochs (59→60) on Wikitext-103. The baseline SMoE shows fluctuation up to ~33% in early layers, while both Similarity-Inform and Attention-Inform SMoE show markedly lower fluctuation across all layers. This directly validates the paper's central claim.

- **Empirical validation of the entropy reduction predicted by Proposition 1.** Figure 2 (Right) plots the ratio of average routing entropy relative to baseline, with both proposed methods staying below 1.0 for every layer. This provides an empirical counterpart to the theoretical bound and links lower entropy to the observed fluctuation reduction.

- **Robustness evaluation across multiple perturbation types.** Tables 1 and 2 evaluate on both clean and adversarially perturbed data (word-swap attacks on Wikitext-103; ImageNet-C, -A, -R, -O variants), with consistent improvements over baselines. This goes beyond standard evaluation and supports the claim of increased model robustness.

## Weaknesses

### Fatal
None.

### Major

- **No experimental comparison against other routing-stabilization methods.** The related work (Section 5) acknowledges several prior methods designed to address routing fluctuation — StableMoE, SMoE-dropout, router Z-loss, hash layers, linear assignment routing — yet all experiments compare only against vanilla SMoE, GLAM, and V-MoE. The paper claims orthogonality, but without empirical comparison against at least one dedicated fluctuation-reduction baseline, a reader cannot assess whether Mutual-Inform SMoE offers competitive or complementary benefits. This is the paper's most significant evaluation gap.

### Minor

- **The fluctuation analysis is limited in scope.** The fluctuation measurement (Figure 2) is conducted on only one dataset (Wikitext-103) and only between one pair of consecutive epochs (59–60). Whether the reduction persists over longer intervals or generalizes to other domains (e.g., ImageNet) is not shown. Additionally, the analysis examines the post-softmax routing distribution but not the effect of the Top-M operation on fluctuation, which is the actual decision that matters for SMoE behavior.

- **The theoretical result (Proposition 1) does not guarantee lower entropy under practical conditions.** The bound \(\mathcal{H}(\mathbf{p}_i) \leq \sum_j s(i,j) \mathcal{H}(\bar{\mathbf{e}}_j) + \mathcal{H}(\mathbf{s}_i)\) includes the additive term \(\mathcal{H}(\mathbf{s}_i)\), so the bound can be larger than the original entropy. The guarantee \(\mathcal{H}(\mathbf{p}_i) \leq \mathcal{H}(\bar{\mathbf{e}}_i)\) holds only in the limit \(\tau \to 0\) or \(\sigma \to 0\), not under realistic parameter settings. The empirical evidence (Figure 2, Right) supports the claimed reduction, but the theoretical framing overstates what has been formally proven.

- **The causal link between reduced fluctuation and improved performance is not established.** The paper shows correlation (lower fluctuation and lower perplexity/error), but does not disentangle whether performance gains stem from reduced fluctuation, better feature averaging (via weighted combination), improved expert specialization, or other confounds. An ablation that isolates the fluctuation-reduction effect (e.g., comparing against a uniformly-weighted token aggregation baseline) would clarify this.

- **No ablation studies for key design choices.** The Attention-Inform method selects only the attention head with the lowest average entropy, but no ablation examines the effect of this approximation versus using all heads or an alternative selection criterion. Similarly, no ablation isolates the effect of the learned similarity weighting in Similarity-Inform versus a uniform weighting baseline. The temperature parameter \(\tau\) and its sensitivity are not studied.

- **Results are reported without error bars or variance estimates.** Tables 1 and 2 report single numbers without confidence intervals, standard deviations, or number of runs. This makes it impossible to assess the statistical significance of the reported improvements.

### Trivial

- The claim "up to 33% of tokens switch their assigned experts in the final epochs" (Section 2.2) is stated before the experimental evidence that supports it (Figure 2, Section 4). Adding a forward reference or placing the number in context would improve clarity.

## Nice-to-Haves

- **Scalability/computational cost analysis.** Similarity-Inform requires computing an \(N \times N\) similarity matrix per MoE layer and per sample, which is \(O(N^2)\) per layer. A discussion of wall-clock time, memory overhead, or how this cost compares to the baseline would help practitioners assess trade-offs.

- **Comparison on a task where routing fluctuation is known to be severe**, such as long-document modeling or multi-modal learning, would strengthen the case for the method's practical value.

- **A simple baseline where all tokens' expert scores are uniformly averaged** would isolate whether the learned weighting (similarity/attention) is responsible for the improvement or merely the aggregation itself.

## Removed Points

- **"The PGM framework is a re-description with little new insight"** — removed. The PGM derivation is a genuine formal contribution. It explicitly derives the regression function for multihead attention as a hierarchical MoE (Equations 3–4), which is not a trivial restatement and provides the theoretical foundation for identifying the conditional independence assumption that motivates the proposed methods.

- **"Similarity-Inform is not clearly new"** — removed. The criticism is too vague ("many prior works combine...") and does not identify specific prior work that performs the same token-to-token routing-score aggregation. The paper's mechanism is distinct from expert-choice routing, token merging, and context-aware routers cited in the literature.

- **"The 33% claim lacks specification"** — removed. The claim is directly supported by Figure 2 in Section 4, which shows the baseline SMoE's per-layer fluctuation rate reaching ~33%. The claim is stated in Section 2.2 as a motivation with a forward reference to Section 4; this is standard paper structure.

- **"V-MoE is from 2021 — more recent vision SMoE models exist"** — removed. V-MoE is the standard baseline for vision MoE. Criticizing a paper for not chasing every newer model without naming specific alternatives is not constructive.

- **"Appendix is stripped, so I cannot assess experimental details"** — removed per hard rules (parser artifact).

- **Strength Finder item about importance of the problem** — removed as generic/superficial. The paper itself does not need external validation of its problem importance.

- **Strength Finder item about orthogonality to prior work** — removed. While the paper states orthogonality, this is a framing choice, not an experimentally validated strength.

## Novel Insights

The reviews do not surface a genuinely novel observation beyond the paper's own contributions. The point about the theoretical entropy bound not providing a guaranteed reduction under practical conditions (Proposition 1 requiring \(\tau \to 0\) or \(\sigma \to 0\)) is a useful clarification that the paper's authors could address by adding an empirical analysis showing how entropy varies with \(\tau\) across a range of practical values.

## Suggestions

1. **Add at least one dedicated routing-stabilization baseline** (e.g., StableMoE or SMoE-dropout) to the experimental comparison. If Mutual-Inform is orthogonal, this comparison establishes whether it can be combined or whether it offers competitive performance on its own.
2. **Include ablation studies**: (a) uniform-weighting baseline (average all tokens' expert scores without learned similarity), (b) all-heads vs. single-head approximation for Attention-Inform, (c) sensitivity to temperature \(\tau\).
3. **Report standard deviations or confidence intervals** for the main results, or specify the number of independent runs.
4. **Extend the fluctuation analysis** to ImageNet and to multiple epoch intervals (not just 59→60).
5. **Discuss computational complexity** explicitly and provide wall-clock time comparisons for a representative setting.
6. **Clarify the theoretical claim**: explicitly state that Proposition 1 provides an upper bound that guarantees lower entropy only in the limit, and that the empirical evidence (Figure 2) demonstrates the reduction under practical conditions.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>