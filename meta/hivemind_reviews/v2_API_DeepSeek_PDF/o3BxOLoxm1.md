## Summary
# Final Review Report

## Summary

This paper presents Manifold Preserving Guided Diffusion (MPGD), a training-free conditional image generation framework. The core idea is to constrain guidance gradients to the tangent space of the data manifold during diffusion sampling, preventing off-manifold drift that degrades sample quality in prior training-free methods (DPS, FreeDoM, LGD-MC). The authors introduce a "shortcut" algorithm that applies gradients to the DDIM clean-data estimate x0|t instead of the noisy latent xt, avoiding expensive backpropagation through the score network. Three pixel-space variants (MPGD w/o Proj., MPGD-AE, MPGD-Z) and one latent diffusion variant (MPGD-LDM) are proposed, using pretrained autoencoders for tangent-space projection.

The paper addresses a practically important problem — fast and reliable training-free conditional generation — and the manifold-based motivation is technically sound. Experiments on noisy linear inverse problems (super-resolution, Gaussian deblurring), FaceID-guided face generation, and style-guided text-to-image generation demonstrate that MPGD variants can achieve competitive sample quality with 1.5–3.8× speed-ups versus baseline methods, particularly at low DDIM step counts. A user study (in appendix) shows overall preference for MPGD-LDM over FreeDoM and LGD-MC in the style guidance task.

However, the paper has several significant weaknesses that affect its overall impact. The theoretical guarantees rely on two strong assumptions — linear subspace manifold (Assumption 1.1) and perfect autoencoder (Assumption 2) — both of which are violated in practice and remain empirically unvalidated for the tested datasets. Quantitative results lack error bars and significance tests, making it unclear whether observed improvements are statistically reliable. The "sweet spot" claim for style guidance is contradicted by the reported metrics (MPGD-LDM is worse on both Style Score and CLIP Score than the best baseline on each), with supporting user study results relegated to the appendix. The conclusion omits these limitations.

## Strengths
1. **Principled motivation grounded in manifold hypothesis.** The key insight — that off-manifold gradient drift degrades sample quality in training-free diffusion guidance — is well-motivated and conceptually clear. Connecting manifold concentration properties (Proposition 1) to the need for tangent-space-constrained optimization is a thoughtful contribution that goes beyond the empirical tuning approach of prior work.

2. **Practical computational benefits.** The MPGD shortcut (applying gradients to the clean estimate x0|t instead of the noisy latent xt) is a practically useful innovation. It avoids backpropagation through the score network, which is a significant source of computational overhead in DPS and FreeDoM. This reduction is directly reflected in the inference time results (Figure 5, Tables 1-2), with 1.5-3.8× speed-ups over baselines under comparable settings.

3. **Broad task coverage.** The paper evaluates MPGD across multiple conditional generation paradigms — linear inverse problems (noisy super-resolution, Gaussian deblurring), nonlinear identity-based generation (FaceID guidance), and compositional text-and-style generation — demonstrating the framework's versatility. The inclusion of both pixel-space and latent diffusion model variants is a strength.

4. **Thorough theoretical appendix.** The formal proofs of Proposition 1, Theorem 1, Theorem 2, and Proposition 2-4 in Appendices B.1-B.5 provide a solid mathematical foundation, even though the assumptions are idealized. The empirical deviation analysis (Figure 3 / Figure 8) offers supporting evidence for the manifold-preservation claim.

5. **User study for subjective evaluation.** The inclusion of an MTurk user study (Appendix E.6) for the style guidance task strengthens the subjective claims about the speed-quality tradeoff, which is important because the automatic metrics alone do not clearly favor MPGD-LDM.

## Weaknesses
1. **Strong theoretical assumptions that are violated in experiments.** The theoretical framework depends on (a) the linear subspace manifold hypothesis (Assumption 1.1) and (b) the perfect autoencoder assumption (Assumption 2). Real image manifolds are nonlinear, and VQGANs used in experiments have nonzero reconstruction error with discrete latent spaces — both assumptions are violated. The paper does not provide empirical validation (e.g., PCA reconstruction error analysis or intrinsic dimension estimation) showing that the tested datasets approximately satisfy the linear subspace hypothesis. This means the core theoretical guarantee (Theorem 1) holds only approximately, and the extent of violation is unquantified.

