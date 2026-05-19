- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 6, 5
Now I have a thorough understanding of the paper and can verify all claims. Let me produce the final consolidated review.

## Summary

This paper addresses the problem of knowledge distillation from strong pretrained models, where teacher strength often correlates with worse student performance. The authors attribute this to low mutual information between inputs and teacher outputs, and propose ReMem, a two-component teacher preprocessing method: (1) fine-tuning with Sharpness-Aware Minimization (SAM) using an unusually large perturbation radius to improve mutual information, and (2) a block-reweighting heuristic that downweights top MLP blocks based on evidence that they are the primary source of mutual information loss. The method is evaluated on 16 datasets, multiple student architectures, distillation algorithms, and fine-tuning methods, showing consistent student accuracy gains.

## Strengths

- **Novel repurposing of SAM for teacher preprocessing**: The paper demonstrates that fine-tuning with SAM at a large perturbation radius (ρ ≳ 0.05, far beyond typical generalization-enhancing values ~0.001) yields a Pareto-superior information-plane position (Figure 2) and directly translates to lower student test error (Figure 3). This is a clearly documented and non-obvious finding — standard SAM targets generalization, not distillation-readiness.

- **Clean ablation localizing mutual information loss to top MLP blocks**: Figure 4 provides a controlled comparison: pruning MLP blocks from the top improves mutual information dramatically with only modest accuracy degradation, while pruning self-attention blocks yields a near-linear tradeoff. This crisp diagnostic experiment identifies a precise architectural target and motivates the block-reweighting heuristic.

- **Theoretical link between expertness and mutual information**: Proposition 5.4 gives an information-theoretic upper bound \( I(\mathrm{MLP}(g_{\leftarrow}(X));X) \leq \log_2 M + \sum_{z\in[M]} |\mathcal{S}_z| b \), formalizing why sparse expert-like activations in top MLP blocks (which Figure 5 shows emerge in stronger models) inherently limit the mutual information of those blocks. This provides principled backing for the empirical observations.

- **Comprehensive evaluation across diverse settings**: The method shows consistent student gains across 16 datasets spanning natural, medical, and satellite imagery; varying dataset sizes; multiple student architectures (ResNet-18, MobileNetV2, EfficientNetV2); multiple distillation algorithms (logit matching, DIST, patient distillation); and parameter-efficient fine-tuning (LoRA). Tables 5–6 show that ReMem reverses the trend where larger teachers / more pretraining data hurt student performance.

## Weaknesses

### Fatal

None.

### Major

- **No empirical comparison against existing teacher-preprocessing approaches**: The related work section discusses early stopping (Wang et al., 2022), cross-fitting (Dao et al., 2021), joint training (Park et al., 2021), and regularized teacher training (Dong et al., 2022), but the only baseline in all main experiments is vanilla fine-tuning. The paper dismisses these alternatives with a brief justification ("may not be readily applied…due to significant computation overhead, or strict constraints on the teacher's model architecture") without empirical validation. Since the paper frames itself as a *teacher preprocessing* method, evaluating against at least one alternative preprocessing approach (e.g., early stopping, which is nearly cost-free) on a subset of datasets is necessary to establish that ReMem's gains are attributable to its specific design rather than simply deviating from full convergence. The paper's existing evaluation protocol does early-stop at multiple checkpoints and select the best — this partially addresses the concern but does not replace a direct comparison against an explicitly early-stopped teacher or other preprocessing strategies.

### Minor

- **Pruning (removal) vs. downweighting gap**: The diagnostic in Figure 4 prunes MLP blocks entirely, but the proposed intervention is *downweighting* them. These are qualitatively different operations — removal eliminates all information flow through a block while downweighting preserves it at reduced strength. The paper extrapolates from one to the other without validating that downweighting produces the same information-plane effects as pruning. This does not invalidate the method (which works empirically), but weakens the causal narrative connecting the diagnostic to the design choice.

- **Expertness measure depends on an arbitrary clustering parameter**: Definition 5.3 fixes the number of clusters (experts) to the number of classes, with the choice attributed to the spectral co-clustering algorithm. This choice is not justified, and expertness values could vary with different cluster counts, weakening the claim that expertness is an intrinsic property of MLP blocks.

