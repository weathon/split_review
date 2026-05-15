Now I have all the information needed to write the final consolidated review.

## Summary

The paper proposes a framework for O(d)-equivariant message passing via local canonicalization with *tensorial messages*. The core idea is to predict equivariant local frames at each node, express features in those frames, and then transform features between frames using tensor representations during message passing. This allows directional/geometric information to be communicated consistently, generalizing prior scalar-message local-canonicalization approaches. The authors demonstrate the framework by adapting PointNet++ for tasks including normal regression, segmentation, and classification.

## Strengths

- **Novel and well-motivated framework**: The paper identifies a genuine limitation of existing local-canonicalization methods (loss of directional information, as illustrated in Fig. 1) and provides a mathematically clean solution via tensorial messages that transform features between local frames using tensor representations. The distinction from prior work (scalar messages that lose directional information) is clearly articulated and experimentally validated.

- **Rigorous theoretical grounding for O(d)-equivariance**: The invariance proof (Eq. 9), the tensorial message passing formulation (Eq. 12), and its invariance proof (Eq. 13) are correctly derived and clearly presented. The framework naturally accommodates arbitrary tensor and pseudotensor representations and generalizes to any dimension d.

- **Practical "drop-in" perspective**: The framework can make any existing message-passing architecture equivariant without requiring specialized building blocks (non-standard nonlinearities, normalization, etc.). This distinguishes it from approaches like SE(3)-transformers or egnn that require bespoke architectural components.

- **Controlled comparison with data augmentation**: The paper provides a direct comparison between built-in equivariance and data augmentation using the same architecture and hyperparameters — a comparison that is often absent in equivariance papers. The data efficiency analysis (Fig. 4) provides interesting empirical evidence about regimes where equivariance helps more or less.

## Weaknesses

### Fatal
None.

### Major

- **"State-of-the-art" claim is not fully supported by contemporary baselines**: The paper claims SOTA results on normal regression and competitive results on segmentation, but the experimental baselines are from Luo et al. (2022), Lou et al. (2023), and Deng et al. (2021) — no post-2023 methods are included as experimental baselines. While the paper cites several 2024 works (Liao et al., 2024; Simeon & De Fabritiis, 2024; Du et al., 2024; Langer et al., 2024) in related work and discussion, none appear in the comparison tables. Given that the paper is from 2026, the absence of comparisons with more recent equivariant point-cloud architectures (e.g., newer frame-averaging methods, fast equivariant architectures) weakens the empirical SOTA claim substantially. The authors should either include contemporary baselines or adjust their claims (e.g., "competitive results" rather than "state-of-the-art").

### Minor

- **Data efficiency experiment lacks statistical rigor**: Figure 4 shows a single run per data fraction with no error bars or standard deviations. The claim of steeper slope (better data efficiency) would be stronger with multiple seeds and confidence intervals. The crossing of curves at large dataset sizes is an interesting phenomenon but is not discussed or tested for replicability.

- **Frame refinement gains are marginal and analysis is shallow**: The iterative refinement (Sec. 4.3.1) yields small improvements (0.927 → 0.929 cosine similarity in Table 1; 85.4 → 85.6 mIoU in Table 2). The paper does not ablate refinement depth (first layer only vs. all layers) or analyze whether the MLP-predicted refinement vectors encode meaningful geometric information. The circular dependency noted (features depend on frames, frames are refined based on features) is not analyzed for stability.

- **Parameter difference between equivariant and data-augmentation models is acknowledged but under-discussed**: The paper mentions that the data augmentation model has 0.33% fewer parameters for normal regression, but the numbers in parentheses (9.1% for normal regression, 10.3% for segmentation, 3.9% for classification) are not clearly explained. Clarifying what these percentages refer to would improve transparency.

