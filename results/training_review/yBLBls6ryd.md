Now I have all the information I need. Let me construct the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal
None

### Major
- weakness 1 — why it matters
- weakness 2 — why it matters

### Minor
...

### Trivial
...

## Nice-to-Haves
...

## Removed Points
...

## Novel Insights
...

## Suggestions
...

## Score and Decision

Let me finalize and output the complete review.

---

Here is my final consolidated review:

## Summary

This paper proposes a Riemannian optimization framework for maintaining a spectral factorization **S = B diag(d) B^T** of a curvature (preconditioner) matrix on the fly during neural network training. By keeping the eigen-pair **(B, d)** directly learnable, the method enables cheap application of arbitrary fractional powers **S^{-1/p}** through elementwise operations on **d** — avoiding costly matrix decompositions at each step. The approach is extended to Kronecker-structured factorizations for scalability, and local coordinate transforms are derived to diagonalize the Fisher-Rao metric so that the Riemannian update has a simple closed form. The paper validates the method on a positive-definite matrix optimization problem (d=60) and on low-precision training of three vision transformers (ViT, FocalNet, FlattenViT) on ImageWoof.

## Strengths

- **Novel spectral parametrization enables cheap arbitrary fractional powers without repeated decompositions.** The core idea — maintaining **S = B diag(d) B^T** as a learnable object and computing **S^{-1/p}** via elementwise **d^{-1/p}** — is original and directly addresses a real computational bottleneck. This is an improvement over Shampoo, which requires a full eigendecomposition at each update to change the fractional power (Sections 2, 2.4).

- **Riemannian framework with local coordinates that diagonalize the Fisher-Rao metric is theoretically elegant and non-trivial.** Claims 4 and 5 show that by constructing appropriate local coordinates (using exponential and Cayley maps with lower-triangular restrictions for uniqueness), the Fisher-Rao metric becomes diagonal (full-matrix case) or block-diagonal (Kronecker case) at the evaluation point. This permits analytical metric inversion without matrix decompositions, extending prior local-coordinate approaches (Glasmachers et al.; Lin et al.) to handle the new constraints of the spectral decomposition (Section 3).

- **Explicit resolution of spectral and Kronecker parametrization redundancies is a principled contribution.** The paper carefully handles (a) permutation ambiguity of eigenvectors via a lower-triangular restriction on the local coordinate M (Claim 3), (b) singularity from repeated/close eigenvalues via Moore–Penrose inversion, and (c) scaling ambiguity in the Kronecker factorization via determinant constraints and a learnable scalar α. These design choices are necessary for a learnable, unique, and well-behaved factorization (Sections 3.1, 3.2).

- **Synthetic curvature-estimation experiments convincingly demonstrate that the spectral update scheme closely tracks the standard preconditioner update.** The fixed-point matching and iterate-matching experiments (Figures 2, 3) use i.i.d. Gaussian gradient sequences with known ground-truth covariance, showing that the spectral parametrization recovers the same curvature estimates as the default scheme and a Cholesky-based alternative. This provides reasonable evidence that the update rule behaves as intended (Sections 2.1, 2.2).

## Weaknesses

### Fatal
None.

### Major

1. **NN experiments are substantially undersupported for the strength of the claims made.**  
   The paper claims efficiency, numerical stability, and practical superiority over strong baselines, yet:  
   - The NN experiments use only **ImageWoof** (a 10-class subset of ImageNet), which is not a standard benchmark for optimizer evaluation.  
   - Only **three vision transformers** are tested; no experiments on language models or at larger scale (e.g., ImageNet-1k) are provided.  
   - **No wall-clock runtime measurements are reported.** The claim that the method "matches AdamW's running time" is supported only by adjusting the preconditioner update frequency (10 iterations for the proposed method vs. 100 for Shampoo) without any actual timing data.  
   - **No error bars, standard deviations, or statistical significance tests** are shown for the NN learning curves. It is unclear whether the reported improvements are reproducible or within the noise of a single run.  
   - **No final accuracy numbers are reported** — only learning curves are shown. Together with the unspecified selection criterion from the 200 random-search runs (best? median?), this makes the results difficult to evaluate.  

   These omissions collectively mean the paper's core claims about practical performance are not empirically verified at the level expected for an optimization paper targeting real-world use.

2. **No comparison to K-FAC, the most natural Kronecker-structured competitor.**  
   The paper compares only to AdamW and Shampoo (with grafting) for the NN experiments. K-FAC (Martens & Grosse, 2015) is the most directly related Kronecker-based method that also uses structured curvature and is mentioned in the introduction. Its absence from the experiments is a significant gap. Without this comparison, the claimed advantages of the spectral Kronecker framework over existing structured preconditioners remain unsubstantiated.

3. **The efficiency argument is asserted without quantitative support.**  
   The paper argues the method is computationally cheaper than Shampoo because it avoids matrix decompositions. However:  
   - **No FLOP analysis or per-iteration cost comparison** is provided. The Cayley map with Neumann series approximation involves multiple matrix multiplications whose cost could be comparable to or exceed an eigendecomposition of the small Kronecker factors.  
   - The statement that the method updates every 10 iterations vs. Shampoo's 100 does not account for the per-update cost difference. A 10× more frequent update could erase any per-update savings.  
   - **No ablation of the Neumann series truncation order** (number of terms) is performed, so the trade-off between approximation accuracy and computational cost is unexamined.

