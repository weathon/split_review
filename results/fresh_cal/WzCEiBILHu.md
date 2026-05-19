Here is my final consolidated review.

---

## Summary

This paper introduces Iterative Markovian Fitting (IMF), a dual formulation to the classical Iterative Proportional Fitting (IPF) for solving Schrödinger bridge problems, and proposes Diffusion Schrödinger Bridge Matching (DSBM), a practical algorithm that implements IMF by alternating forward and backward Markovian projections learned via bridge-matching regression losses. The key algorithmic innovation is that DSBM caches only the coupling (X₀, Xₜ) rather than full trajectories, and explicitly projects onto the reciprocal class to prevent the "forgetting" of the reference bridge. Experiments on 2D benchmarks, high-dimensional Gaussians, image transfer tasks (MNIST↔EMNIST, CelebA, AFHQ), and fluid downscaling show that DSBM outperforms prior DSB methods and scales to resolutions well beyond what previous SB solvers have demonstrated.

## Strengths

- **IMF as a principled dual to IPF with clean theoretical foundations.** The paper clearly establishes IMF as the dual of IPF (Table 1): where IPF preserves the Markov and reciprocal properties while alternating on endpoint constraints, IMF preserves the endpoint distributions at every iterate while alternating projections on the Markov class ℳ and the reciprocal class ℛ(Q). Lemma 1 proves Pythagorean identities for both projections, Proposition 3 establishes the SB as the unique fixed point, and Theorem 1 shows convergence. This is a well-structured theoretical contribution that clarifies the relationship between existing SB solvers.

- **DSBM demonstrably reduces error accumulation compared to DSB.** The Gaussian experiment (Table 2) provides strong quantitative evidence: DSBM-IPF achieves KL divergence of 8.75±0.87×10⁻³ in d=50, versus 32.8±1.28×10⁻³ for DSB and 49.4±3.91×10⁻³ for SB-CFM — roughly 3–5× more accurate. The table reports 21 uniformly spaced time slices with standard deviations, making this concrete evidence that DSBM mitigates the bias accumulation problem.

- **DSBM consistently outperforms DSB across all 2D benchmarks.** Table 1 shows DSBM-IPF, DSBM-IMF, and DSBM-IMF+ all achieve strictly lower 2-Wasserstein errors than DSB on moons, scurve, 8gaussians, and moons-8gaussians. For example, on scurve, DSBM-IMF+ achieves 0.130±0.025 versus DSB's 0.272±0.065. Path energies are also uniformly lower for DSBM variants.

- **DSBM scales to high-dimensional transfer tasks beyond previous SB methods.** The paper demonstrates results on MNIST→EMNIST (28×28), CelebA (64×64 and 128×128), and AFHQ (512×512) — the latter is at a resolution where prior SB methods have rarely shown results. The FID-vs-iteration plot (Figure 3b) shows DSBM does not suffer the deterioration observed in DSB and RF during iterative training.

- **DSBM recovers several existing transport methods as special cases.** Proposition 6 shows DSBM-IPF initialized with Q₀,ₜ recovers DSB's IPF iterates; Section 5 notes DSBM-IMF reduces to Rectified Flow as σ→0; and Denoising Diffusion and Flow Matching arise as specific implementations of the Markovian projection. This provides a unifying taxonomy (Figure 1).

## Weaknesses

### Major

- **Title-content mismatch: the word "topological" never appears in the paper body.** The title reads "Topological Schrödinger Bridge Matching," yet the term "topological" is absent from the abstract, introduction, method, experiments, discussion, and all section headings. The paper is entirely about Euclidean diffusion processes and iterative Markovian/reciprocal projections — there is no topological data analysis, no topological path spaces, no topological constraints. This will mislead readers searching for work on topological transport or topology-aware methods. The fix is straightforward (renaming to something like "Diffusion Schrödinger Bridge Matching," which the body already uses consistently), but the title as-is is genuinely inaccurate.

### Minor

- **The "about 30% more efficient than DSB" runtime claim is unsupported.** Line 789 states "It is also about 30% more efficient than DSB in terms of runtime" with zero supporting evidence: no wall-clock measurements, no per-iteration vs. total-time breakdown, no specification of whether this refers to training, sampling, or total runtime. The paper does have a legitimate efficiency argument (caching only couplings rather than full trajectories), but this specific quantitative claim is vacuous without data. Either provide measurements or remove the number.

- **The Gaussian convergence figure (Figure 2) lacks some reporting detail.** The figure plots convergence of mean, variance, and covariance, but the text does not specify which DSBM variant (IPF, IMF, or both) is shown, whether the curves are averaged over multiple seeds, or whether the single run displayed is representative. The adjacent KL table (Table 2) is properly reported with standard deviations and is the stronger evidence, but the figure itself should be documented to the same standard since it is cited as evidence that "DSBM does not suffer from this issue."

