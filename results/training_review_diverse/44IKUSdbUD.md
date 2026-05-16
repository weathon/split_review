Now I have thoroughly verified the paper against the reviewer claims. Here is my consolidated review.

---

## Summary

This paper proposes a computational framework for gene-gene interaction discovery from single-cell transcriptomic data, built on two main contributions: (1) CelluFormer, a permutation-invariant Transformer trained on multi-cell-type data for Alzheimer's disease classification, whose attention maps are used to score gene-gene interactions; and (2) a two-pass randomized algorithm (Weighted Diversified Sampling, WDS) that estimates a minmax kernel density for each cell, enabling efficient subsampling of the dataset while preserving interaction discovery performance. The paper claims that sampling just 1% of cells via WDS achieves results comparable to using the full dataset.

## Strengths

1. **Novel two-pass randomized algorithm for diversity estimation with strong theoretical grounding.** Algorithm 1 computes an estimated minmax kernel density for each cell in O(n·nnz(X)) time with constant memory (R×B), avoiding the O(n²) cost of pairwise comparisons. Theorem 1 establishes that the output w_x is an unbiased estimator of the minmax density K(q) (up to an o(1) term from the CWS hash functions). This is a clean and practical algorithmic contribution grounded in established LSH theory.

2. **Empirical evidence that WDS outperforms uniform sampling for interaction discovery across multiple cell types.** Table 2 consistently shows that WDS yields higher NES scores than uniform sampling at the same sample rate across 7 cell types and 4 sample sizes. For example, at 1% sampling on L6b, WDS achieves NES 1.17 vs. uniform 0.79 (MSE 0.0004 vs. 0.0226). The advantage is systematic across nearly every configuration, which provides genuine evidence that the diversity-based sampling helps.

3. **Transformer-based framework (CelluFormer) achieves competitive or superior NES against statistical baselines.** In Table 1, CelluFormer achieves the highest NES on 4 out of 8 datasets (Pax6: 1.25, Chandelier: 1.17, L6_IT_Car3: 1.22, All neuron data: 1.17) and is competitive on the remaining ones, outperforming Pearson correlation, Spearman correlation, and CS-CORE across the board.

4. **Theoretical connection between the diversity score and minmax similarity is well-motivated.** The use of 0-bit CWS hash functions (Definition 3), where collision probability equals minmax similarity, provides a principled bridge from pairwise similarity to efficient density estimation without needing explicit pairwise computation.

## Weaknesses

### Fatal
None.

### Major

1. **Mismatch between the WDS estimator target and the full-data baseline used for evaluation (structural).** The full-data interaction score is a uniform average over all cells. The WDS estimator \tilde{Z} in Definition 5 estimates E_{x~I(x)}[Z_x], i.e., a probability-weighted expectation under the IMD distribution, not the uniform mean. The paper acknowledges this definitionally ("an unbiased estimator for the expectation of Z in distribution with density I(x)") but then computes MSE against "the ground truth derived from the entire dataset" — which is the uniform average — without addressing the distribution shift. The MSE numbers in Table 2 compare quantities that estimate different targets; whether the comparison is meaningful depends on whether the ranking (and thus NES) is robust to this shift, which the paper does not discuss. This is the most serious weakness because it undermines the quantitative claim that sampling matches "full dataset" performance. The authors should either (a) use importance-weight renormalization to estimate the uniform average from the WDS subset, or (b) clearly argue why the weighted estimate is the right target and compare against a reweighted full-data baseline.

2. **The central claim that 1% sampling yields "performance comparable to utilizing the entire dataset" cannot be directly verified from the presented tables.** Table 2 reports mean NES and MSE for sampled subsets but does not include a "Full Data NES" column for each cell type. The paper states the ground truth is "as shown in Table 1," but the cross-reference is ambiguous and the reader must manually compare across tables. For example, L5_ET's CelluFormer full-data NES in Table 1 is 1.15, but WDS at 1% gives 0.95 — is this "comparable"? The MSE of 0.0082 suggests closeness on average across 5 runs, but without the full-data baseline column in the same table, the reader cannot easily assess the magnitude of the gap. Adding a "Full Data NES" column to Table 2 is essential.

### Minor

3. **Missing CelluFormer architecture and training hyperparameters.** The paper describes CelluFormer as a permutation-invariant Transformer using gene embeddings, expression-level scaling, and padding masks, but provides zero architectural specifics: number of layers, number of attention heads, embedding dimension, feed-forward dimension, activation functions, learning rate, optimizer, batch size, training epochs, weight decay, or GPU hardware. This is insufficient for reproduction. While the paper does not claim architectural novelty, the method cannot be independently reimplemented without these details.

4. **No within- and across-experiment variance reported in Table 2.** The paper states experiments were repeated 5 times, yet reports only the mean NES and MSE — no standard deviations, confidence intervals, or any dispersion measure. Given that some configurations show near-identical performance (e.g., L6b at 10%: uniform 1.20 vs. WDS 1.21), statistical significance cannot be assessed. This limits the reader's ability to determine whether the observed WDS advantage is robust.

