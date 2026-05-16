Now I have a thorough understanding of the paper. Let me produce the consolidated review.

---

## Summary

This paper derives two statistical tests for detecting pairwise interactions between perturbations from unstructured data (e.g., raw pixels in images). The separability test (Theorem 1) shows that non-interacting perturbations have multiplicative density ratios, and the disjointedness test (Definition 2) shows that non-interacting perturbations have additive density differences. These tests are integrated into an active learning pipeline using Information Directed Sampling (IDS) for efficient discovery of interacting pairs. The approach is validated on synthetic data and on a real biological dataset of 50 pairwise CRISPR knockout experiments with microscopy readouts (1,225 gene pairs), where IDS discovers all top-5% scoring pairs and 12–15% more known biological interactions than baselines.

## Strengths

- **Principled, theoretically grounded interaction tests for unstructured data.** The paper derives two testable implications of non-interaction—separability (Theorem 1: density ratios multiply) and disjointedness (Definition 2/Theorem 2: density differences add)—from causal assumptions about latent variable structure. This provides a formal foundation for detecting interactions from raw pixel-level observations without requiring latent variable disentanglement, which is a genuine theoretical contribution over prior work that assumes structured features or disentangled representations.

- **Demonstrated effectiveness on real biological data.** Using a large pairwise CRISPR knockout dataset in HUVEC cells (50 genes, 1,225 pairs) with microscopy imaging, the paper shows that both test statistics recover known biological relationships (e.g., apoptosis pathway, proteasome components) as seen in the qualitative heatmaps (Figure 4), and that the active learning pipeline discovers biologically meaningful interactions efficiently. The MMD-based test produces particularly interpretable block structure consistent with pathway annotations.

- **Active learning integration that significantly accelerates discovery.** The paper frames pair selection as active matrix completion with IDS, and shows that this discovers all top-5% scoring pairs within 500 experiments (vs. ~50% for baselines) on the real data (Figure 6). The 12–15% improvement in known biological interactions over random, UCB, TS, and US provides clear evidence that the pipeline efficiently exploits the structure in the test statistics.

- **Honest discussion of limitations.** The paper openly acknowledges the low overall correlation between test statistics and known interactions, the sensitivity of the KL estimator to the clipping parameter, and the possibility that novel high-scoring pairs may represent genuine undiscovered biology. This transparency strengthens the paper's credibility.

## Weaknesses

### Fatal
None.

### Major

- **Gap between theoretical derivation and practical implementation of the separability test.** The separability test (Section 3.1) is derived under Assumption 2 (diffeomorphism between latent space $\scZ$ and observation space $\scX$), yielding the result that separable perturbations have multiplicative density ratios. However, on real data (Section 5.2, line 426–428), the test is applied to *1024-dimensional embeddings* from a pre-trained masked autoencoder—a nonlinear, non-invertible, learned mapping. The paper's Remark (lines 150–155) states that the diffeomorphism can be relaxed so long as a change-of-variable formula holds, but it does not justify why an autoencoder embedding (which is neither bijective nor guaranteed to satisfy the required regularity conditions) preserves the theoretical property that separable ↔ multiplicative density ratios. Without this link, the test statistic is applied in a space where its theoretical meaning is unclear, undermining the validity of the separability test as a test of the claimed latent-variable property. This is a structural issue: the method as implemented may not correspond to the theory that motivates it. *Mitigation: the synthetic image experiment (Figure 3, right panel) shows the test works on image data under controlled conditions, partially bridging this gap, but explicit justification or analysis of why the property approximately holds under autoencoder embeddings is needed.*

### Minor

- **Synthetic validation is purely qualitative.** The synthetic experiments (Section 5.1, Figures 2–3) show heatmaps and state that ground-truth interacting pairs are correctly identified, but no quantitative metrics are reported (e.g., AUC, precision-recall, p-value separation between interacting vs. non-interacting pairs). The tabular example uses only four perturbations (A, B, C, D) with two interacting pairs, and the image example similarly uses only four perturbations. While the real-data validation is the paper's main empirical contribution, the synthetic experiments would be substantially more convincing with quantitative metrics across multiple random seeds.

- **No direct comparison of the test statistics themselves against simpler interaction measures.** The paper compares the *active learning selection* (IDS) against bandit baselines, but never evaluates whether the KL-based and MMD-based test statistics are themselves *better at detecting known biological interactions* than simpler alternatives such as cosine similarity of single-perturbation embeddings, Euclidean distance between mean embeddings, or other distance-based measures. The paper notes (lines 68–69) that the test statistics are "complementary" to cosine similarity, and discusses the low correlation with known interactions as a limitation (Section 6). However, a direct comparison (e.g., precision-recall curves for known interactions using the proposed tests vs. cosine similarity) would substantially strengthen the claim that these tests capture meaningful biological signal beyond existing approaches.

