## Summary

ESS-Flow proposes a training-free gradient-free method for controlled generation with flow-based generative models. The key insight is to recast Bayesian inference in the Gaussian source space rather than the data space, where the Jacobian determinant terms cancel (Equation 3), enabling the use of Elliptical Slice Sampling without gradient computation. The method is demonstrated on material design (targeting continuous properties and a non-differentiable space group) and protein structure prediction from sparse distance measurements.

## Strengths

- **Gradient-free operation on a genuinely non-differentiable task (Section 5.1, space group experiment):** The paper targets the P6₃/mmc space group using a binary indicator potential computed by a non-differentiable external program (Togo et al., 2024). ESS-Flow achieves 92.3% hit rate vs 2.5% unconditional—a task none of the gradient-based baselines can even attempt. This is the cleanest demonstration of the method's distinctive value proposition.

- **Theoretical lynchpin: Jacobian cancellation (Equation 3, Section 4.1):** The paper derives that by expressing both prior and posterior in source space, the Jacobian determinant terms cancel exactly, yielding π(z) ∝ g(T_θ(z)) p(z) with no Jacobian evaluation. This clean derivation is what makes ESS applicable where even other source-space methods (D-Flow, Purohit et al., Wang et al.) require expensive backpropagation through the ODE.

- **Strong quantitative results on material property targeting (Table 2):** ESS-Flow achieves substantially lower mean absolute errors than all baselines on bulk modulus (8.99 vs 39.14 for DAPS), shear modulus (10.53 vs 75.48 for PnP-Flow), and band gap (1.85 vs 3.90 for DAPS), with significantly tighter standard deviations on bulk and shear modulus. These are large, unambiguous margins.

- **Formal convergence guarantee (Proposition 1, Section 4.1):** The paper provides a geometric convergence result adapted from Natarovskii et al. (2021), showing the ESS-Flow Markov chain converges geometrically fast in TV distance—a guarantee absent from optimization-based methods like D-Flow and PnP-Flow.

## Weaknesses

### Major

- **Missing MCMC diagnostics for the main experiments:** ESS-Flow is fundamentally an MCMC method that the paper pitches as a sampling alternative to optimization. Yet the paper provides no trace plots, no autocorrelation plots, no acceptance rates, no burn-in discussion, and no convergence diagnostics for the primary material generation and protein experiments. The number of MCMC iterations used is not stated; it is unclear whether the reported 1000 samples (Table 3 caption) come from one long chain or multiple chains, or what thinning factor was used. Effective sample sizes are only reported for the multi-fidelity ablation, not the main results. Without this information, the reader cannot assess whether the reported samples are representative draws from the target distribution or pre-convergence artifacts. For an MCMC paper, this is a significant omission that limits the credibility of the sampling claims.

### Minor

- **Protein structure prediction experiment is thin:** Only 10 samples per method from a single protein (PDB:7r5b/7f5b) are generated, providing a weak basis for general claims. ESS-Flow achieves the best ELBO (8.89) and low clash count (24.8) among conditional methods—supporting the realism claim—but its data fidelity (d_y=37.02) and RMSD (13.55) are notably worse than ADP-3D and DAPS. While the paper honestly acknowledges the trade-off, the experiment provides limited evidence either way, and involving more proteins would considerably strengthen the evaluation.

- **Multi-fidelity approach collapses for sharp targets (Section 5.1.1):** The simple importance weighting scheme achieves reasonable effective sample sizes for bulk modulus (65.3%) and shear modulus (33.9%) but collapses to 0.1% and 1.0% for band gap and stability tasks. The paper acknowledges this, but it substantially limits the practical value of the multi-fidelity proposal for the cases where it would be most needed.

### Trivial

- The material generation comparison would benefit from clearer visual separation between baselines that are structurally handicapped by the continuous relaxation of atomic numbers (D-Flow, PnP-Flow) and those that handle discrete variables natively (DAPS, ESS-Flow). The paper discusses this issue in the text but the tables could reflect it more clearly.

## Nice-to-Haves

- Expanding the space-group-style non-differentiable experiments (more potentials, more black-box simulators) would more decisively demonstrate the method's unique value.
- Adding standard MCMC diagnostics (trace plots, acceptance rates, R-hat, chain length) for the main experiments.
- Running the protein experiment on more proteins (5–10) with more samples per protein.
- A more principled multi-fidelity approach (delayed acceptance or tempering) for sharp targets, as the paper itself suggests.

