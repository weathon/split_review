## Summary

This paper identifies a key limitation of conditional diffusion models: low output diversity at high classifier-free guidance scales or on small datasets. The proposed solution, CADS (Condition-Annealed Diffusion Sampler), adds scheduled, monotonically decreasing Gaussian noise to the conditioning signal during inference — heavily corrupting it early in sampling and gradually removing noise toward the end. This breaks the statistical dependence on the condition early (allowing broader exploration) and restores it later (preserving alignment). CADS requires no retraining, is plug-and-play with any sampler, and is shown to achieve SOTA FID of 1.70 (ImageNet 256×256) and 2.31 (512×512) using a pretrained DiT-XL/2 model.

---

## Strengths

- **New SOTA FID without retraining**: CADS achieves FID 1.70 on ImageNet 256×256 and 2.31 on 512×512, surpassing the previous best (MDT) purely through inference-time modification (Section "State-of-the-art ImageNet generation", line 107). This is the strongest evidence that the method addresses the diversity-quality trade-off at a level competitive with architectural improvements.

- **CADS demonstrably outperforms the natural baseline (Dynamic CFG)**: The head-to-head comparison shows CADS achieves FID 9.47 vs. 18.42 and Recall 0.62 vs. 0.39 against Dynamic CFG (lines 130-132). This gap is large and shows that the noise-annealing mechanism provides concrete benefits beyond simply downweighting guidance early.

- **Condition alignment is preserved**: Despite injecting noise into the conditioning signal, alignment metrics remain nearly identical — MPJPE stays at 0.02, CLIP-Score at 0.31, and Top-1 accuracy drops only from 0.98 to 0.96 (Table, lines 154-156). This directly supports the core design claim that annealing restores conditioning dependence by the end of sampling.

- **Broad task coverage**: CADS is validated on class-conditional generation (ImageNet, DiT-XL/2), pose-to-image (DeepFashion, SHHQ), identity-conditioned face generation (ID3PM), and text-to-image (Stable Diffusion) (Section "Setup", line 87). This breadth shows the method is not tied to a specific architecture or condition representation.

- **Compatibility with multiple samplers**: The sampler comparison table (line 116) demonstrates that CADS consistently improves FID and Recall across different off-the-shelf samplers, supporting its claim as a general-purpose sampling add-on.

---

## Weaknesses

### Fatal

None.

### Major

- **Insufficient explanation of why CADS outperforms Dynamic CFG**: The paper shows a dramatic gap (FID 9.47 vs. 18.42) but explains it only as "the additional stochasticity in CADS results in more diverse generations" (line 79). This restates the observation rather than providing a mechanism. The Bayesian intuition in Section 3.2 explains why condition-annealing *reduces conditional influence* (similar to Dynamic CFG), but does not explain why adding *noise* rather than *downweighting* produces qualitatively different sampling dynamics. Given that the method's central claim is superiority over Dynamic CFG, this is a significant gap. The paper references appendix sections for further theory, but the main text's explanation is insufficient for a top-venue paper.

### Minor

- **CADS hyperparameters are tuned per guidance scale without analysis of fixed configurations**: The paper acknowledges (line 113) that s and τ₁ are adjusted as functions of w_CFG. While transparency is commendable, the paper does not show whether CADS with *fixed* hyperparameters still outperforms DDPM across guidance scales. This makes it unclear how much of the advantage comes from the method vs. the per-configuration tuning. An ablation with fixed (s, τ₁) would clarify the robustness of the approach.

