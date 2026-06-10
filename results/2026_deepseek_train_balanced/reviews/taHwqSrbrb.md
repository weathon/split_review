## Summary

The paper proposes DyDiT (Dynamic Diffusion Transformer), an architecture that reduces computation in Diffusion Transformers through two complementary mechanisms: (1) Timestep-wise Dynamic Width (TDW), which activates different attention heads and MLP channel groups depending on the generation timestep, and (2) Spatial-wise Dynamic Token (SDT), which allows easy image patches to bypass MLP blocks. The method fine-tunes pre-trained DiT models with a FLOPs-constrained loss and achieves a 51% FLOPs reduction on DiT-XL with competitive FID (2.07 vs. 2.27 for the full model), along with 1.73× real hardware speedup.

## Strengths

- **Hardware-friendly design that enables real speedup, not just theoretical FLOPs reduction.** Unlike prior dynamic networks that adapt per-sample and struggle with batched inference, DyDiT's TDW conditions width decisions solely on the timestep embedding, allowing masks to be pre-computed offline before deployment (Section 3.2, lines 109–110). This translates to verifiable wall-clock speedup: 1.73× on a V100 GPU (Table 1), not just FLOPs claims.

- **Consistent and large-margin outperformance of static pruning baselines across model scales and datasets.** Across DiT-S/B/XL (Figure 3) and five datasets (Table 2), DyDiT achieves substantially better FID than structural pruning methods at similar or lower FLOPs. For example, on fine-grained datasets, DyDiT-S achieves average FID 13.98 vs. 35.44 for magnitude pruning at comparable speed (Table 2). This directly supports the core claim that dynamic computation removes redundancy that static pruning cannot.

- **Empirically grounded motivation with concrete evidence for both redundancy dimensions.** Figure 1(a) quantifies loss differences between DiT-S and DiT-XL across timesteps, showing they diminish to near zero at later timesteps. Figure 1(b) visualizes loss maps showing spatial imbalance (higher loss on objects, lower on backgrounds). This grounds the architecture in observable phenomena before any method is introduced.

- **Comprehensive compatibility with orthogonal acceleration methods.** Tables 4–5 demonstrate DyDiT combines productively with DDIM (FID 2.36 at 1.17 s/image), DPM-solver++ (FID 4.22 at 0.46 s/image), and DeepCache (FID 2.43 at 2.99 s/image), showing that gains from dynamic architecture are additive with other efficiency techniques.

- **Ablation studies cleanly isolate each component's contribution.** Table 3 shows: TDW alone (avg FID 20.93), SDT alone (35.12), combined (16.94). The random-router baseline collapses (FID 136.01), confirming the routers learn meaningful patterns. The layer-skip variant (18.29) underperforms token-level SDT (16.94), validating that per-token bypassing is necessary to handle spatial heterogeneity.

## Weaknesses

### Fatal

None.

### Major

1. **Missing control experiment for the FID improvement claim over static DiT-XL.** The paper reports that DyDiT-XL at λ=0.5 achieves FID 2.07 vs. DiT-XL's 2.27 at half the FLOPs, and attributes this to the dynamic architecture offering "greater flexibility." However, all DyDiT models are fine-tuned from pre-trained DiT checkpoints, and no control is provided where the *static* DiT-XL is fine-tuned for the same number of iterations with the same hyperparameters but without the dynamic components. Without this control, it is impossible to tell whether the 0.20 FID improvement stems from the dynamic architecture or simply from additional fine-tuning. This does **not** undermine the core efficiency claim (halving FLOPs while maintaining competitive quality is already valuable), but the specific claim that DyDiT *outperforms* its static counterpart at reduced compute is not fully substantiated as presented.

### Minor

1. **Warm-up phase duration is not specified.** The paper states that "for a warm-up phase we maintain a complete DiT model" (line 148) to stabilize training, but never states how many iterations this phase lasts or what fraction of total fine-tuning it represents. This is a reproducibility gap in the training procedure.

