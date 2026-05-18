Now I have all the information needed to verify each reviewer claim against the paper. Let me compose the final consolidated review.

---

## Summary

This paper proposes FACTS (FACTored State-space), a recurrent state-space model that uses graph-structured memory with a routing mechanism to achieve permutation invariance with respect to input features. The model treats both memory and input as sets of nodes, uses attention-based routing to assign features to latent factors, and incorporates a linearisation trick to enable parallel computation within segments. FACTS is evaluated on multivariate time-series forecasting (9 datasets, 8 baselines), object-centric video prediction (CLEVRER), and graph-based traffic prediction (METR-LA), demonstrating competitive or superior performance across all settings. The paper also includes a formal proof (Theorem 1) that the implemented model is left-permutation-equivariant and right-permutation-invariant.

## Strengths

- **Formal proof of permutation invariance/equivariance for the implemented model (Theorem 1).** The paper proves that the linearised FACTS recurrence (Equation 20, which is what is actually run) is both L.P.E. and R.P.I. This provides rigorous theoretical backing directly tied to the evaluated architecture, not just a hypothetical version.

- **Empirical robustness to input permutation.** Figure 2 shows that FACTS maintains near-identical prediction errors when input features are randomly permuted at test time, while strong baselines like S-Mamba and iTransformer suffer large degradation (e.g., S-Mamba's MSE on Traffic more than triples). This experiment directly validates the core claim and is the paper's most compelling evidence.

- **Consistently competitive performance across diverse domains.** FACTS achieves top-2 MAE on 7 of 9 MTS datasets (Table 1), the best LPIPS (0.09) on CLEVRER object dynamics (Table 2), and the best MAPE (9.08%) on METR-LA traffic prediction (Table 3), despite being a general-purpose framework competing against specialised models. This breadth supports the versatility claim.

- **Ablation of parallelisation vs. recurrence.** Figure 3 empirically shows that FACTS maintains stable forecasting performance across segment window sizes from fully recurrent (1) to fully parallel (96). This demonstrates that the linearisation for parallelism does not degrade accuracy.

## Weaknesses

### Fatal
None.

### Major

- **The routing linearisation weakens the claimed "dynamic factor assignment" mechanism.** The paper's central motivation is that FACTS "dynamically assigns input features to distinct latent factors" (line 26) via routing that depends on the evolving memory $Z_{t-1}$. However, the actual implementation (Equations 17–20) replaces $Z_{t-1}$ with $Z_0$ (the initial segment memory) in all routing functions for $\bar{A}, \bar{B}, U$. Within a segment, the assignment of features to factors is therefore determined by the fixed $Z_0$, not by the evolving state. The paper acknowledges this linearisation (line 119–120) and shows that segmentation mitigates it (window size 1 refreshes $Z_0$ at every step), but provides **no ablation** comparing the $Z_0$-based routing against a fully $Z_{t-1}$-dependent version on any task. Without this, it is unclear whether the dynamic-binding narrative actually explains the model's performance, or whether the model works well for other reasons (e.g., the set-based preprocessing or the recurrent state update $Z_t = \bar{A}\odot Z_{t-1} + \bar{B}\odot U$ itself). The paper should either (a) compare against a small-scale $Z_{t-1}$-routing variant, (b) provide analysis showing $Z_0$-dependent routing still yields effective tracking of changing factor assignments, or (c) honestly reframe the contribution to separate the implemented model from the more ambitious theoretical possibility described by Theorem 2.

### Minor

- **No control for the set-based embedders in the MTS experiments.** The paper replaces the standard linear embedders/projectors in TSLib with "set functions" to accommodate FACTS's output structure (line 183). This is a non-trivial architectural change. While it would not be meaningful to graft set embedders onto ordered baselines (they would no longer be the same models), the paper does not ablate whether the set embedder itself (coupled with a simple predictor, without FACTS's routing recurrence) contributes to performance. A straightforward ablation — FACTS with the *same* linear embedders used by baselines, accepting the loss of permutation invariance to isolate the core state-space contribution — would strengthen the evidence.

- **Single dataset for the graph prediction experiment (Section 4.3).** The claim that FACTS handles graph-structured inputs is supported by only one dataset (METR-LA). While the results are positive, this limits the generality of the graph-modality claim.

