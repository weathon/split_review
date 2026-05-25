**Calibration Rounds Summary**

**Round 1 — Bracketing:**
- Low band (`score<3.5`): weak, poorly-executed diffusion papers (e.g., RFJGFrMvYj avg 1.50, vK8C37eHXM avg 3.20)
- Mid band (`3.5<score<7.5`): papers with solid contributions but notable flaws (e.g., pzpWBbnwiJ avg 5.25 accepted, QO3yH7X8JJ avg 5.25 rejected, 1YO4EE3SPB avg 5.50 accepted)
- High band (`score>7.5`): strong, clean papers with no serious weaknesses (e.g., 6O3Q6AFUTu avg 8.00, OlzB6LnXcS avg 8.00)

Initial bracket: 4.5–6.5. The paper has genuine contributions (strong empirical results, clean ablation) but is undermined by overclaiming, a table formatting error, and missing analyses.

**Round 2 — Narrowing within the bracket:**
Queried `(4.0, 6.0)` for topically similar papers. Key anchors:
- Universal Guidance (pzpWBbnwiJ, avg 5.25, accepted): similar unified-guidance framing, comparable strength but also noted for incremental novelty.
- StyleShot (Qy3UwW4OJ9, avg 5.50, rejected): strong task-specific results but rejected — not directly comparable.
- Variational Perspective on Inverse Problems (1YO4EE3SPB, avg 5.50, accepted): solid theory + experiments.
- Momentum-driven Noise-free Guidance (i8bdPSmOwk, avg 5.33, rejected): similar technical domain, rejected due to insufficient novelty.

The paper under review sits between Universal Guidance (accepted, less evaluation breadth) and the rejected papers. Its evaluation breadth across 3 tasks and clean ablation argue for the higher end of the bracket, but the overclaiming, table formatting error, and missing computational analysis pull it back.

**Final score:** 5.0

---

## Summary

This paper proposes DPG (Data and Process Knowledge Guidance), a framework for diffusion-model guidance in imperfect-label tasks — weak-label (style transfer) and degraded-label (super-resolution, deblurring). DPG integrates two ideas: (1) *data knowledge* — diffusing the imperfect label and injecting it early in the reverse diffusion process, and (2) *process knowledge* — a progressive alignment loss (Eq. 11) that encourages each step's clean prediction to be closer to the label than the previous step's prediction. The method is evaluated on style transfer (40,000 images, 11 baselines), 4× super-resolution, and deblurring, with quantitative results in Table 1 and qualitative results in Figure 4.

---

## Strengths

1. **Consistent strong empirical performance across three diverse tasks (Table 1, Figure 4).** DPG ranks first or second on nearly every metric across style transfer, super-resolution, and deblurring. For example, DPG achieves the lowest Style Loss (0.6313) and CLIP Loss (4.2334) in style transfer, the highest PSNR (28.86) in super-resolution, and the highest SSIM (0.7736) and lowest LPIPS (0.2236) in deblurring. The qualitative comparisons show consistently higher visual quality than 10–12 baselines per task.

2. **Clean ablation study validating both components (Table 2, Figure 5).** Removing data knowledge ("w/o D") degrades Style Loss by 33% and CLIP Loss by 18% in style transfer. Removing process knowledge ("w/o P") degrades all metrics across all three tasks (e.g., Style Loss rises from 0.6054 to 0.9201, deblurring SSIM drops from 0.7736 to 0.7496). The qualitative ablations confirm that both components contribute meaningfully and are not redundant.

3. **Comprehensive baseline coverage.** The paper compares DPG against 10–12 methods per task, including both training-free methods (InstantStyle, StyleAlign, CSGO) and fine-tuned methods (StyleDrop, StyleCrafter, DEADiff), as well as prior unified approaches (TFG, FreeDom). This breadth strengthens the empirical case.

---

## Weaknesses

### Major

- **Overclaiming in framing.** The paper repeatedly claims to be "the first study to analyze the gap between weak-label and degraded-label guidance tasks and to propose a unified approach to bridge it." The claimed "unified framework" is in practice a modular template: the label preprocessing operation `M(y)`, the task loss `f_loss`, and blending weights (`α_data`, `γ_data`) are entirely task-specific. The core task-agnostic components (data knowledge injection in Eq. 7, process knowledge loss in Eq. 11) are genuinely general, but the framing overstates what is unified. The paper would be more credible if it re-scoped DPG as a *modular guidance template* and clearly identified the process-knowledge loss as the truly novel, task-agnostic contribution.

- **Missing computational cost analysis.** The abstract mentions "efficiency," but the paper provides no wall-clock time, FLOPs, or runtime comparison against any baseline. DPG involves multiple forward passes per step (data-knowledge blending with `N_iter`, gradient updates on clean estimates in both Eqs. 9 and 11) and is likely substantially more expensive than standard guidance methods. Without any efficiency analysis, the practical value of the method cannot be assessed. This is a standard expectation for a systems/application paper.

### Minor

- **Algorithmic description is unclear at a critical point (Eqs. 10–12).** The variable `z_{t-1}` is defined in Eq. 10 (using the L1-refined `z_{0|t}`) and then defined again in Eq. 12 (using the L2-refined `z_{0|t-1}`). This appears to be a predictor–corrector refinement scheme, but the paper does not explain the algorithmic flow — it reads as if `z_{t-1}` is simply overwritten. The Markovian consistency of the final `z_{t-1}` used for the next step is not discussed. This is fixable with a paragraph clarifying the flow and an algorithm pseudocode box in the main paper (currently relegated to the appendix, which is not accessible in the submission).