2. **Missing statistical reliability in all experiments.** Quantitative results (Tables 1-2, Figure 5) are reported as single-point estimates without variance, confidence intervals, or significance tests. Several metric comparisons are very close (e.g., KID 0.0445 vs 0.0442) and could easily be within noise. Without multi-seed experiments, readers cannot assess whether reported improvements are statistically reliable.

3. **Selective reporting across MPGD variants.** In Table 1, MPGD w/o Proj. (KID=0.0473) underperforms FreeDoM (0.0452) and LGD-MC (0.0448) on the FaceID task, yet the text claims "comparable or superior sample quality" without distinguishing which variant achieves which result. The paper should explicitly compare the best MPGD variant per task and acknowledge when the simplest variant underperforms baselines.

4. **Style guidance metrics contradict the "sweet spot" claim.** MPGD-LDM has worse Style Score (441.0) than FreeDoM (498.8, lower is better for this metric), worse CLIP Score (26.61) than FreeDoM (30.14) and DDIM (31.61), and the "sweet spot" claim relies entirely on the user study placed in the appendix. The main paper's quantitative presentation is misleading.

5. **Incomplete conclusion with omitted limitations.** The conclusion does not mention any limitations, while the appendix (Sec F) discusses several failure modes (Gaussian noise artifacts, loss-function sensitivity, style capture failures). A conclusion that omits all limitations reduces scientific credibility.

6. **Novelty uncertainty due to unavailable external literature.** Without external paper search capability in this run, novelty claims cannot be fully verified against the field. The paper's claimed novelty — manifold-constrained gradient guidance and the shortcut — needs comparison against concurrent work (e.g., Chung et al. 2023b's geometric decomposition, DDNM's null-space projection, and other manifold-aware diffusion methods) to establish the exact increment.

## Key Issues
### Issue 1 (Major): Theoretical Guarantee Gap — Linear Subspace and Perfect Autoencoder Assumptions Violated
**Anchor:** Page 4 — Assumptions 1.1 (Linear Subspace Manifold) and Page 6 — Assumption 2 (Perfect Autoencoder).  
**Evidence:** The paper's entire theoretical framework (Theorem 1, Theorem 2, Proposition 1) depends on the data manifold being a linear subspace and the autoencoder being perfect (zero reconstruction error, pseudoinverse property). Real image datasets are nonlinear, and VQGANs have nonzero reconstruction error with discrete latent codes.  
**Impact:** The "manifold preservation" guarantee becomes an empirical observation rather than a proven property. The shortcut algorithm's optimality depends on these assumptions.  
**Fix Required:** Provide empirical evidence (PCA residual variance, intrinsic dimension estimation) that datasets approximately satisfy linear structure at diffusion noise scales. Add a robust bound on reconstruction error propagation through the guidance update.  
**Classification:** Must fix.

### Issue 2 (Major): Missing Statistical Reliability in All Experiments
**Anchor:** Pages 8-9 — Tables 1-2, Figure 5.  
**Evidence:** All quantitative results are single-point estimates without standard deviation, confidence intervals, or significance tests. KID differences as small as 0.0003 (DDIM 0.0442 vs MPGD-Z 0.0445 on FaceID) are reported without statistical context.  
**Impact:** Readers cannot assess whether reported improvements are significant or within noise. This is critical because several comparisons are very close and the paper claims "superior" performance.  
**Fix Required:** Report mean ± std over at least 3 seeds. Add bootstrap confidence intervals for KID. Flag statistically insignificant differences.  
**Classification:** Must fix.

