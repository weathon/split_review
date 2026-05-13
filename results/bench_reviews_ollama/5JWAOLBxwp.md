Important finding: On the "Varying density" column, the "No rotation" baseline achieves CD of 0.00611, while FER-VN-EquivReg achieves 0.00714. The method is actually **worse** than the trivial "assume no rotation" baseline in this setting, despite being marked as bold/best among the learning methods. On "Distinct sample," it barely edges out 0.00347 vs 0.00310. This is a critical finding for the registration experiments.

Now, let me consider: is this really a fair criticism? The "No rotation" row represents assuming the two point clouds are already aligned (i.e., assuming R = I). The Chamfer Distance then measures the overlap between P1 and P2 when no rotation correction is applied. For symmetrical objects (which ShapeNet has many of), this trivial baseline could be accidentally good because symmetrical objects look similar from multiple orientations. The paper explicitly notes they use CD "due to the symmetrical characteristics of ShapeNet objects" (line 172). So the low CD of the "No rotation" baseline is partially an artifact of shape symmetry in the dataset. The method IS learning rotations (as evidenced by the Copy column where it achieves 0.00000), but the CD metric makes it hard to show improvement over the trivial baseline on symmetric shapes. Still, the paper includes this row and doesn't discuss this issue, which is a weakness.

Let me write the final review now.</think>Now I have a complete picture. Let me write the final consolidated review.

## Summary

The paper proposes FER (Frequency-based Equivariant feature Representation), which maps 3D points to an n-dimensional feature space by constructing a homomorphism D: SO(3) → SO(n) that preserves rotation structure. The resulting features decompose into sinusoids whose maximum frequency is ⌊(n−1)/2⌋, providing an equivariant multi-frequency representation that can be used as input to Vector Neuron networks to overcome VN's limitation of 3D-only features.

## Strengths

- **Directly resolves VN's acknowledged limitation with empirical confirmation.** The original VN paper noted VN-OccNet (69.3 IoU) underperforms OccNet (71.4 IoU) at canonical poses. Table 1 shows FER-VN-OccNet achieves 71.9 IoU, surpassing both baselines and confirming the high-dimensional frequency features capture details that 3D VN features miss. This is the strongest result in the paper because it demonstrates an equivariant method finally beating its non-equivariant counterpart at canonical pose.

- **Shape complexity analysis provides controlled evidence of frequency benefits.** The EGAD dataset systematically categorizes shapes by complexity levels 0–25, and Figure 4 shows FER-VN-OccNet's performance degrades at a slower rate than VN-OccNet as complexity increases, directly validating the frequency-based improvement claim along a meaningful axis of variation.

- **Consistent improvements across six diverse tasks.** The method shows gains in shape completion (Table 1), shape compression (Figure 4), normal estimation (Table 2: 0.143 vs 0.152 RMSE), point cloud registration (Table 3), classification (Table 5: 90.5 vs 89.5), and segmentation (Table 6: 83.4 vs 81.4 mIoU), demonstrating the generality of the feature representation.

- **Qualitative evidence strongly aligns with quantitative gains.** Figures 1–2 show VN-OccNet smooths out car wheels, chair legs, and lamp shades while FER-VN-OccNet recovers these details, making the frequency-based improvement concrete and interpretable.

## Weaknesses

### Fatal
None.

### Major

- **No ablation on the dimensionality hyperparameter n in the main text.** The key hyperparameter n directly determines the maximum frequency ⌊(n−1)/2⌋, yet the main text contains no sweep across different n values on any task. The paper references dimensional analysis in appendices (line 139: "Dimensional analysis reveals that FER enhances detail accuracy with reduced inference impact, detailed in Appendices"), but the core claim that *frequency structure* specifically (not just higher dimensionality) drives the improvements is unsupported in the main submission. Without this ablation, it is impossible to distinguish whether gains come from the frequency decomposition or simply from having higher-dimensional features. The paper shows naive duplication [x̄, x̄, x̄] doesn't help (Section 3), but does not rule out other high-dimensional baselines (e.g., random equivariant projections, or non-equivariant Fourier features). This directly threatens the central novelty claim.

