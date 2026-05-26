Now I have a thorough understanding of the paper. Let me construct the consolidated review.

## Summary

This paper introduces NuSA-CL (Null Space Adaptation for Continual Learning), a memory-free continual learning framework for vision-language models. The core idea is to compute the SVD of the model's weight matrices before each new task, identify a low-energy "null space" of underutilized directions, and persistently constrain all subsequent low-rank updates to lie within that subspace. After training, the update is merged back into the backbone, maintaining a fixed parameter budget with no replay buffer, no distillation, and no growing module library. Experiments on MTIL (11-task) and CIFAR-100 (up to 50-task) benchmarks using CLIP ViT-B/16 show that NuSA-CL matches or approaches storage-based methods at a fraction of the resource cost (1.5M trainable params, 6.6 GB peak GPU, 1.21 GPU-hours) and outperforms other storage-free approaches (LoRA, MiLoRA) by substantial margins.

## Strengths

- **Superior efficiency–performance trade-off against both storage-based and storage-free methods.** Table 1 shows NuSA-CL achieving Transfer=68.6%, Avg=75.1%, Last=82.8% on MTIL with 1.5M trainable params, zero additional storage, 6.6 GB peak GPU, and 1.21 GPU-hours — matching or approaching storage-based methods (e.g., MoE-Adapters: Last=85.0%, 59.8M params, 4.8 GB storage, 3.42 GPU-hours) at a fraction of the resource footprint, while decisively outperforming all other storage-free approaches.

- **Memory-free, fixed-parameter-budget design demonstrated across every experiment.** Tables 1–3 consistently show NuSA-CL requires no replay buffer, no distillation, and no growing module library. The merge-and-update cycle (Eq. 4, Section 3.3) keeps the total parameter count constant, unlike ZSCL (10.5 GB storage), MoE-Adapters (expanding router library), DIKI (task statistics), or InflLoRA (gradient projection memory).

- **Persistent null-space constraint is empirically shown to be critical.** Table 4a: unfreezing the null-space bases drops Avg from 75.08% to 68.12% and Last from 82.79% to 77.32%. Figure 3a further shows the *Tail* (null-like) subspace consistently yields the lowest forgetting across all tested ranks (e.g., at r=128: Tail 2.57% vs. Top 4.44% vs. Random 4.57%). This confirms that strict confinement to low-energy directions, not merely low-rank form, drives the forgetting reduction.

- **Theoretical motivation with bounded interference guarantees.** Lemma 1 proves that the Frobenius inner product between existing weights and a null-space-constrained update is bounded by σ_max^null · ‖M‖_F, and Theorem 2 extends this to a cumulative bound over multiple tasks. The authors appropriately note this is a parameter-space stability condition, not a full function-level guarantee.

- **Long-sequence scalability on CIFAR-100 with widening advantage as task count grows.** Table 3: NuSA-CL achieves Last=74.51% (10-step), 73.84% (20-step), 71.85% (50-step), outperforming ZSCL (73.65%, 69.58%, 67.36%) by margins that increase from <1% to >4%. This directly validates that the dynamic null-space re-computation strategy remains effective across 50 sequential tasks.

- **Robust performance in data-limited 5-shot settings.** Table 2: NuSA-CL achieves the best Transfer (68.1%), Avg (70.3%), and Last (75.4%) among all storage-free methods on 5-shot MTIL, and surpasses InflLoRA (which uses additional gradient-projection memory) in Transfer and Last. The null-space constraint is particularly effective when data is scarce.

- **Practical computational overhead with negligible SVD cost.** Table 4b: SVD initialization per task takes <1 minute for NuSA-CL vs. ~81 minutes for InflLoRA's data-dependent subspace computation, while NuSA-CL achieves higher Avg (75.1% vs. 74.2%) and shorter total training time (1.21 vs. 4.29 GPU-hours).

- **Direct empirical evidence of knowledge accumulation versus overwriting.** Figure 2 tracks effective rank and null ratio across tasks: while LoRA and Full-FT exhibit nearly static spectral behavior, NuSA-CL shows a clear progressive increase, supporting the claim that the model fills underutilized low-energy dimensions rather than overwriting existing principal components.

## Weaknesses

### Fatal
None.

### Major

