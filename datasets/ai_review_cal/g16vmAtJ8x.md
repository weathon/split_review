- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 8, 6, 3, 5
Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

This paper identifies critical flaws in similarity-based privacy metrics (SBPMs) used by commercial synthetic data providers to claim "truly anonymous" data. The authors systematically enumerate five fundamental limitations of SBPMs (no theoretical guarantees, binary privacy, non-contrastive computation, lack of worst-case analysis, privacy as a data property), then present ReconSyn — a reconstruction attack that recovers train-data outliers with black-box access to the generative model and the privacy metrics. Across five generative models and five datasets, the attack reconstructs at least 78% of low-density training records with perfect precision. Crucially, the attack succeeds even when models are trained with Differential Privacy (ε as low as 0.1) or have severely limited utility, because the leakage originates from the deterministic metrics themselves, not the generative model.

## Strengths

- **Systematic critique of SBPM fundamentals (Section 3)**. The paper identifies five concrete, well-argued issues — notably the non-contrastive nature of the metrics (Issue 3) and the lack of worst-case analysis (Issue 4) — that collectively explain why SBPMs cannot provide meaningful privacy guarantees. This theoretical analysis directly motivates the attack and is the paper's strongest intellectual contribution.

- **ReconSyn achieves ≥78% outlier reconstruction with perfect precision across all settings (Table 1, Figures 1/3/5)**. The attack recovers 78–100% of train outliers across 5 models × 5 datasets, with zero false positives. The results are consistent across models of different families (graphical models, GANs) and datasets of varying dimensionality (2d Gauss through MNIST), demonstrating that the vulnerability is not an artifact of a particular model class.

- **ReconSyn succeeds under DP and with low-utility generators (Section 5.2, Figure 6)**. Even at ε=0.1 (DPGAN, PrivBayes) or using Random/Independent generators that cannot model the data distribution, the attack reconstructs >95% of targets. This is a striking result: it shows the leakage is structural to the metrics' design, not a side-effect of model quality or insufficient noise. This directly refutes the common industry counterargument that DP deployment makes SBPM-based release safe.

- **Realistic adversarial assumptions tied to actual industry practice (Section 4)**. The three required capabilities (unlimited sampling, record insertion/deletion, metric score access) are explicitly advertised by Gretel, MOSTLY AI, Hazy, and Tonic, as cited in the paper. The adversary has no side knowledge about the model architecture, hyperparameters, or training data.

- **Responsible disclosure process (Ethics Statement)**. The authors shared findings with Gretel and MOSTLY AI ≥90 days prior to submission, following standard security research practices and demonstrating grounding in real deployment concerns.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **No statistical variance reported for attack results.** The paper reports single-number results (e.g., 78% recall, "perfect precision") without confidence intervals, standard deviations, or acknowledgment of randomness from sampling. The trends across models and datasets are clear enough to support the core claims, but the precision of individual numbers is unknown. Adding standard deviations over even 3–5 independent runs would strengthen the evidential value.

- **DP evaluation conducted only on Adult Small (a low-dimensional domain).** Section 5.2.1 experiments with DP are confined to Adult Small (cardinality ≈ 10⁵). The paper plausibly argues the leakage is structural (coming from the metrics, not the model), and the argument is theoretically sound, but an empirical demonstration on a higher-cardinality dataset (e.g., full Adult or Census with ε=1 or 0.1) would substantially strengthen the claim that "DP does not mitigate ReconSyn" in more realistic settings.

- **Outlier definition and ground-truth determination are underspecified in the main text.** The paper defers "criteria for defining outliers" to Appendix C (stripped by parser). The attack uses OutliersLocator (GMM on synthetic samples) to find candidate outliers, but it is unclear how the *ground-truth* set of "train outliers" (against which recall is measured) is established — whether it is defined by an independent procedure on the actual training data, or via the same OutliersLocator mechanism (which would create circularity). This should be stated explicitly.

- **OutliersLocator depends on the model's ability to produce representative synthetic samples.** The attack's first step fits a GMM on a large synthetic sample to identify low-density regions. If the generative model is of very poor quality (addressed partially with Independent/Random experiments, but those targeted *all* train records, not outliers via OutliersLocator), the identified clusters may not correspond to actual train-data outliers. The paper could discuss this dependency more explicitly.

### Trivial
- **"Perfect precision" verification could be clearer.** The paper states precision is 100% with "no false positives" (line 130). The attack checks exact matches via the metrics API against the train data, which the authors hold for evaluation. This mechanism is correct, but the text could state explicitly that false positives are ruled out because the metrics API itself verifies exact matches against the held train data — a reader could otherwise misinterpret "perfect precision" as a property of the attack's output rather than the evaluation procedure.

- **No analysis of computational cost.** The paper reports number of rounds (1,000–5,000 for SampleAttack) but does not provide a concrete analysis of query cost, wall-clock time, or number of API calls required. This information would help practitioners assess the attack's practicality in deployment.

## Nice-to-Haves
- Replicate DP experiments on at least one larger dataset (e.g., full Adult with ε=1, ε=0.1) to strengthen the empirical claim beyond low-dimensional data.
- Add a dedicated limitations section acknowledging that the attack requires metrics to be accessible and that not all providers may expose scores even when tests pass; some may use DP-only release without metric-based filtering.
- Provide a brief analysis of query count / time cost for the attack.

## Removed Points
The following points from the reviewers were removed with justification:

- **"API assumptions not thoroughly validated" (Harsh Critic's Critical Issue 5)**: The paper provides specific citations to company documentation (MOSTLY AI, Gretel, Hazy) for each assumption. The criticism that the paper "does not verify whether current APIs actually permit this level of control" is a request to confirm the accuracy of cited claims, which goes beyond the standard of evidence expected for paper-accessible references. The paper's adversarial model is described as "plausibility" assumptions with citations, which is appropriate.

- **"Missing dedicated limitations section" and "Section 2 threshold discussion could be more explicit"**: These are presentation preferences that do not affect the validity of the paper's claims. The Discussion (Section 6) touches on limitations indirectly.

## Novel Insights
The reviewer comments do not surface an insight substantially beyond what the paper itself offers. The paper's own core insight — that deterministic similarity metrics break the end-to-end DP pipeline because they are non-contrastive and leak information through pass/fail tests — is already well-articulated in Issues 3 and 4 of Section 3.

## Suggestions

1. Explicitly state how ground-truth outliers are determined for the evaluation (e.g., "outliers are the K records with lowest kernel density estimate on the full training data, independently of OutliersLocator").
2. Add standard deviations or ranges to the main quantitative results (Table 1, Figure 3) from multiple runs.
3. Replicate the DP experiment on at least one larger dataset (full Adult or Census) to empirically confirm the structural argument holds beyond small domains.
4. Briefly describe the computational cost (approximate number of API calls or wall-clock time) for a representative attack configuration.