## Removed Points

- **"Comparison on material generation is structurally uneven" (Harsh Critic, Critical Issue 3):** The paper explicitly acknowledges and explains why D-Flow and PnP-Flow use continuous relaxation and that D-Flow fails to explore atomic compositions. ESS-Flow outperforms the fair baseline (DAPS) by large margins. The paper is transparent about this setup; this is not a weakness. REMOVED: authors already address this reasonably.

- **"Computational cost is unstated" (Harsh Critic, Critical Issue 4):** The paper states "Hyperparameter details and the runtime costs of the methods are provided in the Appendix" (line 183) and mentions "moderate numbers of function evaluations" (line 271). The appendix was stripped by the parser. The paper does address this; the missing content is a parser artifact. REMOVED: paper states runtime info is in appendix.

- **"Protein experiment does not support the claims" (Harsh Critic, Critical Issue 2, strong framing):** The harsh critic frames this as fatal, but the paper's claim is about "improved structural realism" which IS supported by the ELBO and clash count data. The paper is transparent about the trade-off and acknowledges the high RMSD. REMOVED: overstates the severity; the actual weakness is about limited scale (10 samples, 1 protein), which is already listed as a Minor weakness.

- **Strength Finder generic strengths removed:** Strength Finder claims about "addressing an important problem" are too generic to retain. The concrete strengths (Jacobian cancellation, space group experiment, Table 2 results, convergence guarantee) are retained.

## Novel Insights

None beyond the paper's own contributions. The core technical insight (Jacobian cancellation enabling ESS in source space) is clean and well-presented; the reviews do not surface additional observations beyond what the paper itself states.

## Suggestions

1. Add MCMC diagnostics (trace plots, acceptance rates, chain length, R-hat) for the main material and protein experiments to support the method's validity as a sampling algorithm.
2. Expand the space-group-style non-differentiable experiments—this is where the method's unique advantage is most decisive and where it clearly outperforms all competitors.
3. Run the protein experiment on more proteins (5–10) with more samples per protein to strengthen the conclusions about structural realism.
4. Replace or augment the simple importance-weighting multi-fidelity approach with delayed acceptance or tempering for sharp targets, as the paper suggests in future work.

## Calibration

**Round 1 bracket:** 5.5–7.0, determined by comparing ESS-Flow against retrieved anchors in three bands (weak: Dreamguider 4.00, Think Twice 4.75; middle: TFG-Flow 6.25, OC-Flow 6.50; strong: 6EUtjXAvmj 8.00, RuP17cJtZo 8.00).

**Round 2 anchors (read in full):**
- TFG-Flow (6.25, sim 0.79, *Training-free Guidance in Multi-modal Generative Flow for Inverse Molecular Design*): Similar topic and approach. ESS-Flow has a cleaner theoretical contribution and stronger material results, but TFG-Flow does not have an equivalent MCMC diagnostics gap.
- OC-Flow (6.50, sim 0.68, *Training Free Guided Flow-Matching with Optimal Control*): Related topic. ESS-Flow has cleaner, more transparent experiments and a simpler core idea. OC-Flow's reviewers flagged questionable baseline results, which ESS-Flow avoids.
- Dreamguider (4.00, sim 0.78, *Dreamguider: Improved Training free Diffusion-based Conditional Generation*): ESS-Flow is clearly stronger—more novel contribution, cleaner theory.
- Think Twice/DPMC (4.75, sim 0.72, *Think Twice Before You Act: Improving Inverse Problem Solving With MCMC*): ESS-Flow is stronger—more novel, better results, though DPMC also uses MCMC for posterior sampling.
- FIG (6.00, sim 0.71, *FIG: Flow with Interpolant Guidance for Linear Inverse Problems*): ESS-Flow has a more distinctive contribution; FIG's reviewers noted limited novelty. ESS-Flow's experiments are on specialized domains rather than standard image benchmarks, which is both a limitation and a strength.

**Final score determination:** ESS-Flow is clearly stronger than the 4–5 range anchors and comparable to the 6.0–6.5 anchors. Its core contribution (gradient-free source-space MCMC via Jacobian cancellation) is clean and well-motivated, and the material generation results are strong. However, the missing MCMC diagnostics constitute a notable gap for an MCMC paper, and the protein experiment is thin. Score: 6.0.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>