- **Active learning simulation treats test statistics as deterministic rewards without modeling estimation uncertainty.** In the active learning pipeline (Section 4), the reward matrix $\mathbf{R}$ contains the test statistics computed from experimental data. These statistics are themselves point estimates (e.g., estimated MMD or KL divergence) with sampling noise. The posterior model places a Gaussian prior on the *true* underlying matrix, but observed entries are treated as exact values. The paper does not incorporate observation noise into the posterior updates or discuss how finite-sample variance of the test statistics affects the IDS regret guarantees. While this is a common simplification in bandit settings, its impact on the realism of the simulation is not addressed.

- **The TSC2/MTOR guide-level test interpretation is incomplete.** Figure 5 shows that some within-gene guide pairs (e.g., MTOR guide 1 vs. MTOR guide 2) have lower separability scores than other same-gene pairs. The paper states the results are "consistent with what we would expect" but does not explain this specific pattern. If guides targeting the same gene produce different morphological effects, this has implications for the aggregation procedure used in the 50-gene analysis (line 423: "aggregating the effects of the individual CRISPR guides"), which is not specified in the main text.

- **Aggregation of CRISPR guides to genes is underspecified.** Line 423 states "aggregating the effects of the individual CRISPR guides" but does not specify the aggregation method (e.g., mean, max, pooling). This matters for reproducibility.

- **Number of random seeds for active learning is not stated.** The shaded regions in Figure 6 are described as "min-max over all runs" but the number of independent runs/seeds is not reported, making it difficult to assess the variability of the results.

### Trivial

- The improvement in known biological interactions (12–15%) is modest, and the paper's abstract describes it as "significantly more." While not inaccurate, the abstract could be more precise about the magnitude.

## Nice-to-Haves

- A quantitative comparison of the test statistics vs. cosine similarity (or other simple baselines) for detecting known biological interactions on the 50-gene dataset, e.g., precision-recall curves.
- An analysis of whether the low-rank assumption on the reward matrix holds for the real data (e.g., singular value plot of the observed test statistic matrix).
- Discussion of multiple testing considerations, even if the scores are used continuously rather than as formal hypothesis tests.

## Removed Points

These points are flagged to be removed per the meta-reviewer instructions; treat them with caution.

- *Criticism about missing model specification for active learning (posterior parameters, rank determination) being deferred to appendix.* → Removed per hard rule: the parser strips appendix content; these details exist in the original submission.
- *Criticism about missing appendix content, proofs, or experimental details.* → Removed: these are present in the original submission.
- *Criticism that the improvement over random is only 12–15%, described as "marginal."* → Removed: the paper's primary result is the top-5% pairs discovery (IDS finds all vs. baselines ~50%), and the paper itself notes the discrepancy between this and the known-interactions metric. The 12–15% figure is presented transparently and is not inflated.
- *The remark that the paper does not discuss power or sample complexity of the KL test.* → Removed: this is a request for a different paper's contribution; the paper is an empirical systems paper, not a statistical testing paper.
- *Request for multiple testing correction.* → Moved to Nice-to-Haves: the scores are used as continuous ranking scores, not formal hypothesis tests.
- *Criticism that the correlation with known interactions is low but not analyzed.* → The paper already discusses this in the limitations section (lines 517–522) and explicitly states this could reflect genuine undiscovered biology. This is acknowledged, not ignored.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the paper's core contributions (principled interaction tests from latent variable assumptions, integration with active learning, real biological validation) and surface the expected concerns about the theory-practice gap for embeddings and the qualitative nature of the synthetic validation. No reviewer raised a perspective that fundamentally reframes or extends the paper's findings.

## Suggestions

1. **Bridge the theory-practice gap for the separability test.** Provide explicit justification (analysis or additional synthetic experiments) that the multiplicative density ratio property holds approximately when the test is applied to non-invertible autoencoder embeddings. One concrete approach: construct a synthetic DGP where the true latent space is low-dimensional, observations are high-dimensional pixels, and compare the test on raw observations (where theory applies) vs. on autoencoder embeddings. Show that the test still works.

2. **Add quantitative metrics to synthetic experiments.** Report precision, recall, or AUROC for detecting interacting vs. non-interacting pairs across multiple random data instances in the synthetic settings.

3. **Evaluate the test statistics against simpler alternatives on real data.** Compute how many known biological interactions appear in the top-k scored pairs from the MMD test, the KL test, and a cosine-similarity-based score. Reporting precision-recall or enrichment curves would directly validate the tests' biological relevance.

4. **Specify the guide-to-gene aggregation method** explicitly, report the number of active learning runs/seeds, and discuss how estimation noise in the test statistics might affect the active learning results.

## Score and Decision

The paper presents a theoretically motivated and practically instantiated framework for detecting pairwise interactions from unstructured data, with compelling real biological validation. The core weakness is the gap between the separability test's theoretical assumptions (diffeomorphism) and its practical application (autoencoder embeddings), which the paper does not adequately justify. However, the synthetic image experiment partially mitigates this, and the disjointedness test (MMD-based) does not share this gap. The paper's contributions—two testable notions of interaction derived from causal assumptions, integration with active learning, and demonstrated real-world effectiveness—are significant. The weaknesses are addressable in revision and do not undermine the core claims.

**MY FINAL SCORE: <pineapple>7.0</pineapple>**
**MY FINAL DECISION: <orange>Accept</orange>**