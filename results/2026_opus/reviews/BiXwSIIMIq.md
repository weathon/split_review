Now I have a good understanding of the paper. Let me do calibration search.Based on round 1, the most relevant anchor is HXjXPQU3yJ (avg 6.25) - very similar paper on PnP-ADMM convergence. The paper under review seems likely in the 5-6.5 range. Let me narrow.## Summary

The paper proposes ADMM-PnP with an AC-DC denoiser: a three-stage denoiser that adds Gaussian noise (auto-correction), runs conditional Langevin dynamics (directional correction), and then applies a score-based denoising step (Tweedie or ODE). It establishes two convergence results — a δ-ball convergence under strong convexity with fixed step size, and a fixed-point convergence under non-convex losses with an adaptive ρ schedule — generalizing prior ADMM-PnP convergence theory (Ryu et al., Chan et al.) to score-based denoisers. Experiments cover six inverse problems on FFHQ and ImageNet, showing consistently best or second-best PSNR/SSIM/LPIPS against eight baselines.

## Strengths

- **Genuine theoretical contribution.** Theorems 1–3 extend the Ryu et al. (2019) and Chan et al. (2016) PnP convergence framework to the score-based denoiser setting; Theorem 1 in particular relaxes the strict-contractivity requirement of Ryu et al. to a "weakly nonexpansive" residual condition, and recovers their result as the δ=0 special case (Section 4.1, line 179).
- **Broad and competitive empirical evaluation.** Table 1 covers six inverse problems (super-resolution, random/box inpainting, motion/Gaussian deblur, phase retrieval) on two datasets, with eight baselines including DPS, DAPS, DDRM, DiffPIR, RED-diff, DPIR, DCDP, and PMC. The proposed method is best or second-best across nearly every cell, including notably strong phase-retrieval numbers where most baselines collapse (DPS PSNR ~10 vs. Ours ~28 on FFHQ).
- **Concrete mechanistic story.** The AC + DC decomposition (Algorithm 1, Eq. 9-10, Fig. 1) gives a clean account of why injecting noise alone is insufficient and why a Langevin refinement step toward the conditional distribution helps return iterates to the trained manifold.
- **Honest scoping.** The remark closing Section 4.3 explicitly acknowledges that the convergence results are fixed-point, not stationary-point, and the Limitations paragraph (line 389) is candid about NFE costs and the gap between adaptive vs. constant step sizes in practice.

## Weaknesses

### Fatal
None. The criticisms below are real but do not invalidate the core claims.

### Major

- **Mismatch between the schedules used in experiments and the schedules the theorems require.** Theorem 2(b) requires $(\sigma^{(k)})^2 \nu_k \to 0$ and Theorem 3(b) explicitly requires $\sigma^{(k)} \to 0$, $\sigma_{s^{(k)}} \to 0$ (line 225). The implementation in Section 6 (line 307) fixes $\sigma^{(k)} = \max(0.1, 10 - 9.9 k/W)$ — floored at 0.1, not driven to zero — and $\sigma_{s^{(k)}} = 0.1/\sqrt{\sigma^{(k)}}$, which *increases* as $\sigma^{(k)}$ decreases. Neither sequence satisfies the limits. The theorems therefore describe a regime the algorithm is not run in, and the paper does not address this gap. The conclusions of the theorems may still hold, but as written the theory is not shown to apply to the algorithm that produced Table 1.
- **Missing "ADMM + plain Tweedie" head-to-head ablation.** The headline empirical claim is that AC-DC inside ADMM-PnP is the source of the gain. The cleanest test — ADMM-PnP with a vanilla Tweedie denoiser vs. ADMM-PnP with AC vs. ADMM-PnP with AC-DC, on the same problems with the same ADMM hyperparameters and full metrics — is absent. Figure 5 shows the DC ablation only qualitatively on phase retrieval with $J \in \{0, 10, 20\}$ and no numbers. Without this comparison the contribution of AC-DC over the ADMM wrapper itself is not isolated.
- **The dual-variable framing in the introduction is broader than the method's actual mechanism.** The Contributions paragraph (line 33) singles out that ADMM is uniquely hard because "the presence of dual variables further distorts the 'noise' geometry — likely explaining why score-based denoising has rarely been combined with primal–dual methods." But AC-DC is dual-variable-agnostic: it treats $\tilde z^{(k)} = x^{(k+1)} + u^{(k)}$ as just an arbitrary off-manifold point, and Section 3 explicitly notes the denoiser "can be plugged into any other proximal operator based schemes" (line 86). No experiment isolates the dual-variable distortion (e.g., AC-DC inside HQS or proximal-gradient on the same problem). The framing oversells the primal–dual specificity of the contribution.