### Minor

4. **The half-precision stability claim is not validated with any numerical diagnostics.**  
   The paper states the method is "stable in half precision" (abstract, Section 2.4) and presents training curves in FP16, but provides no quantitative diagnostics such as gradient/update condition numbers, occurrences of NaN/Inf, or comparison of gradient norms between FP16 and FP32 training. This weakens the evidence for a central selling point.

5. **The positive-definite matrix optimization experiment (d=60) is too small to be informative.**  
   This experiment demonstrates that the full-matrix spectral scheme matches standard RGD by design (as the paper acknowledges). A problem dimension of 60 with a known ground-truth inverse matrix is a minimal sanity check, not a demonstration of scalability or practical advantage.

6. **The relationship between the update frequency (every 10 iterations) and the truncated Cayley approximation is not analyzed.**  
   The paper uses a truncated Cayley map to reduce cost but never studies how the truncation affects convergence, numerical stability, or the quality of the orthogonal update. This is important because the approximation quality depends on **‖βN‖ < 1**, and the paper provides no evidence that this condition holds during training.

### Trivial

7. The abstract states the method "does not require matrix decompositions," which could be misinterpreted — the method uses a truncated Neumann series to avoid exact matrix inversion in the Cayley map, but still involves approximate matrix inversions. A more precise phrasing would avoid potential confusion.

## Nice-to-Haves
- Wall-clock runtime comparison against AdamW, Shampoo, and K-FAC at matched update frequencies on ImageNet-1k or a similarly standard benchmark.
- Ablation of the Neumann series truncation order and its effect on training loss, accuracy, and numerical stability.
- Numerical diagnostics for half-precision stability (e.g., condition number evolution, gradient norm ratios across precisions).
- Study of the learned scalar α: does it converge to a meaningful value, and how does it interact with the fractional power p?
- Evolution of eigenvalues d over training to show the spectral factorization remains well-behaved.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **Criticism about Claim 1 not being theoretically established (from Harsh Critic point 2).** The paper references the appendix for the proof; the appendix was stripped by the parser. Per policy, weaknesses about missing appendix content in the parsed text are not valid criticisms.
- **Complaint that Shampoo comparison uses grafting, making it "unfair."** The asymmetry favors the baseline (grafting improves Shampoo, making it harder for the proposed method to beat it). This is intentionally asymmetric and not a valid weakness.
- **Criticism about "no new insight into optimal fraction"** — this is outside the paper's stated scope. The paper proposes a framework for applying arbitrary fractions, not a theory of which fraction is optimal.
- **Complaint that update schemes are "dense and hard to parse"** — this is a presentation nitpick and not a substantive weakness.
- **Generic complaint that experiments should be on larger models** — the paper acknowledges this as future work in the conclusion.
- **Strength Finder's claim about "matching AdamW's running time"** (from Supporting strength 2) — since no actual timing data is provided, this strength conflicts with the verified weakness about missing runtime measurements. Moved here per policy.

## Novel Insights

Beyond the paper's own contributions, the reviews raise an interesting tension: the local-coordinate approach that makes the Riemannian metric diagonal also inherently requires the assumption that **d** entries are distinct (or uses Moore–Penrose inversion when they are close). This creates a potential brittleness when eigenvalues coalesce during training — a scenario that may be common in deep networks with redundant features. The paper acknowledges this but provides no empirical exploration of how frequently eigenvalues become close during real training, or how sensitive the method is to the threshold for "closeness" in the Moore–Penrose treatment. This is a genuinely open question that future work on spectral factorization methods would need to address.

## Suggestions

1. **Run the NN experiments on a standard benchmark** (e.g., ImageNet-1k with ViT-B/16) and report wall-clock times alongside training curves. Include error bars from at least 3 random seeds.
2. **Add K-FAC as a baseline.** Since the paper's contribution is a Kronecker-structured spectral method, comparing to the leading Kronecker-based optimizer is essential.
3. **Provide a per-iteration FLOP analysis** comparing the proposed method (with truncated Cayley) to Shampoo and K-FAC, and report actual runtime per iteration (not just update frequency).
4. **Include a brief ablation** showing how the Neumann series truncation order affects convergence and numerical stability on a small model.
5. **Report numerical diagnostics** for half-precision training: condition numbers of S, fraction of NaN/Inf steps, and gradient norm comparisons across FP16 and FP32.
6. **Clarify the selection criteria** from the 200 random-search runs (what is plotted, and why).

## Score and Decision

The paper presents a novel and theoretically grounded approach to maintaining spectral factorizations on the fly for fractional natural gradient descent. The core idea is original, the handling of parametrization constraints is principled, and the synthetic curvature-estimation experiments provide reasonable validation of the update scheme's behavior. However, the NN experiments are substantially under-supported: they use a small non-standard dataset, lack wall-clock timing, error bars, final accuracy numbers, and comparison to a key competitor (K-FAC). The efficiency claims are asserted without FLOP analysis or runtime measurements, and the half-precision stability claim lacks numerical diagnostics. While the theoretical contribution is real, the experimental validation is not yet sufficient to support the practical claims made in the paper.

I recommend **rejection** of the current version. The paper could become acceptable after major revisions that substantially strengthen the empirical evaluation — particularly by adding wall-clock comparisons, larger-scale experiments, K-FAC baselines, and ablation studies.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>