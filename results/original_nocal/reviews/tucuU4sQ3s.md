Now I have thoroughly verified all claims against the paper. Here is the consolidated review.

---

## Summary

This paper introduces NuSA-CL, a memory-free continual learning method for vision-language models (VLMs) like CLIP. The core idea is to perform SVD on each weight matrix before a new task, identify its low-energy "null space" (the spectral directions with small singular values), and then persistently constrain all parameter updates to lie strictly within that subspace via a frozen-basis LoRA-like formulation ($\Delta W = U_n M V_n^\top$). After training, the update is merged into the backbone, maintaining a fixed parameter budget with no replay buffer, no distillation, and no parameter growth. Experiments on the MTIL benchmark (11 tasks) and class-incremental CIFAR-100 (up to 50 tasks) show that NuSA-CL outperforms other storage-free PEFT methods (LoRA, MiLoRA) and rivals storage-based methods at a fraction of the computational cost.

## Strengths

1. **Superior efficiency-performance tradeoff.** Table 1 shows that NuSA-CL (1.5M params, zero storage) achieves Transfer 68.6%, Avg. 75.1%, Last 82.8% on MTIL, outperforming LoRA (15.7M params: 63.9/70.1/79.9) and MiLoRA (15.7M params: 62.8/68.7/77.4) while using 10× fewer trainable parameters. It rivals storage-based MoE-Adapters (85.0% Last) with 40× fewer parameters, <½ the peak GPU memory, and ~3× faster training.

2. **Core mechanism validated through careful ablations.** Table 4a shows that unfreezing the null-space bases $U_n, V_n$ drops Last from 82.79% to 77.32%, confirming the persistent constraint (not just initialization) is critical. Figure 3 confirms that the "Tail" (null-like) subspace consistently yields lower forgetting than "Top" (principal) or "Random" subspaces across all tested ranks.

3. **Spectral evidence of knowledge accumulation rather than overwriting.** Figure 2 demonstrates that NuSA-CL's effective rank gradually increases across tasks, whereas LoRA and Full-FT show static spectral behavior. This provides direct evidence that the method integrates new knowledge into previously underutilized directions rather than overwriting dominant components.

4. **Practical advantages are quantified.** Table 4b shows SVD initialization takes <1 min per task vs. ~81 min for InflLoRA's data-dependent gradient projection. Performance is stable across energy cutoff thresholds $\rho \in [0.80, 0.999]$, demonstrating no sensitive hyperparameter tuning.

## Weaknesses

### Fatal

None.

### Major

1. **Missing storage-free baselines on CIFAR-100 long-sequence benchmark.** Table 3 reports class-incremental CIFAR-100 results (10/20/50 steps) comparing NuSA-CL only against ZSCL, LwF, ICaRL, and Continual-FT. LoRA and MiLoRA — the paper's own primary storage-free competitors from Tables 1–2 — are absent. Since the paper frames long-sequence scalability as a key advantage (e.g., "the advantage grows with task length"), the absence of these baselines makes it impossible to assess whether the improvement is due to the null-space constraint or simply because PEFT methods in general handle long sequences better than full-finetuning approaches. This gap directly weakens the central claim of long-sequence scalability.

### Minor

2. **Parameter count confound between NuSA-CL and LoRA/MiLoRA baselines.** In Tables 1–2, NuSA-CL uses 1.5M trainable parameters while LoRA/MiLoRA use 15.7M. While NuSA-CL's superior performance despite fewer parameters is itself a positive result, the scientific question of whether the null-space constraint (vs. simply reduced capacity) drives the improvement cannot be fully resolved without a matched-parameter LoRA baseline (e.g., rank ≈10–16, yielding ~1.5M params). This is a cleanliness issue, not a correctness issue — reduced capacity alone would typically *hurt* plasticity, making NuSA-CL's gains on Transfer and Avg. even more striking — but an explicit control would tighten the causal evidence.

3. **Theoretical grounding is acknowledged as limited to parameter space.** Lemma 1 and Theorem 2 bound the Frobenius inner product between weights and their updates, showing cumulative parameter-space interference is controlled by the largest null-space singular value. The authors explicitly note (Section 4) that this is "not a full function-level guarantee" and is best viewed as a "local stability condition." While the paper is appropriately honest about this limitation, the theory section would be stronger with arguments connecting parameter-space bounds to function-level forgetting (e.g., via Lipschitz continuity of the model).

