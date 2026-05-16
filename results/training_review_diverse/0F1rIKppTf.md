Here is my consolidated review after verifying all claims against the paper text.

---

## Summary

This paper introduces the mirror Schrödinger bridge (MSB) — the problem of finding the minimal-KL path measure between a distribution and itself — and proposes an alternating minimization procedure (AMP) that exploits time-symmetry to train only a single neural network, halving per-iteration training cost relative to standard diffusion Schrödinger bridge (DSB/DSBM) methods. The authors prove convergence in total variation with an \(o(1/k)\) rate and demonstrate controlled in-distribution resampling on 2D and image datasets by varying the noise parameter \(\sigma\).

## Strengths

- **Novel and well-motivated problem formulation.** The paper identifies that the Schrödinger bridge problem between a distribution and itself (the "mirror" setting) has been largely overlooked and formalizes it with clear definitions (Section 4, Equation (3)). This naturally enables proximal resampling with in-distribution variation, going beyond the standard two-distribution setting.

- **Convergence proof for AMP in continuous state spaces.** Theorem 1 establishes that the AMP iterates (Equations (4)–(5)) converge in total variation to the mirror Schrödinger bridge with an \(o(1/k)\) rate. This extends convergence guarantees beyond the finite-state-space setting of Csiszár & Tusnády (1984) to \(\mathbb{R}^n\), a nontrivial theoretical contribution.

- **Algorithmic simplification: single-network training.** Section 4.3 and the comparison in Figure 1 demonstrate that the AMP scheme trains only a single drift network \(v_t^\theta\) (modeling the time-symmetrized drift) instead of separate forward and backward networks. Each outer iteration therefore requires half the training iterations of DSB/DSBM, a clear practical advantage derived from the mirror setting.

- **Test-time control over proximity via \(\sigma\).** Section 4.4 derives closed-form expressions for the 1D Gaussian case showing how \(\sigma\) controls both mean shift and variance of \(\mathbf{X}_1 \mid \mathbf{X}_0\). The empirical results (Figures 2–5) visually bear this out across 2D, MNIST, and CelebA, and the model does not need retraining for different \(\sigma\) values.

## Weaknesses

### Fatal
None.

### Major

1. **Experimental evaluation lacks the quantitative rigor needed to support key claims.**
   - **No reported FID numbers.** The paper states only that "FID scores [are] decreasing with training iterations" (Section 5) but provides no final FID values, learning curves, or comparisons to any baseline for image experiments. For a paper claiming a new generative method, this is a significant omission.
   - **No empirical comparison to Albergo et al. (2023).** The paper criticizes their interpolants for lacking kinetic optimality (Sections 1, 6) and claims this optimality is "correlated to sampling effectiveness" (Shaul et al., 2023), but never demonstrates any practical advantage — sample quality, sampling speed, or otherwise — over that work on a common task.
   - **No wall-clock time or gradient-step measurements.** The computational savings claim is supported only by outer-iteration convergence on a Gaussian toy (Figure 1). Without wall-clock time or total gradient steps, "half the training iterations per outer iteration" may not translate into real savings if outer iterations themselves become more expensive.
   - **No quantitative metric for the "in-distribution variation" claim.** The paper's central application claim — controlled proximal resampling — is supported only by visual inspection (Figures 2–5). No metric quantifying the trade-off between proximity (distance from input to output) and diversity (spread of outputs) is provided, nor is there a comparison to simple baselines (e.g., Gaussian-noise-then-denoise).

2. **The proof of Theorem 1 relies on Lemma 2 without sufficient justification.** Lemma 2 asserts that the forward and reverse KL projections onto \(\mathbb{D}(\cdot,\pi_1)\) and \(\mathbb{D}(\pi_0,\cdot)\) have the same argmin. While this is cited to Vargas & Nüsken (2023), the paper does not reproduce the argument, state the precise conditions, or explain why it applies to the specific sets in the AMP scheme. The proof then invokes a "Pythagorean theorem for reverse \(D_{\mathrm{KL}}\) projections" without citing conditions or establishing its applicability to \(\mathbb{D}(\cdot,\pi)\) and \(\mathbb{S}\). Given that the convergence proof hinges on these steps, the theoretical contribution feels incomplete.

3. **The practical algorithm (Section 4.3) is under-specified.** The paper states that the reverse KL projection onto \(\mathbb{S}\) (time-symmetric path measures) can be done "completely analytically" but provides no derivation or formula in the main text. The text on line 126 is garbled ("of the form , for ."), and the description jumps to a figure reference (Algorithm 1) without explaining *how* one parameterizes a time-symmetric measure or computes this projection. This makes the algorithmic contribution difficult to reproduce independently.

### Minor

