Now I have all the facts I need. Let me compose the final consolidated review.

---

## Summary

This paper proposes Convolutional Signal Propagation (CSP), a non-parametric method for propagating signals on hypergraphs (bipartite graphs). CSP consists of alternating averaging steps over nodes and hyperedges, requires no training or hyperparameter tuning, and can be implemented in a few lines of code. The paper derives formal connections between CSP and Hyper-Conv, label propagation, and binomial Naive Bayes, and evaluates it on classification and retrieval tasks across 8 datasets spanning citation networks, social media, and movie ratings. The core claim is that CSP offers competitive performance with dramatically lower computational cost, making it suitable as a first-choice baseline for hypergraph tasks.

## Strengths

- **Extreme simplicity and computational efficiency**: CSP's asymptotic complexity is O(d(Σ_V+Σ_E)) and the paper's timing results (Table 4) confirm it is orders of magnitude faster than HGCN. The algorithm genuinely requires no training, no GPU, and essentially no tuning — a real practical advantage for practitioners seeking a quick baseline.

- **Theoretical connections to established methods are well-drawn** (Sections 4.3–4.5): The paper formally derives CSP as a special case of Hyper-Conv with identity weight matrices, as a generalization of label propagation with α=1/2 to hypergraphs, and relates its signal-averaging steps to binomial Naive Bayes parameter estimation. These connections are mathematically precise (Equations 6, 9–10) and provide genuine insight into why CSP works without learned parameters.

- **Parameter-free design is a genuine contribution**: Unlike NMF-based methods (which require choosing latent dimension and iteration count) or HGCN (which requires optimizer, architecture, and training epochs), CSP has no learnable parameters and the number of layers can be set to a small fixed value (1–3 suffice in experiments). This makes it a uniquely lightweight option in the hypergraph toolbox.

- **Inductive extension is clearly described** (Section 4.6.3): The decomposition of CSP into a hyperedge-score "training" phase and a per-node "inference" phase provides a principled path to inductive settings, which the paper correctly identifies as future work rather than claiming empirical validation it hasn't performed.

## Weaknesses

### Major

- **The NMF-based baselines (Random Forest, Logistic Regression, HGCN) are evaluated with a fixed, untuned NMF setting (dimension 60, 10 iterations) across all datasets.** The paper acknowledges this (Section 5.4: "Feature extraction using Non-negative Matrix Factorization (NMF) was not fine-tuned for each dataset, potentially impacting the performance of NMF-based baselines"), but the acknowledgment does not fix the problem. The NMF dimension is a critical hyperparameter that directly controls representational capacity, and no evidence is provided that dimension 60 is reasonable across datasets with vastly different structures. By contrast, CSP operates directly on the incidence matrix without any feature extraction step. This creates an apples-to-oranges comparison: we cannot tell whether the NMF-based methods would match or exceed CSP with per-dataset tuning of their NMF representation. Since the paper's central claim that CSP is "competitive" rests on these comparisons, this is a significant weakness.

- **The retrieval task protocol (Section 5.2.2) introduces asymmetric label noise that disadvantages baselines requiring negative examples.** CSP receives only positive training labels and propagates them. For Naive Bayes, logistic regression, and random forest, the authors "randomly sample a set of the same size as the testing set and consider these labels as negative." They acknowledge this "introduces some label noise" but assume "the negative class is dominant, making the noise acceptable." This assumption is not validated, and its impact could vary dramatically across datasets and class frequencies. The experimental protocol itself biases toward CSP in retrieval — the conclusion that CSP is "suited for retrieval" may be correct, but the current evidence is contaminated by this asymmetric design. A fair evaluation would require either a protocol that treats both CSP and baselines symmetrically (e.g., both receive positive-only training with a suitable decision rule) or a validated negative-sampling strategy.

- **The HGCN evaluation is too incomplete to support meaningful comparative conclusions.** Only 5 of 10 folds are evaluated for all datasets, and for the Movies dataset only 4 of 20 classes are considered (Section 5.4). The paper provides no justification that these subsamples are representative, nor does it analyze potential selection bias. Additionally, HGCN uses a single-layer architecture with 15,000 epochs of Adam at default settings — no architecture search, early stopping, or hyperparameter tuning. This does not represent what a modern hypergraph neural network can achieve with reasonable effort, so the paper's conclusion that HGCN "shows potential" is not supported by the evidence presented. If HGCN is included as a comparison point, it should be tuned with the same diligence practitioners would apply.

### Minor

- **No measures of variance or statistical significance are reported.** All results in Tables 2 and 3 are point estimates (averages over folds and classes) with no standard deviations, confidence intervals, or significance tests. Given that 10-fold cross-validation is used, reporting fold-level variance is straightforward and would let readers assess whether observed differences (e.g., CSP 0.73 vs. Naive Bayes 0.72 on Cora classification) are meaningful or due to random variation. The informal "within 0.05" threshold for flagging comparable methods is arbitrary and not statistically grounded.