4. **No variance or error bars on any result.** All empirical results are reported as point estimates. While the margins between NuSA-CL and baselines are often large enough to be convincing (e.g., Last 82.8% vs. LoRA 79.9%), the absence of standard deviations or confidence intervals is a gap in statistical rigor that could matter for comparisons with smaller margins.

### Trivial

None.

## Nice-to-Haves

- A matched-parameter LoRA ablation on MTIL (rank ≈10–16) to fully isolate the effect of the null-space constraint from reduced capacity.
- Storage-free PEFT baselines (LoRA, MiLoRA) on the CIFAR-100 class-incremental benchmark.
- A function-level forgetting analysis (e.g., change in logits on past-task data) to complement the parameter-space bound.
- Task-order sensitivity analysis showing variance across different random orders.
- Visualization of the singular value spectrum evolution across tasks.

## Removed Points

- **"Uncontrolled comparison with LoRA/MiLoRA" framed as an evidential issue.** The harsh critic claimed the advantage "cannot be separated from the effect of far fewer parameters," implying that fewer parameters might explain the improvement. This is factually backwards: in continual learning, reduced capacity constrains *both* forgetting and learning. The fact that NuSA-CL achieves higher Transfer (+4.7pp) and Avg. (+5.0pp) *despite* having 10× fewer parameters than LoRA is evidence *for* the method, not a confound. The point is retained as a Minor weakness (matched-parameter control would be cleaner) but the "evidential issue" framing is removed.

- **"Weak theoretical grounding" as a methodological gap.** The paper explicitly acknowledges (Section 4, final paragraph) that the bounds are in parameter space and not a function-level guarantee. The critic's point is valid but the paper already addresses it transparently. Retained as Minor but softened.

- **Criticism about overstating the dichotomy with storage-based methods.** The comment about "unbounded growth" overlooking negligible-growth methods like InflLoRA/DIKI is a minor framing issue that does not affect the paper's technical correctness. Removed as nitpick.

- **Missing related works / citations.** Per policy, I cannot flag missing citations as a weakness.

- **Generic reproducibility concerns about missing hyperparameters, training logs, etc.** Removed per policy.

## Novel Insights

The reviewers' analyses surface an interesting tension that the paper does not fully resolve: NuSA-CL's null-space constraint operates in parameter space (controlling the Frobenius inner product between updates and prior weights), yet the ultimate claim is about preserving *function-level* knowledge. The spectral analysis in Figure 2 partially bridges this gap by showing that NuSA-CL's effective rank increases (suggesting genuine integration of new knowledge into previously unused directions) while LoRA's remains static (suggesting overwriting). This spectral fingerprint — increasing effective rank as a measurable proxy for non-destructive learning — is a genuinely insightful diagnostic that could generalize beyond this paper. The key open question is whether the missing CIFAR-100 storage-free baselines would reveal that any PEFT method (not just null-space-constrained ones) shows similar long-sequence robustness, or whether the null-space constraint is truly responsible.

## Suggestions

1. **Add LoRA/MiLoRA baselines to CIFAR-100 (10/20/50 steps).** This is the single most impactful addition: it directly tests whether the long-sequence scalability claim holds against the paper's own reference class of storage-free methods, and it is straightforward to run.
2. **Add a matched-parameter LoRA ablation (rank ≈10–16) on MTIL.** This would silence concerns about capacity confounds and cleanly isolate the null-space constraint as the causal factor.
3. **Report variance (at minimum, 3 runs with mean ± std) for the main results.** Given the paper's strong point estimates, this would significantly increase statistical credibility.

---

## Score and Decision

**Score:** 6.0

**Decision:** Accept

**Rationale:** The paper presents a clean, principled, and empirically strong method with well-designed ablations that validate the core mechanism. The main weakness — missing storage-free baselines on CIFAR-100 — is real and should be addressed, but it does not invalidate the core contribution. The MTIL results (Tables 1–2) already demonstrate that NuSA-CL significantly outperforms storage-free baselines on a challenging 11-task benchmark, and the efficiency gains over storage-based methods are substantial and unambiguous. The theoretical motivation, while limited to parameter space, is honestly scoped. The remaining issues (variance reporting, matched-parameter control) are addressable. The method is original, practical, and likely to be impactful for deploying VLMs in resource-constrained continual learning settings.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>