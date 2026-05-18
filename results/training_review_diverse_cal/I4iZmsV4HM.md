Now I have all the information needed to produce the consolidated review. Let me write it.

## Summary

This paper studies model inversion attacks on voxel-based 3D feature extractors used in autonomous driving. The authors identify that prior regression-based inversion fails because: (1) zero-padded (empty) voxels are semantically ambiguous with points at the origin, and (2) non-empty voxels disperse into empty ones through downsampling layers, causing an explosion of false-positive points that bias restoration toward the origin. To address this, they propose ConcreTizer, which reformulates point regression as Voxel Occupancy Classification (VOC) to resolve the ambiguity, and uses Dispersion-Controlled Supervision (DCS) — block-wise training aligned with downsampling layers — to curb VoI dispersion. Experiments on KITTI and Waymo across two feature extractors show large improvements over point regression and a conditional generative baseline (modified UltraLiDAR), and the ablation study cleanly isolates the contribution of each component.

## Strengths

1. **Clear identification of why prior regression-based inversion fails for 3D voxel features.** The paper diagnoses two specific mechanisms — zero-padding ambiguity and VoI dispersion — and supports the diagnosis with quantitative evidence (Figure 3 shows point explosion and origin-concentration as layer depth increases, and VoI density spikes at downsampling layers). This analysis is the paper's most valuable intellectual contribution and convincingly explains why the prior attempt (Hwang et al., 2023) concluded inversion was infeasible.

2. **VOC is a simple, principled reformulation that directly addresses the root cause.** Converting coordinate regression to binary occupancy classification resolves the semantic ambiguity of zero-padded voxels. The ablation (Figure 7) shows that even BCE-based VOC enables restoration at the 6th layer where point regression completely fails, confirming the classification shift is critical.

3. **DCS is well-motivated by the diagnosis and the ablation cleanly validates it.** DCS partitions the feature extractor at downsampling layers and trains each inversion block with both occupancy classification and channel regression, then masks to prune false VoIs. Figure 7 shows that only VOC+DCS produces point distributions matching the original at the 12th layer, while VOC alone still shows biased restoration. Figure 8 further demonstrates that the optimal number of DCS instances (2–4) aligns with the number of downsampling layers, and that over-partitioning (10) degrades performance due to error accumulation — confirming the design rationale.

4. **Consistent quantitative gains across two datasets and two backbones.** Table 1 shows ConcreTizer outperforms UltraLiDAR by 23.4% in CD and 12.4% in F1 on KITTI at the deepest layer, with similar margins on Waymo (21.1% CD improvement). Table 2 demonstrates that restored scenes recover 75–87% of original detection AP on KITTI and 63–76% on Waymo, proving the restoration preserves task-relevant geometry. Figure 6 verifies the method on VoxelResBackbone, establishing generalizability.

5. **Thoughtful trade-off analysis (Section 5.6) on privacy vs. utility for potential defenses.** The paper systematically evaluates several perturbation defenses (rotation, scaling, sampling, Gaussian noise with different spatial configurations) and shows that current defenses degrade detection accuracy before meaningfully increasing restoration error — highlighting the difficulty of defending against this attack. The finding that sparse 3D features cause noise to impact regions unevenly is a useful insight for future defense design.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **The "first" claim is overstated and should be revised.** The abstract and contributions claim "the first in-depth study of model inversion attacks for 3D data" and "the first to study inversion attacks for 3D data" (lines 4, 30, 33). Yet the paper itself cites Hwang et al. (2023) as "the only known attempt at an inversion attack on 3D point cloud data" that "developed a point regression method to invert voxel-based backbones" (lines 14, 44). Hwang et al. is a prior study of inversion attacks on 3D data, even if it concluded infeasibility. The genuine novelty is showing that the *failure was due to the regression formulation, not an inherent property of 3D features* — a legitimate and valuable finding. The authors should position their work as the first *successful* inversion attack or the first *in-depth analysis* revealing why naive regression fails. This is a framing issue, not a factual error about the method, but the repeated "first" claims create an appearance of overclaiming.

2. **The UltraLiDAR adaptation is underspecified.** The paper states "We modified the encoder part of UltraLiDAR to accept voxel features as an input" (line 143) without describing what was modified, how much of the architecture changed, or how the model was retrained. Since UltraLiDAR's original design converts 3D sparse features into 2D dense features for a 2D VQ-VAE, the adaptation likely involves non-trivial architectural changes that could either advantage or disadvantage the baseline. The paper attributes UltraLiDAR's lower performance to "loss of 3D sparse characteristics" (line 153), which is a plausible explanation, but the reader cannot fully assess whether the comparison is fair or whether the performance gap reflects a suboptimal adaptation. The paper's core claims do *not* depend on this comparison alone — the ablation study (Figure 7) independently validates the method — but the comparison as presented would benefit from more transparency.

