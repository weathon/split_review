Now I have a thorough understanding of the paper and the reviewer claims. Let me produce the final consolidated review.

## Summary

This paper introduces a framework for O(d)-equivariant message passing built on local canonicalization with tensorial messages. The key idea is to transform node features between local coordinate frames during message passing using explicit change-of-basis transformations on tensor-valued features, overcoming the information loss inherent in scalar-only message passing under local canonicalization. The authors demonstrate the framework by adapting PointNet++ into an equivariant architecture and evaluate it on point cloud tasks including normal vector regression, segmentation, and classification.

## Strengths

- **Tensorial messages as a strict generalization of scalar messages**: The paper formalizes scalar (Eq. 11) and tensorial (Eq. 12) message passing, proving that tensorial messages remain invariant under global transformations while enabling direct communication of vector/tensor features between local frames. Table 3 confirms this experimentally: tensorial messages outperform scalar messages even with randomly chosen local frames (cosine similarity 0.946 vs. 0.776 on normal regression), providing strong evidence that the conceptual limitation illustrated in Fig. 1 is real and that the proposed solution addresses it.

- **A clean, non-architecturally-restrictive approach to equivariance**: Unlike many equivariant methods (SE(3)-Transformers, Tensor Field Networks) that require specialized linear layers, non-linearities, and normalization layers, the local-canonicalization approach works with any standard building block. The paper demonstrates this concretely by adapting PointNet++, achieving competitive or state-of-the-art results. This lowers the barrier for practitioners to add equivariance to existing architectures.

- **Local frame refinement improves performance consistently**: The proposed iterative frame refinement (Sec. 4.3.1) shows consistent gains across tasks (Table 1: cosine similarity from 0.960 to 0.963 for normal regression; Table 2: mIoU from 84.6% to 84.9% for segmentation), validating the claim that refining frames with aggregated geometric information makes local frames more informative.

- **Framework enables controlled comparison between equivariance and data augmentation**: The same architecture can be trained with built-in equivariance (via learned frames) or with data augmentation (via random global frames), using identical hyperparameters. This is a genuine advantage over prior equivariant approaches that lack a straightforward non-equivariant counterpart, and the paper exploits this to make meaningful comparisons.

## Weaknesses

### Fatal
None.

### Major

- **No statistical rigor across all experiments**: Tables 1–3 and Figure 4 report single-point results without standard deviations, confidence intervals, or any indication of multiple runs. Differences in Table 1 (e.g., 0.922 vs. 0.918) could plausibly lie within run-to-run noise. The data efficiency comparison (Fig. 4) similarly lacks variance estimates. Without this information, the reader cannot assess whether the reported improvements—including the central claim that tensorial messages outperform scalar messages—are statistically significant. This is the paper's most significant weakness.

- **The "state-of-the-art" claim on normal vector regression relies on a narrow baseline window**: Table 1 reports results from a single source paper (Luo et al., 2022). While the table includes several relevant baselines (TFN, SE(3)-Transformer, EPN, PFC, Li et al., Luo et al.), these are drawn from a 2022 paper and do not reflect more recent equivariant architectures or variants that may have been evaluated on the same task. Given that SOTA claims typically require a comprehensive and up-to-date baseline comparison, the current evidence is insufficient to substantiate this claim. The paper correctly qualifies this elsewhere as "competitive results," which is more appropriate.

### Minor

- **Architectural differences between equivariant and data-augmentation baselines are not fully controlled**: The equivariant model includes learned frame-prediction MLPs (Eq. 4) and iterative frame refinement (Sec. 4.3.1), which the data-augmentation baseline omits. The paper notes a 0.33% parameter difference for the non-refined normal regression model (and 9.1% with refinement), but the structural architectural difference—frame-prediction networks that process geometric information—may affect representational capacity beyond simple parameter count. The paper's claim of a "fair comparison" is reasonable but not fully justified, as the comparison conflates built-in equivariance with the presence of these additional learned components.

- **Data efficiency experiment (Figure 4) lacks critical methodological detail**: The paper does not describe how training subsets are sampled (random subsets? stratified?), how many fractions were tested, or whether the observed trend is robust across multiple random seeds. The observation that "error rate is not necessarily smaller for all dataset sizes" is presented without discussion of whether this is a consistent finding or statistical noise. This undermines one of the paper's central claims about data efficiency.

