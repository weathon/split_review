Now I have a clear picture from the calibration. Let me finalize the review.

**Calibration Summary:**

| Anchor | Score | Decision | Comparison to PKA |
|---|---|---|---|
| Highlight Diffusion (Jt1gGIumJo) | 3.00 | Reject | PKA much stronger: 10× vs 1.52× speedup, novel architecture vs training-free heuristic, better evaluation |
| SparseDM (3kADTLbKmm) | 4.00 | Reject | PKA clearly stronger: dramatic speedup vs 1.2×, novel decomposition vs standard pruning |
| ETC (0lVQBMhsPG) | 4.20 | Reject | PKA stronger: clearer motivation, more dramatic efficiency gains, no theoretical concerns |
| Universal Guidance (pzpWBbnwiJ) | 5.25 | Accept | Comparable: PKA has stronger novelty & efficiency, Universal Guidance has broader applicability |
| DyDiT (taHwqSrbrb) | 5.50 | Accept | Most comparable: both DiT efficiency papers; DyDiT has better evaluation, PKA has larger gains |
| UniCon (uJqKf24HGN) | 7.00 | Accept | PKA below: UniCon has more thorough experiments, cleaner evaluation |

**Round 1 bracket:** 4.0–5.5
**Round 2 narrowed:** PKA sits between SparseDM (4.00) and DyDiT (5.50), comparable to Universal Guidance (5.25) but with weaker evaluation rigor.

**Final Score: 5.0** — The paper has genuine contributions (efficiency gains, attention decomposition, KV-cache) but evaluation gaps (non-standard FID, missing quantitative ablation, unexplained ablation column) prevent it from clearly exceeding the acceptance threshold.

---

## Summary
This paper proposes Patch-wise and Keyword-Aware Attention (PKA), an attention decomposition framework for efficient multi-condition control in Diffusion Transformers. Based on an analysis showing that spatial-condition attention is diagonal-dominant and subject-condition attention is keyword-localized, PKA introduces two modules: Position-Aligned Attention (PAA) for one-to-one aligned-patch interaction and Keyword-Scoped Attention (KSA) for region-restricted subject attention. A condition KV-cache and early-timestep sampling further improve efficiency. The paper demonstrates up to 10× inference speedup and 5.12× VRAM reduction at 16 conditions while reporting competitive quality metrics on three multi-condition tasks.

## Strengths
- **Empirically grounded design via attention-pattern analysis (Figures 2–3):** The method decomposition is not ad-hoc — the paper first characterizes attention sparsity patterns (diagonal-dominant for spatial conditions, keyword-localized for subject conditions), directly motivating the PAA and KSA modules. This principled approach distinguishes PKA from generic efficiency heuristics.
- **Near-constant scaling with condition count (Figures 7–8):** PKA's latency remains nearly flat as conditions increase from 1 to 16, while UniCombine grows to over 175s and OminiControl2 to ~40s. VRAM shows similar asymptotic advantage. The 10× speedup at 16 conditions is a compelling practical result and the paper's strongest piece of evidence.
- **Condition Cache as architectural consequence (Figure 4a, Section 3.2):** By restricting condition tokens to self-attend only within their type, KV projections become time-invariant — computed once and reused across all denoising steps. This is a clean, non-trivial efficiency gain that follows directly from the decomposition rather than being bolted on.
- **Early-timestep sampling grounded in controlled perturbation study (Figure 5):** The paper runs a perturbation experiment showing that perturbing conditions at early (high-t) steps causes SSIM to drop sharply (0.50 → ~0.34), while late perturbations barely affect output. This provides empirical justification for the shifted Logit-N sampling strategy.
- **KSA robustness demonstrated through threshold sweep (Figure 10):** The ablation across ε ∈ {0.2, 0.4, 0.6, 0.8} shows graceful degradation rather than catastrophic failure, making the method practically deployable without fragile hyperparameter tuning.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **PAA's softmax over a single scalar always evaluates to 1 (Eq. 2):** The softmax in Eq. 2 operates over a single scalar Q_{X,i}K_{SP,i}^T / √d, which always normalizes to 1. PAA therefore reduces to direct V_{SP,i} injection at each position — positional feature injection, not weighted attention. The Q and K projections receive zero gradient during training since ∂softmax(scalar)/∂(scalar) = 0, making them dead parameters. This does not invalidate the method (one-to-one feature transfer is the intended behavior), but the paper should acknowledge this and either justify retaining the Q/K projections or simplify the module to direct V-projection injection.
- **Unexplained "swa condition" column in Figure 9:** The ablation table includes a column labeled "swa condition" that achieves lower latency (13.58s) and VRAM (198MB) than PAA (13.63s, 237MB), yet the text claims PAA "outperform[s] even the most efficient SWA." The paper never defines or discusses this column. This creates an inconsistency that undermines confidence in the ablation's conclusions.
- **Non-standard FID computation with unreported evaluation details:** FID is computed "between the generated and ground-truth image sets" rather than against a reference distribution (e.g., training set features). The paper does not report test set size, number of generated images per method, image resolution, number of denoising steps, or any variance measures. These omissions make the quantitative quality comparisons in Table 1 less reliable — the FID gap between PKA (52.99) and UniCombine (61.03) on Subject-Canny cannot be assessed for statistical significance.
- **No quantitative component ablation for quality metrics:** The ablation studies (Sections 4.3.1–4.3.3) provide only qualitative examples and efficiency numbers. There is no ablation reporting FID/SSIM/CLIP-I for configurations that systematically add/remove PAA, KSA, KV-cache, or early-timestep sampling. The paper's claim that quality is maintained or improved therefore rests on aggregate comparisons without causal attribution to individual components.
- **Baseline training protocol not fully specified:** The paper fine-tunes FLUX.1 with LoRA for 20k iterations but does not specify whether OminiControl2 and UniCombine were retrained on the same data split under identical conditions or used with publicly released checkpoints. If training conditions differed, the quality comparison in Table 1 may conflate method differences with training differences.

