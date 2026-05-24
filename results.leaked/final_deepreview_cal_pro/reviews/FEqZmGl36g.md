Now I have a thorough understanding of the paper and the calibration anchors. Let me write the consolidated review.

---

## Summary

ESS-Flow proposes a training-free method for controlled generation with pretrained flow-based models. The key insight is to perform Bayesian inference in the Gaussian source space of the flow model, where the Jacobian of the transport map cancels out (Eq. 3), enabling gradient-free sampling via Elliptical Slice Sampling. The method requires only forward passes through the generative model and potential function, making it applicable when gradients are unavailable (e.g., discrete variables, non-differentiable simulators). The paper demonstrates effectiveness on materials design with target properties (including a truly non-differentiable space-group task) and protein structure prediction from sparse distance measurements.

## Strengths

- **Elegant, well-motivated method**: The Jacobian cancellation in Eq. 3 is clean and leads directly to a simple MCMC algorithm (Algorithm 1) that requires only forward evaluations. The connection to existing ESS convergence theory (Proposition 1) provides theoretical grounding without reinventing the wheel.

- **Genuine gradient-free capability demonstrated**: The space-group experiment (Section 5.1) is a compelling demonstration — targeting P6₃/mmc symmetry using an external, non-differentiable program achieves 92.3% target rate vs. 2.5% unconditionally. Gradient-based baselines cannot even be applied here, making this a clean, falsifiable test of the method's core claim.

- **Strong empirical results on materials design**: ESS-Flow substantially outperforms D-Flow, PnP-Flow, and DAPS on four quantitative property-targeting tasks (Table 2; e.g., bulk modulus MAE 8.99 vs. 39.14 for DAPS). It also achieves the highest S.U.N.T. rates across all tasks (Table 3), despite targeting extreme property values (99th percentile).

- **Demonstrates the sampling-vs-optimization trade-off in protein prediction**: Table 4 shows that while ADP-3D and DAPS achieve lower RMSD by overfitting to observations, they produce physically implausible structures (731 and 483 clashes, negative ELBO). ESS-Flow preserves the generative prior, yielding realistic structures (24.8 clashes, ELBO 8.89, comparable to unconditional sampling). Figure 4 makes this visually compelling.

- **Honest about limitations**: The paper explicitly acknowledges when the method struggles — high RMSD in protein prediction, poor multi-fidelity ESS for sharp target distributions, and the fundamental limitation with lower-dimensional manifold constraints.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Convergence diagnostics not shown in the main text**: For an MCMC-based method, trace plots, R-hat, or effective sample sizes would strengthen confidence that the reported results reflect well-mixed chains. The paper cites theoretical convergence (Proposition 1) and references numerical scaling evaluations in Appendix A.1, and the strong empirical results provide indirect evidence that the sampler works. Nevertheless, even a brief summary of key diagnostics (e.g., ESS per parameter, acceptance rates) in the main body would meaningfully strengthen the paper.

- **Computational cost comparison deferred to appendix**: The paper states that "runtime costs of the methods are provided in the Appendix" (line 241), which is stripped. While the main text notes that ESS-Flow uses "moderate numbers of function evaluations in the ODE solver, fewer than what is typically used for unconditional generation" (line 383), the reader cannot evaluate the practical cost of ESS-Flow relative to baselines from the main text alone. A summary table of NFE counts or wall-clock times would improve accessibility.

- **Multi-fidelity results are preliminary and mixed**: The importance-weighting scheme achieves reasonable ESS for bulk modulus (65.3%) and shear modulus (33.9%) but near-zero ESS for band gap (0.1%) and stability (1.0%). While the paper appropriately labels this as a "proof of concept" and "preliminary evaluation," the contribution would be stronger with at least one task showing that the multi-fidelity approach yields computational savings without quality degradation.

- **Limited sample size in protein experiment**: Only 10 backbone structures are generated per method (Table 4). While the qualitative difference in realism is clear (clash counts differ by orders of magnitude), a larger sample would enable more robust statistical comparisons, particularly for RMSD.

