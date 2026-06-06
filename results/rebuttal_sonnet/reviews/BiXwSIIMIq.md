Now I have read the full paper and can verify the rebuttal claims. Let me produce the updated review.

---

## Summary

This paper proposes ADMM Plug-and-Play (ADMM-PnP) with an AC-DC (Auto-Correction / Directional Correction) denoiser for solving imaging inverse problems using pre-trained diffusion score functions. The AC step injects Gaussian noise to pull ADMM iterates toward noisy data manifolds, while the DC step uses conditional Langevin dynamics to precisely refine iterates onto the target manifold. Two convergence results are established: ball convergence under strongly convex data-fidelity (Theorem 2), and bounded-denoiser convergence without convexity under an adaptive step-size schedule (Theorem 3). Experiments across six inverse problems on FFHQ and ImageNet demonstrate competitive performance against eight baselines.

---

## Rebuttal Assessment

**Weakness: No NFE or wall-clock comparison**
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author points to DAPS-4K as a partial anchor (its name signals 4K NFEs), and Table 1 confirms the proposed method outperforms DAPS-4K on most tasks. However, the proposed method's own NFE budget remains completely unspecified in the paper. The rebuttal does not reveal the actual count, only promises to add a table in revision. The anchor is too coarse to address the concern rigorously.
- **Score impact:** Weakness unchanged

**Weakness: DC ablation is qualitative only**
- **Author's response:** Acknowledge
- **Assessment:** Unconvincing as a rebuttal — The author honestly confirms that Figure 5 shows only visual results for J=0/10/20 on phase retrieval, with no PSNR/SSIM/LPIPS numbers. They acknowledge this "is a genuine evidential gap" and promise to add it in revision. Per the review criteria, promises of revision do not count. The weakness stands in full.
- **Score impact:** Weakness unchanged

**Weakness: Practical noise schedule does not satisfy Theorem 3(b) conditions**
- **Author's response:** Acknowledge (partially)
- **Assessment:** Partially convincing, but incomplete — The author correctly acknowledges that σ^(k) = max(0.1, ...) saturates at 0.1 and violates the lim_{k→∞} σ^(k) = 0 requirement. Their mitigation claim—that Theorem 2(a) "still applies on a per-iteration basis"—is valid but irrelevant to the global convergence guarantee: Theorem 2(b) and Theorem 3(b) require the schedule to decay to zero, which the practical one does not. The Limitations section (verified in paper, line 379) acknowledges only that "noise schedules are currently guided by empirical heuristics" without explicitly stating the schedule-theorem incompatibility. The author promises to add a clarifying remark in revision. The weakness remains major.
- **Score impact:** Weakness unchanged (slightly softened: author now acknowledges it explicitly)

**Weakness: Gaussian likelihood approximation in DC not empirically validated**
- **Author's response:** Acknowledge
- **Assessment:** Unconvincing as a rebuttal — Author confirms the condition Var(s^(k))^{1/2} ≪ σ^(k) is stated but never verified (confirmed at line 135 of the paper), and promises to add validation in revision. Revision promises do not count.
- **Score impact:** Weakness unchanged

**Weakness: DCDP outperforms on PSNR for box inpainting by 1.2 dB**
- **Author's response:** Partially address
- **Assessment:** Partially convincing, but misleading in one claim — The author correctly notes that on FFHQ box inpainting, their method leads DCDP on SSIM (0.859 vs 0.754) and LPIPS (0.131 vs 0.163). However, the author claims "outperforms DCDP on all metrics on ImageNet box inpainting (PSNR 21.626 vs 20.991; SSIM 0.789 vs 0.727)"—this omits that DCDP has better LPIPS on ImageNet (0.195 vs 0.222), confirmed directly in Table 1. The author's claim of full ImageNet superiority is inaccurate. The overall minor weakness is partially addressed but the author's response contains a factual misrepresentation.
- **Score impact:** Weakness unchanged (minor)

**Weakness: Two PMC rows for super-resolution with no caption explanation**
- **Author's response:** Acknowledge
- **Assessment:** Honest acknowledgment of a presentation error. Trivial concern.
- **Score impact:** Weakness unchanged (trivial)

---

## Strengths

- **Non-trivial convergence theory for score-based ADMM-PnP.** Theorems 1–3 extend prior fixed-point theory to diffusion-score denoisers with high-probability ball convergence under strong convexity (Theorem 2), and bounded-denoiser convergence under adaptive steps without convexity (Theorem 3). The footnote at line 207 correctly confirms that Theorems 2–3 have appendix extensions removing the DC stationarity assumption.

- **Strong, comprehensive empirical evaluation.** Table 1 reports PSNR, SSIM, and LPIPS across six inverse problems on both FFHQ and ImageNet against eight baselines. Both Ours-tweedie and Ours-ode achieve best or second-best performance in the large majority of settings.

