## Summary

This paper proposes Self-Matrix Factorization (SMF), a non-negative matrix factorization approach augmented with a self-expressive regularization term that encourages the learned embedding matrix \(W\) to capture linear manifold structure from the association data \(X\). The key idea is to add a second loss term \(\|X - [T\circ(WW^\top)]X\|_F^2\) that reconstructs each row of \(X\) as a linear combination of other rows, with coefficients determined by the dot products of the embeddings. This couples embedding learning with simultaneous discovery of object similarities, without requiring any side information. SMF is evaluated on three datasets (MovieLens, Drug-SE, ModCloth) for both missing-association prediction (RMSE, precision@K) and unsupervised embedding quality (intra- vs. inter-class cosine similarity separation using held-out attributes like movie genres and drug ATC levels).

---

## Strengths

- **Novel and well-motivated integration of self-expressive constraint into NMF.** The loss design (Equation 2) is principled: the first term performs standard low-rank factorization, while the second term forces \(WW^\top\) to encode the linear manifold structure implicit in the rows of \(X\). The paper explains this clearly with the geometric illustration in Figure 1 and a concrete mathematical derivation (Equations 2–5). This is a genuine extension beyond vanilla NMF and offers a clean way to constrain embeddings without external similarity matrices.

- **Consistent and strong empirical evidence that SMF embeddings encode held-out object attributes.** The embedding analysis (Section 4.2, Figures 3b–d) evaluates whether objects belonging to the same category (movie genres, drug ATC levels, clothing types) have more similar embeddings than cross-category pairs — using a Z-score separation metric. Across all three datasets and all attribute groupings, SMF achieves higher Z-scores than NMF and HCCF, and attains statistical significance in ~99% of runs vs. 41% for NMF and 87% for HCCF. This is the paper's strongest evidence because these attributes were *never* provided during training.

- **Competitive predictive accuracy with good robustness properties.** SMF achieves lower RMSE than NMF and SLIM across all three datasets (e.g., 15% lower than NMF on ModCloth, at least 65% lower than SLIM overall). In precision@K, SMF outperforms all baselines in 7 of 10 settings. The paper also demonstrates that SMF is stable across a wide range of \(k\), \(\lambda_1\), and \(\lambda_2\) values, with \(\lambda_{se}=1\) fixed across all experiments, suggesting the method does not require expensive per-dataset tuning.

- **Principled handling of unknown associations via weighted loss.** The matrix \(P\) with zero-weighting factor \(\alpha\) (Equation 5) correctly distinguishes between zeros representing unknown associations vs. true negative signals. The paper discusses how \(\alpha\) controls the RMSE vs. ranking-metric trade-off, which is a practical design choice grounded in prior work.

---

## Weaknesses

### Fatal

None.

### Major

- **No description of how baseline hyperparameters (NMF, SLIM, HCCF) were selected.** The paper carefully discusses SMF's own hyperparameter sensitivity (lines 130–132), including a validation-set analysis on MovieLens, but provides zero information about how the hyperparameters for NMF (elastic-net weights), SLIM (regularization, which is known to be highly sensitive), and HCCF were tuned. Were they optimized with the same validation splits? With a comparable budget? With a grid search? Without this information, the reported performance gaps (especially the "at least 65% lower RMSE than SLIM" claim) could partially reflect suboptimal baseline configuration rather than algorithmic superiority. **This is the most consequential weakness in the paper** — the central experimental comparisons lack the transparency needed to trust the reported margins.

- **No ablation study isolating the self-expressive term.** The paper never reports results for \(\lambda_{se}=0\) (i.e., SMF without the self-expressive term, reducing to elastic-net NMF). Such an ablation would directly measure the contribution of the paper's core innovation. The current experimental design compares SMF against a *separate* NMF implementation, but even the same NMF with different initialization or optimizer settings can yield different results. An internal ablation is the cleanest way to isolate the effect of the self-expressive term and is standard practice for papers proposing a new regularizer.

### Minor

- **AUROC and AUPRC mentioned but never reported.** Line 125 states these metrics "are also useful," and line 132 references AUPRC in the hyperparameter discussion, yet no actual AUROC or AUPRC results appear anywhere in the paper. The conclusion (line 154) argues that precision@K is "more relevant," but the reader is left wondering whether SMF would also excel on these widely used ranking metrics — or whether the omission masks a weakness. At minimum, the paper should report these or explicitly explain why they are not applicable.

- **Embedding evaluation, while meaningful, tests a property closely aligned with the method's objective.** The self-expressive term directly encourages \(WW^\top\) entries to be large for objects on the same linear manifold. The Z-score analysis then checks whether cosine similarities of \(W\) rows separate by held-out attributes. This is a valid test, and the results are genuinely informative (SMF consistently outperforms baselines). However, the paper overstates the novelty of this finding by calling it evidence of attributes "that were not part of the learning process" — in reality, the self-expressive loss *does* learn to structure \(WW^\top\) by data-driven manifolds that happen to correlate with these attributes. A stronger test would be a supervised attribute prediction task (e.g., train a classifier on the embeddings to predict held-out movie genres), which would demonstrate that the embeddings *generalize* these attributes to unseen objects. The current setup is closer to a sanity check than a demonstration of emergent semantic understanding.

