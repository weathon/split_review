Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

GML-NeRF proposes a multi-NeRF framework that allocates parameters along the ray dimension (rather than the point dimension) using a learnable soft gate module, combined with depth-based mutual learning to regularize geometry across sub-NeRFs. The key intuition is that point-based allocation causes "interference" because rays that don't visibly reach assigned points still contribute training signal, whereas ray-based allocation is inherently visibility-aware.

## Strengths

- **Learnable ray-level allocation eliminates hand-crafted scene partitioning.** Unlike Block-NeRF and Mega-NeRF which require manually defined scene-specific allocation rules, GML-NeRF's soft gate module is jointly optimized with sub-NeRFs, making it applicable to diverse scene types without prior knowledge. The visualizations in Figure 4 show the gate learns semantically meaningful partitions (foreground/background, directional splits) across different scene types.
- **Comprehensive evaluation across five diverse datasets.** The paper evaluates on object-centric (MaskTAT), 360-degree unbounded (NeRF-360-v2, TAT), and free-trajectory scenes (Free-Dataset, ScanNet), demonstrating broader generalizability than prior multi-NeRF methods designed for specific scene layouts.
- **The gate-guided depth mutual learning is a well-motivated regularizer.** Using gate-weighted fused depth as a soft teaching signal across sub-NeRFs (Section 4.3) is a clean design that couples allocation and cross-model consistency, with qualitative improvements shown in Figure 6.
- **Framework modularity demonstrated via Zip-NeRF integration.** The GML-ZipNeRF results (Table 13) show the method generalizes beyond the Instant-NGP backbone.

## Weaknesses

### Fatal
None.

### Major

- **The core motivation—"interference" from occluded rays—is asserted but not empirically or analytically validated.** The paper claims (Section 1, Section 4.1) that training a sub-NeRF with rays that don't contain valid information about its assigned points "interferes" with training. However, in NeRF's volume rendering, occluded points receive low transmittance weights $T_i$, which proportionally reduces their gradient magnitude during backpropagation. The paper provides no experiment or analysis measuring the actual degree of this interference or showing it causes degradation in practice. A simple experiment—e.g., training a point-based multi-NeRF while masking out gradient contributions from low-transmittance points, or measuring the difference in sub-NeRF loss between visible and occluded rays—could establish whether this interference is a real problem or a theoretical concern mitigated by volume rendering.

- **Table 3 confounds allocation dimension with fusion stage, weakening the core empirical claim.** The paper's central claim is that ray-based allocation is superior to point-based allocation. Table 3 compares "point-based fusion" (fuse sub-NeRF outputs at each point before volume rendering) vs. "ray-based fusion" (render each sub-NeRF independently, then fuse after volume rendering). These systems differ in two ways simultaneously: (1) the allocation dimension (point vs. ray) and (2) the fusion stage (pre- vs. post-volume-rendering). While this confound is partly inherent—point-based allocation naturally entails pre-rendering fusion—the paper attributes the improvement solely to "visibility-aware" allocation without acknowledging that post-volume-rendering fusion itself may contribute independently to better results (e.g., because each sub-NeRF must produce a complete, self-consistent rendered color). The claim that ray-based allocation is superior to point-based allocation remains unisolated.

- **Multi-NeRF baselines are adapted to a different backbone with a shared feature grid, potentially disadvantaging them.** The paper compares against "Switch-NGP" and "Block-NGP"—adaptations of Switch-NeRF and Block-NeRF to the Instant-NGP backbone with shared feature grids. Switch-NeRF was originally designed with per-expert MLPs that interact with a single representation; transplanting its gating mechanism onto a shared feature grid architecture is a significant design change that may not reflect Switch-NeRF's original capability. The paper is transparent about this adaptation (Table 1 note), but the comparisons are still the most important baselines for the core claim, and their fidelity is questionable.

### Minor

- **The shared feature grid limits the effective capacity scaling.** Only the MLP decoders (a small fraction of total parameters) are independent per sub-NeRF, while the feature grid is shared. Figure 5 shows near-flat improvement curves on ScanNet beyond K=2 when scaling the number of sub-NeRFs, suggesting limited practical scalability despite the "scale up model capacity" framing (Section 4). The paper does acknowledge this design choice as a practical compromise (Section 4.2), but the "scaling" narrative is stronger than what the evidence supports.

- **The claim that gating scores reflect "prediction confidence" for depth is unjustified.** Section 4.3 states "the gating score G(r) reflects the prediction confidence of each sub-NeRF for the ray r." The gating score measures which sub-NeRF a ray is *assigned* to, not which sub-NeRF produces a more accurate depth estimate. A sub-NeRF with high gating weight for a ray could still produce a poor depth estimate (e.g., early in training). The claim should be softened or supported with evidence.