### Minor

- **Unverified regime of validity for the Gaussian likelihood approximation in DC.** Equation (10) and line 145 license the practical DC step by assuming $\mathrm{Var}(s^{(k)})^{1/2} \ll \sigma^{(k)}$, where $s^{(k)} = \tilde z^{(k)} - z_q^{(k)}$ includes the variance of $p_{\text{data}}$. The paper neither argues nor measures that this condition holds for the iterates encountered with $\sigma^{(k)} \in [0.1, 10]$ (particularly near 0.1). A simple measurement of $\mathrm{Var}(s^{(k)})$ along a run would convert this from assertion to evidence.
- **Convergence framing somewhat oversold relative to result.** The abstract and introduction frame the contribution as "convergence guarantees" for the algorithm finding good solutions. Theorems 2–3 actually deliver stability (δ-ball / implicit fixed-point) only. The closing remark in Section 4.3 acknowledges this, but the abstract does not, and a reader naturally conflates stability with reconstruction quality.
- **Constants in Theorem 1 are not made concrete.** The radius $r = (1 + \rho/(\rho+\mu))\delta/\sqrt{1-\bar\epsilon^2}$ with $\bar\epsilon$ a non-trivial rational function of $\rho, \mu, \epsilon$ is dense; a worked numerical example for a representative problem would let readers tell whether the bound is informative or vacuous.
- **No NFE / wall-clock table in the main paper.** The Limitations paragraph notes that AC-DC requires multiple score evaluations per ADMM iteration; given DPS / DAPS / DiffPIR have very different NFE profiles, an NFE-matched comparison would help interpret the wins in Table 1.

### Trivial

- The phase-retrieval ablation in Figure 5 would benefit from numbers alongside the qualitative panels.
- The discussion at line 191 about "$-\log p_{\text{data}}$ escaping to infinity" is decorative given the explicit $D = \mathrm{diam}(\mathcal X) < \infty$ assumption in Theorem 3.

## Nice-to-Haves

- A theory-compliant experimental run (with $\sigma^{(k)} \to 0$ and $\sigma_{s^{(k)}} \to 0$) that demonstrates the empirical behavior the theorems predict, even if quality is somewhat worse than the headline schedule.
- An experiment specifically isolating the dual-variable distortion — e.g., AC-DC inside ADMM vs. AC-DC inside HQS / proximal gradient on the same problem — that substantiates the motivation in Section 1.
- A sensitivity study on the $\sigma^{(k)}$ schedule, particularly for phase retrieval.

## Removed Points

These points are flagged to be removed, treat them with caution.

- *Strength Finder produced no usable content* (returned "你好，我无法给到相关内容"); strengths above were extracted directly from the paper.
- *"PMC appearing twice per task / empty cells in Table 1"*: removed as a parser artifact, not a paper error.
- *"Missing related works"*: not raised by the critic in a specific way; removing per instructions because external references cannot be verified.

## Novel Insights

None beyond the paper's own contributions. The most useful synthesis observation is that the AC-DC denoiser is best understood as a *manifold-correction* construction that happens to be deployed inside ADMM, not as a primal–dual-specific construction — but this is essentially how the paper itself frames AC-DC in Section 3 (line 86), so it is not a fresh insight.

## Suggestions

- In Section 4, add a paragraph that states the schedules under which Theorems 2(b)/3(b) are intended to apply, and either run one experiment using a theory-compliant schedule or explicitly explain how the practical schedule is consistent with the theorem hypotheses (e.g., by considering finite-horizon stability rather than asymptotic convergence).
- Add a quantitative ablation table: ADMM + Tweedie / ADMM + AC / ADMM + AC-DC-Tweedie / ADMM + AC-DC-ODE on at least 3 of the 6 inverse problems with full PSNR/SSIM/LPIPS.
- Add an NFE-matched comparison table against DPS, DAPS, DiffPIR in the main text.
- Replace the "convergence guarantees" language in the abstract with "stability guarantees / fixed-point convergence" to match what the theorems actually establish.

## Evaluation on Standard Axes

