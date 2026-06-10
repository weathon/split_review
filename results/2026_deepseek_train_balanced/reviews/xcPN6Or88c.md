## Summary

ImputeINR proposes using implicit neural representations (INR) for time series imputation, learning a continuous function \(f: t \mapsto \mathbf{X}(t)\) decomposed into trend (polynomial), seasonal (Fourier series), and residual (adaptive group-based MLP) components. The residual uses global layers for cross-channel information and group layers for variables with similar distributions, where groups are determined by clustering. A multi-scale CNN + transformer encoder predicts the INR parameters from observed data. Experiments on 7 datasets with mask rates from 10% to 90% show strong improvements over baselines, especially at high mask rates (69.2% avg MSE reduction at 90% masking).

## Strengths

- **Strong empirical results in the high-mask-rate regime.** At 90% masking, ImputeINR achieves a 69.2% average MSE reduction over the second-best method (Section 4.2, line 210). This is a concrete demonstration of superiority in a regime where prior deep learning methods degrade severely. The improvement is consistent across all mask rates from 10% to 90% and grows as less data is observed (Section 4.4, line 224).

- **Clean ablation study with internal consistency.** Table 3 (Section 4.3, lines 216-218) tests all seven combinations of the three modules (multi-scale extraction, variable clustering, adaptive group architecture). The pattern is monotonic and coherent: any single module improves over none, any two improve over one, and the clustering+group pair outperforms other two-module combinations — exactly matching the design rationale since clustering determines the groups. This strengthens the causal claims for each design choice.

- **Controlled synthetic experiment validating the group architecture.** Figure 2 (line 119) uses a synthetic 4-variable, 2-distribution setup to show that same-distribution variables sharing a group MLP outperforms alternatives (single MLP, mixed-distribution groups). This is direct, non-tautological evidence for the core architectural innovation.

- **Broad evaluation coverage.** Seven datasets spanning different domains, variable counts, and dataset sizes, evaluated at five mask rates (10%–90%) against nine baselines including statistical, RNN, CNN, MLP, and transformer methods.

## Weaknesses

### Major

- **How "INR tokens" map to the heterogeneous continuous function parameters is entirely unspecified.** The paper states repeatedly that the transformer predicts "INR tokens" which "serve as the parameters for the INR continuous function" (lines 65, 67, 127). However, the continuous function contains: (a) polynomial coefficients \(\alpha_i\) of unspecified degree \(m\), (b) Fourier coefficients \(\beta_i, \gamma_i\) for up to \(\lfloor T/2-1\rfloor\) sine and cosine terms, (c) one global MLP layer's weights and biases, (d) \(K\) group MLP layers' weights and biases (each producing \(|C_k|\) outputs). How the transformer output tokens are decoded into this heterogeneous collection of parameters — ranging from scalars to possibly thousands of MLP weights — is never explained. This is not a trivial implementation detail; it is a core architectural mechanism without which the method cannot be reproduced or fully evaluated.

- **Variable clustering procedure is critically underspecified.** The paper defines a similarity matrix \(S(\mathbf{x}_i, \mathbf{x}_j)\) (lines 71, 83) but never states what similarity measure is used (cosine? correlation? Euclidean? mutual information?). The clustering function \(\mathcal{C}\) is applied to \(\mathbf{X} \in \mathbb{R}^{N \times T}\) (line 71), but it is ambiguous whether this is the complete ground-truth data or only the observed entries. If the full ground truth is used, this constitutes information leakage (values to be imputed would influence the grouping that determines the architecture). If only observed entries are used, at 90% masking each variable has only 10% of its timestamps observed — the reliability of similarity estimates under such sparsity is not discussed. Additionally, the agglomerative clustering variant used (linkage criterion, distance threshold) is not specified (line 197), only that it "adopts diverse inputs without the need to pre-specify the number of clusters."

- **No measures of uncertainty or variability across runs.** Every result — main results (Table 2), ablation (Table 3), robustness analysis (Figure 3) — is reported as a single point estimate with no confidence intervals, standard deviations, or even a statement about the number of random seeds or trials. Given that masking is random (line 197: "randomly mask values"), the results could be sensitive to the particular mask realization. Without any variance information, the reader cannot assess whether the reported improvements are stable or reflect favorable random draws.

### Minor

- **The headline "62.7% relative improvement" conflates very different performance regimes.** The paper acknowledges (lines 208-209) that on IAQ the improvement is 96.1% (where transformer baselines collapse to mean/median performance), on BAQ it is 54.9%, and on Solar it is 16.6%. However, the per-dataset breakdown for the larger datasets (ETT, Weather, Phy2012, Phy2019) — where baselines are stronger — is not discussed in the text. The aggregate 62.7% is heavily driven by conditions where the competition degenerates. The paper should provide per-dataset, per-mask-rate relative improvements for all datasets to give a transparent picture of where the method truly excels versus where it has marginal gains.

- **Ablation studies performed only at 50% mask rate (line 199), not at the 90% regime the method targets.** Since the paper's central claim is about extreme missing rates, the ablation should demonstrate that each module contributes meaningfully precisely in the high-mask regime. The current setup shows the modules matter at a moderate mask rate, which is less informative.

