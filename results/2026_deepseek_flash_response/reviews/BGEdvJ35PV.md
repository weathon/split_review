## Summary

This paper argues that molecular data distributions have a "dense-concentrated structure" (DC-structure) — narrow, densely packed probability peaks — making diffusion models fragile because reverse steps can overshoot valid regions. To address this, the authors propose DIST, a plug-in corrective sampling module that generates multiple candidate trajectories, runs pilot inference on them, and discards batches whose pilot scores indicate drift away from valid molecular distributions. DIST is evaluated on QM9 and GEOM-Drugs across three backbone architectures (EDM, GeoLDM, RADM), showing consistent improvements in stability and validity while reducing the average number of timesteps.

## Strengths

1. **Formal definition of DC-structure with a concrete overshoot condition (Definition 3.1 + Equation 7).** The paper does not merely observe that molecular distributions are sharp — it formalizes them as a mixture of narrow Gaussians with bounded covariance and separated means, then derives the condition β_t·Δ/σ_*² > cσ_* under which a reverse step overshoots the valid peak. This gives the fragility claim a quantitative grounding that goes beyond intuition.

2. **Consistent improvements across three backbone architectures with fundamentally different inductive biases (Table 2).** On QM9, DIST improves molecule stability by 7.9pp for EDM (82.0% → 89.9%), 4.0pp for GeoLDM (89.4% → 93.4%), and 4.1pp for RADM (87.3% → 91.4%). On GEOM-Drugs, validity improves for all three (e.g., EDM: 92.6% → 96.0%). The gains span GNN-based equivariant, VAE-latent-space, and Transformer-based non-equivariant models, supporting the claim that the problem is architectural-agnostic.

3. **Diagnostic experiment isolating the source of degradation (Table 1).** Running reverse inference starting from intermediate timesteps t shows monotonic degradation from 95.2% mol. stability (t=0, clean data) to 82.0% (t=1000, full diffusion). This directly supports the claim that error accumulation over the reverse trajectory is the core problem.

4. **Ablation on pilot subset size showing monotonic quality-cost tradeoff (Table 4).** Varying pilot sizes (30, 50, 100) produces monotonic improvements in molecule stability (89.5% → 89.9% → 90.5%) with corresponding timestep costs (428 → 556 → 645), confirming the mechanism is responsible for the gains.

## Weaknesses

### Major

1. **Baselines are not re-run in a controlled setting.** The paper states (line 206) that baseline results are "directly obtained from their original work." DIST-augmented models are run using official weights, but the baseline numbers come from different papers — potentially different hardware, random seeds, evaluation code, or data splits. This is a significant credibility concern: the claimed improvements (up to 7.9pp) could partly reflect variance rather than genuine gains. Re-running EDM, GeoLDM, and RADM in the same environment is not a tangential request; it is central to whether the contribution is convincingly demonstrated. The paper would be stronger if it included standard deviations for baselines, or re-ran them.

2. **Conceptual gap between theoretical diagnosis and proposed cure.** The theoretical analysis (Section 3.1, Equations 6–7) identifies a dynamical problem: the reverse step size β_t·Δ/σ_*² is large relative to peak width cσ_*, causing updates to step past valid peaks. DIST does not address this dynamical problem — it does not modify step size, correct the score estimate, or prevent overshoot. Instead, it applies a selection filter at an intermediate timestep (generate many candidates, evaluate pilot scores, discard poor ones). This is fundamentally rejection sampling / filtering, not a correction of the sampling dynamics. The Selective Reverse Error Bound (Proposition 3.1) is a generic statement about any filtered distribution and does not specifically depend on the DC-structure analysis. The theory motivates *why* trajectories fail but does not justify *why* this particular filtering strategy repairs them.

