I've now read the paper thoroughly and verified the reviewer claims against the actual content. Let me produce the final consolidated review.

## Summary

This paper analyzes similarity-based privacy metrics (SBPMs) used by synthetic data companies and demonstrates their inadequacy through both theoretical critique (five fundamental limitations in Section 3) and a practical reconstruction attack called ReconSyn. The attack recovers at least 78% of training data outliers across five generative models and five datasets with perfect precision, under the assumption that the adversary has black-box access to the generative model *and* the privacy metrics API. The paper further shows that DP training of the generative model does not stop the attack because the unprotected metrics themselves leak information.

## Strengths

- **Novel reconstruction attack with strong empirical results.** ReconSyn achieves ≥78% recall of train outliers with perfect (100%) precision across all five models and datasets (Table 1), including on high-dimensional data like MNIST where SampleAttack alone fails but SearchAttack succeeds. This concretely demonstrates that SBPMs fail to protect even the most vulnerable records.

- **Systematic identification of fundamental flaws in SBPMs.** Section 3 enumerates five well-reasoned weaknesses — no theoretical guarantees, binary privacy framing, non-contrastive evaluation, lack of worst-case analysis, and treating privacy as a data property rather than a process property — that go beyond prior ad-hoc criticism and provide a structured framework for understanding why these metrics are insufficient.

- **Clear demonstration that the metrics themselves (not the generator) are the weak point.** The key negative result (Section 5.2, Figure 6) shows that ReconSyn succeeds even when the generative model is trained with DP (ε=0.1) or replaced by trivial generators (Independent, Random). The paper explicitly isolates the leakage source: the deterministic, train-data-dependent privacy metrics break the end-to-end DP pipeline. This is a novel and practically important finding.

- **Responsible disclosure practice.** The authors contacted Gretel and MOSTLY AI >90 days before submission and are working with them on next steps, which strengthens credibility and shows real-world impact.

## Weaknesses

### Fatal
None.

### Major

1. **The attack's threat model is clearly stated but differs from some real deployment scenarios.** ReconSyn assumes the adversary has ongoing black-box access to the privacy metrics API — i.e., they can submit arbitrary synthetic datasets and observe pass/fail results repeatedly. The paper justifies this by citing company documentation (lines 115-118). However, the paper never discusses the one-shot release scenario where a provider uses SBPMs as an *internal* quality gate before releasing a single static synthetic dataset, and does *not* expose a metrics API to the data recipient. In that scenario, the adversary receives only one synthetic dataset and cannot iteratively query the metrics. The paper's argument that companies "offer" these metrics (line 117) conflates offering a metrics *score* alongside the data vs. offering an interactive query API. The attack is valid against interactive deployments; the paper should explicitly discuss which real-world deployments match its threat model. Without this clarification, the paper risks implying that *any* use of SBPMs is vulnerable, when the vulnerability is conditional on granting repeated query access to the metric oracle.

2. **The claim that ReconSyn is "agnostic to... the type of dataset" (lines 30, 119) is extrapolated beyond the evidence.** The evaluation covers five tabular datasets and one image dataset (MNIST). The paper has not tested non-tabular, non-image data (e.g., text, time series, graphs). While MNIST adds some breadth, calling the attack fully dataset-type-agnostic is a stronger claim than the evidence supports. The authors should either temper this claim or add a non-tabular dataset to the evaluation.

### Minor

3. **How ground-truth outliers are defined for computing recall is underspecified in the main text.** The adversary's OutliersLocator uses a GMM fitted to synthetic data to find candidate outliers, which is a reasonable procedure for the *adversary*. But the paper also reports recall — the proportion of *true* train outliers reconstructed. The paper mentions that Appendix C defines the criteria for labeling training records as outliers for evaluation, but the main text should at minimum summarize the criterion (e.g., distance from cluster centers, density threshold) to make the evaluation self-contained and interpretable.

