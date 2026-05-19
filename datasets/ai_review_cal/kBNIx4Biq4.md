- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 5, 8, 5
Now I have all the information I need. Let me synthesize the final consolidated review.

## Summary

The paper introduces Free-form Injective Flows (FIF), which lift the architectural constraints that previously limited injective flows (such as coupling blocks and shared encoder-decoder parameters). The key technical contributions are: (1) replacing the expensive iterative conjugate-gradient estimator for the log-determinant gradient with a single-step surrogate that uses the encoder Jacobian as a proxy for the pseudo-inverse of the decoder Jacobian, yielding a 1.5–6× speedup; (2) identifying a previously unrecognized pathology in joint manifold-likelihood training — diverging decoder curvature — and fixing it by evaluating the encoder Jacobian at the data point rather than its reconstruction. Experiments show FIF outperforms prior injective flows on CelebA by a wide margin (FID 47.3 vs. 55.6/56.2) and achieves competitive results on the Pythae generative autoencoder benchmark.

## Strengths

- **Efficient single-step surrogate for the log-determinant gradient.** The paper derives that $\frac{\partial}{\partial\theta_j}\frac12\log\det(J^\top J) = \operatorname{tr}(J^\dagger\frac{\partial}{\partial\theta_j}J)$ (Eq. 13), and then exploits the property that for a well-trained autoencoder $f'(\hat x) \approx g'(z)^\dagger$ to replace the iterative CG method with a single-pass estimator requiring only two Jacobian-vector products per term (lines 130–144). This reduces per-batch cost from up to $2(d+1)$ products to exactly 2, delivering a measured 1.5×–6.1× speedup on tabular data (Table 1).

- **Identification and correction of the high-curvature pathology in joint manifold-likelihood training.** Section 4.2 clearly distinguishes two failure modes: intersecting manifolds (known) and diverging curvature (newly identified). The paper demonstrates that naive maximum likelihood can drive decoder curvature to infinity, concentrating projected data. The proposed fix — evaluating the encoder Jacobian at $x$ rather than $\hat x$ (Eq. 16) — counteracts this pathology, and the toy experiment in Figure 3 confirms the behavior visually and quantitatively. This is a genuine insight that past work missed.

- **Clear SOTA improvement over prior injective flows on CelebA.** Under equal computational budget, FIF achieves FID 47.3 (Gaussian sampler) and 37.4 (GMM sampler), substantially better than DNF (55.6/52.7) and Trumpet (56.2/47.7) — Table 2. These results directly demonstrate that removing architectural constraints while using the proposed estimator yields practical gains.

- **Competitive performance on the Pythae generative autoencoder benchmark.** FIF achieves the best FID among all compared methods on Cele bA on ResNet+Gaussian (62.3), ConvNet+GMM (47.3), and ResNet+GMM (55.0) — Table 3. This places FIF competitively within a much broader class of bottleneck generative models.

## Weaknesses

### Fatal
None.

### Major
- **The gradient surrogate's bias is not characterized.** The core technical contribution replaces the unbiased (but expensive) CG-based gradient estimator with a single-pass surrogate that uses the encoder Jacobian as a proxy for the pseudo-inverse of the decoder Jacobian. The derivation is exact only when $f'(\hat x) = g'(z)^\dagger$ exactly — i.e., when the autoencoder is perfectly consistent. The paper acknowledges this ("only accurate if $f$ and $g$ are at least approximately optimal") and appeals to observed stable training (line 144). However, the bias of this estimator is never characterized: no diagnostic compares the surrogate gradient to the true gradient (e.g., on a small problem), no analysis quantifies how the bias evolves during training, and no argument establishes that the surrogate optimizes something close to the true likelihood. The strong empirical results mitigate this concern substantially, but the central theoretical question — *what objective is actually being optimized?* — is left open. A small-scale diagnostic study comparing gradient directions or convergence on a low-dimensional problem would significantly strengthen the paper's scientific contribution.

### Minor
- **Limited statistical significance for the HEPMASS comparison.** On HEPMASS, the RF baseline has an enormous standard deviation ($0.779 \pm 0.191$) while FIF achieves $0.541 \pm 0.034$. While the point estimate favors FIF, the large RF variance makes it unclear whether the difference is statistically meaningful. The paper asserts "superior performance on 3 of 4 datasets" (Table 1 caption), but this claim should be qualified for HEPMASS.

- **Tabular performance comparison uses published RF numbers, not a fully controlled rerun.** The speed comparison reruns RF on the same hardware (which is good), but the performance numbers in Table 1 are taken directly from the RF paper. Differences in data preprocessing, evaluation protocol, random seeds, or hyperparameter tuning could confound the comparison. Since the RF code was available (they reran it for timing), the paper could have rerun RF for a fully controlled performance comparison.

### Trivial
None worth listing individually. The paper is generally well-written.

## Nice-to-Haves
- A small-scale diagnostic experiment (e.g., on the 2D sinusoid from Figure 3) comparing the surrogate gradient to the unbiased CG gradient would directly address the central theoretical gap and elevate the paper.
- Reporting the number of CG iterations per step that RF required on each tabular dataset would help contextualize the speedup numbers.
- The full Pythae benchmark table is dense; a summary version in the main text with a full table in the appendix would improve readability.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"The fix for the high-curvature pathology is explained intuitively but its mathematical effect is not fully justified."** The paper explicitly references \cref{app:modified-estimator} for the detailed derivation (line 191). The main text provides the intuition and the equation; the formal treatment exists in the appendix, which is stripped by the parser. Per policy, missing appendix content is not a valid weakness.

2. **"The derivation of Eq. 13 is too terse in the main text."** The full derivation is in \cref{app:gradient-est}. The main text states the key identity and sketches the logic; this is standard practice for papers with appendices.

3. **"Model selection uses test data (best of 10 hyperparameters)."** The paper is fully transparent about this (line 274: "ten hyperparameter configurations are trained and the best model according to FID is reported"). This is the standard Pythae benchmark methodology and is appropriately disclosed. No problem exists.

4. **Section-by-section notes about "computational cost details" and "table density" and similar presentation suggestions.** These are minor formatting/preference notes that do not affect the paper's scientific contribution.

5. **Criticism that the tabular comparison is "incomplete" (suggesting RF should have been rerun for performance).** This criticism is partially valid (hence kept in Minor), but the harsh critic's framing as a severe weakness is overblown — using published numbers is standard practice, and the paper is transparent about the source of the RF results.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation about the paper that the authors themselves do not already articulate.

## Suggestions

1. Add a diagnostic experiment comparing surrogate gradients to unbiased CG gradients on a small problem (e.g., the 2D sinusoid). This would directly address the most significant theoretical gap and substantially strengthen the paper.
2. Qualify the "3 of 4 datasets" claim with a note about the large RF variance on HEPMASS.
3. Either rerun the rectangular flow baseline to get fully controlled performance numbers, or explicitly note the limitation in the main text.
4. Consider moving the full Pythae benchmark table to the appendix and summarizing in the main text for readability.
