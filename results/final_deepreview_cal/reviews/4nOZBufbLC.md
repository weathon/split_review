## Summary

This paper introduces Count Bridges, a stochastic bridge process on ℤᵈ that uses Poisson birth-death dynamics to provide closed-form conditionals for exact count-data generation and sampling. The core mathematical contribution — Proposition 3.1 — gives tractable bridge kernels decomposable into Binomial, Hypergeometric, and Bessel draws, enabling a distributional training objective via energy scores. The paper then extends Count Bridges to deconvolution from aggregate observations via an EM-style algorithm with a projection-guided sampler, and demonstrates the framework on synthetic benchmarks, nucleotide-resolution single-cell RNA-seq modeling with bulk deconvolution, and reference-free spatial transcriptomic deconvolution.

## Strengths

- **Novel, closed-form integer bridge kernels (Proposition 3.1).** The decomposition into Binomial, Hypergeometric, and Bessel-distributed slack variables (Equations 8–9) provides exact, tractable conditionals for count data. This fills a genuine gap: prior discrete diffusion models treat counts as unordered categories, while Count Bridges respect the ordinal/lattice structure. The composition property is verified experimentally in Figure 1 (right column), where one-step and two-step bridges produce indistinguishable ECDFs.

- **Strong high-dimensional scaling.** Figure 3 demonstrates that Count Bridges maintain near-zero Wasserstein-1 error as ambient dimension increases from 4 to 512 (128 NFE), while continuous flow matching and discrete flow matching baselines degrade severely. This is a practically important result showing the method's advantage for high-dimensional count data.

- **Optimal transport interpretation.** The derivation connecting Count Bridges to entropy-regularized Schrödinger bridges with cost |x₁ − x₀|, and the recovery of discrete OT in the low-intensity limit (κ → 0), provides a principled theoretical grounding absent from prior discrete diffusion models.

- **Substantive biological applications with competitive results.** Count Bridges outperform a fine-tuned Enformer on nucleotide-level MSE for both bulk and cell-type-specific predictions (Table 1), achieve better cell-type proportion deconvolution than CIBERSORTx and MuSiC (Table 3), and outperform STDeconvolve on spatial transcriptomic deconvolution (Table 4). The learned projection module (Sec. 6.2) partially mitigates the heuristic nature of the basic projection.

## Weaknesses

### Fatal

None.

### Major

- **The projection step in deconvolution is a heuristic with limited theoretical support, and the authors acknowledge this.** Proposition 4.1 provides only a first-order exponential tilt approximation to the true aggregate-conditional distribution; the authors state it "gives a kind of first-order approximation" and explicitly note in the limitations (Sec. 7) that the projection "lacks serious theoretical support." The entire M-step of Algorithm 4 depends on this projection (or on a learned variant that requires unit-level training data, blurring the boundary between supervised and unsupervised deconvolution). While the empirical results (Figures 4, Tables 2–5) demonstrate practical utility, the theoretical fragility of the projection means the deconvolution component is more empirical than principled. The core bridge contribution (Sec. 3) is unaffected.

### Minor

- **Synthetic baseline comparisons may not account for output discretization.** The paper describes the 8-Gaussians task as "scaled and rounded" (data are integers), and CB naturally outputs integers. However, the main text does not specify whether CFM outputs (which are continuous) were rounded to the nearest integer before computing W₂, MMD, and Energy metrics. If rounding was not applied, CFM is penalized for producing non-integer values even when its distribution is correct in a continuous sense. The appendix (D.1–D.2) may resolve this, but the main text is ambiguous. This does not affect the scaling experiment (Figure 3 uses W₁, which is more tolerant of small deviations), but could affect claims of superiority on the 8-Gaussians task.

- **Biological deconvolution evaluation uses distributional rather than per-cell metrics.** For bulk RNA-seq deconvolution, Table 2 reports MMD, W₂, and Energy comparing the set of deconvolved profiles to the true single-cell distribution. These metrics can be satisfied by a model that generates plausible but incorrectly matched profiles. Similarly, the cell-type proportion metrics (Table 3) confirm proportion recovery but not that individual cells receive correct expression values. The paper does not report per-cell correspondence metrics (e.g., per-cell gene-expression correlation against ground truth after optimal matching), which would more directly validate the claim of recovering single-cell count profiles.

### Trivial

- The paper does not discuss computational cost (runtime, memory) relative to baselines, which would be informative for practitioners applying the method to large-scale biological data.

## Nice-to-Haves

- An ablation over bridge hyperparameters (birth/death intensity λ± or κ, jump-intensity schedule w(t)) in a synthetic setting would provide practical guidance.
- A controlled synthetic experiment that explicitly measures the error introduced by the projection step (separate from identifiability limits of deconvolution) would help characterize the approximation quality.
- Per-cell evaluation metrics (e.g., per-gene correlation between true and predicted expression, after optimal assignment) for the biological deconvolution tasks where ground truth exists would strengthen the validation.

## Removed Points

These points were raised in the input reviews but are excluded from the final review:

- **"Missing appendix proofs / Appendix sections are stripped."** The parser removes appendices from all papers; the original submission includes them. The main text explicitly references Appendices A, B, D, E, and F for derivations, regularity conditions, and experimental details. This is not a weakness of the paper.