3. **No confidence intervals or variance estimates are reported.** Tables 1 and 2 report point estimates without standard deviations, confidence intervals, or error bars. For a method comparison paper, the reader cannot assess whether observed differences (e.g., the 4.5% F1 gap on Waymo at the deepest layer) are statistically reliable. This is especially relevant for Table 2 where UltraLiDAR's detection accuracy on Waymo is described as "very poor" — a single number without variance is insufficient to characterize baseline performance. *(Note: reporting confidence intervals is standard practice in machine learning and is a reasonable ask given the computational scale of these experiments.)*

4. **Sensitivity to the key hyperparameter β is not explored.** The regression loss weight β is set to 1 (line 137) without any analysis of how this value affects the trade-off between classification accuracy and channel regression fidelity. Since β controls the balance between the two supervision signals in DCS (L_cls + β·L_reg), a sensitivity study (e.g., β ∈ {0.1, 0.5, 1, 5, 10}) would strengthen the empirical characterization.

### Trivial

- The paper could briefly clarify how voxel center coordinates are derived from spatial grid indices in the VOC restoration (the current explanation on line 88 — "range of coordinate values is bounded by the spatial location of the voxel" — is sufficient for readers familiar with voxel grids but could be explicit).
- No computational cost (training time, inference speed) is reported for the inversion attack, which would be useful for practitioners assessing deployment feasibility.
- The limitations section is brief (line 259 mentions only scope expansion to other representations); explicit discussion of when the approach may struggle (e.g., coarse voxelization, extreme downsampling beyond recovery) would strengthen the conclusion.

## Nice-to-Haves

- A dedicated analysis of the intra-voxel position error (distribution of ground-truth points relative to their voxel centers) would directly test the claim that placing points at centers is a sufficient approximation.
- A quantitative dispersion metric (e.g., ratio of non-empty voxels in restored deep features vs. original shallow features, with and without DCS) would concretely demonstrate DCS's mechanism beyond the qualitative density trends in Figure 3.
- A brief discussion of what happens when the inversion block is *not* symmetric in depth or structure would preempt a natural reader question.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Criticism about training details being deferred to the supplementary material*: The parser strips supplementary content from all papers; these details exist in the original submission. The main text already states the training regime ("trains each segment individually" in line 28, "train the restoration in block units" in line 105) and reports β=1. Removed per the rule about missing appendix content and because the claim that the training regime is unspecified is factually incorrect.
- *Criticism that error propagation / gradient flow implications are "not discussed in the main text"*: Section 5.5 explicitly discusses error accumulation through the cascade ("the restoration error of each block accumulates," line 178). The paper does not quantify the per-block error accumulation in absolute terms, which is noted as a valid sub-point in the Minor section above, but the blanket claim that it is absent is inaccurate.
- *Parts of the "first in-depth study" criticism that claim the paper "ignores" prior work*: The paper does cite and discuss Hwang et al. (2023) in both the Introduction (line 14) and Section 3 (line 44), acknowledging it as "the only known attempt." The overclaiming issue is about framing, not omission. Kept the substantive part in Minor above.
- *Strength from Strength Finder claiming "First in-depth study of 3D model inversion attacks"*: This conflicts with the verified weakness about the "first" claim being overstated. The core substantive strength (identification of the failure mode of prior regression-based methods) is preserved in Strength #1 above, without the "first" framing.

## Novel Insights

The review reveals one insight beyond the paper's own contributions: the paper's strongest evidence is not the UltraLiDAR comparison but the ablation study (Figure 7), which independently validates the method's core logic. The VOC+DCS progression shows that even against a straw-man baseline of VOC alone (without generative modeling), the method succeeds where regression fails. This means the paper would be nearly as convincing without any generative baseline — the ablation is doing the real argumentative work. The UltraLiDAR comparison, while standard practice, is mostly corroborative.

## Suggestions

1. Revise the novelty framing to "first *successful* in-depth inversion attack on 3D voxel features" or "first analysis revealing *why* prior regression-based inversion fails" — this is accurate and avoids the tension with the paper's own citation of Hwang et al.
2. Provide a brief description of the UltraLiDAR adaptation (which modules were modified/replaced, what training procedure was used) so readers can assess fairness. Alternatively, note that the paper's core claims are validated independently of this comparison.
3. Add confidence intervals or error bars to the main quantitative tables (bootstrapped or across multiple runs/seeds).
4. Include a β-sensitivity analysis in the main text or supplement.
5. Add a brief limitations paragraph discussing boundary conditions (coarse voxelization, extreme downsampling, domain shift) explicitly.

## Score and Decision

The paper makes a genuine and well-executed contribution: it identifies a real failure mode of prior approaches, gives a convincing explanation, and proposes simple, targeted solutions that demonstrably work. The experiments are thorough, the ablation is clean, and the evaluation includes both point cloud similarity metrics and downstream task performance. The weaknesses (overclaimed novelty framing, under-specified baseline adaptation, missing variance estimates and β sensitivity) are real but minor — none undermine the core finding that occupancy classification with dispersion control succeeds where point regression fails. The paper is a solid contribution to the 3D data privacy and security literature.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>