- **Originality**: The AC-DC construction is novel as a primal–dual-flavored denoiser; the convergence extension to score-based denoisers is also new.
- **Importance**: The research question — making score denoisers compatible with ADMM-PnP — is genuinely useful for the inverse-problem community.
- **Claim support**: Mixed. Empirical claims are well-supported; theoretical claims are well-proven but loosely connected to the algorithm that produced the tables.
- **Soundness of experiments**: Broad coverage and strong numbers, but the headline ablation (ADMM + Tweedie) is missing.
- **Clarity**: Good in Sections 2–3; Sections 4 constants are dense.
- **Value to the community**: Reasonable. Both the construction and the theoretical extension are reusable.

## Calibration

**Anchors retrieved:**

Round 1 (bracketing):
- `dAavOuxZvo.md` (VIPaint), avg 3.00, R1, weak anchor — substantially weaker than the paper under review.
- `W4djmqKZC6.md` (Pixel-Aware Accelerated Reverse Diffusion), avg 3.00, R1, weak anchor — clearly weaker.
- `vK8C37eHXM.md` (Sample what you can't compress), avg 3.20, R1, weak anchor — different domain, clearly weaker.
- `7jUQHmz4Tq.md` (D3AD), avg 3.00, R1, weak anchor — clearly weaker.
- `1YO4EE3SPB.md` (RED-diff), avg 5.50, R1 mid, **read**: comparable scope (PnP-style with diffusion priors for inverse problems), arguably weaker on theory but cleaner narrative.
- `Z9Odi09Rv9.md` (Fast and Noise-Robust Diffusion Solvers), avg 4.75, R1 mid — somewhat weaker.
- `bEDTZxwJjT.md` (DiracDiffusion), avg 5.50, R1 mid — comparable.
- `HXjXPQU3yJ.md` (Prior Mismatch and Adaptation in PnP-ADMM), avg 6.25, R1 mid, **read**: most topically similar (PnP-ADMM convergence theory). The paper under review has broader experiments but a similar "theorem doesn't quite match the algorithm being run" complaint.
- `6O3Q6AFUTu.md` (NoiseDiffusion), avg 8.00, R1 strong — clearly stronger.
- `6EUtjXAvmj.md` (Variational Diffusion Posterior Sampling with Midpoint Guidance), avg 8.00, R1 strong — clearly stronger and more rigorous.
- `I5lcjmFmlc.md` (RDC), avg 8.00, R1 strong — different problem; not a useful anchor.
- `CxXGvKRDnL.md` (Progressive Compression with Universally Quantized Diffusion), avg 8.00, R1 strong — different problem.

Round 1 bracket: **between ~5 and ~6.5**.

Round 2 (narrowing):
- `5AtHrq3B5R.md` (PnP-Flow), avg 5.50, R2, **read**: very close analog — PnP with a different generative-model-based denoiser, evaluated on similar inverse-problem benchmarks. Paper under review adds explicit convergence theory and broader phase-retrieval coverage, but has the theory-practice schedule gap PnP-Flow doesn't claim to address.
- `kNPcOaqC5r.md` (Learned Proximal Networks), avg 5.75, R2 — comparable, more focused on proximal-network construction.
- `1YO4EE3SPB.md` (re-encountered).
- `bEDTZxwJjT.md` (re-encountered).
- `92KV9xAMhF.md` (gauge freedom), avg 6.75, R2 — pure-theory diffusion paper, different focus.
- `ZwO2I8gS5O.md` (Riemannian DDPMs), avg 6.00, R2 — different problem.
- `BZtEthuXRF.md` (Manifold Diffusion Fields), avg 6.67, R2 — different problem.
- `tD4NOxYTfg.md` (Convergence of VE Diffusion under Manifold Hypothesis), avg 6.50, R2 — pure theory, different focus.

**Comparison:** the paper sits closest to HXjXPQU3yJ (6.25) and PnP-Flow (5.50) — both PnP/inverse-problem papers with novel denoiser/prior constructions and partial theoretical support. The paper under review has stronger empirical coverage than HXjXPQU3yJ (six tasks vs. two), and a more substantive theory than PnP-Flow, but has the schedule-theorem mismatch and missing-baseline ablation issues that pull it below HXjXPQU3yJ. It is meaningfully stronger than the ~5.0 cluster (RED-diff, DiracDiffusion, PnP-Flow) on empirical breadth and theoretical scope, but the theory-practice gap and missing ADMM+Tweedie ablation are real frictions. Lands at **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>