- **No discussion of computational cost.** The paper does not report runtime, memory usage, or parameter counts relative to baselines. Given the attention-based routing and factored memory, this information is relevant for judging practical applicability.

### Trivial

- The figure captions in the PDF contain garbled characters (e.g., "different col ou⟳oured pathways"), which appear to be PDF extraction artifacts.

## Nice-to-Haves

- Reporting standard deviations or confidence intervals for the main MTS results (Table 1) would clarify whether the differences between FACTS and top baselines are statistically significant.
- Adding a second graph benchmark (beyond METR-LA) would strengthen the claim of general graph processing ability.
- A discussion of how the number of latent factors $k$ is chosen and its sensitivity would be helpful.

## Removed Points

- **"Key quantitative evidence absent (unsupervised object discovery references Table 7 and Figure 8 in the appendix)."** — Removed per hard rules: the parser strips appendix sections from all papers; they exist in the original submission. The main text describes the experimental setup, qualitative finding (moving vs. static object discovery), and the claim that FACTS outperforms SAVi. The quantitative table and figure referenced are part of the submission. This criticism reflects a parsing artifact, not an author omission.

- **"Theorem 2's conditions not satisfied by the implementation."** — The harsh critic asserted that the theoretical analysis (Theorem 2) proves properties for the general recurrence (Eq. 10) but "the paper never establishes that the linearised version inherits these properties." This is factually incorrect. Theorem 1 (line 154) explicitly states: *"FACTS as defined in equation 20 is L.P.E. and R.P.I."* — where Equation 20 IS the linearised version. The theoretical claim about permutation invariance IS established for the implemented model. The critic confused Theorem 2 (a forward-looking result about the general Eq. 10 that is *not* claimed to be the implemented model) with Theorem 1 (which IS about the implemented model). The real issue (retained above) is about the *dynamic binding* claim, not the permutation invariance claim.

- **"Missing related works."** — Removed per hard rules: I cannot verify existence of external sources.

- **Formatting nitpicks and typos.** — Removed per hard rules (parser artifacts, not author issues).

## Novel Insights

None beyond the paper's own contributions. The two reviewers' perspectives did surface a meaningful tension that the paper itself does not fully address: the gap between the conceptual motivation (routing that depends on the evolving memory $Z_{t-1}$ for dynamic factor assignment) and the linearised implementation (routing that depends on the fixed initial memory $Z_0$). This is a real design trade-off that the paper presents as a practical necessity but does not empirically validate. The reviews also converged on the permutation-robustness experiment (Figure 2) as the strongest and most distinctive evidence — this experiment cleanly demonstrates a property that no baseline possesses, and the formal proof gives it theoretical backing. The paper would be strengthened by honestly discussing the scope and limits of the linearisation rather than presenting the full $Z_{t-1}$-dependent formulation as the model's description.

## Suggestions

1. **Add an ablation of the routing linearisation.** On a small-scale task (e.g., a synthetic dynamical system or a single MTS dataset), implement a version where $\bar{A}, \bar{B}, U$ depend on $Z_{t-1}$ rather than $Z_0$ (sacrificing parallel computation). If performance is similar, it validates the linearisation. If not, it clarifies the gap between the conceptual model and the practical one — and the contribution should be reframed accordingly.

2. **Ablate the set embedder in the MTS experiments.** Run FACTS with standard linear embedders (as used by baselines) on at least one dataset to isolate whether the performance comes from the set preprocessing or the core state-space routing mechanism.

3. **Reframe the "dynamic assignment" narrative to match what the model actually does.** The routing relative to $Z_0$ is still content-based (it depends on $X_t$ and the initial memory), but it does not adapt to the evolving state within a segment. The paper should be precise about this and discuss when it matters.

## Score and Decision

This is a solid paper with a clear contribution: a permutation-invariant SSM with formal guarantees and strong empirical results across diverse domains. The primary weakness is the gap between the motivating narrative (dynamic $Z_{t-1}$-dependent routing) and the implementation ($Z_0$-based routing), which is acknowledged but not analyzed or ablated. This is a significant limitation but not a fatal one — the permutation invariance claim (Theorem 1) is correctly proven for the implemented model, and the empirical results are independently interesting. The paper would benefit from addressing this tension in revision but already provides sufficient novelty and evidence to merit acceptance.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>