- **The timing comparison (Table 4) excludes NMF preprocessing time for NMF-based methods.** The paper states NMF "was excluded from the execution time" because it is a preprocessing step. However, for a fair assessment of total pipeline cost — which is directly relevant to the claim that CSP is an "efficient baseline" — the NMF time should be reported alongside the method runtimes. Without it, CSP appears artificially more efficient relative to NMF-based pipelines. (The paper does acknowledge this omission in the text, which is good practice, but the table itself remains misleading.)

- **The oversmoothing explanation for CSP's degradation with more layers (Section 5.4) is asserted without supporting analysis.** The paper states "multiple layers may contribute to oversmoothing of the signal" but provides no evidence — e.g., measuring how node representations evolve across layers, or comparing to label propagation's known behavior. This is a plausible hypothesis but remains unsubstantiated.

### Trivial

- The phrase "leave-one-out cross-validation with 10 folds" (Section 5.2.1) is an imprecise description of what appears to be standard 10-fold cross-validation.

- The claim in the abstract about achieving "good results in tasks typically not associated with hypergraphs, such as natural language processing" (referring to the Corona tweets dataset) is not developed further — no NLP-specific baselines are compared. This is a minor over-claim.

## Nice-to-Haves

- A grid search over NMF dimensions (e.g., 10, 50, 100, 200) on a held-out validation fold for each dataset would substantially strengthen the claim that CSP is competitive with feature-based methods.
- For the retrieval task, designing a protocol that treats CSP and baselines equally — either by providing both with positive-only training and a suitable decision rule, or by developing a principled negative-sampling strategy — would remove the current asymmetry.
- Adding standard deviations to all result tables (across folds) and, where possible, a paired significance test across datasets would ground the comparative claims.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Missing related work — Zhou et al. (2006) regularization framework":** REMOVED (factually wrong). The paper explicitly cites Zhou et al. (2006) in Section 3 (line 33) and lists the full reference. The critic did not see it.
- **"PubMed dataset with 90.4% isolated nodes weakens the evaluation":** REMOVED (misunderstands paper's intent). The paper includes PubMed precisely to show a failure case where all methods perform near-randomly due to structural sparsity. This is a valid data point, not a weakness.
- **"Inductive settings section defers evaluation":** REMOVED (critic acknowledges this is reasonable).
- **"Abstract NLP claim not developed":** REMOVED (scope creep — the paper is a hypergraph baseline paper, not an NLP paper; the Corona dataset is included to demonstrate hypergraph applicability to non-traditional domains).
- **"Oversmoothing claim not supported" kept as Minor** — but note the critic's framing of this as a major issue is inflated; it is a plausible interpretation that the paper could support with minimal additional analysis.
- **Strength from Strength Finder ("Competitive performance on retrieval tasks"):** REMOVED (conflicts with verified weakness about asymmetric retrieval protocol; the weakness wins).

## Novel Insights

None beyond the paper's own contributions. The reviews surface genuine methodological concerns about evaluation design (confounded comparison protocols, untuned baselines, missing variance) but do not introduce novel perspectives that fundamentally reframe or deepen the paper's contributions. The main insight from the reviews is that the paper's core algorithmic contribution (CSP) is sound and well-motivated, but the evaluation infrastructure needed to support the "competitive baseline" claim requires substantial reworking.

## Suggestions

1. **Fix the retrieval protocol.** Provide both CSP and baselines with the same training signal — either positive-only training with a suitable scoring mechanism, or a principled negative-sampling strategy with validated noise levels across datasets.
2. **Tune the NMF baselines.** At minimum, perform a grid search over NMF dimensions on a validation fold and report the best configuration per dataset. If CSP still matches or outperforms under those conditions, the claim is much stronger.
3. **Report standard deviations** for all averaged metrics across folds.
4. **Either tune HGCN properly (architecture search, early stopping) or drop it as a comparison point.** The current half-evaluated HGCN with suboptimal defaults does not meaningfully inform the reader.
5. **Include NMF preprocessing time** in the timing table, or add a footnote giving the approximate overhead per dataset.

## Score and Decision

The paper has a genuinely useful core idea: CSP is simple, fast, interpretable, and parameter-free. The theoretical connections are well-executed. However, the experimental evaluation — which is the primary evidence for the central claim that CSP is "competitive" — has significant confounds that prevent the reader from drawing reliable conclusions about comparative performance. The NMF baselines are untuned, the retrieval protocol is asymmetric, and the HGCN evaluation is incomplete. These issues are fixable, but they currently undermine the paper's main thesis.

**Score:** 5.5  
**Decision:** Reject

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>