5. **The MLP comparison in Section 2.3 is not a controlled experiment.** Table "model_performance" compares CelluFormer (trained on all neuronal cell types) against MLPs trained on *individual* cell types. The text says "outperforms traditional MLP with downstream training on a single cell type," which is true but uninformative — the comparison conflates architecture with training data diversity. The MLP row on "All Neuronal Cell Types" achieves 97.23/97.25, narrowing the gap to 98.12/98.12. The paper should either also train the MLP on the full data for a cleaner comparison, or de-emphasize this comparison. (Note: the main RQ1 evaluation in Table 1 uses proper baselines including scGPT and scFoundation, so this issue does not affect the paper's central interaction discovery claim — it only affects the architecture motivation section.)

6. **The sampling algorithm for drawing without replacement with softmax-normalized probabilities is unspecified.** The paper states "we perform sampling without replacement to generate a subset X_sub ⊂ X, where x ∈ X has the sampling probability I(x)" but does not describe how this is done. Since I(x) depends on the entire dataset (via the softmax denominator), standard without-replacement sampling schemes (e.g., systematic sampling, sequential Poisson sampling, Gumbel-top-k) should be specified for reproducibility.

### Trivial

- The paper refers to "the ground truth derived from the entire dataset, as shown in Table \ref{tab:RQ1_res}" — Table 1 shows model comparisons, not a dedicated "ground truth" column. The cross-reference is confusing and should be clarified.
- Theorem 1 is declared as informal with the formal version deferred to an appendix. While acceptable, the o(1) term is not quantified or bounded in the main text.
- Minor: "minmax (q)" is used sometimes as notation for the density, but Definition 2 defines K(q); the notation is slightly inconsistent.

## Nice-to-Haves

- **Ablation on layer/head averaging:** The paper averages attention maps over all layers and heads (Section 2.4) without justification. Different layers might capture different interaction scales. An ablation showing whether a specific subset of layers/heads produces better NES would strengthen confidence in the pipeline.
- **Discussion of the diversity-representation trade-off:** The IMD gives higher weight to rare/diverse cells. This is by design, but the paper does not discuss whether rare cell types are oversampled at the cost of missing common-cell-type interactions — or why that trade-off is acceptable for interaction discovery.
- **The minmax similarity on sparse data:** Single-cell data is extremely sparse (most entries zero). The minmax similarity denominator sums over all V genes, so zeros dominate. A brief discussion or empirical check of whether minmax similarity on sparse data is meaningfully differentiating between cells would be helpful.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The importance-weighted estimate Z̃ uses weights I(x) that are proportional to the sampling distribution, but unweighted aggregation over the full dataset is implicitly assumed as the ground truth. The authors never correct for the change of measure."* — Kept but downgraded to Major (see Weakness #1). The paper does not "implicitly assume" unweighted aggregation; it explicitly states what the estimator estimates. However, the comparison to full-data baseline via MSE is not properly justified, which is the real issue.
- *"The MLP baseline is not used in the same gene-gene interaction pipeline — NID extracts interactions from a trained MLP, but the MLP itself is never evaluated on the same attention-based discovery task."* — RQ1 (Table 1) does evaluate NID alongside other baselines on the interaction discovery task, so this claim is factually incorrect.
- *"The formal theorem is deferred to supplementary material, which is missing from the extract."* — Per policy, appendix sections are stripped by the parser; they exist in the original submission.
- *"The o(1) term makes the estimator's guarantees opaque"* without acknowledging the explicit reference to Li et al. (2021) Theorem 4.4 for details. This is standard practice for citing prior theoretical results.
- *"Missing appendix"* and related criticisms — per policy, these are parser artifacts.
- *Formatting/style nitpicks* and *typos* — per policy, these are parser artifacts.
- *"The paper should also cover Y / domain Z"* style scope-creep demands.

## Novel Insights

The most interesting observation emerging from these reviews is the tension between the paper's formal definitions and its evaluation protocol. The WDS estimator \tilde{Z} is carefully defined to estimate a weighted expectation under the IMD distribution, yet the evaluation (MSE against full-data NES) implicitly treats it as an estimator of the uniform average. This is not necessarily fatal — if the ranking induced by the weighted estimator aligns with the ranking from the uniform average, the NES comparison could still be meaningful — but the paper never argues why this alignment should hold. A second insight is that the systematic superiority of WDS over uniform sampling across nearly all configurations is actually quite strong evidence that *some* form of diversity-based sampling helps, even if the exact quantitative claim about "comparable to full dataset" needs tighter scrutiny. The paper would be strengthened substantially by (a) adding a full-data column to Table 2 so the reader can directly assess the gap, and (b) either reweighting the estimator to target the uniform average or explicitly justifying why the weighted target is preferable.

## Suggestions

1. **Reconcile the estimator with the evaluation target.** Either use importance-sampling reweighting so that \tilde{Z} estimates the uniform average (making the MSE comparison apples-to-apples), or provide a clear argument that the ranking (and thus NES) is robust to the distribution shift, with supporting empirical evidence.
2. **Add a "Full Data NES" column to Table 2** for each cell type so the reader can directly assess how close the 1% WDS result is to the full-dataset baseline. This is the single most impactful fix.
3. **Report standard deviations** for the 5 repeated experiments in Table 2 so readers can assess the stability of the results.
4. **Provide architecture details** (number of layers, heads, embedding dimension, and training hyperparameters) for CelluFormer in a dedicated table or appendix.
5. **Specify the sampling-without-replacement algorithm** used to generate subsets from the softmax-normalized IMD probabilities.
6. **Clarify the cross-reference** in the ablation section — make explicit what the "ground truth derived from the entire dataset" is and where it is reported.

## Score and Decision

The paper presents a genuinely novel algorithmic contribution (two-pass minmax density estimation for diversity sampling) with theoretical grounding and shows systematic evidence that WDS outperforms uniform sampling. However, the main claim about 1% sampling matching full-dataset performance is weakened by (a) an unaddressed mismatch between what the WDS estimator targets and what it is compared against, and (b) the absence of explicit full-data baselines in the sampling results table. These issues are fixable in revision but prevent full confidence in the paper's central quantitative claim as presented. The paper is above the rejection threshold — the core ideas are sound and the algorithmic contribution is clear — but the evaluation needs tightening.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>