- **Table 1(c) PSNR formatting error.** In the deblurring table, DPG's PSNR value (27.5794) is bolded alongside DCDP's higher value (27.9110). The caption states "The best results are in bold," so DPG's value should not be bolded on this metric (DCDP is best). While the running text correctly states "PSNR slightly below DCDP," the table formatting is misleading. This is a concrete presentation error that needs fixing.

- **Missing analysis of the process loss's effect on diversity.** The margin-based loss in Eq. 11 actively enforces a specific trajectory (later steps must be closer to the label). This could bias the generated distribution or reduce sample diversity. The paper does not analyze this — no FID comparison between DPG and "w/o P" is provided, and no discussion of potential mode-seeking behavior appears. A brief experiment or formal discussion would strengthen the paper.

- **Pixel-space vs. latent-space confound unaddressed.** Several baselines in Figure 4 operate in pixel space (marked with *), while DPG operates in Stable Diffusion's latent space. Known differences in reconstruction quality, artifacts, and perceptual metrics between the two spaces are not discussed or controlled for. The paper should at minimum acknowledge this limitation.

- **Iterative computation of ċ_t (Eq. 6) is underspecified in the main text.** The dependency of `ε_θ(t)` on `ĉ_t` and vice versa requires the appendix pseudo-code to be understood. A short description in the main text would improve self-containedness.

### Trivial

None.

---

## Nice-to-Haves

- Include a runtime/GPU-hour comparison table for DPG vs. the simplest and strongest baseline (e.g., TFG or DCDP).
- Add an FID comparison between DPG and "w/o P" to measure the diversity impact of the process loss.
- Discuss failure cases (e.g., when `α_margin` is too large, or style image is strongly OOD).
- Compare with additional training-free style transfer methods (e.g., StyleID) in the same table.

---

## Removed Points

These points were raised in the input reviews but are removed after cross-checking against the paper. They should be treated with caution.

- **"Eq. 10 vs. Eq. 12 breaks the Markovian structure / is formally invalid"** (Harsh Critic #1). After reading the equations in context, this is a predictor–corrector refinement (z_{t-1} from Eq. 10 is an intermediate state; the final z_{t-1} passed to the next step is from Eq. 12). The lack of clarity is a real weakness (noted above under Minor), but calling it "formally invalid" overstates the issue. The algorithm is coherent as an iterative refinement scheme; the paper just does not explain the flow well.

- **"The paper makes an unsupported claim of superiority on this task" based on Table 1(c)** (Harsh Critic #2). The paper's text states "our method achieves the highest SSIM Score and the lowest LPIPS Loss, with PSNR slightly below DCDP." This is factually correct. The table has a formatting error (DPG's PSNR value incorrectly bolded), but the textual claim is honest and supported. The criticism about "unsupported claim of superiority" is inaccurate.

- **"Unfair comparison: DPG is training-free vs. fine-tuned models"** (Harsh Critic). The asymmetry favors the fine-tuned baselines (which are trained specifically for the task), not DPG. Being training-free yet competitive against fine-tuned methods is a strength, not a weakness. Per the hard rule: remove criticisms where asymmetry favors the baseline.

- **"Pixel-space vs. latent-space confound" as a major issue** (Harsh Critic). The paper transparently marks pixel-space methods with asterisks. While this confound deserves acknowledgment (noted under Minor), no evidence is given that it "likely dominates the comparison." This is speculative.

- **"Strength: the framework is compatible with multiple diffusion backbones (U-Net and DiT)"** (Strength Finder). The paper only evaluates with U-Net. The mention of DiT compatibility is a claim without experimental evidence. Removed per the rule that strengths must cite a specific experimental finding.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface a useful organizing insight: the paper's strongest contribution is the *process knowledge loss* (Eq. 11), which is truly task-agnostic and well-validated by ablation, while the "unified framework" framing inflates what is essentially a modular template. The data knowledge injection (Eqs. 5–7) is conceptually similar to SDEdit but applied per-step rather than as a one-time initialization — this distinction is real but underexploited in the paper's narrative.

---

## Suggestions

1. **Fix the table formatting error.** In Table 1(c), only DCDP's PSNR (27.9110) should be bolded as the best value. Remove the erroneous bolding from DPG's 27.5794.

2. **Add an algorithm pseudocode box to the main paper** (2.3 Method section) showing the per-step loop and clarifying that z_{t-1} from Eq. 10 is an intermediate proposal, while the final z_{t-1} from Eq. 12 is what enters the next denoising step.

3. **Add a runtime/efficiency table** comparing DPG with the simplest baseline (TFG) and the strongest baseline on each task, reporting either wall-clock time per 1,000 images or total GPU-hours.

4. **Re-scope the "unified framework" claim.** Frame DPG as a *modular guidance template* with two general components (data-knowledge injection and process-knowledge loss) that are instantiated via task-specific M and f_loss. This would match what the paper actually demonstrates and avoid the perception of overclaiming.

5. **Include a diversity analysis** — compute FID for DPG vs. "w/o P" on at least one task to verify that the process loss does not collapse sample diversity.

---

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>