- **Relationship to spherical harmonics / Wigner-D matrices is unaddressed.** The paper's D: SO(3) → SO(n) construction and the resulting frequency decomposition bear a strong structural resemblance to irreducible representations of SO(3) via Wigner-D matrices and spherical harmonics. The paper acknowledges the connection in Section 2.1 (noting spherical harmonics map 3D points to n-dimensional features and describe rotations with Wigner-D matrices) but then claims to offer a "more accessible and intuitive alternative" without establishing whether FER produces features that are equivalent to, a subset of, or genuinely different from low-degree spherical harmonics. If FER spans the same function space, the contribution shifts from "novel representation" to "accessible rederivation"; if it differs, the paper must demonstrate this. The current framing claims both novelty and superiority over spherical harmonics without the necessary formal analysis.

- **Point cloud registration evaluation is problematic: method barely outperforms or loses to the trivial "No rotation" baseline.** Table 3 includes a "No rotation" row (assume R = I). On Distinct sample, FER-VN-EquivReg achieves CD 0.00347 vs No rotation's 0.00310 — a marginal improvement of 0.00037. More critically, on Varying density, FER-VN-EquivReg achieves 0.00714 vs No rotation's 0.00611 — the method is **worse** than assuming no rotation at all. The paper does not discuss this, despite including the baseline in the table. The likely explanation is shape symmetry in ShapeNet making the trivial baseline accidentally strong (the paper itself notes using CD "due to the symmetrical characteristics of ShapeNet objects"), but the lack of discussion and the bold-highlighting of FER-VN's numbers as "best" despite losing to the trivial baseline on Varying density is misleading.

### Minor

- **No error bars or repeated runs in any table.** Several reported improvements are within likely run-to-run variation: e.g., shape completion 71.4 → 71.9 IoU, classification 90.3 → 90.5. While single-run reporting is common in this venue, the small margins make statistical significance uncertain.

- **Overclaiming "state-of-the-art among equivariant networks" in the abstract.** The abstract says the method achieves "state-of-the-art performance among equivariant networks," but PaRINet (rotation-invariant) outperforms FER-VN on classification (91.4 vs 90.5) and segmentation (83.8 vs 83.4). The body text (line 206) partially qualifies this by noting PaRINet is "specifically designed for invariance," but abstract-level claims should be precise. The equivariant/invariant distinction is meaningful architecturally but "equivariant networks" includes methods that use equivariant features and add invariant layers — which is what FER-VN does too.

### Trivial
None.

## Nice-to-Haves

- A formal comparison between FER features and spherical harmonics features at matching dimensionality, fed through the same VN architecture, would definitively establish the novelty (or equivalence) of FER.
- Feature visualizations plotting individual frequency components ψ(x) for different frequencies (analogous to spherical harmonics visualizations) would help the reader verify the frequency decomposition and compare with spherical harmonics.
- Comparison with a non-equivariant Fourier feature baseline (e.g., Tancik-style features concatenated to coordinates) would isolate the contribution of equivariance from the contribution of frequency structure.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Likely rediscovery of spherical harmonics under different notation"** (Harsh Critic, Critical Issue #1): The core claim that FER is "precisely" equivalent to spherical harmonics/Wigner-D matrices is speculative — it is raised as a concern that needs formal analysis, but the harsh critic states it as fact. The relationship IS a genuine major weakness (moved to Major above), but the claim of definitive equivalence without proof is just as unsupported as the paper's claim of novelty without proof. Downgraded from "fatal" to "major" and reworded as an unaddressed gap rather than a proven duplication.

