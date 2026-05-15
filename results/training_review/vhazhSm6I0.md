Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper proposes a two-step test-time adaptation (TTA) framework for GNNs. The first step (BNSA) adapts batch normalization statistics using a data-driven weighting derived from Jensen-Shannon divergence between training and test activation distributions, combined with a learnable mask matrix for selective dimension adjustment. The second step (BNPA) refines BN scale/shift parameters using an energy-based model with entropy- and confidence-filtered pseudo-labels. Experiments on seven datasets across three GNN backbones (GCN, GraphSAGE, GAT) show consistent accuracy improvements over existing TTA methods.

## Strengths

- **Two-step framework separates statistic and parameter adaptation**: Decomposing BN adaptation into statistic adjustment (BNSA) followed by parameter refinement (BNPA) is conceptually clean and differs from end-to-end entropy minimization approaches. This design (Section 3) allows each step to address different aspects of the distribution shift.

- **Data-driven α via JS divergence is principled**: Rather than tuning the BN statistic mixing weight α empirically (as in prior work like a-BN, DUA), the paper computes α from the actual distribution shift between training and test activations using JS divergence (Eq. 3–4). The ablation study (Table 2, BNSA vs. BNSA w/o A) confirms that removing this learned weighting degrades performance.

- **Mask matrix provides selective adaptation and prevents collapse**: The learnable Bernoulli mask M (Eq. 5–6) allows the model to adjust only relevant BN dimensions. Ablation results (Table 2, BNSA vs. BNSA w/o M) and hyperparameter analysis (Section 4.3, Fig. 3) support that M helps prevent catastrophic collapse, particularly on challenging datasets like FB-100.

- **Component-level contributions validated by ablation**: The ablation study (Table 2) systematically removes each proposed component (weight A, mask M, closest-sample selection, entropy/confidence filtering), and each removal degrades performance, providing evidence that all sub-modules contribute to the final result.

- **Strong empirical results across diverse backbones**: The method achieves best or second-best accuracy on the majority of 21 dataset–backbone combinations, with notable margins on Cora (+2.84% with GCN) and Elliptic (+2.60% with GraphSAGE), supporting the claim of consistent improvement over prior TTA methods.

## Weaknesses

### Fatal
None.

### Major

- **Ambiguous definition of "instances" for node-level benchmarks**: The problem statement (Section 2.1) treats each test sample as a graph "G_i ∈ D_te," and Eq. 3–4 compute per-instance activation distributions P_m^{(i,d)}(G_m). However, four of seven evaluation datasets (Cora, Amazon-Photo, OGB-Arxiv, OGB-Products) involve a single graph with node-level train/test splits. The paper never clarifies whether each "instance" is a node or a graph in these cases, nor how a per-instance activation distribution is estimated from a single node's activation in a BN layer. For multi-graph datasets (Twitch-E, Elliptic, FB-100) the formulation is natural, but for single-graph node classification the mapping is undefined. This ambiguity makes the core BNSA procedure difficult to reproduce and assess.

- **Computational cost of pairwise JS divergence is unaddressed**: Equation 4 defines α^{(i,d)} as an average over all |D_tr|·|D_te| pairs. Even under a favorable interpretation (per-batch distributions rather than per-instance), the paper provides no wall-clock runtime comparison with baselines, no discussion of approximations or mini-batch strategies, and no analysis of how the method scales to datasets like OGB-Products (~2.4M nodes). The paper acknowledges that maintaining distributions has "computational overhead" (line 107) and that SGLD is costly (line 221), but the core pairwise computation itself may be prohibitive at the reported scale. Without any runtime data or tractability analysis, the practical feasibility of the method as described is uncertain.

- **No variance or significance reporting in main results**: Table 1 reports only mean accuracies over ten random seeds, with no standard deviations, confidence intervals, or statistical significance tests. The claimed improvements (e.g., +2.84% on Cora with GCN) could fall within noise range. Given that baselines use hyperparameters from their original publications (which target different data modalities), this evidential gap weakens support for the headline claim of "superior performance."

### Minor

