Now I'll write the final consolidated review.

## Summary

This paper introduces Count Bridges, a stochastic bridge process on ℤ^d based on Poisson birth-death dynamics, providing closed-form conditionals for efficient training and sampling. The method is extended to deconvolution from aggregated observations via an EM algorithm, and applied to nucleotide-level single-cell expression modeling, bulk RNA-seq deconvolution, and spatial transcriptomic deconvolution. The core theoretical contribution—tractable bridge kernels on the integer lattice with Bessel-based slack posteriors (Proposition 3.1)—is genuinely novel and mathematically grounded.

## Strengths

- **Closed-form birth-death bridge kernels on ℤ^d (Proposition 3.1):** The paper derives exact, tractable conditionals for the integer bridge process using Poisson superposition, binomial thinning, and hypergeometric draws for the slack variables. This is a nontrivial mathematical contribution that generalizes prior discrete diffusion models (Blackout Diffusion's pure-death process, categorical diffusion models) to a proper bridge process capable of transporting between arbitrary integer-valued distributions. The composition property (Eqs. 1–2) is verified for this construction, enabling principled multi-step sampling.

- **Superior scaling on high-dimensional integer transport (Figure 3):** Count Bridges maintain near-zero Wasserstein-1 distance across dimensions 4 to 512 on a low-rank Gaussian mixture task, while continuous flow matching and discrete flow matching degrade significantly, especially at low NFE. This demonstrates robust scaling behavior where prior approaches fail, and the advantage persists across multiple NFE settings.

- **Competitive performance on real biological deconvolution tasks:** Tables 3 and 4 show Count Bridges outperform established deconvolution methods (CIBERSORTx, MuSiC, STDeconvolve) on cell-type proportion prediction (JSD, RMSE, Spearman) for both bulk RNA-seq and spatial transcriptomics. Table 1 shows nucleotide-level expression prediction substantially outperforming a fine-tuned Enformer (MSE 0.601 vs 2.590). These results demonstrate practical utility on large-scale biological problems.

- **Distributional scoring loss with energy score (Section 3.2):** The use of a strictly proper scoring rule (energy score) with the ℓ2 semimetric is well-motivated for the ordinal-count setting and avoids the factorized independence assumption of cross-entropy losses used in categorical diffusion models.

- **Honest limitations section:** The paper explicitly acknowledges the heuristic nature of the projection step, identifiability limits for deconvolution as group sizes grow, and the regime where continuous models may match or exceed CB performance. This transparency is commendable.

## Weaknesses

### Major

- **Deconvolution evaluation lacks direct unit-level validation despite available ground truth.** For the spatial transcriptomics application (Section 6.3), the MERFISH dataset provides single-cell ground truth ("This synthetic dataset gives us access to spot-level aggregates and their corresponding single-cell ground truth," line 351), yet the evaluation never reports per-cell metrics comparing predicted single-cell count vectors to the true ones. Instead, the paper reports (a) cell-type proportions after assigning each predicted profile to its nearest cell type (Table 4), and (b) distributional metrics (MMD, W2, Energy) comparing the full set of predicted profiles against a spot-mean baseline (Table 5). Neither directly validates that the model recovers individual unit-level count profiles. The same issue applies to bulk RNA-seq deconvolution (Section 6.2): held-out patients have ground truth scRNA-seq profiles, but evaluation is limited to aggregated metrics (cell-type proportions, distributional quality against bulk mean, Table 2–3). Since the paper claims "resolving multicellular spatial transcriptomic spots into single-cell count profiles" (abstract) and "deconvolving bulk gene expression into inferred single-cell gene expression profiles" (Section 6.2), the lack of per-cell comparison metrics (e.g., per-spot RMSE, cosine similarity, or proportion-estimation error per spot) is a significant gap in the evidence chain. This does not invalidate the core Count Bridges method but means the deconvolution claims are not as strongly supported as they could be.

### Minor

- **The EM E-step is heuristic with uncharacterized bias.** The projection-guided sampling (Algorithm 3) replaces the intractable exact conditional with a diffusion process that imposes aggregate constraints at each reverse step. The paper acknowledges this ("the projection step we use is a first-order surrogate and lacks serious theoretical support," limitations section), and Proposition 4.1 justifies the simple rescaling for sum aggregates under a large-sample approximation. However, the discrepancy between this validated case (synthetic deconvolution in Figure 4 uses the simple rescaling) and the learned projection used in real applications is not addressed. A synthetic deconvolution benchmark where the true conditional is known (e.g., small G with a tractable prior) would help quantify the approximation's bias. This weakness is partially mitigated by the paper's own transparency, but it means the deconvolution pipeline rests on an approximation whose bias is unquantified.

- **Missing error bars for the Enformer baseline (Table 1).** The Count Bridge results report standard errors over 3 inference seeds, but the fine-tuned Enformer baseline is reported as point values (2.590, 3.142) without any variance estimate. This makes it impossible to assess whether the performance gap is statistically significant relative to run-to-run variation.

- **The energy score's strict propriety for the chosen semimetric is stated but not verified.** The paper states the energy score is "strictly proper when ρ is characteristic" (line 191) and uses ρ(x,x') = ‖x - x'‖₂ (ℓ2 norm). While the ℓ2 norm is indeed a negative-type semimetric generating a characteristic kernel on ℤ^d (so propriety holds), the paper does not provide this justification or a citation establishing characteristicity for ‖·‖₂ on ℤ^d specifically.