- **Limited computational cost analysis**: The paper promotes the framework as a "drop-in replacement" for data augmentation but does not report wall-clock training or inference times for the equivariant model vs. the data-augmented baseline. The frame construction and tensorial transformations add computational overhead that practitioners need to evaluate.

- **No discussion of limitations**: The paper does not discuss scenarios where tensorial messages might be unnecessary, where frame estimation could fail (sparse/noisy neighborhoods), or when the handedness correction threshold could cause issues. A brief limitations paragraph would strengthen the paper's completeness.

- **Handedness correction discontinuity**: The hard threshold in Eq. 5 (if-statement based on sign of a dot product) could cause discontinuities in the local frame as a function of input, potentially affecting gradient flow and robustness. This is not discussed.

### Trivial
None.

## Nice-to-Haves

- Ablations isolating the effect of radial/angular embeddings from the effect of equivariance itself would strengthen the comparison
- Hyperparameter sensitivity analysis for the cutoff radius \(r_c\) and frame-prediction MLP architecture
- Runtime benchmarks on ModelNet40 to help practitioners assess the computational cost of the approach

## Removed Points

These points are flagged as removed but preserved for reference in case they are useful:

- **Criticism that SE(3)-Transformer and TFN baselines are missing from Table 1**: Removed as factually wrong — both methods appear in the table (as listed in the caption). The critic appears to have misread the table.
- **Criticism that the proof "assumes that all node features transform under some representation" without acknowledging scalars**: Removed — the paper explicitly states "The representation of the input features is determined by the problem setup and may be a combination of scalars, vectors and tensorial features." Scalars correspond to the trivial representation and are covered by this formalism.
- **Criticism that the frame refinement update (Eq. 14-15) lacks clarity about whether it includes scalar channels**: Removed — the update \(f_i^{(k)} \to U_i^{(k)} f_i^{(k)}\) applies U (an SO(3) matrix) to features; scalars in the trivial representation are invariant under SO(3) by definition, and this is standard in equivariant literature.
- **Strength that "State-of-the-art results on normal vector regression" from Strength Finder**: Downgraded to a minor strength — the claim is only supported by baselines from a single 2022 paper, so it should be recognized as "competitive" rather than definitively SOTA.

## Novel Insights

Beyond the paper's own contributions, the reviews highlight a nuanced tension: the framework's key selling point—that it enables controlled apples-to-apples comparisons between equivariant and non-equivariant models—is also its key vulnerability. Because the equivariant model necessarily contains additional learned components (frame-prediction networks) that the data-augmented baseline lacks, the comparison can never be perfectly controlled. This tension is intrinsic to any local-canonicalization approach and suggests that future work should develop systematic methods for disentangling the effect of equivariance from that of the auxiliary networks required to achieve it. The paper's own data-efficiency observation (Fig. 4)—that equivariance sometimes hurts at small dataset sizes—is an honest and interesting finding that deserves deeper investigation.

## Suggestions

- Add results from multiple random seeds (at least 3-5) with standard deviations to all tables and Figure 4. This is essential for the paper to meet the evidential bar for its core claims.
- Expand the baseline comparison to include more recent equivariant architectures beyond Luo et al. (2022), or temper the SOTA claim to "competitive results" as done elsewhere in the paper.
- Provide a clearer description of the data-efficiency experiment methodology (subsampling procedure, number of trials) and add error bars to Figure 4.
- Include wall-clock runtime comparisons and a brief limitations paragraph.
- Ablate the effect of the radial/angular embeddings by running the data-augmented baseline with the same embeddings to isolate the effect of equivariance.

## Score and Decision

The paper presents a clean and theoretically well-motivated framework for equivariant message passing. The idea of tensorial messages between local frames is novel and clearly explained. However, the experimental evaluation is the primary weakness: the lack of error bars across all experiments, the narrow baseline window for the SOTA claim, the uncontrolled architectural differences in the central comparison, and the underspecified data-efficiency experiment collectively mean that the claimed advantages are not convincingly established at the evidential standard of a top venue. The methodological contribution is promising, but the paper needs substantial experimental strengthening before it can be accepted.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>