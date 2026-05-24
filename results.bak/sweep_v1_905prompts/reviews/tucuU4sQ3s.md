Now I have sufficient calibration data. Let me write the final consolidated review.

## Summary
NuSA-CL introduces a memory-free continual learning framework for vision-language models that constrains low-rank updates to a dynamically-identified null space of the current weight matrix (via SVD), then merges the update into the backbone. The method achieves a strong performance-efficiency tradeoff: 1.5M trainable parameters (40× fewer than storage-based competitors), zero auxiliary storage, and competitive accuracy (68.6/75.1/82.8% Transfer/Avg/Last on MTIL) that matches or surpasses all storage-free baselines and approaches storage-based SOTA.

## Strengths
- **Novel and clean method design.** NuSA-CL's three-stage cycle (SVD → null-space-constrained adaptation → merge) is conceptually simple and principled. The persistent constraint (freezing U_n, V_n and training only M) is a crisp distinction from prior work like MiLoRA that uses the null space only for initialization. The method is data-agnostic, requiring no replay buffer, gradient memory, or auxiliary storage.
- **Compelling efficiency-performance tradeoff.** Table 1 is the paper's strongest evidence: NuSA-CL uses 1.5M parameters vs. 59.8M for MoE-Adapters, 6.6 GB peak GPU memory vs. 15.5 GB, and 1.21 GPU-hours vs. 3.42, while achieving Transfer/Avg/Last of 68.6/75.1/82.8% — competitive with storage-based methods. This is not incremental improvement; the resource reduction is orders of magnitude.
- **Causal validation that the null space is the right subspace.** Figure 3a directly compares Tail (null-like), Top, and Random subspace selection across ranks. Tail achieves 2.57% forgetting at r=128 vs. 4.44% for Top and 4.57% for Random, and Tail wins at every rank. This isolates the null-space constraint as the causal factor for low forgetting.
- **Strong few-shot and long-sequence results.** On 5-shot MTIL (Table 2), NuSA-CL outperforms InflORA (a storage-based method) on all three summary metrics. On CIFAR-100 50-step CIL (Table 3), NuSA-CL achieves 71.85% Last accuracy, beating ZSCL by 4.4 points, with the advantage growing as sequence length increases.
- **Practical robustness.** Performance varies by less than 1 point across energy cutoffs ρ=0.80 to ρ=0.99 (Table 4b), and the SVD initialization takes <1 minute per task vs. ~81 minutes for InLoRA's data-dependent subspace design. The method does not require sensitive hyperparameter tuning.

## Weaknesses

### Fatal
None.

### Major
- **Parameter-space theory does not provide function-level forgetting guarantees.** Lemma 1 and Theorem 2 bound the Frobenius inner product ⟨W, ΔW⟩_F, which is a parameter-space quantity, not a guarantee about the model's predictions on past tasks changing. The paper is transparent about this ("local stability condition rather than a full function-level guarantee"), but the theory section is framed as "Theoretical Motivation" and the bound itself depends on ‖M_t‖_F, which can grow across tasks. The theory therefore functions as an intuition pump rather than a principled guarantee. This does not invalidate the empirical contribution, but it overstates what the theory establishes.

### Minor
- **Spectral dynamics evidence is thin.** Figure 2 shows that NuSA-CL's effective rank increases from ~51.8% to ~52.4% for the vision encoder (a 0.6% change) and from ~57.9% to ~58.8% for the text encoder (a 0.9% change). The trend is visually consistent across 10 tasks, which is encouraging, but the absolute magnitude is dwarfed by the scale of the metric itself — all methods operate in essentially the same spectral regime. The paper claims "a clear and consistent increase" and "progressive utilization of previously underexplored spectral directions," but these changes could plausibly fall within numerical sensitivity. No variance estimates, per-layer breakdowns, or statistical tests are provided. The claim is plausible but not as strongly supported as the paper's language suggests.
- **No task-order sensitivity analysis.** The paper does not report results under different task orderings. For a method that depends on the spectral structure of previously learned weights, ordering effects could be substantial. The paper lists this as future work, but a single random reordering would provide important evidence of robustness.
- **Long-sequence stress test uses highly correlated tasks.** The 50-step CIFAR-100 experiment tests a stream where all tasks share the same dataset domain. The paper does not test a mixed-domain long sequence (e.g., MTIL extended to 20+ tasks), which would more aggressively exercise null-space exhaustion. The paper acknowledges this limitation, but it weakens the scalability claim for diverse lifelong settings.
- **Re-implemented baselines not validated against original single-task numbers.** The paper re-implements LoRA, MiLoRA, and InflORA in a unified framework but does not report whether these re-implementations reproduce original paper numbers on a single-task setting. This makes it hard to assess whether comparisons are perfectly fair.

### Trivial
None beyond the above.