- **Ablation studies are conducted on a single dataset (TAT).** Tables 2, 3, and 4 all use TAT. Given that the paper claims general applicability across five diverse datasets, demonstrating that each component's contribution holds beyond one dataset would strengthen the conclusions.

- **The (o,d)-conditioned gate has limited expressiveness.** The gate takes only a 6-dimensional input (ray origin and direction), which constrains it to learn smooth, coarse partitions of ray space. The gate cannot condition on local scene geometry or appearance at specific 3D points. The visualizations in Figure 4 confirm the gate learns coarse spatial partitions, which raises the question of how well the method handles scenes requiring fine-grained visibility-aware allocation.

### Trivial
None.

## Nice-to-Haves

- A controlled experiment isolating the allocation dimension from the fusion stage (e.g., ray-based allocation with a baseline fusion strategy, or point-based allocation paired with post-rendering fusion via per-point expert outputs rendered independently) would significantly strengthen the core claim.
- Ablations on 2–3 additional datasets beyond TAT.
- Analysis of failure cases where the gate learns trivial/degenerate allocations.
- Variance across multiple runs, given the stochastic gate initialization.

## Removed Points

- **Critic claim that baselines are "unavailable/unverifiable" or "not yet released."** The paper cites existing published work; all cited models exist and are treated as real.
- **Critic complaint about Figure 5's "unlabeled y-axis."** This is likely a parser artifact from PDF extraction; original submissions typically have proper axis labels.
- **Critic complaint about NeRF/mip-NeRF comparison being "confusing."** The paper clearly explains the 1-hour vs. full-training distinction with a footnote (†). This is a standard practice, not confusing.
- **Strength Finder's claim that Table 3 "validates" the superiority of ray-based allocation.** This is weakened by the confound identified above (allocation dimension confounded with fusion stage). Moved from strengths.
- **Strength Finder's generic claim about "comprehensive evaluation" as a core strength.** While true, it's supporting rather than core.
- **Critic's demand for missing related works.** Cannot verify existence of claimed missing works.

## Novel Insights

The key tension in this paper is between the elegance of ray-level allocation and the difficulty of empirically validating its *necessity* over point-level allocation. The natural coupling between allocation dimension and fusion stage (point-level allocation necessitates pre-rendering fusion, ray-level allocation enables post-rendering fusion) makes it difficult to isolate which factor drives improvements. The shared feature grid design, while practical, further complicates interpretation: it's unclear whether the gains come from the gate learning meaningful partitions or from the ensemble effect of multiple MLP decoders backed by a shared dense representation. The near-flat scaling curve beyond K=2 on ScanNet suggests the capacity advantage may saturate quickly, making depth mutual learning and regularization more important than pure capacity scaling for the method's practical utility.

## Suggestions

- Design an ablation that isolates the allocation dimension from the fusion mechanism: e.g., compare point-level gating with post-rendering fusion (by having each "expert" process all points but weight them by point-level gate scores) vs. the current ray-level gating with post-rendering fusion.
- Run ablations on at least 2 additional datasets (e.g., NeRF-360-v2 and ScanNet) to confirm component contributions generalize beyond TAT.
- Report results with independent (non-shared) feature grids as an ablation to understand the role of the shared representation vs. the gate mechanism.

## Evaluation

**Originality:** The ray-level allocation idea is a natural but meaningful departure from point-level multi-NeRF methods. The gate module and depth mutual learning are relatively standard components applied in a new context. Moderate originality.

**Importance of research question:** Scaling NeRF capacity for complex scenes is an important and active area. The visibility-awareness argument, even if not fully validated, addresses a real design tension.

**Claims support:** The core claim (ray-based allocation > point-based allocation) is undermined by the confounded ablation and the unvalidated motivation. The empirical comparisons against the most relevant baselines are done under a different backbone, making absolute superiority claims difficult to establish.

**Experimental soundness:** Five datasets is thorough for the main results, but single-dataset ablations and the confounded Table 3 weaken the causal claims.

**Clarity:** The paper is well-organized and clearly written. The motivation section is clearly articulated even if not fully validated.

**Community value:** The framework is practical and modular, and the idea of learnable ray-level allocation is a useful addition to the multi-NeRF toolkit. However, the community needs cleaner evidence that the proposed allocation is truly what drives improvements.

## Score and Decision

The paper makes a reasonable and practical contribution (learnable ray-level allocation for multi-NeRF with depth mutual learning), but its core claim about the superiority of ray-level allocation is undermined by a confounded ablation and an unvalidated theoretical motivation. The baseline comparisons are under a different backbone. The method still demonstrates consistent improvements across diverse datasets, and the design is modular and well-motivated. These are real contributions, but the evidentiary gaps are significant enough to warrant revision.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>