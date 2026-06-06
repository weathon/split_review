Now I have enough data to calibrate my score. Let me assess the anchors:

**Round 1 Bracket:** Between 4.5 and 6.0 based on comparison with anchors from 4.00 (BCD, circular argument in main theorem), 5.00 (Grokking, very limited scope), 5.75 (Reevaluating Theory, novelty overlap with prior work), and 7.00 (Learning Dynamics, rigorous focused theory — clearly stronger than MGDL).

**Round 2 Narrowing:** Comparing with 4.75 (Large Learning Rates — practical but limited theory) confirms MGDL has stronger theoretical depth. Comparing with 5.75 (Reevaluating Theory) shows MGDL has more novel contributions but worse evaluation practices.

**Final score: 5.5.** The paper is clearly better than the 4.00-5.00 anchors (no fundamental theoretical flaws, broader experiments) but worse than the 5.75-7.00 range (theory-practice disconnect, missing test accuracy for classification). The eigenvalue analysis and image reconstruction are genuine strengths, but the incomplete classification evaluation and the gap between Theorem 3's scope and the experimental setup hold it back.

Now let me write the final review.

---

## Summary

This paper provides theoretical and empirical analysis of Multi-Grade Deep Learning (MGDL), which decomposes end-to-end deep network training into sequential shallow "grades" trained on residuals. The contributions include convergence guarantees for GD applied to MGDL (Theorems 1–2), a proof that MGDL with single-layer ReLU grades decomposes into convex subproblems (Theorem 3), eigenvalue analysis of a linearized GD iteration showing MGDL maintains eigenvalues within (−1,1) for stability (Theorem 4), and experiments on image reconstruction, classification, and time series tasks.

## Strengths

- **Eigenvalue analysis provides a concrete mechanistic explanation for MGDL's stability (Section 7, Figures 4–6).** By linearizing the GD iteration and monitoring eigenvalues of I−ηH during training, the paper demonstrates that SGDL's eigenvalues routinely fall below −1 (causing loss oscillations) while MGDL's stay within (−1,1). This is verified across synthetic regression, image regression/denoising, and CIFAR-10 tasks, giving direct empirical support to the theoretical convergence framework.

- **Consistent and substantial PSNR improvements in image reconstruction (Tables 1–3).** MGDL achieves gains of 0.42–3.94 dB in image regression, 0.16–4.23 dB in denoising, and 0.85–2.84 dB in deblurring across six images and multiple noise/blur levels. These are clear, reproducible results on a well-understood evaluation protocol.

- **Theorem 3 extends convexification from shallow to deep architectures via the multi-grade decomposition (Section 4).** The proof that MGDL with single hidden-layer ReLU grades reduces to a sequence of convex programs is a non-trivial extension of Pilanci & Ergen (2020). The constructive proof via activation partition regrouping is clean and self-contained.

- **Learning rate robustness experiments validate Theorem 2's wider admissible range (Section 6, Figure 2).** MGDL maintains loss < 0.001 for η ∈ [0.01, 0.3] versus SGDL's [0.03, 0.08] in synthetic Setting 1, directly demonstrating practical robustness advantages.

- **Extension to Multi-Grade Transformers with compelling time series results (Section 8).** MGT achieves test MSE of 1.8×10⁻² vs. 8.9×10⁻² for SGT on SPX data while requiring only 33% training time, demonstrating that the multi-grade principle generalizes beyond FC ReLU networks.

## Weaknesses

### Fatal

None.

### Major

- **No test accuracy reported for classification tasks despite explicit claims.** The paper states it is "evaluating SGDL and MGDL in terms of both accuracy and training dynamics" on CIFAR-100 (line 223) and claims MGDL "delivers superior accuracy" (line 225), but only training loss curves are shown (Figure 3). CIFAR-10 similarly reports only loss and wall-clock time (line 289). Lower training loss does not imply better classification accuracy, especially since MSE loss for classification can overfit without corresponding accuracy gains. The abstract's claim of results "on CIFAR-10 and CIFAR-100" is incomplete without this critical metric.

- **Theorem 3 (convexity) does not apply to any of the paper's experiments.** Theorem 3 requires single hidden-layer ReLU grades (lines 116, 124), but all experiments use multi-layer grades: image regression uses n_h=2 per grade (line 156), denoising uses n_h=3 (line 164), CIFAR-10 uses n_h=2 (line 289). The paper's most novel theoretical contribution has no experimental validation and no demonstrated practical relevance to any reported result.

- **The key distinguishing claim α_l ≪ α is asserted without proof.** Line 112 states MGDL has a broader admissible learning rate range because "α_l ≪ α," but no formal bound relating the per-grade Hessian spectral norm α_l to the full network's α is provided. Theorems 1 and 2 are structurally identical convergence results — the only substantive distinction is this unproven claim. The eigenvalue experiments provide empirical support, but the theoretical contribution is weaker than presented.

- **No control for parameter count or compute across competing methods.** SGDL trains one network while MGDL trains multiple grades sequentially, yet total parameter counts and FLOPs are never reported. For image regression, SGDL has n_h=8 hidden layers while MGDL has 4 grades × 2 layers, but the effective architecture differs due to MGDL's residual composition (equation 3). PSNR improvements could partly reflect capacity differences rather than training methodology differences.

### Minor

- **MSE loss for CIFAR-100 classification is non-standard and unjustified.** Line 223 uses MSE rather than cross-entropy, which is known to be suboptimal for classification — it doesn't naturally handle the softmax probability simplex and can suffer from vanishing gradients for confident predictions. This choice is never discussed or justified, and without cross-entropy or test accuracy results, the classification contribution is unconvincing.

