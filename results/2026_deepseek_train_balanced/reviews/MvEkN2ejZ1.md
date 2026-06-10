Now I have all the information needed. Here is my consolidated final review.

---

## Summary

This paper proposes MamBEV, a framework that replaces/complements transformer-based attention with State Space Model (SSM) blocks — specifically a novel Cross Quasi-separable SSM (XQSSM) — for learning bird's-eye-view representations from multi-camera images for 3D object detection. The core idea is to adapt SSM-based matrix mixers for cross-modal interaction between BEV queries and image features, achieving linear complexity rather than quadratic. Results on nuScenes show improvements over BEVFormerV1-Small in NDS, with extensive ablations across query insertion strategies, temporal frames, and SSM hyperparameters.

## Strengths

- **Novel SSM-based cross-attention mechanism (XQSSM) for BEV fusion**: The paper adapts Mamba-2's SSD formulation to enable cross-modal interaction between BEV queries and image features. The matrix mixer is reduced from shape `(M+V × M+V × 2H)` to `(M × V × 2H)` (Sec. 3.1.3, line 187), which is a principled architectural adaptation that genuinely extends SSMs to the multi-view BEV setting. This is a concrete, novel contribution that goes beyond prior SSM-for-vision work which only applied SSMs within a single modality.

- **Detailed computational complexity analysis**: The paper explicitly derives why naive SSM cross-attention requires quadratic costs (Sec. 3.1, lines 155–161) and then derives the task-specific reduction to linear complexity (lines 187). Table 2 empirically validates memory and FLOPs scaling across varying BEV grid and image sizes. The combination of analytical derivation and empirical measurement is more thorough than typical SSM-for-vision papers.

- **Systematic ablation of query insertion strategies for SSM-based BEV encoding**: Table 6 compares three methods for placing BEV queries into the SSM sequence (append, prepend, and the proposed "BEV Position Aware Merge" projection), with a reasoned explanation that Mamba learns spatial relations through token position. This type of architectural sensitivity analysis is specific to SSM-based BEV designs and provides useful insight for practitioners.

- **Pure SSM variant demonstrates non-trivial representational power**: The "MamBEV-Small-Pure" variant (no deformable attention layers in the encoder) still outperforms PolarDETR-T and BEVFormerV1-Small (line 232), demonstrating that the SSM-based cross-attention provides meaningful representational power on its own.

## Weaknesses

### Fatal

None.

### Major

- **The core method is underspecified to the point of being non-reproducible**: Several critical details are missing or unclear. (1) Section 3.1.1 proposes computing $y_i = \sum_{k=0}^{Z} C_i h_k$ where "image feature vector $k$ is likely to be relevant to $q_i$," but **how the $Z$ relevant locations $k$ are determined is never explained**. This is the central mechanism of the cross-attention — without it the method cannot be implemented. (2) The "BEV Position Aware Merge" (Project) method is referenced as the best query insertion strategy (Table 6), but the merge operation that generates $s_{\text{mask}}$ is never defined, and $R_{1D}$ is introduced (Sec. 3.1.4, line 191) without explanation of what it is. (3) The **temporal fusion mechanism** — which accounts for 57M parameters in the small model — is mentioned only in passing as a "CNN based temporal component" (line 230) with no description in the Methods section at all. Without these details, the paper cannot serve as a reproducible scientific contribution.

- **The best configuration still relies on deformable attention, undercutting the central premise**: The paper claims an "SSM-based architecture that can exceed the performance of existing Transformer-based architectures" (contribution 1). However, the best-performing configuration (MamBEV-Small with 4 frames) uses **mixed SSM + deformable attention**, and the paper explicitly states the pure SSM variant "was outperformed by the small model which made use of deformable layers" (line 232). The paper's own ablation (Table 4) finds "minimal difference" between SSM attention and deformable attention. This suggests the SSM components are supplements, not replacements, and the headline claim is overstated.

- **No latency or throughput measurements despite central efficiency claims**: The abstract claims "significantly improved computational and memory efficiency," and Table 1 says the model "requires fewer computational resources." Yet the paper reports **zero wall-clock measurements** (FPS, latency, or throughput). The FLOP and memory measurements in Table 2 use simplified toy models (R50 backbone, single layer) and the paper even notes "we did not adapt the kernel to reflect the true computational complexity of the XQSSM module" (line 179). For an efficiency-motivated paper targeting real-time autonomous driving, the absence of latency numbers is a critical gap.

- **Parameter count is higher than the baseline**: MamBEV-Small has 65M parameters (excluding temporal) + 57M temporal = **122M total**, versus BEVFormer-Small at **60M**. While the efficiency claim may be about memory rather than parameter count, the paper does not clearly communicate this distinction, and the raw parameter comparison creates a misleading picture. The higher parameter count also muddies whether the +.046 NDS improvement comes from the SSM innovation or simply from having double the parameters.

- **Ablation results consistently show "minimal effect" from SSM-specific design choices**: Table 4 (SSM vs deformable attention: "minimal difference"), Table 5 (SSM hidden state scaling: "minimal effect"), and Table 8 (channel scaling: "minimal effect") all report negligible performance variation. The paper itself says "minimal effect is observed" (line 253). When the core architectural components produce minimal effect, it raises the question of whether the SSM innovation is driving the reported improvements or whether other factors (parameter count, training pipeline differences, temporal module) are responsible.