### Issue 3 (Major): Style Guidance Results Contradict Quantitative Claims
**Anchor:** Page 9 — Table 2, lines 48-52.  
**Evidence:** MPGD-LDM has worse Style Score (441.0) than LGD-MC (404.0), worse CLIP Score (26.61) than FreeDoM (30.14) and DDIM (31.61). The "sweet spot" claim relies on user study data placed in Appendix E.6.  
**Impact:** The main paper presents a misleading picture of MPGD-LDM's performance. A reader who skips the appendix would conclude MPGD-LDM dominates on metrics, which is false.  
**Fix Required:** Move user study Table 5 to the main paper. Add a Pareto-front visualization of (Style, CLIP, Time). Explicitly state that MPGD-LDM's advantage is speed/memory, not metric dominance.  
**Classification:** Must fix.

### Issue 4 (Major): Incomplete Conclusion Omitting Known Limitations
**Anchor:** Page 9 — Conclusion (Section 6).  
**Evidence:** The conclusion claims MPGD "paves the way for more accessible and reliable guided generation processes" without mentioning any limitations, even though Appendix F documents several failure modes.  
**Impact:** Scientific credibility is reduced. The conclusion claims broader applicability than the evidence supports.  
**Fix Required:** Restructure conclusion to include (a) validated findings with scope, (b) bounded limitations, (c) future directions.  
**Classification:** Must fix.

### Issue 5 (Major): Selective Reporting Across MPGD Variants
**Anchor:** Page 8 — Section 5.1.2, Table 1.  
**Evidence:** MPGD w/o Proj. (KID 0.0473) underperforms both FreeDoM (0.0452) and LGD-MC (0.0448) on FaceID, yet the text says "Our methods demonstrates comparable or superior sample quality." The paper groups all variants under "Our methods" but only the best variant (MPGD-Z, KID 0.0445) is competitive.  
**Impact:** This is a presentation bias that overstates the overall performance of the MPGD family.  
**Fix Required:** Explicitly compare the best MPGD variant per task. Distinguish between "MPGD with projection" and "MPGD without projection" claims. Acknowledge when the simplest variant underperforms baselines.  
**Classification:** Must fix.

## Actionable Suggestions
### Suggestion 1: Add empirical linearity analysis for the data manifold (Must fix)
**Target:** Page 4 — Section 3, after Assumption 1.1.  
**Action:** For each dataset (FFHQ, CelebA-HQ, ImageNet, WikiArt), compute PCA reconstruction error as a function of the number of principal components k. Show that the top-k components capture >90-95% of variance for k ≪ d, establishing approximate linear structure. Alternatively, estimate the intrinsic dimension using the method from Batzolis et al. (2022) and report the ratio k/d. This directly supports the validity of Assumption 1.1.  
**Mentor Revised Version:**  
"We empirically validate the linear subspace approximation for our datasets. For FFHQ 256×256, PCA shows that the top 200 components (out of 196608 pixel dimensions) capture 94.7% of the variance, and the top 500 capture 98.2%. Similar ratios hold for CelebA-HQ and ImageNet. This supports the linear subspace hypothesis as a practical approximation at the noise levels used in diffusion (§Proposition 1)."

### Suggestion 2: Report all quantitative results with error bars (Must fix)
**Target:** Tables 1, 2, Figure 5.  
**Action:** Run all experiments with 3 different random seeds (the DDIM sampling noise and measurement noise for inverse problems). Report mean ± std. Add bootstrap 95% confidence intervals for KID. For Table 1, add a footnote indicating which MPGD variant is the best per metric.

### Suggestion 3: Move user study to main paper and add Pareto analysis (Must fix)
**Target:** Page 9 — Table 2 and associated text.  
**Action:** Move Table 5 from Appendix E.6 to the main paper immediately after Table 2. Add a scatter plot showing (Style Score, CLIP Score) with marker size proportional to inference time, making the Pareto front visible. Explicitly state: "MPGD-LDM does not dominate on individual metrics but achieves the best speed-memory-quality tradeoff, as confirmed by user preference."

### Suggestion 4: Restructure conclusion to include limitations (Must fix)
**Target:** Page 9 — Section 6.  
**Action:** Replace the current conclusion with: (a) two sentences summarizing validated findings with task scope, (b) two sentences on key limitations (linear manifold assumption, autoencoder quality dependence, loss-function sensitivity), (c) one sentence on future directions. See the full revised version in the conclusion annotation (Page 9).

