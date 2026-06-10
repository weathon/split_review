## Summary

This paper proposes GS-MoE, a weakly-supervised video anomaly detection (WSVAD) framework that combines two components: (1) a Temporal Gaussian Splatting (TGS) loss that generates Gaussian-kernel pseudo-labels from the model's own anomaly scores to expand the supervisory signal beyond the top-k MIL snippets, and (2) a Mixture-of-Experts architecture with class-specific experts and a cross-attention gate model that captures correlations between coarse and fine-grained anomaly features. The method achieves 91.58% AUC on UCF-Crime and competitive results on XD-Violence.

## Strengths

- **Large, well-documented performance gains on UCF-Crime, especially on the abnormal-only metric (AUC_A).** The paper reports 83.86% AUC_A against UR-DMU's 70.81% (Table 1). This metric isolates anomaly-localization ability on videos that actually contain anomalies, and the magnitude of the gain (~13 pp) far exceeds typical incremental improvements in the field, directly supporting the claim that the TGS+MoE architecture helps with subtle anomalies.

- **Class-expert masking experiment provides a clean causal test of the MoE's role.** Table 4 shows that when an expert for a given anomaly class is masked, the gate model's AUC for that class drops to ~50% (near random), while including it yields substantially higher scores (e.g., 86.37% for "Abuse"). This is controlled, class-level evidence that the experts genuinely learn class-specific representations rather than the gate model simply benefiting from extra parameters.

- **Ablation study cleanly decomposes each component's marginal contribution.** Table 2 shows monotonic improvement: TGS loss (+1.77% AUC), class-experts (+0.79%), and gate model (+2.05%). The gate model bringing the largest gain validates the architectural reasoning that correlating coarse and fine-grained cues is the most impactful step.

- **Category-wise analysis ties aggregate improvements to the specific failure mode the paper targets.** Figure 4 documents up to +24.3% improvement on categories like "Arson," "Assault," "Fighting," and "Stealing" — precisely the subtle, temporally complex anomalies that the paper argues prior MIL-based methods overlook.

- **Cluster-based experts experiment shows the method does not strictly require predefined class labels.** Table 5 demonstrates that clustering training videos into 7 groups (K-Means on task-aware features) and training corresponding experts still outperforms prior SOTA, providing evidence the approach generalizes beyond the idealized class-label setting.

## Weaknesses

### Major

- **The primary experimental setup uses per-class annotations that go beyond the strict WSVAD annotation budget, and this discrepancy is not acknowledged.** The paper situates itself in the WSVAD paradigm where only video-level binary labels are guaranteed, then trains one expert per anomaly class using class-level labels (Section 3.2: "each expert is trained only on refined features belonging to its assigned class and to the normal class"). UCF-Crime (13 classes) and XD-Violence (6 classes) do have class annotations available, but using them for training goes beyond what the standard WSVAD setup provides. The cluster-based experiment (Table 5) partially addresses this concern, but it is too briefly described — the claim that it "outperform[s] current sota models by 0.56%" does not specify which models or which metric, making it impossible to evaluate. The paper needs to either (a) reframe the primary contribution as operating with additional class-level annotations, or (b) promote the cluster-based evaluation as the primary WSVAD-consistent result.

- **An arithmetic error in a headline claim undermines confidence in numerical reporting.** Section 4.1 states that GS-MoE's 83.86% AUC_A is a "13.63% improvement" over UR-DMU at 70.81%. The correct absolute difference is 83.86 − 70.81 = **13.05 percentage points**. Neither absolute (13.05) nor relative ((13.05/70.81) ≈ 18.4%) calculations yield 13.63. This is straightforward arithmetic in a central result that is repeated as evidence of the method's effectiveness.

### Minor

- **Metric labeling confusion in the ablation section.** The Evaluation Metrics section (Section 4) clearly defines that UCF-Crime uses AUC and AUC_A, while XD-Violence uses AP and AP_A. However, the ablation text (Section 4.3) repeatedly refers to "AP_A" for UCF-Crime results (e.g., "+1.16% for UCF-Crime," "+4.46%"). These appear to be references to AUC_A but are labeled with the wrong metric name. This makes the ablation description difficult to parse and suggests careless reporting.

