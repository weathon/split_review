Now let me perform calibration searches to anchor the score.Round 1 bracket: **5.5 to 7.5**. The paper is more specific and better-evaluated than the 5.5 RED-diff anchor, and roughly comparable to the 6.5 DDS anchor. Now narrowing.Now I have sufficient information to write the final review. Let me compile everything.

---

## Summary

This paper proposes ADMM Plug-and-Play (ADMM-PnP) with a novel AC-DC (Auto-Correction / Directional Correction) denoiser for solving imaging inverse problems using pre-trained diffusion score functions. The core insight is that ADMM iterates—especially when combined with dual variables—lie off the noisy data manifolds where score functions are trained; the AC step (Gaussian noise injection) approximates manifold proximity while the DC step (conditional Langevin dynamics) precisely refines iterates onto the target manifold. The paper also provides convergence analysis: Theorem 2 establishes high-probability ball convergence under strongly convex data-fidelity, and Theorem 3 establishes bounded-denoiser convergence under an adaptive step-size schedule without requiring convexity.

---

## Strengths

- **Non-trivial convergence theory for score-based ADMM-PnP.** Theorems 1–3 meaningfully extend prior fixed-point theory (Ryu et al. 2019; Chan et al. 2016) to cover diffusion-score denoisers. Theorem 2 proves the AC-DC denoiser is weakly nonexpansive with high probability (Eq. 14), yielding ball convergence under constant step sizes for μ-strongly convex losses. Theorem 3 removes convexity via an adaptive ρ-schedule with explicit scheduling conditions (Theorem 3(b)).

- **Strong, comprehensive empirical evaluation.** Table 1 reports PSNR, SSIM, and LPIPS across six distinct inverse problems (super-resolution, random inpainting, box inpainting, motion deblurring, Gaussian deblurring, phase retrieval) on both FFHQ and ImageNet (100 images each), against eight baselines. Both Ours-tweedie and Ours-ode achieve best or second-best performance in the large majority of settings, with clear margins over DiffPIR, DDRM, and RED-diff.

- **Well-motivated three-stage design.** The AC-DC structure is derived from first principles: Eq. (9) decomposes z_ac into signal + noise terms; Eqs. (10) show that the conditional Langevin target p(z_{σ^(k)} | z_{ac}^(k)) has its support inside M_{σ^(k)}, directly justifying DC's role. The rationale for why AC alone is insufficient is clearly explained.

---

## Weaknesses

### Fatal
None.

### Major

- **No NFE or wall-clock comparison.** The proposed method accumulates substantial computation per outer ADMM iteration: up to 1,000 Adam steps in the x-subproblem, J=10 Langevin steps (DC), plus a 10-step ODE or Tweedie evaluation. The primary diffusion competitor is cited as "DAPS-4K," explicitly flagging a 4,000-NFE budget. Without reporting NFE counts or runtimes for all methods, readers cannot determine whether the performance gains arise from the AC-DC design or from consuming a larger compute budget. The authors acknowledge this in the Limitations section ("each iteration of AC-DC denoiser needs multiple score evaluations"), but the absence of a concrete comparison table leaves the empirical claims incomplete.

- **DC ablation is qualitative only, leaving the core novelty claim unsupported quantitatively.** Figure 5 shows visual comparisons for J=0, 10, 20 on phase retrieval, but no quantitative metrics (PSNR/SSIM/LPIPS) are reported for these conditions. More critically, there is no ablation isolating the DC contribution *beyond* AC: since prior methods (DiffPIR Eq. (3), SNORE Eq. (5)) already perform noise injection analogous to AC, the paper needs a table showing (AC-only) vs (AC+DC) performance quantitatively. Without this, DC's independent contribution—the paper's primary algorithmic novelty over existing noise-injection methods—is demonstrated only visually on one task.

- **The practical noise schedule does not satisfy the stated convergence conditions in Theorem 3(b).** The experiments use σ^(k) = max(0.1, 10 − (10 − 0.1)·k/W) and σ_{s^(k)} = 0.1/√σ^(k). For k ≥ W, σ^(k) = 0.1 (constant), giving σ_{s^(k)} ≈ 0.316 (also constant). Theorem 3(b) requires lim_{k→∞} σ^(k) = 0 and lim_{k→∞} σ_{s^(k)} = 0—conditions clearly violated by this schedule. Thus, for the majority of the experimentally tested non-convex tasks (phase retrieval, box inpainting, super-resolution), neither the strongly-convex Theorem 2 nor the properly-conditioned Theorem 3 applies to the algorithm actually run. The Limitations section acknowledges the convexity gap but does not acknowledge the schedule incompatibility.

### Minor

- **Gaussian likelihood approximation in DC is not empirically validated.** The DC step approximates p(z_{ac}^(k) | z_{σ^(k)}) as Gaussian, valid when Var(s^(k))^{1/2} ≪ σ^(k) (Section 3). This condition is stated but never verified for the practical schedules used—there is no ablation, residual comparison, or quantitative check. Since this approximation determines what distribution DC actually targets, its quality matters for both correctness of the manifold argument and for trusting that J=10 Langevin steps are sampling anything close to the right distribution.

- **DCDP outperforms on PSNR for box inpainting by a non-trivial margin.** Table 1 shows DCDP at 25.230 dB vs. Ours-tweedie at 24.025 dB (FFHQ). The paper's claim that the method achieves "best or second-best performance in almost all inverse problems" is technically accurate, but this 1.2 dB deficit is not discussed in the text. On SSIM and LPIPS, the proposed method leads, so the claim is not false—but a brief acknowledgment and discussion would be appropriate.

### Trivial

- Table 1 contains two PMC rows for superresolution with distinct non-empty values (27.761/0.639/0.332 and 23.774/0.421/0.407) and additional blank PMC rows for other tasks, with no caption explanation distinguishing configurations or runs.

