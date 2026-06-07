## Summary

DynamicCity proposes a two-stage 4D LiDAR scene generation framework. Stage 1 uses a VAE to encode temporal sequences of semantic occupancy data into a compact HexPlane representation (six 2D feature planes), introducing a transformer-based **Projection Module** for informed dimension reduction (vs. naive averaging) and an **Expansion & Squeeze Strategy** for parallel decoding. Stage 2 uses a DiT-based diffusion model with a **Padded Rollout Operation** to arrange the heterogeneous HexPlane planes into a unified square feature map for generation, supporting conditional modes (trajectory-guided, command-driven, layout-conditioned, inpainting). The method is evaluated on CarlaSC, Occ3D-Waymo, and Occ3D-nuScenes datasets against the OccSora baseline.

---

## Strengths

- **Projection Module delivers a clean, quantified improvement over naive averaging.** The ablation in Tab.~\ref{tab:vae_ablation} shows a 12.56\% mIoU gain by using a transformer-based projection instead of conventional averaging to construct HexPlane planes. This directly validates the architectural choice and addresses a real limitation of prior HexPlane usage (lines 75–80, 155).

- **Expansion & Squeeze Strategy achieves simultaneous gains on three axes.** ESS improves mIoU by 7.05\%, training speed by 2.06×, and memory by 70.84\% compared to point-by-point querying (lines 82–85, 155). Improving reconstruction quality, speed, and memory together—rather than trading one off—is a genuine systems contribution for memory-intensive 4D LiDAR data.

- **Padded Rollout Operation is a principled solution with controlled ablation.** PRO addresses a non-trivial representation alignment problem (six planes with heterogeneous geometries) and is compared against two reasonable alternatives (Direct Unfold, Vertical Concat) in Tab.~\ref{tab:fid_hexplane}, showing clear superiority (lines 101–103, 160).

- **VAE ablation studies are thorough and decompose contributions cleanly.** The paper isolates the contribution of the Projection Module, ESS, HexPlane dimension choices, and PRO arrangement strategy through separate ablation tables, making it possible to assess each component's independent value.

---

## Weaknesses

### Fatal
None.

### Major

- **Only one baseline compared, which is insufficient to support the strength of the claims made.** Both reconstruction (Tab.~\ref{tab:miou}) and generation (Tab.~\ref{tab:fid}) compare DynamicCity against OccSora alone. The paper claims to "significantly outperform existing state-of-the-art 4D LiDAR generation methods" (line 5) and "achieves significantly better 4D reconstruction and generation performance than previous SoTA methods" (line 36). With a single comparison point, these claims are underdetermined. LiDAR4D (Zheng et al., 2024) is cited in related work but not compared. Ablations validate the paper's own components, but the actual SOTA comparison rests on one data point. This weakens confidence that the architecture, rather than evaluation differences, drives the reported margins.

- **No temporal consistency metrics for a method whose central claim is "4D" temporal modeling.** The paper's entire motivation is that prior work captures only static scenes while DynamicCity captures "temporal evolution" (lines 5, 14, 166). Yet generation evaluation relies entirely on per-frame metrics (FID, IS, KID, Precision, Recall) computed either from 2D renderings or a 3D encoder (line 136). None of these measure temporal coherence — whether objects move smoothly, whether vehicles that disappear/reappear are physically plausible, or whether temporal dynamics match real driving data. A method generating high-quality individual frames with jittery motion would score well on these metrics while failing at the paper's stated goal. This is a structural evaluation gap: the core claim is not tested by the metrics chosen.

- **Downstream applications are claimed as contributions but evaluated only qualitatively.** Section 3.3 describes five conditional generation modes (trajectory-guided, command-driven, layout-conditioned, HexPlane extension, inpainting) as core capabilities (lines 110–118). Yet the evaluation in Sec. 5 states only that the model "demonstrates the ability to generate reasonable scenes and dynamic elements while following the prompt to a certain extent" (line 146). No quantitative metrics are provided for any application — e.g., trajectory following error, command classification accuracy, layout mIoU, or inpainting fidelity. If these are qualitative demonstrations, they should be scoped accordingly rather than presented as contributions of equal weight to the core pipeline.