2. **"Comparable" performance language is slightly overclaimed for DyDiT-S.** On fine-grained datasets (Table 2), DyDiT-S λ=0.5 achieves average FID 13.98 vs. the full DiT-S at 12.27 — a 14% relative degradation. The paper describes this as "maintaining performance levels comparable to the original DiT" (line 228). While "comparable" is subjective, the degradation is non-negligible, and the paper's own scaling analysis shows that DyDiT-S only matches the baseline at λ=0.9 (Figure 3). The framing should more accurately reflect this scale-dependent behavior.

3. **Pruning baseline protocol is not sufficiently documented.** The paper states "we set width pruning ratios to 50% for pruning methods, aiming for similar FLOPs" (line 228) but does not specify whether each method's recommended protocol (e.g., iterative vs. one-shot pruning, learning rate schedules) was followed. While this is unlikely to change the qualitative ordering (DyDiT consistently dominates), the comparison would be stronger with a brief description of the fine-tuning protocol used for each pruning baseline.

### Trivial

None.

## Nice-to-Haves

- **Reporting variance for key configurations.** FID is standardly reported as a single 50k-sample estimate in the diffusion literature, so this is not a required practice. However, since several comparisons rest on small FID differences (e.g., 2.07 vs. 2.27), reporting standard deviation over multiple seeds would strengthen confidence in the results.
- **Analysis of SDT routing stability across layers.** The token router decisions compound across layers, and a brief analysis of decision agreement between adjacent layers or stability under perturbations would add depth.
- **Runtime profiling breakdown.** The gap between 51% FLOPs reduction and 1.73× speedup (~42% reduction) is expected, but a brief breakdown of sources (gather/scatter overhead, framework costs) would strengthen the hardware-efficiency claims.

## Removed Points

These points from the reviewers were removed with justification:

- **"Pruning baselines show implausibly poor performance suggesting a setup issue"** — This is speculative. The paper uses standard pruning methods at 50% width reduction on a small model (DiT-S), and severe degradation under aggressive static pruning is a known phenomenon. The critic's "three possibilities" are conjectures not supported by evidence in the paper.
- **"No variance or uncertainty reported"** — Single-run FID with 50k samples is standard practice in the diffusion model literature (DiT, ADM, U-ViT all report point estimates).
- **"FLOPs calculation details are incomplete"** — The paper provides the FLOPs formulas for MHSA and MLP in Section 3.2 (lines 109–110) and explicitly states "total FLOPs of MHSA and MLP blocks" (line 141).
- **"Ablation asymmetry between TDW and SDT not sufficiently acknowledged"** — The paper already explicitly states that "I performs much better than II" (line 272) and explains why (most tokens bypass MLP under SDT alone).
- **"SDT router errors may compound across layers"** — A reasonable suggestion for analysis, not a demonstrated problem.
- **Strength Finder claim about DyDiT-XL outperforming DiT-XL** — This is retained as a strength (it's a real result), but qualified by the missing control weakness.
- **Strength Finder generic phrasing about problem importance** — All retained strengths are concrete and evidence-backed.

## Novel Insights

None beyond the paper's own contributions. However, the synthesis of the two reviews surfaces a useful observation: the paper's strongest finding is the *scaling trend* (larger models benefit more from dynamic computation), which is robustly supported across Figure 3, Table 1, and Table 2. The missing control primarily affects the absolute FID comparison, not this scaling trend. This suggests the paper's most defensible contribution claims should center on the scaling insight and the efficiency-quality Pareto improvement, rather than claiming to "outperform" the static model at reduced compute.

## Suggestions

1. **Add the missing control:** Fine-tune the static DiT-XL for the same number of iterations used for DyDiT-XL training, and report the resulting FID. This resolves whether the FID improvement (2.07 vs. 2.27) comes from the dynamic architecture or from additional fine-tuning. Either outcome is informative and strengthens the paper.
2. **Specify warm-up duration** (iterations or fraction of total fine-tuning) in the training procedure description.
3. **Tone down the "comparable" language for DyDiT-S** on fine-grained datasets, or add explicit discussion of the scale-dependent behavior already present in the paper.
4. **Briefly document the pruning baseline fine-tuning protocol** (learning rate, schedule, iterative vs. one-shot) in the appendix or supplement.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>