- **Lower uniqueness/novelty on some tasks**: ESS-Flow achieves lower U.N. rates than DAPS on bulk modulus (46.1% vs. 80.8%) and shear modulus (30.5% vs. 74.6%). The paper notes this but does not analyze the trade-off between target accuracy and sample diversity in depth. This is acknowledged as a natural consequence of targeting extreme property values, but a brief discussion would be valuable.

### Trivial
None.

## Nice-to-Haves

- A comparison against gradient-based MCMC (e.g., HMC in source space as in Wang et al. 2025) on at least one differentiable task would help quantify what is sacrificed by forgoing gradients — this would strengthen the gradient-free motivation, though it is not required to validate the method.

- A systematic study varying the potential scale σ_y to show the transition between unconditional and highly constrained regimes would deepen the analysis of the prior-likelihood trade-off.

- The claim that ESS-Flow "preserves the pretrained velocity field" (line 94) could be stated more precisely: the method does not modify the ODE dynamics; it operates by accepting/rejecting in source space while using the unmodified transport map.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **"Missing convergence diagnostics is a fundamental omission"** — REMOVED. The paper cites theoretical convergence guarantees (Proposition 1, adapted from Natarovskii et al. 2021) and references numerical evaluations in Appendix A.1. The empirical results across multiple tasks provide strong indirect evidence that the sampler works. While diagnostics in the main text would help, this is not "fundamental" given the existing theoretical and empirical support.

- **"Baselines in protein experiment may be unfairly tuned"** — REMOVED. This is speculative. The paper's explanation for ADP-3D/DAPS behavior (annealed noise weakens prior regularization, shifting toward overfitted MLE) is a well-known phenomenon in diffusion-based inverse problems, not obviously a hyperparameter tuning failure. The baselines are used as described in their original papers (Levy et al. 2024, Zhang et al. 2025). Without concrete evidence of tuning failure, this criticism does not stand.

- **"The soft-embedding scheme may penalize baselines unfairly"** — REMOVED. The paper carefully describes the continuous approximation (Eq. 5) and notes that DAPS avoids this issue by using Metropolis-Hastings for discrete variables. The paper also acknowledges D-Flow's failure due to this approximation. The comparison is handled transparently.

- **"Preserving the pretrained velocity field is slightly misleading"** — REMOVED. This is a standard distinction in the source-space methods literature (see Wang et al. 2025 for the same argument). Source-space methods do not add guidance terms to the ODE, unlike guidance-based methods — this is the intended meaning and is not misleading.

- **"ELBO computation requires justification"** — REMOVED. The paper uses Chroma's ELBO as a realism metric following Levy et al. (2024), which is standard practice for evaluating Chroma-based methods.

- **"Missing comparison to gradient-based MCMC is essential"** — DEMOTED to Nice-to-Have. The paper's core claim is that a gradient-free method works and has unique advantages. This is demonstrated on the non-differentiable space-group task where gradient methods cannot be applied. Comparing against gradient-based MCMC would contextualize the cost of forgoing gradients but is not required to validate the gradient-free contribution.

- **"Multi-fidelity section should be substantially developed or toned down"** — PARTIALLY REMOVED. The paper already appropriately calls it a "proof of concept" and a "preliminary evaluation." The framing is honest. The results remain weak for some tasks, which is retained as a minor weakness.

- **"Strengths about the problem being important / timely / interesting"** — REMOVED as generic and superficial.

## Novel Insights

The review process highlights an interesting tension: ESS-Flow's gradient-free nature is both its greatest strength (enabling tasks like the space-group experiment) and a source of limitations (slower exploration than gradient methods might offer, difficulty with concentrated targets). The multi-fidelity results concretely illustrate this — when the target distribution is sharp (band gap, stability), the coarse prior so poorly overlaps with the target that importance re-weighting collapses. This suggests a natural direction: combining gradient-free exploration with occasional gradient-based refinement, or developing adaptive discretization strategies that tighten the ODE solver in high-potential regions. The paper opens up this design space rather than closing it.

## Suggestions

