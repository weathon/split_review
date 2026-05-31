Now I have a thorough understanding of the paper. Let me write the review.

---

## Summary

The paper proposes **ADMM Plug-and-Play (ADMM-PnP) with the AC-DC denoiser** for solving image inverse problems. To address the mismatch between ADMM iterates (distorted by dual variables) and the noisy data manifolds on which score functions are trained, the authors introduce a three-stage denoiser: (1) Auto-Correction (AC) via additive Gaussian noise, (2) Directional Correction (DC) via conditional Langevin dynamics, and (3) standard Tweedie/ODE-based score denoising. Beyond the algorithm, the paper establishes two convergence results: ball-convergence under constant step size when the AC-DC residual is weakly non-expansive and the data-fidelity term is strongly convex, and fixed-point convergence under an adaptive step-size schedule without convexity. Experiments on seven inverse problems across two datasets demonstrate consistent improvements over a diverse set of baselines.

---

## Strengths

- **Well-identified and genuine problem.** ADMM's dual variable $\mathbf{u}^{(k)}$ further deforms the noise geometry of $\tilde{\mathbf{z}}^{(k)} = \mathbf{x}^{(k+1)} + \mathbf{u}^{(k)}$, making it even harder to align with trained score manifolds than in primal-only PnP methods. This distinction is articulated clearly and distinguishes the paper from earlier score-based PnP work on primal algorithms (DiffPIR, SNORE, RED-diff).

- **Principled and novel denoiser design.** The AC step is tied to a formal decomposition (Eq. 9) showing $z_{\text{ac}}^{(k)}$ can be viewed as a Gaussian perturbation of a data-point. The DC step is derived from the conditional score $\nabla \log p(z_{\sigma^{(k)}} | z_{\text{ac}}^{(k)})$ via Bayes' rule (Eq. 10), providing a principled rationale rather than ad hoc noise injection. The resulting algorithm is self-contained and uses the same pre-trained score network throughout.

- **Convergence theory for score-based ADMM-PnP.** Theorem 1 (ball convergence under weakly non-expansive residuals) is a genuine extension of Ryu et al. (2019), which required strict contractivity. Theorems 2 and 3 characterise when the AC-DC denoiser actually satisfies the required conditions (under standard smoothness/coercivity of the log-density), closing a loop that most score-based PnP papers leave open. Providing explicit expressions for $\epsilon_k$ and $\delta_k$ in terms of algorithmic parameters ($\sigma^{(k)}, \sigma_{s^{(k)}}$) is quantitatively useful.

- **Comprehensive empirical evaluation.** Seven inverse problems (super-resolution, Gaussian deblurring, motion deblurring, random inpainting, box inpainting, phase retrieval, HDR), two datasets (FFHQ and ImageNet 256×256), eight baselines covering posterior-sampling (DPS, DDRM, DAPS), PnP (DiffPIR, RED-diff, DCDP, DPIR), and consistency-model methods (PMC). The proposed method achieves best or second-best on nearly all tasks and metrics. The ablation on DC steps (Fig. 5) concretely demonstrates the contribution of the DC stage.

---

## Weaknesses

### Fatal
None.

### Major

1. **Stationarity assumption vs. practical J=10 DC steps.** Theorems 2 and 3 explicitly state the "DC step reaches the stationary distribution for each $k$." In practice, only $J=10$ Langevin iterations are run. In high dimensions ($d = 256\!\times\!256\!\times\!3 \approx 2\!\times\!10^5$), $J=10$ is far from convergence in distribution. Footnote 1 mentions "counterparts removing this assumption" in Appendix E.2 (stripped from the reviewed version), so it is unclear how the bounds degrade under finite-step DC. This is not a minor relaxation—the key quantity $\delta_k$ depends on how closely the DC step tracks the conditional distribution.

2. **Mismatch between theoretical schedule and experimental schedule.** Theorem 3(b) requires $\lim_{k\to\infty}\sigma^{(k)} = 0$. However, the implemented schedule is $\sigma^{(k)} = \max(0.1,\; 10 - (10-0.1)\cdot k/W)$, which plateaus at $\sigma^{(k)} \to 0.1 \neq 0$. Because both $\epsilon_k$ (Eq. 15) and $c_k$ (Thm. 3(a)) are $O((\sigma^{(k)})^2)$, this means the denoiser residual bound $c_k$ does not vanish as assumed for convergence. The theoretical guarantees therefore do not directly certify the experimental setting; the authors acknowledge this in the limitations for the non-convex case but do not quantify the gap.