- **Well-motivated three-stage design.** The AC-DC structure is derived from first principles (Eqs. 9–10), with supp(z_{σ^(k)} | z_{ac}^(k)) ⊆ M_{σ^(k)} directly justifying DC's role in manifold alignment.

---

## Weaknesses

### Fatal
None.

### Major

- **No NFE or wall-clock comparison.** The proposed method accumulates substantial compute per outer ADMM iteration (up to 1,000 Adam steps in x-subproblem, J=10 Langevin steps, plus a 10-step ODE or Tweedie). The proposed method's own NFE budget is never reported. Pointing to DAPS-4K as an "anchor" only tells us the competitor's budget, not the proposed method's. The weakness is confirmed unaddressed by the rebuttal.

- **DC ablation is qualitative only.** Section 6 confirms only Figure 5 (visual, phase retrieval only) is provided for the J=0/10/20 comparison—no PSNR/SSIM/LPIPS numbers. Since AC alone is analogous to prior noise-injection methods (DiffPIR, SNORE), DC's independent quantitative contribution remains unestablished. The author acknowledges this as a "genuine evidential gap."

- **Practical schedule violates Theorem 3(b) convergence conditions.** The paper uses σ^(k) = max(0.1, ...) which saturates at 0.1, while Theorem 3(b) requires lim_{k→∞} σ^(k) = 0 and lim_{k→∞} σ_{s^(k)} = 0. The Limitations section does not state this incompatibility explicitly. For non-convex tasks (phase retrieval, box inpainting), neither Theorem 2(b) nor Theorem 3(b) formally certifies the algorithm actually used. The rebuttal acknowledges this but offers no fix within the paper.

### Minor

- **Gaussian likelihood approximation in DC is not empirically validated.** The condition Var(s^(k))^{1/2} ≪ σ^(k) is assumed but never checked against practical schedules. The author acknowledges this gap and promises revision.

- **DCDP outperforms on PSNR for box inpainting (FFHQ: 25.230 vs 24.025 dB) and LPIPS on ImageNet (0.195 vs 0.222).** The author's rebuttal incorrectly claims full ImageNet superiority over DCDP, omitting the LPIPS deficit. The "best or second-best" claim holds overall but this gap warrants acknowledgment.

### Trivial

- Two PMC rows for super-resolution in Table 1 have distinct values with no caption explanation. Author acknowledges as a presentation error.

---

## Nice-to-Haves

- A quantitative ablation table (J=0 vs J=10 vs J=20) reporting PSNR/SSIM/LPIPS would definitively establish DC's contribution.
- A per-method NFE table alongside Table 1 would contextualize compute-performance tradeoffs.
- An explicit remark in Section 6 or the Limitations stating that the heuristic σ^(k) = max(0.1, ...) does not satisfy lim σ^(k) → 0 and that Theorem 3(b) characterizes idealized behavior not verified by the practical schedule.

---

## Novel Insights

The AC-DC decomposition pairs cheap noise injection (AC) with conditional Langevin dynamics (DC) to align ADMM iterates with score-training manifolds before denoising. The supp(z_{σ^(k)} | z_{ac}^(k)) ⊆ M_{σ^(k)} argument is notably elegant: in the idealized stationary limit, DC provides a formal guarantee that denoiser inputs lie on the score manifold. This insight generalizes beyond ADMM to any proximal or variable-splitting scheme suffering from manifold mismatch. The dual-track convergence analysis—ball convergence under strong convexity and bounded-denoiser convergence under adaptive steps—provides a useful template for future work incorporating stochastic denoisers into first-order optimization.

---

## Suggestions

1. Add an explicit NFE count per method per image (even estimated) in the supplementary, or at minimum report total score evaluations for Ours-tweedie and Ours-ode.
2. Add a quantitative ablation table for J=0, J=10, J=20 on at least two tasks (not just visual comparison).
3. State explicitly in the paper that the practical σ^(k) = max(0.1, ...) schedule does not satisfy Theorem 3(b) conditions, and frame Theorem 3 as characterizing idealized behavior.
4. Correct the rebuttal's claim that the proposed method beats DCDP "on all metrics on ImageNet box inpainting"—DCDP leads on LPIPS (0.195 vs 0.222) on that split.

---

## Score and Decision

The rebuttal is predominantly an honest acknowledgment of the weaknesses identified in the original review, coupled with promises to add ablation tables, NFE comparisons, and schedule clarifications in a revision. Under the evaluation criteria, revision promises do not count toward addressing weaknesses—only evidence already in the paper does.

Three of the four major/significant concerns (NFE comparison, DC ablation, schedule incompatibility) remain fully unaddressed in the paper. The fourth (Gaussian approximation) is also unaddressed. The rebuttal also introduces a minor factual misrepresentation (claiming full ImageNet superiority over DCDP while omitting the LPIPS deficit). The core contributions—the AC-DC design rationale, Theorems 1–3, and the broad empirical evaluation—remain genuinely strong and intact.

The rebuttal provides no new information that would change the original assessment. The score is maintained at **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>