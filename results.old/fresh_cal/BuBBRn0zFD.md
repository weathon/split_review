Now I'll synthesize the final review.

## Summary

This paper derives two principled statistical tests (separability via KL divergence, disjointedness via MMD) for detecting whether pairwise perturbations interact in unstructured data such as images, and integrates these tests into an active matrix completion pipeline (using Information Directed Sampling) to efficiently search the combinatorial space of pairwise experiments. The method is evaluated on synthetic data (tabular and image), on a small biological sanity check (TSC2/MTOR CRISPR guides), and on a real dataset of 1,225 pairwise CRISPR knockouts across 50 genes in HUVEC cells imaged via cell painting.

## Strengths

1. **Principled derivation of testable separability condition (Theorem 1, Eq. 3).** The paper proves that when two perturbations act on disjoint sets of latent children, the density ratio of the double perturbation factorizes as the product of the single-perturbation density ratios. This provides a well-grounded, estimable null hypothesis for interaction testing from unstructured data without requiring latent disentanglement.

2. **Disjointedness test enabling compositional generalization of summary statistics (Definition 2, Eq. 4–5).** The paper defines a sufficient condition under which the expectation of any feature map satisfies $\vec{h}_{i,j} = \vec{h}_i + \vec{h}_j$, enabling prediction of pairwise embeddings from single perturbations—a practically useful property for reducing the experimental search space.

3. **Active matrix completion with IDS achieves strong empirical performance on real data (Figure 4).** Under a low-rank assumption on the reward matrix, IDS discovers all top-5% scoring pairs within 500 experiments, compared to baselines that recover barely half. On the 50-gene biological benchmark, IDS and TS discover 12–15% more known biological interactions from CORUM, StringDB, Signor, and hu.MAP than random search and UCB.

4. **Synthetic validation across modalities.** Both tests are validated on synthetic data: the separability test on 3D tabular data and 3×128×128 images (Figure 2), and the disjointedness test with two different kernels (RBF, Matern 2.5) showing robustness to kernel choice (Figure 3).

5. **The paper is candid about its limitations.** The Discussion explicitly notes the low correlation between the test statistics and known interaction databases, and the sensitivity of the SMILE-based KL estimator to the clipping parameter — appropriate self-criticism for a methods paper.

## Weaknesses

### Fatal
None.

### Major
1. **Real-data validation of the separability test is limited.** The only direct biological validation before the main 50-gene experiment is the TSC2/MTOR guide-pair comparison (Figure 2, left). While this sanity check works as expected (guides targeting the same gene score higher than cross-gene pairs), it involves only two genes. For the full 50-gene matrix, the paper acknowledges low correlation with known databases and relies on qualitative identification of a few expected pairs (apoptosis, proteasome). A more systematic evaluation — e.g., precision-recall against a held-out set of validated interactions, or quantification of how the separability score compares with simpler baselines — would substantially strengthen the claim that the test detects biologically meaningful structure rather than picking up noise from the KL estimator.

### Minor
1. **The active learning simulation uses oracle-computed scores rather than simulating sequential estimation noise.** The test statistics for all 1,225 pairs are computed from the full dataset, then treated as ground-truth rewards that the algorithm sequentially "reveals." This is a valid way to benchmark active matrix completion (standard in the bandit literature), but it does not evaluate the realistic scenario where test statistics for newly selected pairs would need to be estimated from limited samples. The paper does not discuss how estimates degrade with fewer replicates. The reported efficiency gains are therefore best understood as upper bounds on practical performance rather than validated operational savings.

2. **The mixture-model assumption for disjointedness (Assumption 3) is restrictive and its biological plausibility is not discussed.** The assumption that perturbations do not affect the mixing weights of the latent mixture model is stated but its limitations are not addressed. In real biological systems, knocking out a gene could well change cell-state proportions (e.g., shifting the mixture weights). While this assumption is presented as a sufficient condition (not a necessary one), the paper would benefit from acknowledging its restrictiveness and discussing when it might and might not hold.

3. **No empirical check of the low-rank assumption.** The regret guarantees of ASD depend on the reward matrix being approximately low-rank. The paper does not analyze the empirical rank or singular-value spectrum of the MMD/KL score matrices. The strong empirical performance suggests the assumption is reasonable, but a simple diagnostic (e.g., PCA of the full matrix) would make the argument self-contained.