3. **Efficiency accounting is incomplete.** DIST claims "nearly half the standard number of timesteps" (Table 3: 413–637 vs. 1000). However, DIST generates candidate batches, runs pilot inference on subsets, and discards rejected batches — all of which consume computation that is not transparently accounted for in the reported timestep numbers. The formula (T-t)/|B| + t in line 221 does not include the cost of pilot inference or generating/evaluating discarded candidates. The paper needs to report total computational cost (total model evaluations, or GPU-hours) to generate 10,000 molecules, not just average timesteps on accepted trajectories.

4. **No comparison against alternative corrective or guidance methods.** The paper compares DIST-augmented backbones only against the same backbones without DIST. It does not compare against any alternative trajectory-correction approaches — e.g., classifier-guided diffusion, rejection sampling at the final step, or simpler baselines such as generating many molecules and picking valid ones at t=0. Without such comparisons, it is unclear whether the improvements come from DIST's specific design or merely from any filtering approach.

### Minor

5. **Observation novelty claim is overstated.** Line 27 states "We are the first to highlight that molecular data distributions are highly concentrated and dense that makes diffusion-based generative processes fragile." The fact that molecular geometry is tightly constrained and small perturbations produce invalid structures is well-recognized in prior molecular generation literature (e.g., EDM, GeoLDM, and related works all make this point). The DC-structure *formalism* (Definition 3.1) is novel, but the observation itself is not.

6. **DC-structure assumptions are unverified.** Definition 3.1 assumes the marginal p_t is a mixture of Gaussians with bounded covariance and separated means at all "operative noise levels" t. No empirical evidence is provided that molecular data distributions actually satisfy these structural assumptions, especially at intermediate noise levels where the forward process blurs peaks. The parameter σ_* is claimed to be "small for molecular data" but how it is determined from the data is not specified.

7. **GEOM-Drugs results lack standard deviations.** Table 2 reports only point estimates for GEOM-Drugs without standard deviations or error bars, making it impossible to assess whether improvements are significant relative to run-to-run variance.

### Trivial

None.

## Nice-to-Haves

- An analysis of what DIST actually selects — what fraction of batches are rejected, whether valid molecules are ever discarded, and whether rejected batches correspond to trajectories that would produce invalid final molecules.
- An evaluation on additional fine-grained molecular properties (e.g., energy, dipole moment, QM9 property prediction) would strengthen the case beyond the standard validity/stability metrics.
- A sensitivity analysis of the key DIST hyperparameters (pilot score function s_j, threshold τ, intermediate timestep t, perturbation intensity) in the main text rather than deferred entirely to the appendix.

## Removed Points

These points were flagged by the harsh critic but removed for the following reasons:

- **"The pilot score s_j is never specified."** Removed because the paper explicitly states (line 225) that hyperparameter details are in Appendix H, which was stripped by the parser. The same applies to criticism about hyperparameter ablation being deferred to the appendix.
- **"Corollary 3.1 is generic and doesn't depend on DC-structure."** This is factually correct but is a relatively minor framing point. The paper's main theoretical contribution is the DC-structure formalism and the error bound (Proposition 3.1), not the TV-contraction step. Removed to keep focus on substantive issues.
- **"Structural issues about comparing against papers that don't exist / aren't released."** Removed per the hard rule that any cited model, benchmark, or reference is assumed to exist.
- **"Formatting typos and parser artifacts."** Removed per rules.
- **"Missing related works."** Removed — not verifiable without external sources.

## Novel Insights

An interesting observation that emerges from synthesizing the reviews is that the paper's theoretical apparatus (DC-structure, overshoot condition, TV-contraction) is its strongest differentiator from a simple "generate-and-filter" heuristic, yet it is also where the gap is widest. The overshoot analysis cleanly explains *why* molecular diffusion fails (step size exceeds peak width), but DIST's filtering mechanism does not prevent overshoot — it merely discards samples that have already overshot. A genuinely stronger paper would either (a) derive a step-size adaptation from the overshoot condition itself, closing the theory-method loop, or (b) reframe the theory as motivation and present the method on its own terms as a practical correction module, without overclaiming theoretical grounding. The current presentation occupies an uncomfortable middle ground.