- **No runtime analysis or scalability discussion.** The paper states \(O(n^2 m)\) per-iteration complexity (line 88), and a back-of-the-envelope calculation for ModCloth (n=5,419, m=32,089) yields ~\(9.4\times10^{11}\) operations per iteration. No actual wall-clock times, number of iterations to convergence, or discussion of practical feasibility are reported. The paper mentions "details about computational time and number of iterations" in the same sentence, but these details appear to have been stripped (parser artifact). Without this information, a practitioner cannot judge whether SMF is practical for datasets of moderate size.

- **No convergence analysis for the multiplicative updates.** The update rules are presented without any derivation or convergence guarantee. While borrowing from NMF's standard majorization-minimization framework is plausible, the paper should at minimum state the optimization strategy (e.g., auxiliary function approach) or reference the relevant convergence theory.

- **Actual \(\alpha\) values used in experiments are not reported.** The paper discusses the \(\alpha\) trade-off qualitatively but never states the specific \(\alpha\) values used for each dataset and task. Since the sensitivity analysis is only shown for MovieLens, and the paper acknowledges \(\alpha\) depends on the task, the reader cannot reproduce the results.

### Trivial

- The update rule in Equation 6 (line 81) contains garbled notation ("\(W W W^{\prime}\)") and mismatched parentheses — likely a PDF-parser artifact, but should be corrected in the original source.

---

## Nice-to-Haves

- **Visualization of the learned \(WW^\top\) similarity matrix.** Inspecting whether \(WW^\top\) exhibits block-diagonal structure aligned with ground-truth attribute groups would strengthen the interpretability claims.
- **Held-out attribute prediction experiment.** Training a simple classifier (e.g., logistic regression) on the embeddings to predict held-out attributes (e.g., movie genres) would provide a more direct and convincing test of attribute encoding.
- **Scalability experiment on a larger dataset** (e.g., ML-20M) or a discussion of approximations (e.g., stochastic row sampling for the self-expressive term) to address the \(O(n^2 m)\) complexity.
- **ModCloth precision@K results** with an alternative metric (e.g., recall@K, NDCG) that may be more informative for extremely sparse matrices.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **Harsh Critic's Point 1 (overclaimed novelty due to missing prior work on self-expressive NMF).** The critic cites Lu et al. (2018, *IEEE TNNLS*) and Peng et al. (2019, *Pattern Recognition*) as prior self-expressive NMF methods not acknowledged by the paper. Per the evaluation guidelines, missing-related-work criticisms cannot be independently verified and are removed. The paper's novelty claims ("first to explore this idea in a matrix factorization model," "first method to integrate these two processes") should still be tempered by the authors in revision to reflect the possibility of related formulations, but this specific criticism is excluded here.

2. **Strength Finder's Point 6 (interpretable non-negative representations).** This is a generic property of any NMF method, not a distinct strength of SMF. Moved here to avoid over-claiming.

3. **Harsh Critic's formatting/typo complaints about Equation 6** (e.g., "closing bracket placement makes it unreadable"). These are PDF-parser artifacts, not author errors. Removed per guidelines.

4. **Criticism that HCCF outperforms SMF at top-10/top-20 for Drug-SE.** The paper explicitly acknowledges this (line 123: "HCCF achieves a better precision at the top 10 and top 20 for the Drug-SE dataset"). The critic's concern is already addressed by the authors; including it as a weakness would be redundant.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface a useful tension: the paper's embedding evaluation is simultaneously its strongest evidence *and* a potential overclaim, because the self-expressive term explicitly structures \(WW^\top\), making the observed separation partially a product of the method's design rather than emergent semantic encoding. This tension is common in self-supervised representation learning papers and could be resolved with a held-out prediction task. Otherwise, no review-level insight emerges that meaningfully reframes the paper's contribution.

---

## Suggestions

1. **Report baseline hyperparameter tuning in full.** Describe the search grid, validation procedure, and final selected parameters for NMF, SLIM, and HCCF — with the same level of detail given to SMF's own hyperparameters. If a consistent cross-validation protocol was used, stating so explicitly would largely address this concern.

2. **Add an ablation with \(\lambda_{se}=0\).** This is the single most cost-effective experiment to strengthen the paper: it isolates the contribution of the self-expressive term within the same codebase, optimizer, and initialization scheme.

3. **Report AUROC and AUPRC results** in a table or supplementary figure, or explicitly justify their omission with empirical evidence (e.g., show that precision@K subsumes these metrics for the target use case).

4. **Report actual \(\alpha\) values** used for each dataset and each task (RMSE vs. ranking), and show runtime in seconds with iteration counts for all datasets.

5. **Temper the novelty claims.** Phrases like "the first to explore this idea" and "the first method to integrate these two processes" are difficult to verify absolutely and may be challenged by reviewers familiar with the subspace-clustering literature. Replace with more precise framing: e.g., "to the best of our knowledge, no prior NMF formulation jointly learns embeddings and a self-expressive similarity matrix in a single loss with multiplicative updates."

---

## Score and Decision

The paper proposes a clean, well-motivated extension to NMF with a self-expressive regularization term. The embedding analysis provides compelling evidence that SMF yields representations that better separate objects by held-out attributes than strong baselines (NMF, HCCF). The method is also competitive on predictive tasks. However, the paper has two significant weaknesses that prevent full confidence in the results: (1) the experimental comparisons lack transparency about baseline hyperparameter tuning, and (2) the core contribution is not isolated via an ablation study. These are addressable in revision but undermine the central experimental claims as presented. The paper would benefit from a more rigorous evaluation protocol before it is ready for publication.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>