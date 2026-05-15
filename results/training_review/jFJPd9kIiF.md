Here is my consolidated review.

---

## Summary

This paper introduces *Least Volume* (LV) regularization, a penalty on the product of latent standard deviations that, when combined with a Lipschitz-bounded decoder, compresses an autoencoder's latent set onto a coordinate-aligned low-dimensional subspace. The paper provides theoretical analysis connecting LV to PCA (showing PCA is a linear special case), proves a safety bound for pruning low-STD dimensions, and demonstrates empirically that LV outperforms L1-based regularizers in reducing latent dimensionality at comparable reconstruction error.

---

## Strengths

- **Theoretical connection to PCA (Proposition 3)** — The paper proves that under a linear autoencoder with perfect reconstruction and a 1-Lipschitz decoder, minimizing the volume recovers the principal components. This is a clean and original formal link between a nonlinear regularizer and PCA.

- **Safety bound for pruning (Theorem 2)** — The theorem shows that pruning a dimension with STD σ<sub>i</sub> increases reconstruction error by at most K·σ<sub>i</sub>, providing a principled guarantee that justifies post-hoc dimension reduction. The necessity of the Lipschitz constraint is clearly motivated by this result.

- **Geometric intuition is well-explained and validated by ablation** — The distinction between isotropic shrinkage (trivial solution) and genuine flattening (volume-minimizing solution) is pedagogically clear. The ablation studies (Figures 3–4) cleanly confirm that both the Lipschitz constraint and the volume penalty are individually necessary.

- **Consistent dimension reduction across benchmarks** — Figure 1 shows that LV achieves the lowest latent dimensionality at comparable L2 reconstruction error on synthetic data, MNIST, and CIFAR-10, outperforming L1-norm and Student's t regularizers.

- **Empirical confirmation of importance ordering** — Figure 2 reports Pearson correlations close to 1 between latent STD and explained reconstruction, showing that LV produces a meaningful ranking of latent dimensions by informativeness, analogous to PCA.

---

## Weaknesses

### Fatal
None.

### Major

1. **CelebA results are promised but absent** — The abstract lists CelebA as a benchmark alongside MNIST and CIFAR-10, but the experimental section (§5.1) only presents results for synthetic data, MNIST, and CIFAR-10. No CelebA results appear anywhere in the paper, and the experiments section does not reference them. This is a broken promise that weakens the empirical scope of the paper.

2. **No experimental comparison against related methods that share the same goal** — The related work and Table 1 discuss IRMAE, nested dropout, PCA-AE, and K-sparse AE as methods that "automatically reduce autoencoder latent dimensions," yet none of these are included in the experiments. The paper's stated contribution (§1, item 3) claims superiority over "the traditional regularizer Lasso," and this claim is supported relative to L1-based baselines. However, by positioning these other methods as closely related alternatives and contrasting them in a detailed table, the paper creates an expectation of empirical comparison that it does not fulfill. The omission limits the paper's ability to demonstrate that LV advances the state of the art beyond L1-based regularizers into the broader landscape of latent-dimension-reduction methods.

### Minor

1. **Evaluation metric for "latent dimensionality" is ad-hoc** — The paper defines latent dimensionality as the number of dimensions retained after pruning the smallest STDs until their joint explained reconstruction exceeds a 1% threshold (line 258). This 1% threshold is arbitrary, and the metric is not validated against standard dimensionality measures (e.g., rank of the covariance matrix, PCA eigenvalue elbow, or intrinsic dimensionality estimators). Since the metric directly depends on near-zero STDs — exactly what the volume penalty produces — there is a risk of evaluation bias favoring the proposed method. A sensitivity analysis on the threshold or a comparison with alternative measures would strengthen the results.

2. **Computation of σ during training is underspecified** — The volume penalty operates on the standard deviation vector σ of latent codes, but the paper never states how σ is estimated during optimization: is it computed over the full training set, or per minibatch? If minibatch, what batch size is used? Is the mean re-estimated per batch or from a running average? This is a reproducibility concern, as different estimation strategies can affect training dynamics, especially for the product-based penalty (which is sensitive to values near zero).

3. **Claim of "always achieves the highest compression" is slightly overstated** — Figure 1 shows that LV performs best overall, but error bars from three cross-validation runs overlap with L1-based baselines at several operating points (e.g., MNIST). The paper should acknowledge this overlap rather than claiming uniform superiority.