## Suggestions

1. **Re-run the baselines in a controlled setting.** Use official model weights for all baselines and re-run in the same environment. Report standard deviations for both baselines and DIST-augmented versions. This single change would resolve the most serious credibility threat.
2. **Report total computational cost honestly.** Include the cost of generating candidate pools, pilot inference, and discarded trajectories. Total GPU-hours or total model evaluations for 10,000 molecules, not just average timesteps on accepted trajectories.
3. **Compare against alternative filtering/guidance baselines.** At minimum: rejection sampling at t=0 (generate many molecules, pick valid ones), and a simpler filtering heuristic (e.g., early-stopping based on validity checks at intermediate timesteps).
4. **Either close the theory-method gap or reframe the contribution.** If the method is filtering, state it as such. If the theory is meant to justify the method, explain *why* filtering at intermediate timesteps (rather than any other correction) follows from the overshoot analysis.

## Score and Decision

**Calibration anchors (all rounds):**

| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| Unified Generative Modeling of 3D Molecules with Bayesian Flow Networks | 8.00 | R1 (7.5-11) | Significantly stronger: introduces a wholly new generative framework with SOTA results on the same benchmarks |
| Chemistry-Inspired Diffusion with Non-Differentiable Guidance | 6.00 | R2 (5.5-7.5) | Stronger: clearer novel contribution (non-differentiable guidance) and more thorough evaluation, accepted at ICLR |
| Training-free Guidance in Multi-modal Generative Flow for Inverse Molecular Design | 6.25 | R1 (3.5-7.5) | Stronger: solid theoretical contributions and good experiments, accepted at ICLR |
| Protein-Ligand Interaction Prior for Binding-aware 3D Molecule Diffusion Models | 6.25 | R2 (5.5-7.5) | Stronger: more rigorous evaluation and comparison methodology, accepted at ICLR |
| VFDiff | 6.00 | R2 (5.5-7.5) | Similar strength but rejected for insufficient novelty; our paper has similar novelty concerns |
| Dynamics-Informed Protein Design with Structure Conditioning | 5.50 | R1 (3.5-7.5) | Similar: accepted despite "light on content" concerns, but our paper has more significant methodological weaknesses |
| Molecule Relaxation by Reverse Diffusion with Time Step Prediction | 4.75 | R1 (3.5-7.5) | Slightly weaker: less consistent improvements across architectures, fewer backbones tested, rejected |
| Generating Molecular Conformer Fields | 4.40 | R2 (4.0-6.0) | Similar: moderate-quality molecular diffusion paper with comparable rigor level, rejected |
| A diffusion model on toric varieties with application to protein loop modeling | 4.50 | R2 (4.0-6.0) | Similar: moderate-quality paper, rejected |

**Round 1 bracket:** The paper sits between weak anchors (~3.0, other molecular diffusion papers) and strong anchors (~8.0, SOTA molecular generation). Initial bracket: [4.0, 6.0].

**Round 2 narrowing:** Compared against CHEMGUIDE (6.0, accepted), VFDiff (6.0, rejected), MoreRed (4.75, rejected), and conformer fields (4.40, rejected). The paper is stronger than the rejected papers at the low end (MoreRed, conformer fields) but clearly weaker than the accepted papers at the high end (CHEMGUIDE, TFG-Flow). The baselines-not-re-run issue, theory-method gap, and incomplete efficiency accounting are substantive weaknesses that prevent acceptance at ICLR bar.

**Final score: 5.0.** The paper identifies a genuine problem and shows promising results, but the evidence is undermined by methodological weaknesses that the authors would need to address in a revision. The DC-structure formalism and the consistent improvements across diverse backbones are real contributions, but they are not sufficient to overcome the credibility concerns in their current presentation.

**MY FINAL SCORE: <score>5.0</score>**
**MY FINAL DECISION: <decision>Reject</decision>**