- **Ambiguity about when the mask M is learned**: The paper states "In the training process, the modified BN layers are in Eq. 6" (line 117) while describing mask optimization via contrastive learning. It is unclear whether the Bernoulli variables B are optimized during pre-training (requiring training-time access) or during TTA. The loss L_BNSA (Eq. 8) uses test-batch statistics, suggesting the latter, but the phrasing "training process" is confusing and should be clarified.

- **Key hyperparameters unspecified**: The SGLD sampling steps T (Eq. 13), the decay steps k (Eq. 9), the entropy threshold τ_e (Eq. 16), the probability thresholds τ_c¹, τ_c² (Eq. 17), and the Gumbel-Softmax temperature τ (Eq. 5) are all introduced without specification of their values or how they were selected. While individual hyperparameter choices may be minor, the cumulative lack of specification hinders reproducibility.

- **Pseudo-label reliance limits correction under severe shift**: The BNPA step (Section 3.2) uses pseudo-labels from the pre-adapted model as optimization targets. Under severe distribution shift where the original model makes systematic errors, the method cannot correct these errors, potentially limiting its robustness.

- **No calibration metrics despite calibration claims**: The paper claims the EBM improves model calibration (Abstract, Section 3.2, line 255) but reports no calibration error metrics (ECE, reliability diagrams). This claim is stated but not experimentally supported.

### Trivial
None.

## Nice-to-Haves

- Wall-clock runtime comparison with baselines (especially against a-BN and TENT, which are simpler).
- Calibration metrics (Expected Calibration Error) to substantiate EBM-related claims.
- Simplified or approximated version of the JS computation (e.g., using MMD or batch-level distributions) with analysis of accuracy/runtime trade-off.
- Sensitivity analysis of pseudo-label quality under varying shift severity.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Experimental setup is critically underspecified" (Harsh Critic point 4)**: The paper explicitly states the OOD setting follows GTRANS and EERM (line 226). Referencing established prior work for evaluation protocol details is standard practice and not a deficiency. The datasets and their types of shifts are named.
- **"Hyperparameter sensitivity study claims strong performance even with small k, but no actual results or numbers are given"**: The figures (Fig. 3–4) exist in the original submission; the parser strips image content. The text describes the findings.
- **"The table image is not extractable" / "the parsed output makes detailed checking impossible"**: This is a parser limitation, not a paper flaw.
- **"Cost of estimating per-instance probability densities via non-parametric methods (not specified how)"**: The paper states it uses non-parametric density estimation (line 95). The specific method choice (e.g., histogram/KDE) would be an implementation detail that could be clarified but does not invalidate the approach.
- **Scope-creep demands**: Requests for theoretical proofs, silhouette scores, t-SNE visualizations, and analysis of varying density estimation dimensionality go beyond what is standard for an empirical TTA paper.

## Novel Insights

None beyond the paper's own contributions. The two-step BN decomposition (statistics then parameters) is the paper's main conceptual novelty. The reviews did not surface a deeper insight beyond what the paper already states.

## Suggestions

1. **Clarify the instance definition.** For single-graph node classification benchmarks, explicitly state whether each "instance" is a node, a batch, or the entire graph. Explain how per-instance activation distributions P_m^{(i,d)} are estimated in each case.
2. **Report standard deviations** for all main results (Table 1) and, where appropriate, include statistical significance comparisons.
3. **Provide a tractability analysis.** Describe how the JS divergence computation is implemented in practice (e.g., batch-level approximations, histogram-based estimation) and report wall-clock runtime compared to baselines.
4. **Specify all hyperparameters** (k, T, τ_e, τ_c¹, τ_c², τ, λ) and describe the selection procedure (e.g., grid search or heuristic).
5. **Clarify when the mask is optimized** (during pre-training or during TTA) with a precise algorithmic description.
6. **Add calibration evaluation** (Expected Calibration Error) to support the EBM calibration claims.

## Score and Decision

The paper presents a conceptually interesting two-step framework for GNN test-time adaptation with competitive empirical results and thorough ablation. However, a fundamental ambiguity about how the core computation applies to single-graph node classification benchmarks, combined with unaddressed scalability concerns and missing variance reporting, prevents full assessment of the method's validity and significance. Substantial clarification and additional analysis are needed before the contribution can be properly evaluated.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>