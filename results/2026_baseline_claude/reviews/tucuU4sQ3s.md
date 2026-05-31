## Summary

NuSA-CL proposes a memory-free continual learning framework for vision-language models (VLMs) such as CLIP. The core idea is a three-stage cycle per task: (1) identify low-energy (approximate null) subspace of current weight matrices via SVD, (2) learn a low-rank update strictly confined to this null space by freezing the basis vectors U_n and V_n and training only a small intermediate matrix M, and (3) merge the update into the backbone to maintain a fixed parameter budget. The method requires zero replay buffer, zero growing storage, and zero parameter count growth, while achieving performance competitive with storage-based methods at a fraction of the cost.

---

## Strengths

- **Efficiency-performance tradeoff is genuinely strong.** In Table 1 (full-shot MTIL), NuSA-CL (1.5M params, 0 additional storage, 1.21 GPU-Hours) achieves Transfer/Avg/Last of 68.6/75.1/82.8%, beating all storage-free competitors and matching storage-based DIKI (68.7/76.3/85.1%) at 40× fewer parameters and 3.6× less compute. This is a consequential demonstration, not a marginal win.

- **The 5-shot result is a standout.** In Table 2, NuSA-CL (strictly storage-free) outperforms InflORA (which maintains gradient projection memory) on all three summary metrics (68.1 vs. 66.8 Transfer; 70.3 vs. 68.9 Avg; 75.4 vs. 74.8 Last). Beating a storage-dependent method with a storage-free approach is a meaningful result and validates the core mechanism.

- **Long-sequence scalability is well-supported.** On 50-step CIFAR100, NuSA-CL achieves 71.85% Last vs. 67.36% for ZSCL (the strongest baseline), a 4.5pp improvement on the hardest sequence tested. The null-space dynamics analysis (Figure 2, Appendix Tables 11–12) demonstrates that the null space does not saturate even after 50 tasks, with 313 available null directions remaining vs. the r_max=128 cap.

- **Ablations are comprehensive and convincing.** Table 4a cleanly isolates the persistent constraint as the most critical design choice: unfreezing U_n and V_n degrades performance substantially (Transfer drops from 68.6 to 62.6). Figure 3 validates that the Tail (null-space) subspace consistently outperforms Top and Random across all ranks tested, and the stability-plasticity tradeoff at the rank dimension is empirically well-characterized.

- **Robustness to hyperparameters.** Table 4b shows results are stable across energy cutoffs ρ ∈ {0.80, 0.90, 0.95, 0.99}, requiring no sensitive tuning.

---

## Weaknesses

### Fatal
None.

### Major

1. **Theoretical analysis provides only parameter-space bounds.** Lemma 1 and Theorem 2 quantify the Frobenius inner product ⟨W, ΔW⟩_F, which measures interference in weight space, not in functional or task-performance space. The bound in Eq. 5 reduces trivially to Tr(Σ_n M) ≤ σ_{k+1} · ‖M‖_F by construction of the formulation—it follows directly from the constraint, not from new analytical insight. The paper honestly acknowledges this gap ("results are stated in parameter space and should be viewed as a local stability condition rather than a full function-level guarantee"), but the theoretical section occupies meaningful space and raises expectations it does not meet. Forgetting in practice depends on feature-space alignment, not weight-space Frobenius overlap.

2. **Experiments limited to a single backbone size.** All results use CLIP ViT-B/16. The introduction and related work frame NuSA-CL as a foundation for MLLMs and VLA models with larger encoders, and the paper explicitly discusses scaling to ViT-L/14 and 768–1024 dimensional attention projections. Providing at least one data point on a larger backbone (e.g., ViT-L/14) would substantially strengthen the scalability claims, particularly since the SVD cost grows quadratically with matrix dimension and the "null space" structure of larger models may differ.

### Minor

1. **Null space terminology is imprecise.** The "intrinsic null space" identified by NuSA-CL is the low-energy spectral subspace—singular directions corresponding to small singular values—not the true mathematical null space (directions where W acts as zero). For typical full-rank pretrained weight matrices, the true null space is nearly empty. The distinction matters because the paper's theoretical framing uses exact null space properties (e.g., U^⊤ U_n = [0; I_r]) while the method operates with approximate null directions that have small but nonzero singular values.

2. **The protection guarantee may degrade across tasks.** When W is updated via W_t = W_{t-1} + ΔW_t, the null space U_{t,n} identified at task t+1 is derived from W_t. Since W_t ≠ W_{t-1}, the new null space directions are not guaranteed to be orthogonal to the principal subspace of W_{t-1}, only to W_t. The cumulative interference bound (Eq. 6) sums local per-task bounds but does not address whether updates from task t remain non-interfering with respect to task t-2 or earlier. The empirical results suggest this is not a problem in practice, but the theoretical claim of "minimizing interference with previously acquired knowledge" across all prior tasks is not established.

3. **Re-implemented baselines.** InflORA† in Table 1 achieves only 66.2% Transfer vs. its reported value in the original paper, and MiLoRA† underperforms LoRA†, which seems counterintuitive given MiLoRA's design. While adapting to a CLIP backbone with both vision and text encoders is non-trivial and the authors note re-implementation, the gap raises mild concerns about whether these baselines are at their full potential.

### Trivial
None worth listing.

---

## Nice-to-Haves

- Experiments on at least one larger CLIP backbone (ViT-L/14 or ViT-H) would substantially strengthen scalability claims given the paper's framing.
- A task-order sensitivity experiment—since the null space is recomputed after each merge, task ordering may affect which null directions are used—would address a known fragility of many CL methods.
- A brief discussion of whether the weight-space null space corresponds to a feature-space null space (i.e., directions that do not affect the encoded representations) would make the theoretical motivation more compelling.

---

## Novel Insights

The most novel and underappreciated observation in the paper is the *knowledge accumulation vs. overwriting* dichotomy revealed in Figure 2. Standard methods (LoRA, Full-FT) exhibit near-static spectral profiles—the effective rank barely shifts across 10 tasks—suggesting they overwrite existing principal components. NuSA-CL, by contrast, progressively increases effective rank and null ratio as tasks accumulate. This provides a mechanistic interpretation of how null-space-constrained updates build richer representations over time rather than simply displacing prior knowledge, and is a concrete, measurable behavioral distinction from standard continual fine-tuning that the broader CL community should find useful as an analysis tool.

---

## Suggestions

- Add a function-space interpretation of the interference bound or replace the current theory section with an empirical analysis of how null-space constraint translates to gradient alignment, which would be more directly informative.
- Include at least one experiment on ViT-L/14 to demonstrate that SVD cost remains manageable and null-space structure persists at larger scales.
- Report task-order sensitivity: run the 11-task MTIL sequence in at least 2–3 permutations and report variance, which is cheap given the method's low computational cost.
- Clarify the InflORA re-implementation details and explain the gap to its published numbers, as this affects the validity of the 5-shot comparison where NuSA-CL reportedly beats a storage-based method.

---

## Score and Decision

NuSA-CL is a clean, practical contribution to continual learning for VLMs. The method is well-motivated, simple to implement, and achieves a genuinely favorable efficiency-performance tradeoff with strong empirical support across multiple benchmarks and thorough ablations. The main gaps are a modest theoretical section that provides parameter-space rather than functional guarantees, and experiments limited to a single backbone. Neither is fatal, and the empirical case for the method is convincing.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>