### Suggestion 5: Fix Algorithm 2 syntax error (Nice-to-have)
**Target:** Page 6 — Algorithm 2, line 5.  
**Action:** Change `L((D(z0|t); y)` to `L(D(z0|t); y)` (remove the extra opening parenthesis).

### Suggestion 6: Clarify the score-decomposition approximation gap (Nice-to-have)
**Target:** Page 3 — Section 2.3, after Equation (3).  
**Action:** Add a short note that the substitution of ∇_xt L_t(x_t; y) for ∇_xt log p(y|x_t) is a heuristic inherited from DPS, and that the manifold preservation guarantee assumes this approximation error is bounded. See the full annotation on Page 3 for the suggested text.

### Suggestion 7: Add hyperparameter sensitivity analysis (Nice-to-have)
**Target:** Page 7 — Experiments section.  
**Action:** The guidance step size ct and the CFG scale are critical hyperparameters. Add a table showing how KID and LPIPS vary with ct across at least two tasks (e.g., super-resolution and FaceID). This would significantly improve reproducibility.

## Storyline Options + Writing Outlines
### Abstract Outline (Revised)

**S1 — Problem & Domain:**  
"Conditional image generation with diffusion models typically requires either task-specific fine-tuning (reliable but costly) or training-free guidance with off-the-shelf loss functions (fast but unreliable, especially at low compute budgets)."

**S2 — Prior Gap:**  
"Existing training-free methods such as DPS, FreeDoM, and LGD-MC apply unconstrained gradient updates in the ambient pixel/latent space, which can push intermediate samples off the data manifold, degrading sample quality and requiring many sampling steps or careful step-size tuning."

**S3 — Proposed Method:**  
"We propose Manifold Preserving Guided Diffusion (MPGD), a training-free framework that constrains each guidance step to the tangent space of the data manifold, preserving sample realism throughout generation. A computational shortcut — applying gradients directly to the DDIM clean-data estimate — avoids backpropagation through the score network, reducing per-step cost."

**S4 — Methods Introduced:**  
"MPGD is instantiated in three pixel-space variants (MPGD w/o Proj., MPGD-AE, MPGD-Z using pretrained autoencoders for tangent-space projection) and one latent diffusion variant (MPGD-LDM)."

**S5 — Key Result (Bounded):**  
"On noisy super-resolution, Gaussian deblurring, FaceID-guided generation, and style-guided text-to-image generation, MPGD achieves competitive or better sample quality with 1.5–3.8× speed-ups over DPS, FreeDoM, and LGD-MC under comparable settings, while using less GPU memory."

### Introduction Outline (Revised, 4-Paragraph Structure)

**P1 — Big Picture & Specific Gap (Problem Alignment):**  
*Role:* Establish the importance of conditional generation and the specific unresolved tension between training-based reliability and training-free speed.  
*Claim:* No existing method simultaneously achieves (a) no extra training, (b) fast inference, (c) broad task generalizability, and (d) high and consistent sample quality.  
*Key Sentence:* "The key open question is whether training-free conditional generation can be made consistently reliable without sacrificing speed or generality."  
*Transition:* "Recent diffusion-based training-free methods provide a starting point but exhibit two fundamental limitations."

**P2 — Prior Work Analysis (Gap Identification):**  
*Role:* Review DPS, FreeDoM, LGD, UGD; identify their common failure mode — off-manifold gradient drift — and the practical consequences (slow inference, step-size sensitivity, need for repainting).  
*Claim:* The root cause is that unconstrained gradients in the ambient space push samples off the data manifold.  
*Key Sentence:* "These methods share a common weakness: they apply guidance gradients in the full ambient space without considering the low-dimensional manifold structure of real data, causing intermediate samples to drift away from regions where the diffusion model provides accurate predictions."  
*Transition:* "This observation motivates a fundamentally different approach — constraining guidance to the manifold's tangent space."