- **"Unfair comparison because CFM/DFM may not be rounded" characterized as a fatal flaw.** The harsh critic framed the rounding concern as potentially invalidating the synthetic benchmark claims. However, without the appendix (which is stripped), this remains speculative — the paper may well describe rounding in App. D.1–D.2. Per the rules, speculative-fatal claims dependent on information not verifiable from the paper as provided are demoted.

- **"The projection step makes it unclear whether EM converges to anything meaningful" characterized as fatal.** The paper is transparent about this limitation (Sec. 7), the empirical results demonstrate practical utility, and the core bridge contribution (Sec. 3) stands independently. This is a real limitation but not fatal to the paper's contribution.

- **"The biological deconvolution evaluation fails to validate cell-level recovery" characterized as a structural weakness.** The metrics reported (cell-type proportions, distributional comparisons) are standard in the deconvolution literature (Li et al., 2023). Per-cell recovery is inherently limited by identifiability, which the paper discusses in Apps. B.2–B.3 and acknowledges in limitations. The evaluation is reasonable for what the paper demonstrates, though per-cell metrics would strengthen it.

- **Strength Finder claim that the deconvolution EM is "principled."** The EM formulation is mathematically well-structured, but the projection step is acknowledged as heuristic. The strength is retained but qualified.

- **Strength Finder generic claims about the importance of the problem.** These are not specific to this paper and are removed as superficial.

## Novel Insights

The paper's observation that Poisson birth-death processes can serve as the stochastic foundation for integer-valued diffusion bridges — yielding closed-form conditionals through a decomposition into Binomial, Hypergeometric, and Bessel draws — is genuinely novel and opens the door to principled discrete generative modeling that respects ordinal structure. The connection between the slack variable M_t (the minimum of births and deaths) and entropy-regularized optimal transport, with the recovery of discrete OT as κ → 0, provides a clean theoretical bridge between count processes and optimal transport theory that had not been previously articulated.

## Suggestions

- **Sharpen or scope the deconvolution claims.** Either provide a partial theoretical analysis of the projection (e.g., asymptotic consistency, a variational bound) or explicitly scope the deconvolution contribution as empirical/preliminary. A controlled synthetic experiment measuring projection error separately from identifiability limits would help.
- **Clarify the synthetic comparison protocol.** In the main text, explicitly state whether CFM outputs were rounded to integers before metric computation, or report metrics that are robust to small continuous deviations (e.g., a smooth approximation of Wasserstein distance). This would preempt questions about fairness.
- **Add per-cell evaluation.** For the bulk RNA-seq held-out individuals where ground truth exists, report per-cell gene-expression correlation (after optimal assignment or per-type matching) to directly validate that deconvolved profiles capture individual expression patterns, not just aggregate statistics.

## Score and Decision

**Score calibration:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| No MCMC Teaching For Me (46tjvA75h6) | 3.00 | 1 | Weaker — rejected EBM+diffusion paper |
| Discrete Copula Diffusion (FXw0okNcOb) | 5.25 | 1 | Weaker — incremental discrete diffusion with many approximations |
| STFlow (sYrdb3mhM4) | 5.33 | 2 | Weaker — flow matching for spatial transcriptomics, limited novelty |
| Think while You Generate (MJNywBdSDy) | 5.75 | 1 | Slightly weaker — planner-denoiser for discrete diffusion |
| Diffusion Bridge Implicit Models (eghAocvqBk) | 6.20 | 2 | Slightly weaker — DDIM for DDBM, more incremental |
| Steering Masked Discrete Diffusion (Ombm8S40zN) | 6.25 | 1 | Comparable — novelty roughly similar, cleaner evaluation |
| Denoising Diffusion Bridge Models (FKksTayvGo) | 7.00 | 2 | Slightly stronger — cleaner evaluation, similar novelty in continuous space |
| Convergence of Score-Based Discrete Diffusion (pq1WUegkza) | 7.00 | 1 | Stronger — rigorous theory paper |

**Round-1 bracket:** 5.25–7.00. The paper sits clearly above the 5.25–5.75 cluster (more novel core contribution, broader applications) and slightly below the 7.00 papers (DDBM has cleaner evaluation; the theoretical discrete diffusion paper has more rigorous analysis).

**Round-2 narrowing:** Compared to DBIM (6.20), Count Bridges has a more novel core contribution (closed-form integer bridge vs. DDIM-for-DDBM) but weaker evaluation on deconvolution. Compared to DDBM (7.00), Count Bridges has a similarly novel bridge formulation but in a less-explored space (integers) with more ambitious applications; however, DDBM's evaluation is cleaner and its limitations are less structural. Count Bridges lands between these: above DBIM, below DDBM. **Score: 6.5.**

The paper makes a strong, novel technical contribution (the Count Bridge process) with genuine practical value for count-data modeling. The deconvolution extension, while empirically effective, rests on a heuristic projection that the authors themselves acknowledge as lacking theoretical support. The biological applications are substantive but the evaluation, while competitive with baselines, does not fully validate per-cell recovery. On balance, the paper's strengths — particularly the elegant closed-form bridge construction and its high-dimensional scaling advantages — justify acceptance.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>