- **No variance or confidence intervals reported**: FID, Recall, and other metrics are reported as point estimates without standard deviation, confidence intervals, or even the number of generated images used for evaluation. Given that FID is known to be sensitive to sample size and implementation details, this is a meaningful gap for reproducibility and for assessing the significance of reported gains (e.g., FID 1.70 vs. MDT's previous best).

- **Missing comparisons to simple additional baselines**: Beyond Dynamic CFG, the paper does not compare to (a) adding a fixed (non-annealed) small noise to the condition, or (b) stochastic conditioning via dropout at inference. These would help isolate what the annealing schedule specifically contributes beyond general stochasticity.

- **Stable Diffusion diversity problem is only qualitatively demonstrated**: The paper shows Stable Diffusion can produce repetitive outputs (Figure 2), but does not quantify how often or under what conditions this occurs. Combined with the admission that "the benefits of CADS is less pronounced in Stable Diffusion" (line 104), the motivation for CADS on large models rests on anecdotal evidence.

- **Condition alignment metrics may lack sensitivity**: MPJPE and CLIP-Score remain identical between DDPM and CADS (lines 155-156). While this is presented as a strength, it also raises the question of whether these metrics are sensitive enough to detect degradations that would matter in practice.

### Trivial

- The exact guidance scales, sampling steps, and generation counts used for the SOTA FID results (Table SOTA) are not stated in the main text. The reader must infer them from the appendix.

---

## Nice-to-Haves

- A practical selection rule for CADS hyperparameters in a new domain (e.g., s = α·w_CFG, τ₁ = β/w_CFG) would make the method more actionable.
- An analysis of how CADS affects the number of sampling steps required (e.g., compatibility with fast samplers like DDIM at 50 steps) would strengthen the computational claims.
- Reporting whether CADS changes the distribution of latent trajectories or interacts with architecture-specific internal representations could deepen understanding.

---

## Removed Points

The following points from the inputs were removed with justification:

1. **"SOTA FID claims rest on a comparison that is not apples-to-apples"** — The critic argued that improvement might come from using a higher guidance scale rather than from CADS itself. This misunderstands the contribution: CADS *is* what enables the higher guidance scale without diversity collapse. Comparing best CADS to best MDT is standard practice. The critic also demanded reporting guidance scales for all entries in the SOTA table — this information is in the referenced table (parser-stripped) and appendix. Not a valid weakness; removed.

2. **"Dynamic CFG discussion missing from Related Work"** — Dynamic CFG is introduced as a natural baseline in Section 3.3, not as a prior method. There is no established prior work on this specific approach that the paper omits; the paper already discusses guidance-related prior work in Section 2. No substantive criticism; removed.

3. **"The hyperparameter surface is large"** — The paper has 4 parameters (s, τ₁, τ₂, ψ) but provides defaults (ψ=1) and ablates τ₂ in the appendix. Effectively 2 main knobs. This is a standard amount of tuning for a sampling method. The paper also gives guidance for adjusting by w_CFG. Not a valid weakness; removed.

4. **"SOTA claim without specifying guidance scale in main text"** — Demoted to Trivial (exact guidance scales not in main text) rather than a substantive weakness, since this information is in the referenced table and appendix.

5. **"Theoretical grounding is thin"** — Kept as Major, but re-focused specifically on the CADS-vs-Dynamic-CFG gap rather than the general theoretical grounding, since the paper does provide Bayesian intuition (Section 3.2) and references appendix sections for Langevin dynamics and score smoothing perspectives.

6. **Strength: "Demonstration that diversity problem persists even with billion-scale training data"** — This strength from the Strength Finder was kept as it is concrete and supported by the paper's observation and Figure 2.

---

## Novel Insights

Beyond the paper's own contributions, the most interesting synthetic insight from the reviewer inputs is the recognition that the large performance gap between CADS and Dynamic CFG (FID 9.47 vs. 18.42) represents an unresolved puzzle. Both methods reduce the influence of conditioning early in sampling — one by adding noise to the condition, the other by reducing the guidance weight. The fact that they produce such different results suggests that the mechanism is not simply "less conditioning = more diversity." This points toward an underexplored question in diffusion sampling: whether noise injection interacts with the model's internal representations in a qualitatively different way than weight modulation, potentially through the score function's sensitivity to corrupted inputs. The paper does not explore this, but the reviewer synthesis highlights it as a promising direction.

---

## Suggestions

1. Report exact guidance scales, number of sampling steps, and number of generated images for every quantitative result (especially the SOTA table) directly in the main text or in a clear inline table.
2. Add an ablation experiment where CADS hyperparameters (s, τ₁) are held fixed across guidance scales to isolate the contribution of the method from per-configuration tuning.
3. Provide an analysis — even a simple diagnostic — of why CADS outperforms Dynamic CFG. For example: measuring the distribution of latent trajectories, analyzing the variance of intermediate representations, or comparing score function magnitudes under both methods.
4. Report variance (std or CI) for at least the main FID results, or specify the number of samples generated and random seeds used.

---

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>