- **The magnitude of reconstruction gains over OccSora is anomalously large and unexplained.** The reported mIoU improvements are 38.6\%, 31.8\%, and 43.2\% across the three datasets (line 140). These are extremely large for a semantic segmentation reconstruction task, where typical improvements between methods are single-digit percentages. The paper does not discuss why the gains are this large — whether OccSora's VAE uses a different latent size, input resolution, frame count, or class definition. While the results may be correct, the reader cannot assess their credibility without understanding why the margin is so large, particularly given the single-baseline comparison.

### Minor

- **The "3D Encoder" used for computing 3D metrics (FID, KID) is not described.** Line 136 mentions training a 3D Encoder to extract features from 3D data for metric computation, but its architecture, training procedure, and data are not specified. Since FID/KID are highly sensitive to the feature extractor, this lack of detail limits reproducibility.

- **No variance or confidence intervals reported for any metric.** Even for the main reconstruction and generation results, the paper reports single numbers without standard deviations or significance tests. Given known variance in generative evaluation metrics, reporting some measure of uncertainty would strengthen the evidence.

- **Incomplete section references.** Lines 118 and 136 state "For more details, kindly refer to Sec." without completing the section number. This appears to be an unresolved placeholder.

- **No inference cost reported.** VAE training efficiency gains are reported (2.06× speedup, 70.84% memory reduction), but the inference cost of the full pipeline (VAE encode → DiT denoise → VAE decode) is not provided. For a method targeting large-scale generation, this is practically relevant information.

### Trivial

- **Name inconsistency in the conclusion.** Line 166 refers to "our Masked Rollout Operation" while the body of the paper (and the contribution listing) consistently uses "Padded Rollout Operation." These should be harmonized.

---

## Nice-to-Haves

- A discussion of limitations and failure cases (e.g., how performance degrades with fast-moving objects, longer sequences, or varying object density) would improve the paper's credibility.
- The PRO ablation could be strengthened by comparing against a 3D DiT that processes the full 4D volume natively, to isolate whether the temporal bridging via PRO is the optimal arrangement.
- Reporting standard deviations or confidence intervals for main results would tighten statistical rigor.

---

## Removed Points

These were raised by reviewers but filtered out as speculative, scope-creeping, or based on misunderstanding:

- *"OccSora VAE may be dramatically undertrained"* — speculative; the core concern about unexplained large margins is retained, but the specific conjecture is removed.
- *"Patch size explanation is insufficient for varying plane sizes"* — the paper provides the dimension formula and ablation; this is adequately addressed by the PRO design and comparison ablations.
- *"Static methods (SemCity, X³, PDD) should be compared for VAE reconstruction"* — these methods target static scenes; demanding 4D comparisons against them is scope creep.
- *Missing related works* — per policy, I do not speculate about absent citations.
- *Formatting/style nitpicks* — parser artifacts, not author errors.

---

## Novel Insights

None beyond the paper's own contributions. However, a synthesized observation: the paper has a technically sound and well-ablated architecture, but the evaluation framework is substantially weaker than the architecture deserves. The Projection Module and ESS are validated internally through controlled ablations showing double-digit mIoU gains over simple baselines; these internal comparisons are actually the strongest evidence in the paper. The external comparison (single OccSora baseline) is the weakest link. This asymmetry — strong internal validation but weak external positioning — suggests the paper would benefit far more from adding baselines and temporal metrics than from any architectural change.

---

## Suggestions

1. **Add at least one additional 4D LiDAR baseline** (LiDAR4D, or reproduce OccSora's VAE under matched settings) to the reconstruction and generation comparisons. Without this, the SOTA claim cannot be evaluated.
2. **Incorporate temporal consistency metrics** such as per-pixel flow warping error, temporal semantic consistency for static regions, or object trajectory smoothness. The 4D claim requires measuring temporal quality, not just per-frame quality.
3. **Provide quantitative evaluation of at least one downstream application** (e.g., trajectory following error for trajectory-conditioned generation, or mIoU for layout-conditioned generation).
4. **Discuss why the reconstruction margins over OccSora are so large (38–43% mIoU).** Clarify whether the comparison is apples-to-apples on latent size, resolution, frame count, and class definitions.
5. **Describe the 3D Encoder architecture** used for metric computation.

---

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>