- **The TGS pseudo-labeling pipeline lacks specification of key details that affect reproducibility.** (a) How peaks are detected is never stated — no threshold, minimum prominence, or algorithm is given. (b) How widths \(W_i\) are determined is not described. (c) The text says \(\sigma_i\) is "the standard deviation of the scores around the peak within the width \(W_i\)", but \(W_i\) itself is introduced as a detected quantity without definition. (d) The double-bar norm in Equation 7 (\(\|(\sum ...)\|\)) is never defined (clipping? normalization?). (e) The number of experts is never stated for either dataset, though UCF-Crime has 13 classes and XD-Violence has 6.

- **The self-training dynamics of TGS are not analyzed for confirmation bias.** The Gaussian kernels are extracted from the model's own predicted scores and used to generate pseudo-labels that the model is then trained to match (via BCE loss). The only mitigation mentioned is training "for a few iterations" with the MIL loss beforehand. There is no discussion of whether pseudo-labels are iteratively refined, how many iterations constitute "a few," or what prevents the model from converging to a degenerate solution (e.g., assigning uniformly high scores that the TGS labels then reinforce).

### Trivial

- **The "Gaussian Splatting" terminology borrows from 3D scene rendering (Kerbl et al., 2023) but the paper's operation is standard 1D peak detection with Gaussian fitting — no 3D-to-2D projection, differentiable rasterization, or alpha compositing is involved.** The Related Work section (2.3) describes 3D Gaussian Splatting but draws no substantive connection to the paper's method. This is a naming inflation that does not affect the method's technical merit but makes the paper harder to assess accurately.

## Nice-to-Haves

- Reporting variance or confidence intervals across multiple runs would strengthen confidence in the results, though single-run evaluation is the norm in WSVAD benchmarks.
- Providing category-wise base rates alongside the "+24.3%" improvement claim in Figure 4 would make the improvement interpretable (a category going from 30% to 54.3% is a very different story from 70% to 94.3%).

## Removed Points

- **No limitations section**: Removed — this is a formatting choice, not a substantive weakness.
- **Missing variance/confidence intervals**: Demoted to nice-to-have — single-run evaluation is standard in WSVAD.
- **Gaussian Splatting Related Work section is "decorative"**: Partially valid but this is a criticism of a Related Work subsection that covers Gaussian Splatting as a broader trend; the paper's method is clearly defined on its own terms in Section 3.1.
- **Category-wise base rates not stated**: Merged into nice-to-haves — the "up to +24.3%" claim is still informative.
- Various complaints about presentation, missing appendix content, or formatting — removed per hard rules (parser artifacts, not author errors).

## Novel Insights

The most noteworthy observation from the review process is the tension between the two reviewers' assessments of the cluster-based experiment: one sees it as a "brief afterthought" with vague claims, while the other sees it as a key strength validating robustness. The truth is somewhere in between — the experiment clearly exists and shows the method can work without class labels, but the reporting is so thin (no metrics specified, no baselines named) that it cannot be evaluated as a primary result. This gap represents the single most impactful improvement the authors could make.

## Suggestions

1. **Fix the arithmetic error** (13.63 → 13.05) and **correct all metric labels** in the ablation section (AP_A → AUC_A where referring to UCF-Crime).
2. **Explicitly acknowledge** in the paper that the primary expert training uses class-level annotations available in the UCF-Crime and XD-Violence datasets, distinguishing this from the strict WSVAD setting. Treat the cluster-based experiment as a primary result or at minimum describe it with specific metrics and baselines.
3. **Specify the missing implementation details**: peak detection algorithm/parameters, how \(W_i\) and \(\sigma_i\) are computed, number of experts per dataset, and what the norm in Equation 7 represents.
4. **Add analysis of the TGS self-training dynamics**: how many "few iterations" of MIL pre-training, whether pseudo-labels are iteratively refined, and the stability of the training process across different random seeds.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>