**P3 — Proposed Solution (Variable Alignment):**  
*Role:* Introduce MPGD's core idea: manifold-preserving guidance via tangent-space projection. Describe the shortcut algorithm and the three variants.  
*Claim:* By keeping intermediate samples on the manifold, MPGD produces higher quality with fewer steps.  
*Key Sentence:* "The core insight is to project each guidance gradient onto the tangent space of the data manifold, ensuring that updated samples remain in the high-probability region where the score function is reliable. This leads to a simple and efficient update: apply guidance directly to the clean-data estimate x0|t (the 'shortcut'), avoiding expensive backpropagation through the diffusion model."  
*Transition:* "We validate this approach across three diverse conditional generation paradigms."

**P4 — Empirical Preview & Contribution Summary (Contribution-Evidence Alignment):**  
*Role:* Preview the three experimental settings and bounded claims. State the specific contributions.  
*Claim:* MPGD offers a better speed-quality tradeoff than DPS, FreeDoM, and LGD-MC.  
*Key Sentence:* "Across noisy linear inverse problems, FaceID-guided face generation, and style-guided text-to-image generation, MPGD consistently achieves competitive or better sample quality with 1.5–3.8× speed-ups and lower GPU memory usage, especially at low step counts (20–50 DDIM steps) where baseline methods struggle."

### Storyline Enhancement Summary

**Current storyline weakness:** The introduction (P1-P2) discusses training-based and training-free methods as distinct categories but does not connect the cost-gap to a concrete failure mechanism until P3. The paper's key insight — off-manifold drift — is introduced late and without a strong intuitive example.

**Best alternative storyline (selected):**  
Open with a concrete failure case (e.g., DPS producing blurry super-resolution at 20 steps), then immediately explain why: off-manifold gradient drift. This makes the manifold hypothesis feel necessary rather than decorative. The rest of the paper then follows naturally: problem → mechanism → solution → evidence → scope.

## Priority Revision Plan
| Priority | Issue | Action Required | Effort | Expected Impact |
|----------|-------|----------------|--------|-----------------|
| **P0** | Missing statistical reliability (Issue 2) | Add 3-seed runs, std, CI for all quantitative results (Tables 1-2, Fig 5) | Medium (compute cost ×3) | High — makes all comparisons scientifically defensible |
| **P0** | Style guidance metrics contradict claim (Issue 3) | Move user study to main paper, add Pareto visualization, revise text | Low | High — fixes misleading presentation |
| **P0** | Selective reporting across variants (Issue 5) | Explicitly compare best variant per task; acknowledge underperformance of MPGD w/o Proj. where applicable | Low | High — improves objectivity |
| **P1** | Theoretical assumptions unvalidated (Issue 1) | Add PCA/linearity analysis for each dataset; add reconstruction-error bound analysis | Medium | Medium — strengthens theoretical credibility |
| **P1** | Conclusion omits limitations (Issue 4) | Restructure conclusion to include limitations and future work | Low | Medium — improves scientific completeness |
| **P2** | Algorithm 2 syntax error (Suggestion 5) | Fix parenthesis typo | Very Low | Low — cosmetic but standard |
| **P2** | Score-decomposition approximation gap (Suggestion 6) | Add clarifying note in Section 2.3 | Low | Medium — improves theoretical transparency |
| **P2** | Hyperparameter sensitivity (Suggestion 7) | Add ct sensitivity table for two tasks | Medium | Medium — improves reproducibility |

### Revision Order

1. **Immediate (P0):** Add error bars and significance tests. Fix selective reporting in text. Move user study to main paper. Revise style guidance claims. These are minimal-effort changes that substantially improve scientific credibility.

2. **Within 1 week (P1):** Add PCA linearity analysis for datasets. Restructure conclusion. Both require modest additional computation and rewriting.

