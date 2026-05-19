- Decision: Accept
- Avg Score: 6.00
- Scores: 8, 5, 5
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper presents ACRE and OHARE, two algorithms that certify robustness of OLS linear regression to sample removal by providing valid lower bounds (certificates) on the number of samples that must be removed to change a regression coefficient by a given amount. ACRE handles continuous features; OHARE extends this to one-hot encoded categorical features via a reaveraging transformation and dynamic programming. The algorithms run in polynomial time, provide unconditionally valid bounds, and are shown to be nearly tight under distributional assumptions. Experiments on 14 regressions from three landmark econometrics studies produce the first non-trivial lower bounds for datasets with dimension ≥4.

## Strengths

1. **First non-trivial lower bounds for high-dimensional econometrics datasets**: The paper provides the first certificates for datasets with dimension ≥4 (e.g., Nightlights: d=209, n=3895). Table 1 shows OHARE certifying at least 29 removals needed where prior work only gave heuristic upper bounds (110–136). This directly delivers on the paper's main claim.

2. **Theoretical near-tightness guarantees**: Theorem 1 (ACRE) proves bounds are tight up to 1+o(1) for k up to \(\tilde{\Theta}(\min\{n/\sqrt{d}, n^2/d^2\})\), and Theorem 2 (OHARE) proves bounds are tight up to \(1+O(1/\sqrt{\log n})\) for one-hot-encoded data meeting bucket size conditions. These show the bounds are provably close to optimal under stated conditions.

3. **OHARE's handling of categorical feature singularities**: The reaveraging transformation and dynamic programming (Section 4) overcome the singularities that arise when removing entire categories — a setting where prior continuous methods (including ACRE) fail. Claim 1 proves equivalence to a regression without singularities, and the dynamic programming correctly enforces the per-bucket budget constraints.

4. **Efficient polynomial runtime**: ACRE runs in \(O(n^2 d + n^2 \log n)\) and OHARE in \(O(n^2 (d+m) + n^2 m \log n)\), with no exponential dependence on k, d, or n. Runtimes reported in Table 1 (e.g., 25 seconds for Nightlights) demonstrate practical scalability.

5. **Diagnostic greedy lower-bound algorithm (Algorithm 4)**: This tool identifies problematic features (e.g., heavy-tailed land ownership in the Cash Transfer study), leading to a log transformation that dramatically improved the bounds. This demonstrates practical utility beyond the core algorithms.

6. **Technical contributions in matrix concentration**: The Approximate Matrix Bernstein lemma (Lemma 2) extends standard matrix Bernstein to handle heavy-tailed data with polynomially small failure probabilities and may be of independent interest.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Comparison to heuristic (not provably optimal) upper bounds**: The paper states that lower bounds "match known upper bounds up to a factor of 2 or 3" (line 146). However, the "known upper bounds" come from AMIP and KZC, which the paper itself describes as algorithms that "can only find candidate small subsets to remove (but cannot certify their non-existence)" (line 7). The true minimal number of removals could be smaller than these heuristic upper bounds suggest, so the factor-2/3 gap is between OHARE's lower bound and an upper bound that may itself be loose. The paper should explicitly caveat this when reporting the factor, rather than only stating it in the abstract's description of prior work.

2. **Theory-experiment gap**: The tightness theorems (Theorems 1.3 and 1.4) require i.i.d. features from a well-behaved distribution and Gaussian noise, but the real datasets contain one-hot encodings with very small buckets (e.g., 8 samples for Montenegro in the Nightlights dataset, line 987: "contains only 8 samples from Monetenegro"), features that are not i.i.d. (time trends, fixed effects), and non-Gaussian labels (log GDP). The paper acknowledges this separation (lines 252–253: "Even though they are mild, the assumptions for ACRE are not satisfied by the real-world datasets used in our experiments") and notes that validity is unconditional while tightness is under assumptions. Nevertheless, the narrative in the abstract and introduction emphasizes the theoretical results, while the experiments use data that violate those assumptions. The paper would be stronger if it discussed why the algorithms might still perform well on real data despite violated assumptions, or provided empirical diagnostics of how close the real datasets are to the ACRE-friendly conditions (Definition 4).

3. **Practical significance of certificates could be better contextualized**: OHARE certifies 29 removals needed to flip the sign in Nightlights (n=3895, ~0.74% of the data). The paper frames this as a "non-trivial certificate," which is accurate — no prior work could provide any valid lower bound. However, 29 out of 3895 is still a very small fraction, and the paper does not discuss how to interpret this number. A reader unfamiliar with the literature might assume a "certificate of 29" is large, when in fact it only shows the result is not extremely fragile (more than a few dozen points needed) but is still quite fragile (less than 1% of data can overturn it). A brief interpretive discussion would help readers calibrate.

### Trivial

None.

## Nice-to-Haves

- **Small-scale brute-force validation**: On very small datasets (n<50, d<5) where brute force is tractable, directly computing the true minimal removal count and comparing to OHARE's certificate would strengthen the claim that the bounds are close to the truth (rather than just close to heuristic upper bounds).
- **Synthetic experiments with known ground truth**: Designing datasets with known minimal removal sets and showing OHARE's lower bound is close to that value would complement the theoretical tightness results.
- **Comparison with spectral method on real data**: The synthetic comparison (Figure 1b) shows ACRE outperforms the spectral method of Freund and Hopkins. A small-dimension real dataset where the spectral method can run would further demonstrate practical advantage over the only prior lower-bound method.
- **Memory optimization note**: The paper honestly reports the memory bottleneck (three n×n matrices). A brief discussion of potential approximations or streaming alternatives would be helpful for practitioners.

## Removed Points

These points are flagged to be removed; treat them with caution.
- **Criticism that ACRE "cannot certify robustness beyond dimension 4" is a misreading**: The paper actually says prior work "cannot certify robustness beyond dimension 4" (line 82), not that ACRE cannot. The critic correctly notes this is accurate.
- **Complaint about the KU Triangle Inequality being dense**: The critic notes the algorithm description is "quite dense and its correctness is not immediately obvious from the pseudocode." This is a presentation preference rather than a substantive weakness. The algorithm is accompanied by textual explanation and the technical content is present.
- **Suggestion to add more baselines**: The critic suggests comparing against the spectral method on real data. This is a nice-to-have but not a weakness — the paper already compares against AMIP and KZC (the two prior upper-bound methods used in the econometrics auditing literature) and provides a synthetic comparison against the spectral method.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. When reporting the factor-2/3 gap between lower and heuristic upper bounds, explicitly note that AMIP/KZC are heuristic algorithms that do not provably find the optimal minimal subset, so the true gap may be smaller (i.e., the lower bound may be better than the factor suggests).
2. Include a short paragraph interpreting the practical meaning of the certificate sizes: e.g., "A certificate of 29 out of 3895 shows the result is robust to removing any 0.74% of the data — this is the first valid certificate for this dataset, but it also confirms that the result is overturned by a relatively small fraction of samples."
3. Add an empirical diagnostic table showing how close each real dataset is to the ACRE-friendly conditions (e.g., maximum eigenvector component, maximum off-diagonal inner product, maximum residual). This would bridge the theory-experiment gap.
4. Clarify the normalization of dummy variables in OHARE (the weights w and their interaction with the reaveraging formulas) for readers unfamiliar with the setup.