- **No statistical significance or variance reporting.** The Gaussian transport experiment (Figure 1) appears to show single-run convergence curves without error bars or multi-seed analysis.
- **The effect of the drift coefficient \(\alpha\) is not discussed.** All experiments use an Ornstein-Uhlenbeck reference with drift \(-\alpha\), but the paper never analyzes how \(\alpha\) interacts with \(\sigma\) to affect the resulting bridge or proximity control.
- **Extrapolation from the 1D Gaussian case to general distributions is heuristic.** Section 4.4 derives exact formulas only for \(\pi = \mathcal{N}(0,1)\). The claim that "similar effects occur even when \(\pi\) is not Gaussian" is stated without a theoretical bound or systematic empirical verification.
- **The paper invokes a Pythagorean theorem for reverse KL projections** (line 116) without citing a reference or establishing the conditions under which this holds for the sets \(\mathbb{D}(\cdot,\pi)\) and \(\mathbb{S}\).

### Trivial
None.

## Nice-to-Haves

- A comparison with Albergo et al. (2023) on MNIST or a 2D dataset would concretely validate the kinetic optimality claim.
- Reporting final FID scores with standard errors and showing a quantitative proximity-vs.-diversity trade-off curve (e.g., distance vs. effective sample size as \(\sigma\) varies) would substantially strengthen the empirical evaluation.
- An ablation study isolating the effect of \(\alpha\) relative to \(\sigma\) would improve completeness.

## Removed Points

- **"Lemma 2 is likely false in the claimed generality" (Harsh Critic, Critical Issue 1).** This claim is speculative and not substantiated. The equivalence of forward and reverse KL projections onto sets defined by fixed-marginal constraints is a known result in information geometry (the sets are affine subspaces; the projection yields the same exponential tilt). The paper correctly cites Vargas & Nüsken (2023) for this lemma. The legitimate concern is that the paper provides no proof or conditions — this is retained as a Major weakness above, but the claim that it is "likely false" is removed.
- **"The comparison should be against a naive two-network IPFP for the mirror case, not DSB/DSBM" (Harsh Critic, Critical Issue 3a).** DSB (De Bortoli et al., 2021) and DSBM (Shi et al., 2023) *are* the standard two-network IPFP implementations for Schrödinger bridges. Comparing against them is the correct and fair baseline. This criticism reflects a misunderstanding and is removed.
- **Strength Finder strength about "comparative efficiency claim supported by Gaussian benchmark."** This phrasing overstated what the evidence actually supports. The Gaussian benchmark shows comparable outer-iteration convergence with half the training iterations per outer loop, but (as noted in the major weaknesses) no wall-clock measurement. The strength is downgraded accordingly.
- **Generic strengths from Strength Finder.** Removed the unspecific claim that the paper "leverages time-symmetry to obtain a simpler projection step" phrased as an independent strength — it is an aspect of the algorithmic contribution already covered.

## Novel Insights

The reviews surface a core tension: the paper's theoretical machinery (AMP with reversed KL projections) directly enables its practical contribution (single-network training), but neither side is fully convincing on its own. The convergence proof leans on Lemma 2 without a self-contained argument, while the experimental validation lacks the quantitative baselines and metrics needed to substantiate the claimed practical advantages. The mirror SB formulation itself is genuinely novel and well-motivated, but the paper needs either stronger theory (a more self-contained convergence proof) or stronger experiments (FID numbers, wall-clock comparison, quantitative proximity/diversity curves) — and preferably both — to reach the standard required for acceptance.

## Suggestions

1. **Strengthen the theoretical case.** Either provide a self-contained justification of Lemma 2 (or at minimum state the precise conditions with a clear reference) and establish the Pythagorean theorem for reverse KL projections for the relevant sets \(\mathbb{D}(\cdot,\pi)\) and \(\mathbb{S}\).

2. **Report quantitative experimental results.** Include final FID scores (with comparisons to DSB, DSBM, and Albergo et al. (2023)), wall-clock time or total gradient-step measurements, and a quantitative metric for the proximity/diversity trade-off (e.g., average \(\|x_0 - x_1\|\) vs. effective sample size or LPIPS diversity).

3. **Derive the analytic reverse KL projection.** Add the derivation showing why the reverse projection onto \(\mathbb{S}\) can be done analytically and provide the resulting update rule in the main paper or a clearly referenced appendix.

4. **Add error bars and multi-seed runs.** Report convergence curves with standard deviations over multiple seeds for the Gaussian transport experiment.

## Score and Decision

The paper identifies a genuinely novel and useful variant of the Schrödinger bridge, provides an interesting theoretical convergence result, and derives a genuine algorithmic simplification (single-network training). However, the experimental evaluation is substantially weaker than what is needed to support the paper's broader claims: FID numbers are absent, the kinetic optimality advantage over Albergo et al. (2023) goes unvalidated empirically, and the central "controlled in-distribution variation" claim relies entirely on visual inspection. The theoretical proof also has gaps in its presentation (pivoting on Lemma 2 without justification and invoking a Pythagorean theorem without citing conditions). These are real problems, but they are addressable — not fatal to the core idea.

I recommend **rejection** in the current form, but with encouragement to resubmit after addressing the experimental and theoretical gaps.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>