## Summary
The paper identifies that molecular data distributions exhibit a "dense-concentrated (DC) structure" — sharp probability peaks that are narrow and densely packed — which makes diffusion model inference uniquely fragile compared to image generation. Building on a formal characterization of this structure, the authors propose **DIST** (Diffuse and Steer), a model-agnostic plug-in corrective sampling method that filters and steers intermediate distributions during reverse inference toward valid molecular configurations. DIST is evaluated on QM9 and GEOM-Drugs using three diverse backbone architectures (EDM, GeoLDM, RADM), consistently improving performance while reducing inference cost to roughly half.

---

## Strengths

- **Clear and well-motivated problem identification.** The paper formally defines DC-structure (Definition 3.1), quantifies the overshoot mechanism through the step-size inequality in Eq. 7, and uses Table 1 to empirically verify that error accumulates monotonically with timestep. The conceptual contrast with image distributions (Fig. 1) is crisp and intuitive.

- **Theoretical backing.** Corollary 3.1 (TV-contraction of the ideal reverse kernel) and Proposition 3.1 (selective reverse error bound) provide principled support for the correction approach, making DIST more than heuristically motivated.

- **Model-agnostic generality.** DIST is demonstrated across three architecturally diverse backbones — GNN-based equivariant (EDM), Transformer-based non-equivariant (RADM), and latent-space (GeoLDM) — without altering their weights or hyperparameters. Consistent improvements on both datasets confirm the claim of plug-in compatibility.

- **Significant, consistent empirical improvements.** Molecule stability improves from 82.0% → 89.9% for EDM, and 89.4% → 93.4% for GeoLDM on QM9 — these are substantial margins on a well-studied benchmark. GEOM-Drugs results, while smaller in magnitude, are uniformly positive.

- **Efficiency gain is a concrete, non-trivial bonus.** Table 3 shows a genuine reduction to ≈400–640 expected steps (from 1000), not just a minor speedup. The pilot-batch mechanism is conceptually clean.

---

## Weaknesses

### Fatal
None.

### Major

1. **Pilot score $s_j$ is underspecified in the main text.** The score that drives all filtering is introduced as a list of possibilities ("round-trip residual, self-consistency, ensemble variance, or chemistry-based penalty") without stating what is actually used in experiments. This is the most operationally critical design choice in DIST, and deferring it entirely to an appendix makes it impossible to assess whether the method's empirical success is robust or contingent on a particular scoring function. A one-paragraph summary in the main body is needed for self-containedness.

2. **Efficiency accounting may be incomplete.** The formula $\frac{T-t}{|B|} + t$ steps is correct for one accepted batch, but it does not account for batches that fail the threshold $\tau$ and trigger resampling. The total expected cost depends on the rejection rate, which is not reported. Table 3 shows higher-than-formula values (556 vs. 307 for EDM), indicating significant rejection overhead, but this is not discussed or quantified. The "halving" claim in the abstract therefore rests on an incomplete budget.

3. **Insufficient differentiation from best-of-N / rejection sampling.** At its core, DIST generates multiple candidate trajectories, runs pilot completions to score them, and selects the best. This closely resembles well-known test-time compute strategies (e.g., best-of-N with a verifier). The paper does not include a baseline that simply generates $N$-fold more molecules and filters by the same scoring function at $t=0$, which would test whether the intermediate-timestep correction provides value beyond the inherent benefit of more compute and filtering.

### Minor

1. **Table 1 as motivation has limited discriminative power.** The observed degradation with timestep ($t=0$: 95.2% → $t=1000$: 82.0% molecule stability) follows trivially from any diffusion model with imperfect score matching; it does not uniquely implicate the DC-structure hypothesis. A parallel experiment on images (showing much smaller degradation under the same setup) would make the comparison concrete.

2. **Conditional generation tasks are absent.** DIST is motivated in part by structural validity, which is especially critical for conditional drug design (e.g., binding-pocket-conditioned generation, fragment linking). Restricting evaluation to unconditional generation limits demonstration of practical impact.

3. **Sensitivity of threshold $\tau$.** The main text delegates all hyperparameter ablations to the appendix. At least the qualitative behavior (is the method robust to $\tau$, or does performance cliff near an optimal value?) should be summarized in the main paper.

### Trivial

- The step-count in Sec. 4.3 ($\frac{700}{100} + 300 = 307$) appears to be a per-molecule amortized figure that assumes full GPU parallelism across the batch, which may not hold in practice; the accompanying prose should be more precise.

---

## Nice-to-Haves

- An empirical comparison of DIST against simple best-of-N filtering at $t=0$ (same compute budget) would strengthen the claim that intermediate-timestep correction is the key ingredient.
- A brief case study showing specific recovered molecules (before/after DIST) would make the abstract notion of "steering toward valid peaks" tangible.
- Extension to at least one conditional generation task (e.g., pocket-based ligand generation) would substantially broaden impact.

---

## Novel Insights

The most genuinely novel insight is the formal DC-structure definition paired with the overshoot inequality (Eq. 7), which gives a clean mechanistic explanation for *why* molecule peaks are problematic: not because molecular distributions are complex per se, but because the step magnitude $\beta_t \Delta / \sigma_*^2$ can exceed the peak radius $c\sigma_*$, placing the reverse update past the valid region rather than within it. This overshoot framing is cleaner and more actionable than prior empirical observations about molecular validity degradation, and the TV-contraction result makes the correction objective precise. The insight that this is geometry of the distribution — not model architecture — is valuable and likely applicable beyond the specific method proposed.

---

## Suggestions

- Include a one-paragraph description of the actual scoring function $s_j$ used in all experiments (move from Appendix F into Sec. 3.2).
- Report the rejection rate per batch (or equivalently, the expected number of resampling rounds) to enable a rigorous efficiency comparison.
- Add a best-of-N baseline at equivalent compute to isolate the benefit of intermediate-step correction from the benefit of increased compute and selection.
- Discuss, even briefly, how the DC-structure characterization relates to discrete molecular graphs — the current analysis is framed entirely in continuous coordinate space, but atom-type discreteness also contributes to the sharp peaks.

---

## Score and Decision

The paper addresses a real and well-posed problem with a principled method, provides theoretical grounding, and demonstrates consistent and non-trivial empirical improvements across heterogeneous architectures. The chief weaknesses — opacity of the scoring function and incomplete efficiency accounting — are significant but not fatal; they reflect presentation choices, not flaws in the core idea. The missing comparison to best-of-N at equal compute is the most substantive gap. Overall this is a solid contribution that merits acceptance with revision.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>