- **"Non-standard registration evaluation is unfair to baselines"** (Harsh Critic, Critical Issue #3): The paper clearly explains why it uses different settings (line 172: sparse 300-point ShapeNet vs. denser ModelNet40, and CD metric due to symmetry). The change of dataset/metric is explicitly justified. The real problem is that the method barely outperforms or loses to the trivial baseline — that's the substantive issue, not the dataset choice. Reframed as a Major weakness about the trivial baseline comparison above.

- **"Comparison with non-equivariant Fourier features as input to VN"** (Harsh Critic, Missing Experiments #2): This would break equivariance by construction, so it is not a fair apples-to-apples comparison. It could still be informative as a nice-to-have.

- **"Comparison with spherical harmonics features fed to VN"** (Harsh Critic, Missing Experiments #3): Moved to Nice-to-Have as it would strengthen but the paper's contribution does not fundamentally depend on showing this separation.

- **"Only 3 methods compared in shape completion"** (Harsh Critic): The comparison includes the two most relevant baselines — OccNet and VN-OccNet. This is standard for demonstrating that the proposed augmentation improves over both the non-equivariant and equivariant versions of the same architecture.

- **"No comparison with other contemporary completion methods"** (Harsh Critic): Scope creep — the paper's claim is about FER augmenting VN, not about achieving SOTA in shape completion generally.

- **"Comparison against non-equivariant methods for normal estimation"** (Harsh Critic): The paper already shows non-equivariant methods (DGCNN at 0.212) underperforming equivariant ones; the table structure is inherited from the original VN paper.

- **"Parser artifact / method section missing"** (Harsh Critic): This is a parser issue, not a paper issue. Removed per rules.

- **"Spherical harmonics are standard graduate math, not quantum mechanics"** (Harsh Critic): This is a subjective pedagogical opinion. The paper's claim about accessibility is an argument about framing that readers can judge for themselves. Not a substantive weakness.

- **StrengthFinder: "Provably equivariant high-dimensional feature representation"** as a separate strength: This is real but partially overlaps with the "directly resolves VN's limitation" strength. Consolidated.

- **StrengthFinder: "Frequency interpretation of equivariant features"** as a separate strength: This is a framing contribution, not an empirical one. If FER is equivalent to spherical harmonics, then this "interpretation" already exists in established math. Demoted to a framing observation that the paper makes but doesn't validate independently.

## Novel Insights

The registration experiment reveals an important but unacknowledged tension in the paper: using Chamfer Distance as a proxy for registration quality on symmetric shapes makes it nearly impossible to distinguish meaningful rotation recovery from trivial no-rotation baselines. The paper includes the "No rotation" row (which is commendable transparency) but doesn't discuss the implications — particularly that on the Varying density setting, the method actually loses to this baseline. This suggests either (a) the CD metric on symmetric ShapeNet shapes is insufficient for evaluating registration, or (b) the method struggles with density variation. Either interpretation would have been valuable for the community, and the paper misses the opportunity to address it.

## Suggestions

- Add a main-text ablation table showing FER-VN performance at multiple n values (e.g., n=3,5,7,9,13) on at least one task to establish that frequency structure, not just dimensionality, drives gains.
- Add a brief formal discussion (even 1–2 paragraphs) comparing the span of FER features to the span of degree-ℓ spherical harmonics for matching dimensionality. If they overlap, acknowledge it; if not, prove it.
- Discuss the "No rotation" baseline results in the registration section, particularly why the method underperforms it on Varying density, and what this implies about CD as a registration metric on symmetric shapes.

## Score and Decision

The paper identifies a genuine and important limitation of Vector Neurons (3D feature confinement) and proposes a reasonable, empirically validated solution. The core results on shape completion and the EGAD complexity analysis are compelling. However, the two major weaknesses — lack of ablation on n (the central hyperparameter) and the unaddressed relationship to spherical harmonics — leave the core novelty claim insufficiently substantiated. The registration evaluation also has a significant credibility problem. The paper makes a solid engineering contribution (high-dimensional equivariant features for VN work well in practice), but the theoretical novelty remains unclear and the empirical evidence doesn't isolate *why* it works. The paper would be substantially strengthened by addressing these issues, but could be acceptable in its current form for a venue that values practical contributions over theoretical completeness.

Originality: Moderate. The construction is motivated and different in derivation from spherical harmonics, but the functional relationship is uncharacterized.
Importance of research question: High. Equivariant 3D vision is an active and important area.
Claims well supported: Partially. Empirical results are strong but the causal explanation (frequency structure) is unverified.
Soundness of experiments: Good overall, but registration evaluation has issues and no ablation on n.
Clarity: Good. The paper is well-structured and the intuition is clear.
Value to community: Moderate-to-high. The practical impact of augmenting VN is clear.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>