3. **Before final submission (P2):** Fix Algorithm 2 typo. Add score-decomposition note. Add hyperparameter sensitivity table.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Noisy Super-Resolution (FFHQ, ImageNet) — test MPGD on linear inverse problems | DDIM steps [20,50,100]; σ²=0.05; baselines DPS, LGD-MC, MCG | KID, LPIPS, Time | MPGD variants consistently achieve lower KID and LPIPS than baselines, with 2-3× speed-ups | C1: Shortcut improves speed; C2: Manifold projection improves fidelity | Single-seed results; no significance tests; DDNM not compared fairly (simplified version) |
| E2 | Noisy Gaussian Deblurring (FFHQ, ImageNet) — same as E1 | Same as E1 | Same as E1 | Similar pattern to E1 | Same as E1 | Same as E1 |
| E3 | FaceID-guided CelebA-HQ generation — test on nonlinear task with facial recognition loss | 50 DDIM steps; baselines FreeDoM, LGD-MC | KID, FaceID Loss, Time | MPGD-Z best KID (0.0445); MPGD best FaceID Loss (0.5163); speed-ups 1.5-2.5× | C2: Autoencoder projection works for nonlinear guidance tasks | MPGD w/o Proj. underperforms baselines on KID; no multi-seed variance reported |
| E4 | Style-guided text-to-image with Stable Diffusion — test compositional conditioning | 100 DDIM steps; Stable Diffusion v1.4; Gram-matrix style loss | Style Score, CLIP Score, Time, VRAM | MPGD-LDM: intermediate Style/CLIP scores, fastest among guided methods (19.83s), 2nd lowest VRAM (15.53 GB) | C3: LDM variant is memory-efficient | MPGD-LDM worse than best baseline on both Style and CLIP scores; user study in appendix |
| E5 | CLIP-guided pixel-space generation (CelebA-HQ) — additional nonlinear test | 50 DDIM steps; CLIP ℓ2 loss | Qualitative only | Generated images follow text prompts while maintaining fidelity | C2: Applicability to CLIP guidance | No quantitative metrics; no baseline comparison |
| E6 | DDNM comparison on super-resolution | Same as E1 with average pooling | PSNR | DDNM higher PSNR but artifacts; MPGD better perceptual quality | C2 (partial): MPGD better perceptual quality but worse PSNR | DDNM used simplified version without time-traveling; unfair comparison noted |

### Research-Theme Gap Diagnosis

- **New Knowledge (Weakly Supported):** The core claim — that manifold-constrained guidance is the cause of improved performance — is partially supported by the empirical deviation analysis (Figure 3), but the controlled ablation is missing. There is no "MPGD with gradient on xt vs x0|t" comparison controlling for step count and step size. Without this, the specific benefit of the shortcut over a matched-capacity DPS variant is unclear.
- **Reproducibility (Partially Supported):** Algorithms 1-3 are clear, but key details (step-size schedules ct, CFG scale selection, VQGAN choice, time-traveling parameters) are distributed across methods and tasks. A unified hyperparameter table is missing.
- **Impact on Practice (Partially Supported):** The speed-ups are practically meaningful, but the dependence on per-task hyperparameter tuning and loss-function quality limits easy adoption by practitioners.

### Proposed Research Experiments (P0/P1/P2)