4. **No systematic comparison to simpler embedding-based interaction scores.** The related work notes that cosine similarity of single-perturbation embeddings is used in practice to infer gene-gene relationships, and the abstract claims the proposed tests are "complementary" to such approaches. Yet no quantitative comparison is presented. Showing how the proposed tests compare to this natural baseline in recovering known interactions would help calibrate expectations about the additional value of the pairwise-experimental approach.

### Trivial
None.

## Nice-to-Haves

- **Validate the separability test on a larger set of semi-validated interactions.** For example, hold out a fraction of known pairs from the 50-gene set and report AUC or precision-recall for the separability and disjointedness scores. The current evidence is qualitative and would be strengthened by a rigorous discriminative evaluation.

- **Test active learning under realistic noise.** Simulate the sequential setting by drawing batches of *n* replicates from the full data for each selected pair and recomputing the test statistic from that subsample. This would directly address the most important practical question: how many pairwise experiments does ASD save compared to random selection when estimates are noisy?

- **Compare the two test statistics empirically.** The paper presents separability and disjointedness as alternatives but does not compare their empirical behavior — e.g., are they correlated? do they agree on which pairs are interactive? This would be practically informative for users.

- **Include a rank analysis** of the empirical MMD/KL score matrices to validate the low-rank assumption used in the active learning pipeline.

## Removed Points

These points from the reviews were excluded after verification against the paper:

- **Criticism about the diffeomorphism relaxation needing more argument:** The paper provides a remark and a citation (Lemma 5.1.4 of Krantz 2008) for the generalized change-of-variable formula. This is sufficient for a paper of this scope; demanding a full derivation is scope creep.

- **Criticism about the TSC2/MTOR example:** The critic claimed that "MTOR guide 3 vs MTOR guide 2 appears much lower" within same-gene pairs. The paper text explicitly states "strong interaction scores between guides targeting the same gene (e.g. MTOR guide 3 with both MTOR guides 1 and 2)." Without access to the figure, the paper's stated observation directly contradicts the critic's claim, so this point is removed as likely a misreading.

- **Complaints about missing hyperparameters, training details, and appendix content:** The parser strips the appendix; these exist in the original submission. Per hard rules, such criticisms are removed.

- **Reproducibility concerns rooted in doubting that cited resources exist:** Per hard rules, all cited models, tools, benchmarks, and datasets are assumed to exist.

- **Generic "evaluation lacks rigor" / "evidence is weak" framings without concrete anchor:** Removed per the filtering discipline.

- **Strengths about the "importance of the addressed problem" or generic praise:** These are superficial and not specific to the paper's content.

## Novel Insights

A genuinely novel observation emerges from the comparison between the two proposed tests. The separability test (KL-based) and the disjointedness test (MMD-based) capture different failure modes of non-interaction: separability tests whether pairwise experiments provide *any additional information* beyond single perturbations (a strict notion of independence in latent space), while disjointedness tests whether effects compose *additively in observation space* (a weaker, more operational condition). The paper shows empirically that these tests highlight different sets of gene pairs on the 50-gene dataset — the MMD-based test strongly highlights proteasome components (which interact broadly), while the KL-based test highlights specific physical/genetic interactions (BCL2L1-MCL1, BAX-BCL2L1, etc.). This suggests that the two tests capture distinct biological phenomena, which is itself an interesting finding that warrants deeper investigation. The paper notes this only in passing ("the interactions we detected were also complementary to those which would have been discovered using existing cosine similarity-based approaches"); making the complementarity of the two tests themselves a more central analysis would strengthen the paper.

## Suggestions

1. Add a quantitative discriminative evaluation of the separability and disjointedness scores on the 50-gene dataset (e.g., AUC for recovering known interactions from CORUM/StringDB), to move beyond the qualitative pathway-level observations.
2. Include a comparison to cosine-similarity of single-perturbation embeddings as a baseline for interaction score matrices, to substantiate the claim of complementarity.
3. Discuss the biological plausibility of the mixture-model assumption (Assumption 3) and clarify that it is a sufficient condition, not a necessary one.
4. Add a simple rank analysis (e.g., explained variance by top-k SVD components) for the empirical MMD/KL score matrices to support the low-rank assumption used in ASD.
5. Discuss how the test statistic estimates degrade with sample size and what this implies for deploying the active learning pipeline in a truly sequential (non-oracle) setting.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>