- **Optimal σ values are not stated for the 2D and Gaussian experiments.** The paper uses a Brownian bridge reference (f_t=0, σ_t=σ) throughout, which is clear from context. However, the specific σ value used to produce Table 1 (2D benchmarks) and Table 2 (Gaussian) is not reported. For the Gaussian experiment, the figure filename suggests σ²=0.1 but this is never stated in the text. For the 2D experiments, the paper only notes that "the optimal σ varies for each task" without stating the values used.

- **DSBM-IMF+ does not consistently beat OT-CFM in 2D, and this is not discussed.** On the 8gaussians dataset, OT-CFM achieves 0.238±0.044 while DSBM-IMF+ achieves 0.276±0.030. Since DSBM-IMF+ uses the same minibatch OT coupling as initialization then iterates, a reader would expect iterative refinement to improve — or at least not worsen — the result. The paper should acknowledge this and discuss conditions under which extra iterations help or hurt.

### Trivial

- **FM has a dash ("—") for the moons-8gaussians 2-Wasserstein result with no explanation.** The table (Table 1) shows "—" for FM on this dataset but never explains whether this is because the method failed, was not run, or the metric was not applicable. A footnote or caption remark would help.

- **Path energy is not reported for DSB.** Table 1 shows "—" for DSB path energy, but the paper does not explain why. Since DSB is a primary baseline, this omission weakens the comparison.

## Nice-to-Haves

- The paper could explicitly discuss how the number of IMF iterations is chosen in each experiment (the figures show up to 20 iterations, but table results may use a fixed number).
- For the fluid downscaling experiment, FID or structural similarity would complement the L2 distance metric, though L2 is defensible for physical fields.
- A brief sensitivity analysis of the iteration count's effect on final quality would be practically useful.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **The algorithm listing is missing (macro `\dsbmalgo` not expanded).** The harsh critic flags this, but the macro would have been expanded in the original PDF; only the text-extraction layer failed to capture it. This is a parser artifact, not a paper flaw.
- **Criticism that "the paper does not state which reference process Q is used."** The paper does state this: eq. (1) defines the reference SDE, and line 204 explicitly notes that for f_t=0 and σ_t=σ the bridge is a Brownian bridge. The specific σ values could be stated more clearly (handled in Minor above), but the reference process class is specified.
- **"Proposition 4 (equivalence of forward and backward Markovian projections via time reversal) is correct"** — this is framed as a positive note by the critic but is actually just a statement that the math is sound, not a specific weakness; it does not belong in the Weaknesses section.
- **Nitpicks about the visual quality of downsampled figure images in the review format.** These are format artifacts unrelated to paper quality.
- **Strength Finder claim #5 about computational efficiency** partially conflicts with the verified weakness about the unsupported 30% claim. The general efficiency advantage from coupling-only caching is valid and supported (Section 4, paragraph after Proposition 5), but the specific 30% claim is unsupported; this strength is absorbed into the broader evaluation rather than listed separately.
- **Strength Finder claim about DSBM recovering Rectified Flow and DDMs as special cases** is factually correct and well-supported; kept in Strengths above.

## Novel Insights

None beyond the paper's own contributions. The two-reviewer synthesis surfaces a sharp tension: the strengths are substantive (a genuinely new algorithmic framework with strong empirical results across multiple scales), while the main actionable issues are presentation and documentation gaps (a misleading title, an unsupported runtime number, and under-detailed experiment captions). No genuinely novel insight emerges beyond what the paper itself states.

## Suggestions

1. **Change the title.** Replace "Topological" with "Diffusion" or remove it entirely — the body consistently uses "Diffusion Schrödinger Bridge Matching" and that is what the paper delivers.
2. **Either remove the "30% more efficient" claim or substantiate it** with wall-clock measurements, error bars across runs, and a clear statement of what the 30% refers to (per-iteration training time? total time to convergence?).
3. **Document the Gaussian convergence figure properly:** state which DSBM variant is plotted, how many seeds were used, and add error bars or note that the curves are representative.
4. **Report the σ values used for each experiment** in Table 1 and Table 2 captions or in a dedicated experimental setup paragraph.
5. **Acknowledge the OT-CFM vs. DSBM-IMF+ comparison** — discuss when iterative refinement helps (and why it doesn't on 8gaussians).

## Score and Decision

The paper has a strong core contribution: IMF is a genuinely novel dual formulation to IPF, and DSBM is a practical algorithm that demonstrably improves on prior SB solvers in high dimensions. The experiments are broad and mostly well-conducted. The two most significant weaknesses — the misleading title and the unsupported runtime claim — are fixable without changing the science. No weakness invalidates the core results.

I recommend acceptance.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>