### Trivial
- **μ and δ values for main experiments not reported:** The early-timestep sampling parameters used to produce Table 1 results are never stated. Only Figure 11's qualitative comparison hints at μ=0.5, δ=1.5.
- **KSA first-step handling unspecified:** The paper does not explain how KSA operates at the first denoising step, where no prior mask exists from step t−1 to reuse.

## Nice-to-Haves
- Clarify what mix of condition types is used in the scaling experiments (Figures 7–8) — are they all spatial, all subject, or a mixture?
- Report error bars or run-to-run variance for latency and VRAM measurements.
- Quantify how much attention computation is redundant, beyond visual inspection of Figures 2–3.
- Discuss the design trade-off that condition tokens never attend to the noisy image (a deliberate choice enabling KV-cache, but one that prevents conditions from adapting their representations to evolving image content during denoising).

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Harsh Critic claim that condition tokens never attending to the noisy image is an unaddressed flaw:** This is explicitly a deliberate design choice (Section 3.2) that enables the Condition Cache. The paper states condition tokens "only perform self-attention within their respective conditions." Removed as criticism; retained as nice-to-have discussion point.
- **Harsh Critic claim that KSA fidelity analysis is missing:** Figure 10 directly addresses KSA fidelity across multiple ε thresholds with both visual results and latency/VRAM numbers. Removed as factually incorrect.
- **Harsh Critic claim about cherry-picked qualitative examples without selection protocol:** This is a generic criticism applicable to virtually every paper with qualitative results. The paper includes quantitative results (Table 1) alongside qualitative ones. Removed as noise.
- **Harsh Critic criticism that the paper doesn't quantify how much attention is redundant:** Moved to Nice-to-Haves — the visual evidence in Figures 2–3 is sufficient for architectural motivation.
- **Harsh Critic claim about KSA timestep-mask validity analysis being missing:** The paper invokes temporal consistency (citing Zhou et al., 2025) and Figure 10 empirically demonstrates robustness across thresholds. Removed as partially addressed.
- **Strength Finder claim: "the paper addressed an important problem":** Generic and superficial. Removed.
- **Strength Finder claim about efficiency without quality degradation being strongly supported:** The quality evidence has real evaluation concerns (non-standard FID, no variance, unclear baseline training). Qualified in the summary rather than kept as standalone strength.
- **Strength Finder overstatement that KSA ablation shows "graceful trade-off" with strong evidence:** The KSA ablation uses only 2 examples without quantitative quality metrics. Kept the strength but with appropriate qualification.

## Novel Insights
The attention-pattern characterization (Figures 2–3) provides a concrete empirical foundation for condition-type-aware decomposition that was not previously documented in this form — showing that spatial conditions exhibit diagonal-dominant attention while subject conditions show keyword-localized activation. This typology could inform future efficient DiT designs beyond the specific PKA architecture.

## Suggestions
- Acknowledge that PAA is mathematically equivalent to position-aligned feature injection (softmax over scalar = 1, Q/K projections receive zero gradient) and either remove the dead projections or expand PAA to a small local window (e.g., 3×3 patches) that preserves some cross-position learning while retaining most efficiency gains.
- Clarify or correct the "swa condition" column in Figure 9 — if it represents a genuine configuration, define and discuss it; if an error, fix it.
- Report test set size, number of generated images, and standard deviations for Table 1 metrics. Consider computing FID against a proper reference distribution (e.g., training set features).
- Add a quantitative component ablation reporting FID/SSIM/CLIP-I for at minimum: full system, without PAA (full attention for spatial), without KSA (full attention for subject), without early-timestep sampling.
- Specify baseline training protocol (same data split, same iterations, same optimizer) and report the μ, δ values used in main experiments.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>