- **Evaluation limited to random missingness patterns.** The paper uses random masking (line 197: "randomly mask values"), but real-world missingness often has structure (block missingness, sensor dropout, variable-specific failures). Random masking with 10% observed points uniformly scattered means there are likely observed points near any query timestamp, which is the setting most favorable to INR's interpolation strength. Evaluating on block-missingness or structured missing patterns would substantiate the claim that INR's "infinite sampling frequency" interpolation provides practical advantages in realistic missing-data scenarios.

- **Several hyperparameters and design choices are underspecified.** The polynomial degree \(m\) for the trend component (line 132) is never given. The agglomerative clustering linkage criterion is not stated (line 197 only says "agglomerative clustering method"). The robustness analysis (Section 4.4) says "other comparison methods" without specifying which baselines are included in each figure. The visual analysis of clustering (Section 4.5, Figure 4) shows that clustering produced clusters, but does not assess whether the clustering is sensible (e.g., whether variables of the same type group together) or how clustering quality varies with mask rate.

### Trivial

- Equation (86) for the permutation matrix has garbled notation (parser artifact, but the original likely had a similar presentational issue).
- No limitations or failure-mode discussion is included (Section 5).

## Nice-to-Haves

- Adding structured/block missingness experiments would substantially strengthen the claim that INR's continuous-function properties benefit real-world imputation, not just the uniformly-random setting.
- Reporting results with at least 3 random seeds with standard deviations would transform the credibility of the quantitative claims without changing the experimental scope.

## Removed Points

These points were removed after verification against the paper. Treat them with caution if encountered elsewhere.

1. **"First imputation approach at 70%/90% claim likely false"** — The harsh critic asserted that "several existing time series imputation works evaluate at 80% or higher mask rates (e.g., TimesNet, CSDI)." This claim by the critic cannot be verified from the paper or available sources; the critic may be correct or incorrect. Under the rule to not reference information outside the paper about other works' existence or claims, this point is removed.

2. **"Continuous function has too many Fourier terms (47+47 for T=96)"** — While the critic notes this would produce a large number of parameters, the transformer output dimension and how these coefficients are predicted are not specified in the paper anyway. This is subsumed by the Major weakness about the INR-token-to-parameter mapping and is not independently actionable.

3. **"Synthetic experiment (Figure 2) is tautological"** — The strength finder correctly notes this is a controlled validation (4 variables, 2 distributions) that directly tests the design hypothesis. The harsh critic did not raise this, but on review it is a legitimate supporting experiment, not a tautology.

4. **"Small dataset advantage is not informative about general superiority"** — The paper provides per-dataset breakdowns (16.6%, 54.9%, 96.1%) and the 62.7% aggregate includes all datasets. While the aggregate could be better contextualized, the paper is transparent about the variation. The retained Minor weakness on this point is sufficient.

## Novel Insights

Both reviews converge on the same structural critique: the paper's central weakness is not a flaw in the idea or the results, but in the *specification gap* between the high-level architecture description and the actual mechanism by which the transformer outputs become the parameters of a heterogeneous continuous function (polynomial coefficients + Fourier coefficients + MLP weights). This gap appears repeatedly across different components (clustering similarity measure, INR token decoding, group assignment), suggesting a pattern where conceptual design is carefully articulated but implementation-level decisions are deferred. The reviews also independently identify a mismatch between the claimed motivation (real-world structured missingness) and the evaluation (uniform random masking), which the paper should address to fully leverage its architectural advantages. The strength finder's observation about the synthetic experiment and the clean ablation pattern provides counterbalancing evidence that the architecture's core ideas are sound.

## Suggestions

1. Specify exactly how the transformer output ("INR tokens") is decoded into the heterogeneous parameter set: polynomial coefficients \(\alpha_i\) for each variable, Fourier coefficients \(\beta_i,\gamma_i\), and the weights/biases of the global and group MLP layers. A diagram or explicit tensor reshaping formulas would resolve this.

2. Specify the similarity measure used for variable clustering (cosine? correlation? something else?), whether clustering uses only observed entries or the full data, and how missing values are handled in similarity computation.

3. Report main results with variance across at least 3 random mask seeds.

4. Add a block-missingness experiment to complement the random-masking results, demonstrating that INR's continuous-function interpolation helps in realistic structured-missing scenarios.

5. Run the ablation study at 90% mask rate in addition to 50%.

6. Specify \(m\) (polynomial degree) and the agglomerative clustering linkage criterion.

## Score and Decision

**Score: 5.0**

**Decision: Reject**

The paper tackles a meaningful problem and the core architectural ideas (decomposed INR + adaptive group MLP) are novel and well-motivated. The empirical results are strong, especially the 69.2% improvement at 90% masking. However, two Major weaknesses — (1) the complete underspecification of how INR tokens translate to the heterogeneous continuous function parameters, and (2) the underspecified clustering procedure with unresolved information-leakage concerns — prevent the paper from being reproducible or fully evaluable in its current form. For a top-tier venue, the method specification gap is too large to ignore. The paper has the foundations of a strong contribution but requires substantial clarification and additional experiments before it can be accepted.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>