## Nice-to-Haves
- A per-band analysis partitioning the null space (by singular value magnitude) to test whether the null space is genuinely interference-free or whether there is gradual degradation moving to higher-energy directions within it.
- An ablation testing what happens if the null space is recomputed without merging weights (i.e., starting from original CLIP weights for each task) to isolate whether benefits come from the constraint or from knowledge accumulation through merging.
- Comparison with prompt-based methods (e.g., L2P, DualPrompt) on CL benchmarks, though the paper's scope (fixed-parameter-budget weight merging) is a reasonable exclusion.

## Removed Points
*"No comparison with prompt-based methods"* — Removed because the paper explicitly scopes itself to methods that merge weights under a fixed parameter budget, and prompt-based methods (which grow prompt pools) are a different paradigm. The related work section covers them fairly.
*"Missing related work"* — Removed because I cannot verify whether related works exist or are missing, per hard rules.
*"CIFAR-100 task correlation makes long-sequence test weak"* — This is already captured in the weaknesses section as a minor point about the need for diverse-domain testing, but was softened from the harsh critic's framing since the paper does provide some spectral evidence (Appendix Table 12) and acknowledges the limitation.

## Novel Insights
The most interesting observation from the reviews is that the persistent constraint (freezing U_n, V_n throughout training) is the critical design choice — Table 4a shows that unfreezing either basis causes a sharp performance drop (e.g., Training M, U_n, V_n drops Avg from 75.08 to 68.12). This suggests that the null-space constraint is not merely a good initialization but an active regularizer that must be maintained during the entire optimization trajectory. The spectral dynamics evidence (Figure 2), while quantitatively modest, corroborates this by showing that NuSA-CL's effective rank drifts upward across tasks while LoRA and Full-FT remain static — a qualitative difference in *how* knowledge is integrated (additive accumulation vs. overwriting) that no prior CL method for VLMs has demonstrated directly.

## Suggestions
1. **Add statistical grounding to the spectral analysis.** Run 3–5 seeds on the first 3 tasks of MTIL, compute the mean and variance of effective rank and null ratio. If the trend is statistically significant, the claim of "progressive utilization" becomes substantially stronger. If not, temper the language.
2. **Add one task-order permutation experiment.** A single random reordering of the 11 MTIL tasks would provide important evidence of robustness at minimal cost.
3. **Validate re-implemented baselines.** Report single-task accuracy for LoRA/MiLoRA/InflORA against original paper numbers to confirm the re-implementations are faithful.
4. **Tone down the theory framing.** Rename "Theoretical Motivation" to "Intuitive Justification" and explicitly state that the bounds are parameter-space heuristics, not function-level guarantees.

## Score and Decision

### Calibration Report

**Round 1 bracketing.** Three queries on continual learning for VLMs with null-space/orthogonal-projection methods:
- Weak band (avg < 3.5): anchors at 2.00 (Projected Subnetworks), 2.33 (MCIL benchmark), 2.50 (LVLM-CL), 3.00 (Task-Specific Adapters). All clearly inferior — rejected papers with unsupported claims or weak experiments.
- Middle band (3.5–7.5): anchors at 5.00 (LEAPGen, accepted but relies on GPT), 5.67 (PROOF, rejected), 6.50 (C-CLIP, accepted), 3.80 (CLIP as Online CL, rejected).
- Strong band (>7.5): anchors at 8.00 (Data-Free Distillation), 9.00 (Function Vectors), 8.00 (Hyperbolic VLM), 8.00 (Modality Gap). These are on substantially different topics.

**Initial bracket:** Between 5.5 and 8.0.

**Round 2 narrowing.** Two queries inside the bracket for spectral/orthogonal CL methods and VLM CL:
- "Divide and Orthogonalize" (6.00, rejected) — related orthogonal-projection CL. NuSA-CL is cleaner, better evaluated, and has stronger results.
- "Spectral Regularization" (6.25, accepted) — spectral regularizer for plasticity. NuSA-CL has stronger empirical contributions and a more practical deliverable.
- "Scalable Language Model with Generalized CL" (6.50, accepted) — different domain (LLMs) with re-parameterization. Comparable quality but different scope.
- "Elastic Feature Consolidation" (7.00, accepted) — exemplar-free CIL with strong theory. NuSA-CL targets VLMs specifically and has better efficiency metrics. Comparable overall quality.
- C-CLIP (6.50, accepted) — uses LoRA + distillation (requires storing old model). NuSA-CL is more novel and more efficient.
- PROOF (5.67, rejected) — has an inference mismatch issue. NuSA-CL is clearly stronger.

**Final score determination.** NuSA-CL is clearly stronger than the 5.67–6.50 anchors. It is comparable to EFC (7.00) in overall quality, though in a different sub-area (VLM CL with zero-shot preservation vs. exemplar-free CIL). Its weaknesses (modest spectral evidence, no task-order analysis, heuristic theory) are genuine but not fatal, and its strengths (clean method, strong efficiency metrics, good empirical results) are substantial. Score 7.0.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>