- **Segmentation gains are small**: The tensorial messages improve mIoU by only 0.4 percentage points (85.0 → 85.4 in Table 2) and refinement adds another 0.2. The paper honestly acknowledges that geometric information matters less for this task, but this undercuts the generality claims.

### Trivial
None.

## Nice-to-Haves

- Application of the framework to a different backbone architecture (e.g., DGCNN, Point Transformer) to demonstrate generality beyond PointNet++.
- Computational cost comparison (inference time, memory) against both data-augmented baselines and specialized equivariant architectures.
- Qualitative examples where tensorial messages change predictions (e.g., a case where the scalar-message model misorients a normal that the tensorial model gets right).

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Classification results not shown"** — The paper mentions training for classification and gives parameter counts "for classification." Additional experimental results (including likely classification) are referenced in App. D. Per the hard rule about stripped appendix content, this criticism is removed.

2. **"Specification of ρ_f representation not provided"** — The paper states "see App. A" for the direct sum decomposition of representations, and explains the general approach in Section 4.2. This detail was in the appendix which the parser strips. Per the hard rule, removed.

3. **"Uncontrolled ablation: tensorial vs scalar may differ in parameter count"** — The tensorial transformation ρ_f(R_i R_j^{-1}) in Eq. (12) is a fixed change-of-basis operation, not a learned function. It introduces no additional learnable parameters compared to the scalar baseline in Eq. (11). The parameter counts between the two are essentially identical, so this criticism is factually incorrect.

4. **"Missing related works" (Frame Averaging variants, Group Convolution)** — Per the hard rule, I cannot confirm the existence of specific works the reviewer claims are missing, so this is removed.

5. **"Comparison with data augmentation unfair due to extra capacity"** — The paper acknowledges the 0.33% parameter difference and uses the same architecture and optimizer for both. This is transparent and the difference is negligible. Downgraded from a core criticism.

## Novel Insights

The tension between the strong theoretical framework and the modest experimental validation highlights an interesting pattern in equivariant ML papers: elegantly general mathematical contributions often produce their clearest empirical wins on tasks where directional information is *directly* the target (normal regression), while on tasks where directional information is only indirectly useful (segmentation, classification), the gains shrink dramatically. The paper's honest reporting of this pattern (including the data efficiency curves crossing) is refreshing but also suggests that the practical value of tensorial messages may be more task-specific than the general formalism would suggest. The framework's real contribution may be less about achieving new SOTA numbers and more about providing a principled way to ablate the role of geometric information communication — the ability to "turn off" tensorial messages while keeping everything else identical is a useful diagnostic tool that the paper under-exploits.

## Suggestions

1. **Update experimental baselines**: Include comparisons with at least 2-3 post-2023 equivariant methods (e.g., recent frame-averaging or equivariant point-cloud architectures) to substantiate the SOTA claim, or temper the claim to "competitive."

2. **Add statistical rigor**: Report results over at least 3 random seeds with standard deviations for the main tables and the data efficiency plot.

3. **Clarify the parameter percentages**: The numbers in parentheses (9.1%, 10.3%, 3.9%) alongside the data-augmentation parameter differences need explicit explanation.

4. **Ablate the refinement mechanism**: Compare refinement at the first layer only vs. all layers to isolate where refinement helps.

5. **Explicitly state the tensor representations used**: Even if the detailed breakdown is in the appendix, a brief summary in the main text (e.g., "we use scalars and vectors in layers 1-2, adding pseudovectors in layer 3") would improve reproducibility for readers who skip the appendix.

## Score and Decision

The paper presents a theoretically sound and practically motivated framework. The core idea — tensorial messages between local canonical frames — is novel, well-motivated, and correctly formalized. The experiments demonstrate clear improvements over the compared baselines. However, the headline "state-of-the-art" claims are not fully supported by the limited set of (pre-2024) baselines, and several experimental details lack rigor (single-run data efficiency plot, marginal refinement gains unablated). These are real but addressable weaknesses that do not undermine the core theoretical contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>