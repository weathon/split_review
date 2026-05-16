Now I have all the evidence I need. Let me produce the consolidated review.

---

## Summary

This paper proposes TopoFormer, a Transformer architecture for reactive motion prediction in two-person close interactions. The key ideas are (1) encoding pairwise Gauss Linking Integral (GLI) values—a topological measure of body-part entanglement—as input features through a Topology-Aware Spatio-Temporal (TST) embedding, and (2) a Spatial Relation-aware Relative Position Encoding (srRPE) that injects geometric proximity information into multi-head self-attention. On ExPI and CHI3D benchmarks, TopoFormer achieves substantially lower Aligned Mean Error (AME) than prior methods (21–48% over InterFormer on ExPI cross-trial) and a new metric (AIF) meant to capture interpenetration frequency.

## Strengths

- **Large and consistent AME improvements across datasets and protocols.** On ExPI (cross-trial), TopoFormer reduces AME by 21–48% relative to InterFormer across all prediction durations from 0.2s to 4.0s (Table 1). On CHI3D, the improvement is 5–26% (Table 2). These margins are large enough to suggest a genuine advance even accounting for modest baseline-reproduction differences.

- **Comprehensive ablation study validates both proposed modules independently.** Tables 4–6 systematically ablate the TST embedding (GLI features), srRPE, and their subcomponents on both AME and AIF. Removing the TST block roughly doubles AIF (Table 5), and ablating srRPE Query/Key/Value or replacing it with MLP-based encoding raises AME by 8–35% (Table 6). The ablation covers both accuracy and plausibility metrics, which is more thorough than typical in this area.

- **Effective cross-subject generalisation.** Under the challenging cross-subject protocol where test subjects have unseen bone lengths, TopoFormer still outperforms InterFormer despite InterFormer having access to the first-frame reaction pose (which reveals skeletal structure). This demonstrates robustness beyond memorising bone-length patterns.

- **Principled use of topological features for interaction plausibility.** Encoding pairwise GLI values—a continuous topological invariant that changes sharply when body parts cross—is a well-motivated strategy for reducing interpenetrations. The ablation evidence (Table 5) confirms the TST block's role in lowering GLI-based interpenetration scores.

## Weaknesses

### Fatal
None.

### Major

- **Unclear whether baselines received the same preprocessing, making quantitative comparisons less definitive.** The paper describes specific preprocessing for CHI3D (downsampling 50→25fps, removing fingers/thumbs/toes, scaling by estimated height) in Section 4.1, but never states whether the reported baseline numbers (Men et al. 2022; Goel et al. 2022; InterFormer) were obtained by re-running those methods under *identical* preprocessing, or are quoted from original papers. If the latter, the comparison may be invalid because the baselines would have been evaluated on a different (harder or easier) version of CHI3D. This ambiguity weakens the quantitative evidence for the claimed SOTA. **This is the most consequential weakness because it directly affects the believability of the central accuracy claim.**

- **Narrative overclaims on "topology" while the evidence points to geometric proximity as the primary driver of AME improvement.** The paper's motivation (Section 1, abstract) argues that existing Euclidean representations "do not capture the spatial relations between the body parts effectively" and positions the GLI-based topological features as the key novelty. Yet the ablation results repeatedly show that **srRPE—a purely geometric encoding of minimum joint-joint distance—has a larger impact on AME than the TST block** (Table 4: removing srRPE hurts more than removing TST; Table 6: replacing srRPE with MLP hurts significantly). The paper's own text acknowledges this ("srRPE has a more positive impact on the quality of the prediction motion"), but the introduction and conclusion still frame the contribution as primarily topology-aware. This mismatch between the claimed motivation and the empirical evidence is confusing and makes the paper feel oversold.

### Minor

- **The AIF metric, while a reasonable proxy, is not validated against a standard collision-detection metric.** AIF is defined based on whether per-frame GLI changes exceed a threshold (0.5). Since the TST block explicitly takes GLI values as input, a model that simply learns to output smooth GLI trajectories could score well on AIF without actually avoiding physical interpenetrations. The paper does not validate AIF against a physics-based collision test (e.g., number of colliding body segments via a mesh-overlap test). This does not invalidate the AIF results—the ablation still shows meaningful variation—but it means the claims about "more plausible interactions" rest on a metric whose real-world correspondence is unverified.

- **No error bars or variance reported.** All AME/AIF tables show single numbers. Given that deep learning results can vary with random seeds, the lack of any variance measure (especially for cross-subject protocols where per-subject variability is high) makes it impossible to assess statistical significance.

- **Reproducibility: chain construction is not fully specified.** Section 3.1 says the skeletal pose is divided into "6 serial chains" and refers to Figure 3 (left), but does not enumerate which specific joints belong to which chain. For the 18-joint (ExPI) and 19-joint (CHI3D) skeletons, the mapping from joints to chains affects both the GLI computation and the srRPE distance calculation.

- **No hyperparameter sensitivity analysis for srRPE.** The paper sets α=0.001, β=90, γ=16000 (Section 4.2) but provides no analysis of how these values affect performance or whether the results are stable under reasonable variation.