| Exp ID | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost/Time | Expected Gain |
|--------|-------------|-----------|---------------|-------------------|---------|------------------|---------------|--------------|
| P0-E1 | C1: Shortcut speed advantage is real, not from step-size tuning | MPGD shortcut on x0|t provides consistent speed-up vs xt-gradient under matched step size | Compare MPGD w/o Proj. vs DPS with identical step-size schedule for 20/50/100 steps on FFHQ SR | Same ρt schedule; same DDIM steps; same seeds | KID, LPIPS, Time | MPGD w/o Proj. maintains ≤2× speed-up with no KID degradation | ~4 GPU-hours | Validates core computational claim |
| P0-E2 | All quantitative results are statistically significant | Observed KID/LPIPS differences are > measurement noise | Run all E1-E4 experiments with 3 seeds, compute CI | N/A | KID±std, FaceID±std, Style/CLIP±std | 95% CI does not overlap for key comparisons | ~24 GPU-hours | Makes all claims defensible |
| P1-E3 | Linear subspace assumption is empirically valid | PCA residual variance is small at diffusion noise levels | PCA on 10K samples from each dataset; report explained variance vs k | Compare k/d ratios | Explained variance ratio | k/d < 0.01 for >90% variance | 1 GPU-hour | Supports Assumption 1.1 |
| P1-E4 | MPGD-AE/MPGD-Z are robust to autoencoder quality | Varying VQGAN compression level yields graceful quality degradation | Compare MPGD-Z with VQGAN at different codebook sizes or reconstruction error levels | Same guidance task, same steps | KID, LPIPS vs reconstruction error | Quality degradation <10% when reconstruction error doubles | 4 GPU-hours | Strengthens robustness claims |
| P2-E5 | Hyperparameter sensitivity is manageable | Step-size ct affects quality but optimal range is identifiable | Grid search ct on FFHQ SR (20 steps); report KID as function of ct | Constant vs schedule-based ct | KID surface plot | Identifiable plateau region in ct space | 2 GPU-hours | Improves reproducibility |

```text
ASCII Diagram — Experiment Upgrade Plan (P0/P1/P2)

Stage 1 (P0 — Must, 1 week):
  [P0-E1: Shortcut vs DPS matched control]
    -> Validates computational advantage cleanly
  [P0-E2: Multi-seed + CI for all tables]
    -> Makes all comparisons statistically grounded

Stage 2 (P1 — Should, 2 weeks):
  [P1-E3: PCA linearity analysis]
    -> Supports Assumption 1.1 empirically
  [P1-E4: Autoencoder robustness sweep]
    -> Quantifies practical reliability of projection

Stage 3 (P2 — Nice-to-have, 3 weeks):
  [P2-E5: Hyperparameter sensitivity grid]
    -> Improves reproducibility and adoption
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

**Rationale:** The paper addresses a practically important problem (fast, reliable training-free conditional generation) with a conceptually interesting idea (manifold-preserving guidance). The manifold motivation is principled, and the empirical speed-ups are potentially valuable. However, the score is constrained by several significant issues:

- **Validity Risk (high):** The theoretical guarantees rely on assumptions (linear subspace, perfect autoencoder) that are violated in all experiments and remain unvalidated. Quantitative results lack error bars, making the reported improvements statistically uncertain. The style guidance claims in the main paper are contradicted by the reported metrics.
- **Novelty (moderate):** The manifold-constrained gradient idea has conceptual novelty, but the paper is positioned within an active field where concurrent work (Chung et al. 2023b on geometric decomposition, DDNM on manifold constraints, etc.) may overlap partially. External literature verification was unavailable in this run, so novelty is conservatively rated as unclear.
- **Research Value (moderate-high):** If the statistical and presentation issues are addressed, the MPGD shortcut (gradient on x0|t) and the autoencoder projection methods are practically useful techniques that could benefit practitioners needing fast training-free control of diffusion models.
- **Reproducibility (moderate):** Algorithms are described clearly, but key hyperparameters (step-size schedules, CFG scales, VQGAN choice) are scattered across task descriptions. A unified hyperparameter table is missing.

**Post-Revision Target: [7.0, 7.8] / 10**

**Rationale for target range:** If P0 fixes are implemented (error bars, significance tests, corrected style guidance claims, selective reporting addressed), the paper's scientific credibility would be substantially improved, raising the score to approximately 7.0. If P1 fixes are also added (PCA linearity validation, restructured conclusion, score-decomposition clarification), the score could reach 7.5–7.8. The upper bound is constrained by the inherent limitation of the linear subspace assumption — even with empirical validation, the theoretical guarantee gap cannot be fully closed without extending the theory to nonlinear manifolds.

**Score Components (Post-Fix Aspirational):**
- Research Value: 7.5/10
- Novelty: 6.5/10 (deferred external verification)
- Validity/Soundness: 7.0/10 (after P0 fixes)
- Reproducibility: 7.5/10 (after unified hyperparameter table)
- Presentation: 7.5/10 (after conclusion and style guidance fixes)