- **Best-checkpoint selection across sweeps could inflate reported gains**: The evaluation selects the best student checkpoint across multiple teacher checkpoints and hyperparameter settings. While this is a common protocol for evaluating teacher processing strategies (and is applied symmetrically to baseline and ReMem), it raises the question of how much of the reported improvement is due to broader effective search over checkpoints rather than the method itself. Reporting the variance across seeds or the performance of a fixed selection rule would strengthen confidence.

- **Proposition 5.4 assumes a true MoE structure but is applied to dense MLPs**: The formal bound holds for MLP blocks that are explicitly mixture-of-experts; the argument that dense MLPs "resemble" MoEs is qualitative. The bound is also noted to be quite loose (3000 bits vs. 4 million bits in the input), which limits its practical explanatory power despite its conceptual value.

- **Hyperparameter sensitivity of ρ and α is not analyzed across datasets**: The paper notes that SAM requires ρ ≳ 0.05 (much larger than typical SAM), and α controls block reweighting, but does not study how sensitive results are to these hyperparameters or how they should be set for new datasets.

### Trivial

None.

## Nice-to-Haves

- Comparing against a teacher that has been explicitly early-stopped (the most lightweight baseline from the related work) on a representative subset of datasets would significantly strengthen the paper.
- Reporting results with standard deviations across 3 random seeds for at least the main table (Table 1) would help assess whether gains are systematic.
- An ablation disentangling the contributions of SAM alone vs. block reweighting alone on the 6 representative datasets used in Tables 2–4.

## Removed Points

These points were considered and removed from the main review with justification:

1. **"Block reweighting math is internally contradictory"** — Factually incorrect. The reviewer's own analysis shows that for α < 1, the effective weight \(\tilde{\alpha}_l = \alpha \cdot (2-\alpha)^{(l_{\text{tot}}-l)}\) is *smaller* for top layers (smaller exponent) and *larger* for bottom layers (larger exponent). This confirms the paper's claim that "top MLP blocks [are] downweighted more than the bottom ones." The reviewer mistakenly equated "the bottom layers have larger effective weight" with "the paper's claim is wrong," when in fact the paper's claim is exactly that top layers have smaller effective weight. Removed as factually wrong.

2. **"Missing mutual information estimation details"** — The mutual information estimator (e.g., binning scheme, neural estimator) is not described in the extracted main text. This detail would reside in the experimental setup section of the appendix, which the parser has stripped. Per instructions, criticisms about content that existed in the original appendix are removed.

3. **"Missing ablation study"** — The paper text says at line 339: "1, we provide necessary ablation study of our method to show the individual effects of memory reweighting and SAM." This appears to reference an ablation table whose content was stripped by the parser. Removed as a parser artifact.

4. **"No variance or statistical tests"** — Single-run evaluation with hyperparameter sweeps is standard practice in this literature (knowledge distillation on large-scale benchmarks). Requesting 3-seed variance bars for all 16 datasets is reasonable as a nice-to-have but not a genuine weakness given community norms. Moved to Nice-to-Haves (implicitly via the suggestion about reporting variance).

5. **Generic criticisms without specific anchors** — Criticisms like "the connection between SAM and mutual information is asserted rather than reasoned" or "the paper does not explain why a sharpness penalty would increase mutual information" demand theoretical proof that is not standard for an empirical systems paper. The paper provides empirical evidence (Figures 2, 3) which is sufficient for its scope.

6. **"ReZero comparison missing"** — The paper explicitly acknowledges the similarity to ReZero and notes the difference. Requesting a full experimental comparison against every closely related technique is scope creep; the paper's claim is about the combined ReMem method, not about block reweighting as a novel architectural primitive.

## Novel Insights

None beyond the paper's own contributions. The reviewer critiques did not surface an observation about the paper that is not already present in the paper itself.

## Suggestions

1. Add an empirical comparison against at least one existing teacher-preprocessing baseline (e.g., early-stopped teacher, or label-smoothed teacher as a negative control) on a representative subset of datasets. This would directly address the most significant gap in the evaluation.
2. If the pruning-diagnostic (Figure 4) is meant to motivate block reweighting, validate the connection by showing that the downweighted model (with α < 1) produces a similar information-plane trajectory as the pruned model, even if weaker in magnitude.
3. Report the variance of student test accuracy across 3 seeds for the main results to demonstrate that improvements are systematic rather than artifacts of checkpoint selection.