- **Scalability claims regarding larger VLMs are not empirically supported.** The paper's title, abstract, and motivation target "Zero-Shot Vision-Language Models" broadly and position NuSA-CL as a "practical and scalable solution for resource-constrained, real-world continual learning environments." However, all experiments are conducted on a single backbone: CLIP ViT-B/16 (86M parameters). The SVD step's complexity scales with matrix dimensionality, and whether the null space remains sufficiently large or the overhead remains negligible on larger models (e.g., ViT-L/14 or EVA-CLIP) is untested. While the paper acknowledges this in the limitations (Section 7) and includes a brief "Practical guidance for larger backbones" paragraph (Section 6.3), these acknowledgments do not substitute for empirical evidence. The core contribution on ViT-B/16 remains convincing, but the generalizability of the scalability claims is unsubstantiated. The paper would be substantially strengthened by demonstrating the method on at least one larger backbone.

### Minor

- **Parameter-count comparison with LoRA baselines conflates two variables.** NuSA-CL (1.5M params) is compared against LoRA and MiLoRA (both 15.7M params) at equal rank r=128. Because of its parameterization (ΔW = U_n M V_n^⊤), NuSA-CL naturally uses ~10× fewer parameters, so the comparison conflates the null-space constraint with reduced model capacity. The paper partially addresses this via the MiLoRA baseline (same parameter count as LoRA, different initialization strategy) and through extensive ablations (Table 4a, Figure 3a) that strongly suggest the persistent constraint is the key factor. Nevertheless, a direct ablation with standard LoRA matched to NuSA-CL's parameter count (rank ≈ 15–20) would cleanly sever the ambiguity and make the argument airtight.

- **Task-order sensitivity is acknowledged but not studied.** The limitations (Section 7) mention sensitivity to task order and semantic relatedness as a direction for future work, but no experiments characterize this. A simple experiment swapping two early tasks on the MTIL benchmark would provide an initial empirical characterization of this acknowledged weakness.

### Trivial
None.

## Nice-to-Haves

- **Demonstrate on a larger backbone (e.g., ViT-L/14).** This directly addresses the main evidential gap and would validate that the SVD step does not become a bottleneck and the null space remains viable, turning a point of doubt into a strength.

- **Provide wall-clock time breakdowns** for SVD versus training on larger models, to supplement the current hand-waving in Section 6.3.

- **Run a rank-matched LoRA ablation** (rank ≈ 15–20 to match NuSA-CL's 1.5M parameters) to fully decouple the effect of the null-space constraint from the effect of reduced model capacity.

- **Characterize task-order sensitivity experimentally** with a simple permutation of two early tasks on MTIL, which would be straightforward given the existing experimental infrastructure.

## Removed Points

These points were raised by reviewers but are removed for the reasons stated:

- *"Transient memory overhead of frozen bases during training contradicts 'zero storage' claim."* — The paper's "zero storage" claim refers to persistent external storage (no replay buffers, no gradient memories, no growing module libraries). The frozen bases U_n and V_n are standard computational intermediates derived from the model's own weights during training, not persistent artifacts. This is not a meaningful distinction.

- *"Table 4b comparison of initialization time conflates data-agnostic SVD with data-dependent subspace computation."* — The paper explicitly explains this difference in the accompanying text (Section 6.3: "our data-agnostic SVD is a one-time calculation per task with negligible overhead, competing methods like InLoRA require heavy, data-dependent computations").

- *Various presentation, formatting, and style nitpicks.* — These reflect parser artifacts or reviewer preferences, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the paper's framing and contributions without adding fundamentally novel observations.

## Suggestions

1. Narrow the title/claims to reflect the empirical scope, or expand the empirical scope to match the claims (e.g., add a ViT-L/14 experiment). The most impactful single addition would be a larger-backbone validation.
2. Add a rank-matched LoRA ablation (rank ≈ 15–20) to Table 1 or the appendix to isolate the effect of the persistent constraint from the reduced parameter count.
3. Include a brief task-order sensitivity experiment (permuation of two MTIL tasks) to characterize the acknowledged limitation.

## Score and Decision

This is a strong paper with a clear, novel, and well-motivated contribution. The central idea — persistently constraining updates to an SVD-derived null space — is simple, principled, and demonstrably effective. The experimental evidence is convincing within its chosen scope (CLIP ViT-B/16), and the analysis section (Figures 2–3, Table 4) provides unusually deep insight into why the method works. The limitations are honestly acknowledged.

The primary weakness is the gap between the broad narrative (scalable continual learning for "zero-shot VLMs" in general) and the narrow empirical support (a single backbone). This is a genuine limitation on the strength of the claims, but it does not invalidate the core contribution. The paper makes a real, well-supported contribution that warrants acceptance.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>