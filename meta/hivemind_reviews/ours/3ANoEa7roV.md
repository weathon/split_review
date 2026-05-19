## Summary
This paper proposes a systematic evaluation framework for tabular data synthesis, introducing new metrics for fidelity (Wasserstein distance on marginals), privacy (Membership Disclosure Score — a worst-case metric measuring how much the presence of a record changes nearest-neighbor distances in synthetic data), and utility (Machine Learning Affinity and Query Error), along with a unified tuning objective and an open-source implementation (SynMeter). The paper evaluates 8 synthesizers (HP and DP) on 12 real-world datasets, yielding findings such as diffusion models achieving top fidelity/utility but high privacy risk, and statistical methods remaining competitive under differential privacy.

## Strengths
- **Wasserstein-based fidelity metric (Section 3.2, Eq. 3):** Provides a unified criterion for numerical and categorical marginals at arbitrary order, generalizing disparate metrics like TVD, KST, and correlation statistics. The cost matrix design with L1 distance for numerical attributes and strict match (infinite cost) for categorical attributes is principled and well-motivated.

- **Membership Disclosure Score (MDS) (Section 4.2, Definition 4, Eq. 5):** Addresses two concrete drawbacks of DCR — (1) DCR's averaging over records ignores worst-case individuals, while MDS takes a max over records; (2) DCR overestimates risk when data are naturally clustered (closeness can occur without a specific record), while MDS measures the *change* in closeness caused by including the record. The metric aligns conceptually with differential privacy's notion of neighboring datasets.

- **Machine Learning Affinity (MLA) (Section 5.2, Definition 5):** Mitigates the single-evaluator problem by measuring relative performance discrepancy across a diverse set of 8 ML models, providing a more robust utility signal than any single classifier's accuracy.

- **Concrete, well-documented critiques of existing metrics (Sections 3.1, 4.1, 5.1):** The paper identifies specific limitations rather than gesturing at general concerns — e.g., scale invariance of correlation statistics (Section 3.1), DCR's clustering overestimation problem with a concrete Gaussian mixture example (Section 4.1), and the fact that single-model ML efficacy gives divergent conclusions depending on which model is chosen (Section 5.1).

- **Comprehensive scope of comparison:** The framework covers 8 synthesizers including recent methods (TabDDPM, GReaT) that prior benchmarks omitted, evaluated across 12 real-world datasets, making this one of the more extensive head-to-head comparisons in the literature.

## Weaknesses
### Fatal
None.

### Major
None.

### Minor

- **"Empirical upper bound" claim is undefined (Section 1, line 74):** The paper states TabDDPM "nearly reaches the empirical upper bound in terms of both fidelity and utility" but never defines what this upper bound is. If it means the performance achievable by training on real data and testing on the same test set, that should be stated explicitly. The current phrasing is ambiguous and could mislead a reader about the significance of the result.

- **MDS approximation quality not validated (Section 4.3):** The definition (Eq. 4) requires an expectation over pairs of subsets that differ *only* in record x. The implementation (line 268) trains m models on independent random subsets and pairs them up. Because the subsets are independent rather than paired (differing only in x), the estimator introduces uncontrolled variance from differing compositions of other records. The paper claims m=80 is "sufficient" but provides no sensitivity analysis or ablation to justify this choice. While the approximation approach is reasonable and standard for computationally expensive leave-one-out estimation, the lack of any diagnostic (e.g., variance across runs, comparison to exact computation on a small dataset) weakens the evidence that MDS measures what it claims to measure.

- **MDS on high-dimensional sparse categorical data not discussed:** The metric relies on L1 nearest-neighbor distances in the output space, which can become uninformative when applied to high-dimensional categorical attributes with sparse domains (due to the curse of distance concentration). The paper uses MDS on datasets with categorical attributes but does not discuss this potential limitation or validate that L1 distance remains meaningful in those settings.

- **Fidelity evaluation limited to 1-way and 2-way marginals (Section 3.2):** The Wasserstein metric is computed only on univariate and bivariate marginals, which cannot capture high-order dependencies. While this is standard practice in the field and the metric itself can extend to higher-order marginals in principle, the paper does not acknowledge this limitation or discuss what types of distributional discrepancies might be missed.

### Trivial

- **Pathological synthesizer example in Section 4.2 (line 271):** The "synthesizer that adds a large constant" example is used to illustrate a limitation of MDS, but the paper immediately acknowledges this is not a practical concern. The example is arguably unnecessary and could confuse readers.

## Suggestions
1. **Define the "empirical upper bound" explicitly** — state what it is (e.g., performance of a model trained on D_train and evaluated on D_test) and why it's considered an upper bound for synthesis.

2. **Add an MDS sensitivity analysis** — show how the estimated MDS varies with m (e.g., plot m=20, 40, 60, 80, 100) on at least one dataset to justify the claim that m=80 is sufficient. Alternatively, compute exact MDS on a small dataset for validation.

3. **Acknowledge the limitation of 1-way/2-way marginal fidelity** and discuss when higher-order dependencies might matter for the evaluation.

4. **Discuss the behavior of L1 nearest-neighbor distances for high-dimensional categorical data** in the MDS section, and consider whether alternative distance functions might be needed for such settings.

## Score and Decision

**Originality:** High. The paper introduces genuinely new metrics (Wasserstein-based fidelity with unified categorical/numerical treatment, MDS for worst-case privacy, MLA for robust utility) that address specific documented limitations of existing metrics.

**Importance of research question:** High. Systematic evaluation of tabular data synthesis is critical given the proliferation of synthesizers and the documented inconsistencies in current evaluation protocols.

**Claims well-supported:** Mostly. The methodological contributions are clearly defined and motivated. The empirical claims (13%/11% improvements, comparative rankings) are stated in the main text and refer to experimental sections that were stripped by the parser. The minor weaknesses (undefined "empirical upper bound," unvalidated MDS approximation) are addressable without undermining the core contribution.

**Soundness of experiments:** The experimental methodology described (8 synthesizers, 12 datasets, 4-phase pipeline) is sound and appropriate for a benchmark study. The tuning objective is simple but principled.

**Clarity of writing:** Excellent. The paper is well-structured, the metrics are clearly defined with formal notation, and the critiques of existing metrics are specific and well-reasoned.

**Value to the research community:** High. The proposed metrics and framework can serve as a standardized evaluation protocol, and the open-source implementation facilitates adoption.

This is a solid contribution to an important problem. The remaining weaknesses are minor and do not threaten the paper's core claims.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>

## Questions


## Decision
Accept