4. **The DP framing, while technically accurate, could mislead a casual reader.** The paper explicitly states "this does not mean that DP does not work. In fact, in this context, the leakage comes from the privacy metrics; as they require access to the train data and are deterministic... they break the end-to-end DP pipeline" (line 216). This is correct and clear. However, the section title "5.2.1 DP GENERATIVE MODELS" and the abstract's phrasing "applying DP... does not successfully mitigate ReconSyn" can create the impression that DP itself is being tested and found wanting. The paper would benefit from consistently foregrounding that the result is about a *system* failure (DP model + unprotected metrics API) rather than DP's failure per se — which the clarifying sentence already does, but the surrounding framing undercuts.

### Trivial
- The utility metric (aggregated 1-way marginals and 2-way mutual information) is reasonable but not defended against alternatives. Since this is used only to demonstrate the privacy-utility trade-off (Figure 6) and does not affect the core claim, it is a minor presentational gap.

## Nice-to-Haves

- An information-theoretic or combinatorial analysis showing a lower bound on how many bits are leaked per metric query (independent of the generative model) would significantly strengthen the theoretical contribution and decouple the result from ReconSyn's specific implementation.
- A discussion of how the number of attack rounds scales with dataset size, dimensionality, or domain size would help practitioners assess feasibility.
- A brief explicit discussion of the one-shot release scenario (where metrics are used internally and never exposed as an API) would help clarify the threat model's scope.

## Removed Points

- **"SearchAttack not handling continuous attributes"** — The paper states that data is discretized as a pre-processing step (line 44), making the column-by-column shaking procedure well-defined.
- **"Paper relies heavily on appendices"** — Per evaluation rules, the appendices exist in the original submission but were stripped by the parser; this is not a flaw the authors can address.
- **"Low utility generators not distinguished"** — The paper explicitly distinguishes this scenario in Section 5.2.2 (lines 220-226), noting the different mechanism (trivial generators force the adversary to target all train data, not just outliers).
- **"DP doesn't work" strawman** — The paper explicitly states "this does not mean that DP does not work" (line 216), addressing this concern directly.
- **"Should also test text/time series"** — This is scope creep beyond what is reasonable. 5 tabular datasets + MNIST provide meaningful breadth; asking for every data modality would turn the paper into a different, broader paper.

## Novel Insights

The single most important insight from crossing the reviewer analyses is that the paper's central negative result — DP-trained models still leak — is both its strongest contribution and its most easily misinterpreted finding. The paper is technically correct that the *unprotected metrics API* creates a side channel that bypasses DP, but this is not a limitation of DP as a mechanism; it is a system-design flaw where DP protects only one component while another component (the metrics oracle) provides unfiltered access to training data statistics. The reviews collectively highlight that the paper's impact would be strengthened by more sharply separating these two narratives: (1) SBPMs are inherently unsound (a theoretical claim), and (2) exposing a non-DP-protected metric oracle alongside a DP-trained model negates DP (a system-design warning). These are related but distinct contributions, and the paper sometimes conflates them in ways that weaken its otherwise strong argument.

## Suggestions

1. Add a paragraph explicitly discussing the one-shot vs. interactive API deployment scenarios. Acknowledge that ReconSyn requires the latter and clarify which companies expose an interactive metrics API (vs. only a released static dataset with scores).
2. Temper the "agnostic to the type of dataset" claim or add a non-tabular evaluation (e.g., a text-based synthetic data benchmark).
3. Include a brief summary of the ground-truth outlier labeling criteria from Appendix C in the main text's evaluation section.
4. Retitle Section 5.2.1 to something like "DP-Trained Models Do Not Prevent Metric-Based Leakage" and ensure the clarifying sentence about DP working correctly is prominent (it already exists but could be earlier in the section).

## Score and Decision

This paper makes a genuine contribution: it is the first work to systematically demonstrate a reconstruction attack that exploits similarity-based privacy metrics as the vulnerability vector. The attack is well-designed, the experiments are thorough across multiple models and datasets, and the fundamental limitations analysis in Section 3 provides a principled framework for understanding why SBPMs fail. The weaknesses are about scope qualification and framing — they do not invalidate the core finding. With the suggested clarifications (particularly about deployment scenarios and dataset-type claims), this would be a very strong paper. As it stands, it is a solid paper with clear contributions and addressable limitations.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>