4. **Only η=1 is tested** — The paper introduces η as a parameter that interpolates between the volume penalty and L1 (line 97–112) and fixes η=1 throughout. No ablation or sensitivity analysis is provided for different η values, so the reader cannot assess how robust the advantage is to this choice.

### Trivial
None.

---

## Nice-to-Haves

- A sensitivity study varying the η parameter in the volume penalty to demonstrate robustness.
- Downstream task evaluation (e.g., training a classifier on pruned latents, or generating samples from the reduced latent space) to demonstrate practical utility of the compressed representation.
- Visualization of learned latent structure (e.g., scatter plots of 2D projections or heatmaps of STD across dimensions).
- A systematic comparison of the 1% pruning threshold against alternative criteria (e.g., explained variance elbow, cross-validated reconstruction error).

---

## Removed Points

These points from the reviewers were checked against the paper and removed as unreliable:

- **Harsh critic's claim that the STD-explained-reconstruction correlation is a "near-tautological consequence" of Theorem 2.** The safety theorem provides an *upper bound* on reconstruction error increase after pruning (K·√∑σ²), not a guarantee of proportionality. The empirical finding that Pearson correlation is close to 1 is not a logical consequence of this bound; it is a genuine empirical discovery about the tightness of the bound in practice. This criticism misreads the theorem.

- **Criticism that the invariance-of-domain framing "sets expectations the paper does not meet."** The paper uses this topological motivation to explain *why* low-dimensional latent spaces are desirable (better robustness for generative models). It does not promise experimental validation of this property. This is scope creep.

- **Nitpick that Proposition 3 (PCA relation) requires "strict minimization" which is "never achieved."** Standard for theoretical propositions; all theoretical statements are understood as idealized conditions. Not a meaningful weakness.

- **Strength Finder's generic strengths that lack specific content** (e.g., "this paper addressed an important problem") — dropped because they are superficial.

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any genuinely novel observation that the paper itself does not already make.

---

## Suggestions

1. **Either add CelebA results or remove it from the abstract.** This is the most pressing fix, as the current discrepancy between the abstract and the experimental content is a straightforward omission.

2. **Specify how σ is estimated during training** (full-batch vs. minibatch statistics, batch size, mean re-centering). This is essential for reproducibility.

3. **Add at least one comparison against a related method** from the set discussed in Table 1 (IRMAE is the most natural candidate, as it shares the same implicit goal of subspace compression). Even a single additional baseline would substantially strengthen the empirical evaluation.

4. **Acknowledge the limitations of the 1% pruning threshold** and consider adding a sensitivity analysis or comparing against alternative dimensionality measures.

5. **Tone down the claim of "always achieves the highest compression"** to reflect the error bar overlap at some operating points.

---

## Score and Decision

This paper presents a clean geometric idea with solid theoretical grounding (PCA connection, safety bound). The core intuition is well-motivated, and the ablation studies cleanly validate the design. However, the empirical evaluation is incomplete in two notable ways: CelebA results are promised but absent, and the experimental baselines do not include several related methods that the paper itself discusses as comparable. The underspecified computation of σ during training is a reproducibility concern. The theoretical contributions are genuine and carry the paper, but the empirical gaps prevent a strong acceptance.

**Overall Assessment:** The paper makes a worthwhile contribution. The theoretical results (PCA connection, safety bound) are original and well-executed. The empirical results are positive relative to the included baselines but need strengthening before the paper can be considered a complete evaluation. Given the significance of the theoretical contribution, a weak accept is justified, contingent on at least addressing the CelebA omission and the σ estimation detail.

**Originality:** Good — the geometric perspective on latent-space compression via volume minimization is novel.
**Importance of question:** High — automatic latent dimensionality reduction is a practically relevant problem.
**Claims support:** Moderate — the main claim about Lasso is supported, but the broader claims are weakened by missing baselines and a missing benchmark.
**Soundness of experiments:** Moderate — reasonable methodology but incomplete scope and under-specified implementation details.
**Clarity:** Good — the geometric intuition and theoretical analysis are clearly presented.
**Value to community:** Moderate — the theoretical connections are valuable, and the method is simple enough to be practically useful, but a stronger evaluation is needed.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>