---

## Nice-to-Haves

- A single quantitative table reporting (AC-only, constant-ρ) vs. (AC+DC, constant-ρ) across all tasks would definitively establish how much of the gain is from DC vs. AC, and would be the strongest case for the paper's primary novel claim.
- Providing explicit schedules (σ^(k), σ_{s^(k)}) that analytically satisfy the conditions in Theorem 3(b), with a separate note that the practical heuristic schedule is used for efficiency but is not theoretically certified, would make the theory-practice boundary explicit rather than implicit.
- NFE-vs.-performance tradeoff curves would contextualize the gains relative to DAPS-4K and allow readers to evaluate whether the method is efficient at a given compute budget.

---

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **DC stationarity J=10 as a "fatal" flaw**: The harsh critic labels this a central evidential gap, but Footnote 1 explicitly states "For their counterparts removing this assumption, see Appendix E.2." Since the appendix is stripped in the reviewed submission—not absent from the actual paper—this cannot be treated as a fatal or even major flaw. Demoted: the practical approximation concern is absorbed into the "Gaussian likelihood unvalidated" minor weakness.

- **Strength: "well-motivated three-stage denoiser design with ablation"** (Strength Finder) — The ablation claim is partially invalid: Figure 5 is qualitative only. The strength is retained but scoped: the design motivation is genuinely solid; the ablation is insufficient for quantitative validation of DC. Accordingly, the ablation element is moved to Major weakness rather than credited as a strength.

- **Section 3 notation inconsistency** (harsh critic): The critic alleges internal inconsistency in the notation of z_σ^(k). After reading lines 125–129, the notation is dense but not evidently contradictory—z_σ^(k) consistently refers to the denoised signal and s^(k) to the residual. This reads as parser-induced formatting noise rather than a genuine logical inconsistency. Removed.

- **Theorem 3(a) c_k growth analysis** (harsh critic): The claim that log²(ν_k) growth undermines convergence is a speculative mathematical concern not clearly verifiable from the printed expression, and the convergence result explicitly accounts for scheduled decay of σ_{s^(k)}. Removed from Major; the practical schedule concern (which is verifiable) is retained.

---

## Novel Insights

The AC-DC decomposition—pairing cheap noise injection (AC) with a small number of conditional Langevin steps (DC) to align iterates with the score's training manifold before denoising—offers a principled design pattern beyond ADMM. The Langevin targeting of p(z_{σ^(k)} | z_{ac}^(k)) is notably elegant: since supp(z_{σ^(k)} | z_{ac}^(k)) ⊆ M_{σ^(k)}, the DC step provides a formal guarantee that—in the idealized stationary limit—the denoiser input lies on the score manifold. This insight generalizes to any proximal-gradient or variable-splitting scheme that suffers manifold mismatch, making the AC-DC denoiser a transferable module rather than an ADMM-specific trick. The dual-track convergence analysis (ball convergence under strong convexity; bounded-denoiser convergence under adaptive steps without convexity) is a useful template for future work incorporating stochastic or probabilistic denoisers into first-order optimization.

---

## Suggestions

1. **Add an NFE/runtime table** alongside Table 1, or at minimum report total score evaluations per image for each method. Given that the authors already flag this in Limitations, it is a straightforward addition.

2. **Add quantitative ablation rows** in Table 1 for "AC-only" (J=0) and "AC+DC" (J=10) variants, so that the contribution of DC can be assessed numerically rather than visually.

3. **Clarify the theory-practice boundary for schedules**: note explicitly that the heuristic σ^(k) = max(0.1, ...) does not satisfy lim σ^(k) → 0, and frame the convergence results as characterizing idealized behavior that the practical schedule approximates.

---

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| dAavOuxZvo (VIPaint) | 3.00 | R1 | Much weaker; rejected, no convergence theory |
| 1YO4EE3SPB (RED-diff) | 5.50 | R1 | Weaker novel contribution; paper under review has clearer algorithm and better empirics |
| bEDTZxwJjT (DiracDiffusion) | 5.50 | R1 | Comparable scope; fewer tasks, no convergence theory |
| DsEhqQtfAG (DDS) | 6.50 | R1/R2 | Similar: combines classical optimization + diffusion; paper here has more diverse tasks + convergence theory |
| HXjXPQU3yJ (PnP-ADMM mismatch) | 6.25 | R2 | Direct cousin: PnP-ADMM + mismatch + convergence theory; *rejected* due to limited experiments (only SR/deblur). Paper under review is clearly stronger: more tasks, novel denoiser, two convergence regimes |
| kRBQwlkFSP (DiffStateGrad) | 6.75 | R2 | Similar empirical breadth; accepted; no convergence theory but cleaner presentation and robustness story |
| x7d1qXEn1e (Restoration as Implicit Prior) | 6.25 | R2 | Accepted; convergence to stationary point; paper under review is comparable in depth |

**Round 1 bracket**: 5.5–7.5

**Round 2 narrowing**: The paper is clearly stronger than the 6.25 rejected HXjXPQU3yJ anchor (broader tasks, novel denoiser vs. analysis-only). It is comparable to DiffStateGrad (6.75), which covers similar empirical territory and manifold-alignment idea, but without convergence theory. The missing NFE comparison and qualitative-only DC ablation prevent a score higher than 6.75. The strong convergence theory dual contribution (Theorems 1–3) and comprehensive 6-task evaluation justify landing above the 6.25-6.5 cluster. 

**Final score: 6.5** — Accepts on the strength of the AC-DC design, convergence theory, and broad empirical validation; would be stronger with quantitative NFE comparison, DC ablation table, and explicit acknowledgment that the practical schedule does not satisfy Theorem 3(b).

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>