### Trivial

- None beyond standard formatting artifacts attributable to the PDF extraction process.

## Nice-to-Haves

- A direct per-cell comparison (e.g., per-spot RMSE or cosine similarity between predicted and ground-truth single-cell count vectors) on the synthetic MERFISH spatial data would substantially strengthen the deconvolution claims.
- An ablation comparing the energy score against a factorized cross-entropy loss would empirically justify the distributional approach's advantage.
- A runtime/memory comparison against CFM/DFM would help practitioners assess the practical cost of the custom CUDA kernel for Bessel sampling.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Add per-cell evaluation metrics (RMSE, cosine similarity) comparing predicted vs. ground-truth single-cell count profiles on the synthetic MERFISH spatial data, where ground truth is available.
- Provide standard errors or confidence intervals for all baseline methods (especially fine-tuned Enformer) to enable proper comparison.
- Include a small-scale synthetic deconvolution experiment where the true conditional distribution is computable (e.g., G=2, known prior) to quantify the bias introduced by projection-guided sampling.

---

## Score and Decision

### Calibration

**Round 1 — Bracketing:** Searched for reviews of discrete diffusion / integer generative models with avg scores in the bands (0–3.5), (3.5–7.5), and (7.5–10). Low-band anchors (3.0–3.2) were papers with fundamental methodological issues. High-band anchors (8.0) were papers with complete theoretical + empirical validation. The initial bracket for this paper was [5.5, 8.0], given its strong theoretical contribution coupled with the validation gap in the deconvolution experiments.

**Round 2 — Narrowing:** Compared against four anchors in the (5, 8) range:
- DDBM (anchor FKksTayvGo, avg 7.0): Accepted bridge paper with comparable theoretical ambition but some prior-work novelty concerns. This paper's theoretical contribution is cleaner, but DDBM's image-to-image experiments are more complete. Similar tier.
- Stem (anchor FtjLUHyZAO, avg 6.67): Accepted application paper with less theoretical novelty. This paper is stronger than Stem on theoretical grounds.
- SEDD (anchor 71mqtQdKB9, avg 6.60): Rejected despite strong theory due to incomplete experiments. This paper has complete synthetic benchmarks and thus stronger empirical support for the core method.
- DDPP (anchor Ombm8S40zN, avg 6.25): Accepted methods paper. This paper's theoretical novelty exceeds DDPP's.

**Final score:** 7.0 — positioned between the strong accepted anchors (7.0) and the accepted-methods anchors (~6.5), justified by the genuinely novel theoretical contribution (Proposition 3.1) and strong synthetic benchmarks, tempered by the incomplete validation of the deconvolution claims. The core Count Bridges method is well-supported; the deconvolution extension is promising but not fully substantiated.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>