3. **No computational cost comparison.** Each ADMM iteration requires: (a) up to 1000 Adam steps for the $\mathbf{x}$-subproblem, (b) $J=10$ score evaluations for DC, and (c) 1 or 10 score evaluations for Tweedie/ODE denoising. Total per-iteration NFEs can easily be $\times\!5$–$\times\!20$ of a baseline like DPS or DAPS. The paper does not report wall-clock times, GPU memory, or NFE counts, making it impossible to assess the efficiency–quality trade-off. For a method paper that explicitly lists computational cost as a limitation, this quantification is important for the community.

### Minor

1. **Box inpainting exception.** For box inpainting, DCDP achieves PSNR 25.23/20.99 on FFHQ/ImageNet while Ours-tweedie reaches 24.03/21.63. The paper's claim "best or second-best in almost all tasks" is accurate but glosses over this task where the margin is non-trivial (≈1.2 dB on FFHQ). A brief discussion of why box inpainting is more challenging for the proposed method would be informative.

2. **Gaussian approximation for $\nabla \log p(z_{\text{ac}}|z_{\sigma^{(k)}})$.** The condition "$\text{Var}(\mathbf{s}^{(k)})^{1/2} \ll \sigma^{(k)}$" used to justify the Gaussian likelihood approximation is stated informally and never verified empirically or analytically. Its effect on denoising quality is conflated with the DC step's efficacy.

3. **Duplicate rows in Table 1.** Multiple "PMC" rows appear for some tasks (e.g., two PMC rows for super-resolution and two for box inpainting) without differentiation, making the table ambiguous.

4. **AC ablation absent.** Figure 5 isolates DC by varying $J$, but does not isolate the AC contribution (e.g., comparing $J=0$ with AC to $J=0$ without AC), leaving a partial picture of each stage's independent effect.

### Trivial
None worth listing beyond the parser-induced duplications noted above.

---

## Nice-to-Haves

- A runtime / NFE comparison table to contextualise the efficiency cost alongside the quality gains.
- Empirical verification that $J=10$ DC steps are sufficient (e.g., tracking the TV or KL distance to $\mathcal{M}_{\sigma^{(k)}}$ through DC iterations).
- An experiment with $\sigma^{(k)} \to 0$ schedule (matching theory) vs. $\sigma^{(k)} \to 0.1$ (current) to show that the plateau does not hurt in practice.

---

## Novel Insights

The paper makes a precise and previously underappreciated observation: in ADMM-PnP, the dual variable $\mathbf{u}^{(k)}$ systematically shifts the denoiser input $\tilde{\mathbf{z}}^{(k)} = \mathbf{x}^{(k+1)} + \mathbf{u}^{(k)}$ away from any Gaussian-noise manifold $\mathcal{M}_{\sigma}$, in a direction that is neither Gaussian nor zero-mean. This motivates a two-phase manifold correction: a stochastic AC step to pull $\tilde{\mathbf{z}}^{(k)}$ into the vicinity of some $\mathcal{M}_{\sigma^{(k)}}$, followed by a targeted Langevin DC step targeting the *conditional* distribution $p(z_{\sigma^{(k)}} | z_{\text{ac}}^{(k)})$, which by construction has support contained in $\mathcal{M}_{\sigma^{(k)}}$ while retaining measurement information through the conditioning. This decomposition—borrowed from Bayesian structure but implemented through score networks—shows a clean pathway for making any gradient-based PnP algorithm compatible with diffusion-trained denoisers.

---

## Suggestions

- Provide wall-clock time and NFE counts in Table 1 or a dedicated cost table.
- Include a dedicated AC ablation (no noise injection vs. AC+no DC vs. full AC-DC) to separate each stage's contribution.
- Clarify or quantify the $J=10$ approximation error relative to the stationary-distribution assumption in the proofs, even if only empirically.
- Consider stating the schedule condition explicitly: if $\sigma^{(k)}\to0.1$ is used in practice, note explicitly that Theorem 3(b) does not apply and that ball convergence (Theorem 1 under empirical non-expansiveness) is the operative guarantee.
- Resolve the duplicate PMC rows in Table 1.

---

## Score and Decision

The paper addresses a genuine and well-scoped problem, proposes a principled and novel solution (AC-DC), establishes convergence theory that is new in the score-based ADMM-PnP setting, and demonstrates competitive empirical results across a thorough benchmark. The major weaknesses—the gap between the stationarity assumption and finite Langevin steps, the mismatch between theoretical and practical schedules, and the absent computational cost analysis—are real but do not undermine the core message. They are resolvable, either analytically (finite-step bounds from Appendix E.2) or empirically. The paper represents a solid, well-executed contribution appropriate for ICLR.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>