- Move key convergence diagnostics (acceptance rates, effective sample sizes for at least one task, scaling plots from Appendix A.1) into the main text or a dedicated subsection. Even one page of diagnostics would substantially strengthen reader confidence.

- Add a summary table or paragraph in the main text characterizing computational cost: NFE per MCMC iteration, total NFE per sample, and how this compares to baselines. This information already exists in the appendix — surfacing it in the main body would address the most common concern readers will have.

- Expand the protein experiment to more than 10 samples per method, or justify why 10 is sufficient for the claims being made (the qualitative point about realism is clear even with 10, but statistical reporting would benefit from more samples).

- Briefly discuss the uniqueness/novelty trade-off in the main text rather than leaving it for the reader to infer from Table 3.

## Score and Decision

**Round-1 bracket**: The paper clearly sits above weak anchors like EnKG (4.75, rejected for methodological concerns) and Flow Matching for Posterior Inference (4.20, rejected for insufficient empirical validation). It sits below the strongest anchors in the 8.0 range (Variational Diffusion Posterior Sampling, Generator Matching) which have more comprehensive theoretical contributions and broader empirical scope. The initial bracket is **5.0–7.0**.

**Round-2 narrowing**: Compared against TFG-Flow (6.25) and OC-Flow (6.50) — both accepted training-free guidance methods for flow-based models — ESS-Flow has a comparably clean method with strong empirical results on scientific tasks. It is slightly weaker on theoretical novelty (citing rather than proving convergence) and has some evaluation gaps (convergence diagnostics not in main text, preliminary multi-fidelity results). It is clearly stronger than EnKG (4.75). This places ESS-Flow at approximately **6.0**: a solid accept with meaningful but addressable weaknesses.

**Final score**: 6.0

### Anchor comparison summary

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| `46tjvA75h6` (No MCMC Teaching) | 3.00 | R1 | ESS-Flow is substantially stronger |
| `WxLwXyBJLw` (FM One-Step) | 3.25 | R1 | Different topic; ESS-Flow more complete |
| `SEvJfuCtPY` (Phase-aware FM) | 3.00 | R1 | Different topic; ESS-Flow stronger |
| `sK2A7Ve2co` (a-GPS) | 2.50 | R1 | ESS-Flow substantially stronger |
| `DoDNJdDntB` (FM Simulator Feedback) | 4.20 | R1 | ESS-Flow has stronger empirical results |
| `61ss5RA1MM` (OC-Flow) | 6.50 | R1/R2 | OC-Flow more theoretically ambitious; ESS-Flow cleaner but slightly narrower |
| `AC1QLOJK7l` (Training-free inpainting) | 4.00 | R1 | Different focus; ESS-Flow stronger |
| `FKksTayvGo` (DDBM) | 7.00 | R1 | Different contribution type; DDBM stronger |
| `6EUtjXAvmj` (VDPS) | 8.00 | R1 | Stronger theoretical/empirical scope |
| `zMoNrajk2X` (CADS) | 8.00 | R1 | Different focus; broader impact |
| `E78OaH2s3f` (CAS) | 8.00 | R1 | Different focus |
| `RuP17cJtZo` (Generator Matching) | 8.00 | R1 | Substantially stronger contribution |
| `D7PQ54l5Q1` (DPMC) | 4.75 | R2 | ESS-Flow is stronger |
| `vgt2rSf6al` (MindSimulator) | 5.75 | R2 | Different topic; comparable quality |
| `ykt6I21YQZ` (EnKG) | 4.75 | R2 | ESS-Flow has cleaner method, stronger results |
| `3JoLo0mmHH` (Audio fMRI) | 5.25 | R2 | Different topic; ESS-Flow stronger |
| `GK5ni7tIHp` (TFG-Flow) | 6.25 | R2 | Comparable; TFG-Flow slightly stronger theoretically |
| `TVQLu34bdw` (Proteina) | 6.60 | R2 | Different contribution; Proteina broader |
| `9qS3HzSDNv` (Protein Dynamics) | 6.20 | R2 | Different contribution type; similar quality |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>