- **No qualitative comparisons of generated motion sequences.** The paper relies on ERF heatmaps (Figures 1, 4) and numerical tables, but does not show side-by-side renderings of the same interaction (e.g., hugging) predicted by TopoFormer versus InterFormer. Such visualisations would substantiate the "more synchronised and plausible interactions" claim.

### Trivial

- The paper does not discuss limitations, failure cases, or computational cost. Adding a brief limitations paragraph would be standard practice.
- The cross-subject AME gap between TopoFormer and InterFormer shrinks considerably (Table 1), and the paper's explanation (InterFormer uses the first-frame reaction pose) is reasonable but would be stronger if accompanied by an ablation that provides TopoFormer with the same first-frame information.

## Nice-to-Haves

- Validate AIF against a physics-based collision detection metric (e.g., mesh-overlap count or signed distance field interpenetration volume) to confirm that lower AIF corresponds to fewer real interpenetrations.
- Report results with multiple random seeds (at least 3) with mean and standard deviation.
- Show qualitative comparisons (rendered motion sequences) for a few representative interactions.
- Add an ablation that feeds GLI features *without* srRPE and srRPE *without* GLI, reporting both AME and a non-GLI penetration metric, to cleanly separate the contributions of topology and geometry.

## Removed Points

*These points were flagged for removal; treat with caution.*

- **"AIF is circular/tautological with the method's design."** Removed because it overstates the issue. GLI values are *input features* describing the current frame's topology; AIF measures *changes* in GLI between consecutive frames of the *output*. These are not the same object—a model can take GLI as input and still produce large GLI changes. The metric is a reasonable proxy for interpenetration; the legitimate concern (noted above in Minor) is that it lacks external validation, not that it is tautological.
- **"AME improvements on CT may stem from bone length overfitting."** Removed as speculative and contradicted by the paper's own data: TopoFormer outperforms InterFormer on the CS protocol where bone lengths are unseen, which argues *against* overfitting.
- **"The 15 pairwise GLI values are per-pose; inter-character GLI would be more relevant."** Partially removed/reduced—the AIF definition (line 171) uses A and B for the two characters with 6 chains each, meaning inter-character GLI changes *are* captured in the AIF metric. The input features use 15 intra-character pairs per pose, which is a design choice, not a flaw.
- **"InterFormer has advantage from first-frame reaction pose on CS protocol."** The paper already acknowledges this point in Section 4.4 ("it is worth noting that InterFormer...requires the first frame of the reacting person as input"). This is the authors' own observation, not a criticism they failed to address.
- Various formatting nitpicks and complaints about missing appendix content (the parser strips appendices).

## Novel Insights

The most interesting finding to emerge from the review process is the *unequal importance* of the two proposed components: the ablation evidence (Tables 4 and 6) consistently shows that the geometric proximity encoding (srRPE) contributes more to AME improvement than the topological GLI features (TST). This is not a flaw per se—both components are needed for best results—but it reveals that the paper's stated motivation (topology is what matters) is somewhat at odds with its empirical fingerprint (explicit geometric prior in attention is what drives accuracy). An honest reframing that acknowledges this, and positions the srRPE as at least as central as the GLI features, would make the paper both clearer and more convincing.

## Suggestions

1. **Clarify baseline reproduction: state explicitly** whether all baseline numbers come from re-running public code under the same preprocessing pipeline (and report that code/details), or cite original papers and justify why the comparison is fair despite preprocessing differences.
2. **Validate AIF against a physics-based penetration metric** (e.g., using SMPL body mesh overlap counts) and report the correlation. This would remove the circularity concern entirely.
3. **Reframe the contribution** to honestly reflect that both the topological (GLI) and geometric (srRPE) components are essential, and that the geometric proximity bias appears to drive more of the AME improvement. Consider repositioning the "topology-aware" framing as one part of a two-part contribution.
4. **Add error bars** by running each experiment with at least 3 random seeds.
5. **Enumerate chain-to-joint mappings** in the paper (or confirmed in the SM) for reproducibility.

## Score and Decision

The paper makes a genuine empirical contribution: the AME improvements over prior work are large (21–48% on ExPI CT), consistent across two datasets and two protocols, and supported by thorough ablation. The idea of coupling GLI-based topological features with a geometric proximity bias in attention is well-motivated and the architecture is clean.

However, the paper has two significant weaknesses that prevent unqualified acceptance: (1) the baseline comparison is not demonstrably fair—without knowing whether baselines received the same preprocessing, the reported margins are uncertain; (2) the narrative overclaims "topology-aware" as the key insight when the evidence shows the geometric proximity encoding is at least as important, creating a mismatch between framing and data. The AIF metric would also benefit from external validation.

The paper is on the right track and could be strong after revisions. In its current form, the evaluation gaps are too substantial to fully support the claims.

**Score:** 5.5

**Decision:** Reject (but encourage resubmission with stronger evaluation, validated metric, and honest reframing)

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>