### Minor

- **Comparisons are limited to BEVFormerV1 and PolarDETR-T**: BEVFormerV2 (Yang et al., 2023) is cited in the related work (line 38) and uses the same backbone and closely related architecture, but is not included in the main comparison table. Contemporary methods sharing similar experimental conditions (nuScenes, camera-only) are absent. The +.002 NDS improvement for MamBEV-Tiny is within the range of typical metric variance, and no variance/confidence intervals are reported.

- **Temporal dependency claim lacks a controlled comparison**: The paper claims to "better capture longer dependencies in multiview video" (contribution 3) and that the model "scales better than transformer-based attention over the same number of frames" (conclusion, line 270). However, the temporal ablation (Table 3) only evaluates MamBEV under varying frame counts without any comparison against a transformer-based temporal baseline under identical conditions. Every BEV method improves with more frames; this experiment does not demonstrate that SSMs are better at capturing longer dependencies.

- **Section 3.1.2 is missing**: The text jumps from Section 3.1.1 directly to Section 3.1.3. While this may be a parser artifact, it contributes to the overall impression that the method description is incomplete.

### Trivial

- The paper states "For simplicity, we use Mamba when discussing the Hydra block" (line 51). Since Hydra is bidirectional and Mamba is causal, this naming conflation could confuse readers about which architecture variant is used where. The paper does acknowledge this, but it would benefit from precision.
- The description of backbone pretraining is ambiguous: "ResNet101 and ResNet50 which are trained in a depth prediction task and COCO, respectively" (line 204). It is unclear which backbone uses which pretraining.

## Nice-to-Haves

- **Qualitative analysis of SSM behavior**: Visualizations showing which image regions the SSM hidden state attends to, or how the hidden state evolves across the sequence, would substantially strengthen the paper's claim that the SSM is learning meaningful spatial correspondences.
- **A controlled comparison** isolating the temporal contribution: comparing MamBEV's temporal fusion against BEVFormerV1's recurrent temporal attention under identical encoder settings would directly test the temporal dependency claim.
- **Ablation of the 57M-parameter temporal component**: Given that this accounts for nearly half the total parameters, ablating its contribution would help separate the value of the temporal mechanism from the SSM cross-attention innovation.

## Removed Points

These points were flagged by the reviewers but are removed or downgraded after verification against the paper:

- *"The 'multi-modality' framing is misleading"* — The paper mentions SSMs "struggle in BEV scenarios involving multiple input modalities" (line 14), but in context this refers to the multiple camera views (six egocentric cameras), not necessarily different sensor types. The framing is not misleading.

- *"Comparisons against outdated baselines"* — The paper is on an older submission cycle; BEVFormerV1 was the primary baseline at time of writing. PolarDETR is included. This is not a meaningful weakness.

- *"The background section about SSMs is generic"* — This is a standard background section necessary for the paper to be self-contained. Not a weakness.

- *"The paper should address problems outside its stated scope"* — Various demands for additional tasks (segmentation heads, multi-modality fusion) that the paper explicitly scoped out.

## Novel Insights

The reviews surface a consistent tension: the paper introduces a genuinely novel architectural adaptation (XQSSM) with a principled complexity analysis, but the experimental evidence does not align with the claimed contributions. The ablations showing "minimal effect" from SSM-specific components suggest either (a) the SSM machinery is interchangeable with deformable attention (which would make it an engineering alternative rather than a scientific advance), or (b) the experiments are not designed to measure the right thing (e.g., efficiency gains that would manifest in latency but not NDS). This disconnect between the architectural novelty (real) and the evidence (too weak to support the claimed story) is the paper's fundamental, unresolved tension. Notably, neither reviewer fully articulated this as a *measurement gap* — the paper needs to measure what the SSM uniquely provides (e.g., linear memory scaling at inference under matched parameter counts, or wall-clock speed at matched performance) rather than only reporting NDS where "minimal effect" is observed.

## Suggestions

The paper would be strengthened by:

1. **Fully specifying the method**: Define how the $Z$ relevant image locations per BEV query are determined (learned offsets? geometric projection?). Define $R_{1D}$, $s_{\text{mask}}$, and the "Project" merge operation. Describe the temporal fusion mechanism. The paper must be reproducible from the text alone.

2. **Providing wall-clock latency/throughput measurements** on actual hardware (e.g., A100) for both MamBEV and BEVFormer at matched parameter and FLOP budgets. This is essential to substantiate the efficiency claims.

3. **Reporting results with matched total parameter counts** (or clearly separating parameter-efficiency from memory-efficiency claims). Running a controlled experiment where MamBEV's total parameters (including temporal) are matched to BEVFormer-Small's 60M would clarify whether the SSM architecture itself contributes to the performance gain.

4. **Addressing the "minimal effect" ablations**: Either design experiments where the SSM's advantages are observable (e.g., measuring how performance degrades under limited memory budgets, or showing scaling behavior on longer sequences where quadratic attention would be prohibitive), or reframe the contribution honestly as a mixed SSM+deformable approach rather than a pure SSM replacement.

## Score and Decision

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>