- **Convergence theorems assume smooth activations but all experiments use ReLU.** Theorems 1–2 require σ to be twice continuously differentiable (lines 70, 104), while all experiments use ReLU. The paper acknowledges this implicitly in the eigenvalue discussion (line 257, "under ReLU") but never addresses how the smoothness assumption relates to practice. The compact convex set assumption (line 58) is also never verified experimentally.

- **No error bars, variance, or number of runs reported.** All experimental results appear to be single runs, making it impossible to assess statistical significance of the reported improvements.

### Trivial

None.

## Nice-to-Haves
- Ablations on the number of grades L to show how MGDL performance varies with decomposition granularity.
- Comparison with other training stabilization methods (learning rate warmup, cosine scheduling, batch normalization, skip connections) to isolate MGDL's contribution.
- Runtime comparisons for image reconstruction and classification tasks (currently only time series reports wall-clock time).
- Discussion of when MGDL might NOT help, e.g., when end-to-end training already converges well.

## Removed Points
These points are flagged to be removed, treat them with caution.
- None.

## Novel Insights

The eigenvalue analysis is the paper's most genuinely novel insight: by linearizing the GD iteration and monitoring eigenvalues of I−ηH during training, the paper provides a concrete, mechanistic explanation for MGDL's stability advantage. SGDL's eigenvalues routinely fall below −1 (causing oscillations) while MGDL's stay within (−1,1). This spectral framework connects the theoretical convergence guarantees to observed training dynamics across multiple tasks and architectures, offering an interpretable lens that goes beyond empirical observation of faster convergence.

## Suggestions
- Report test accuracy for CIFAR-10 and CIFAR-100 with both MSE and cross-entropy losses.
- Run at least one experiment with single-layer grades to demonstrate Theorem 3's convexity result in practice.
- Report total parameter counts and FLOPs for all SGDL vs. MGDL comparisons.
- Provide a formal bound or precise conditions under which α_l ≪ α, rather than asserting it.

## Calibration Report

**Anchors retrieved:**

Round 1:
| Path | Avg Score | Band | Comparison |
|------|-----------|------|------------|
| NbbsRnPBoS.md | 2.33 | Weak | Much weaker than MGDL — rejects on shallow theoretical analysis of depth in linear networks |
| l2odw7OiNw.md | 2.50 | Weak | Much weaker — batch size/learning rate scheduling with narrow contribution |
| Zap3nZhRIQ.md | 3.00 | Weak | Weaker — non-differentiability effects, limited scope |
| xpmDc76RN2.md | 2.33 | Weak | Weaker — optimization of operator networks, narrow focus |
| MY8SBpUece.md | 5.50 | Middle | Comparable — one-step feature learning theory, broader theoretical contribution but limited experiments |
| n2RIkaf1S4.md | 4.00 | Middle | MGDL is stronger — BCD paper has circular argument in main theorem |
| J4Dvxv7WnG.md | 7.00 | Middle | MGDL is weaker — deep matrix factorization EOS analysis is more rigorous and focused |
| 7Cx05z4pUc.md | 5.00 | Middle | MGDL is comparable/slightly stronger — grokking paper has very limited scope |
| 4xWQS2z77v.md | 8.00 | Strong | MGDL is much weaker — convex duality paper has deep, well-supported theory |
| AoraWUmpLU.md | 8.00 | Strong | MGDL is much weaker — Neural ODE activation functions, rigorous theory |
| TTrzgEZt9s.md | 8.00 | Strong | MGDL is much weaker — DRO with linear convergence, strong contribution |
| fMTPkDEhLQ.md | 8.00 | Strong | MGDL is much weaker — tight lower bounds, highly novel |

Round 2:
| Path | Avg Score | Band | Comparison |
|------|-----------|------|------------|
| LNYL96VIsD.md | 4.75 | Narrow | MGDL is slightly stronger — PSS for LR stability is practical but has limited theory; MGDL has more theoretical depth |
| KJYIgEteHX.md | 5.00 | Narrow | MGDL is stronger — MRI robustness paper is application-focused |
| TSrhLq5hSA.md | 4.67 | Narrow | MGDL is stronger — computational imaging hidden property, narrow |
| R9W6fFlr8W.md | 5.00 | Narrow | MGDL is comparable — primal-dual for image reconstruction, similarly mixed |
| JslyktsKMY.md | 5.75 | Narrow | MGDL is comparable — theory gap paper has novelty overlap but cleaner evaluation |
| 2xvisNIfdw.md | 5.67 | Narrow | MGDL is comparable — bilevel optimization, Accept but with mixed reviews |
| awHTL3Hpto.md | 6.33 | Narrow | MGDL is weaker — ReLU expressivity under convex relaxations, stronger theory |
| KP4xJQcG3H.md | 5.50 | Narrow | MGDL is comparable — Lagrangian proximal GD, similar contribution level |

**Round 1 bracket:** 4.5 – 6.0. MGDL is clearly stronger than the 4.00 BCD paper (no fundamental theoretical flaw) but weaker than the 7.00 EOS paper (more rigorous, focused contribution).

**Round 2 narrowing:** 5.0 – 6.0. MGDL is stronger than the 4.75 PSS paper (more theoretical depth) and comparable to the 5.50–5.75 papers, but the theory-practice disconnect and missing classification metrics push it below the 6.33 paper.

**Final score: 5.5** — The paper has genuine theoretical and empirical contributions (eigenvalue analysis, image reconstruction, learning rate robustness), but the incomplete classification evaluation, theory-practice gap (Theorem 3 not matching experiments), and the unproven key claim (α_l ≪ α) prevent it from being a strong contribution.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>