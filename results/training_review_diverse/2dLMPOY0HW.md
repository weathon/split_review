Now I have a thorough understanding of the paper and all the reviewer claims. Let me write the final consolidated review.

---

## Summary

This paper studies when MLP-based methods can match GNNs on node classification from an information-theoretic perspective. It introduces a tractable bound on the conditional entropy H(A|X) to quantify how much graph structure is already captured in node features, finding qualitative alignment with empirical MLP-GNN performance gaps. Building on this analysis, the paper proposes InfoMLP, a method that first constructs a graph-augmented feature matrix via graph diffusion (minimizing H(A|X_aug)) and then maximizes mutual information between node embeddings from original features and those from augmented features. InfoMLP achieves MLP-level efficiency during training and testing, and demonstrates strong empirical results across transductive, inductive, and cold-start settings.

## Strengths

1. **Novel information-theoretic framing of MLP-GNN performance gaps.** The paper introduces a tractable upper bound for H(A|X) (Theorem 1) and derives a closed-form expression for the gap between H(A|X) and H(A|Â) (Theorem 2). This provides a principled framework to quantify how much graph structure information is already encoded in node features, going beyond the purely empirical observations in prior work. The qualitative alignment in Figure 2 between entropy estimates and observed performance (e.g., CS with low H(A|Â) matches good MLP performance; Computer with high H(A|Â) shows persistent GNN advantage) is compelling.

2. **Efficient design preserving MLP-level complexity.** InfoMLP's two-step decomposition — a non-parametric preprocessing step (graph diffusion; O(KEd)) and a training-time MI loss (O(ND²), matching a linear layer) — means the method has the same training and testing complexity as a vanilla MLP (Section 3.3, Table 1). This is a genuine advantage over distillation-based methods like GLNN that require message passing during training.

3. **Strong empirical results across diverse settings.** In the transductive setting (Table 3), InfoMLP outperforms all previous MLP-based models on all seven datasets and beats GNNs on six out of seven. In the challenging cold-start setting (Table 4), it achieves the best accuracy on every dataset with notable margins (e.g., +5.4% on Pubmed). These results demonstrate that the design translates into practical gains.

4. **Insightful experimental design covering three realistic scenarios.** The paper evaluates in transductive, inductive, and cold-start settings (Section 4.1). The cold-start setting is under-explored in prior work, and InfoMLP's consistent superiority there highlights a practical advantage when graph structure is unavailable at inference.

5. **Practical connection between feature dimensionality and structure information.** The observation that datasets with higher feature dimensionality relative to graph size (CS with 6,800 features vs. Computer with ~700) capture more structure information in node features (Section 3.2) provides concrete guidance for practitioners.

## Weaknesses

### Fatal
None.

### Major

1. **Disconnect between the claimed objective and the actual optimization.** The paper repeatedly states that InfoMLP maximizes I(Z_mlp; A) — the mutual information between node embeddings and the adjacency matrix. The actual implementation is: (Step 1) construct X_aug by minimizing H(A|X_aug), and (Step 2) maximize I(Z_mlp; X_aug) (then a lower bound I(Z_mlp; Z_aug)). The paper never establishes a theoretical link between maximizing I(Z_mlp; X_aug) and maximizing I(Z_mlp; A). Since Z_mlp = MLP(X) depends only on X, and X_aug = g(X, A) depends on both X and A, there is no direct data-processing inequality that connects the two quantities. Z_mlp could capture only the X-part of X_aug's information while missing the A-specific part, yielding high I(Z_mlp; X_aug) but low I(Z_mlp; A). The paper asserts rather than demonstrates that the two-step procedure maximizes I(Z_mlp; A). This undermines the internal coherence between the paper's motivating principle and its method. (See Section 3.3, lines 121–141.)

### Minor

2. **The analysis conflates I(X;A) with the task-relevant quantity I(Y;A|X).** Section 3.1 correctly notes that MLPs fail when graph structure carries information not present in features. However, the quantity that determines the performance gap is the *conditional* mutual information between labels and structure given features: I(Y;A|X). Two datasets with the same I(X;A) can have very different I(Y;A|X) if the feature–structure overlap is either task-relevant or noise. The paper treats I(X;A) as the key determinant (e.g., the claim that "the performance gap between MLPs and GNNs is constrained by I(X,A)" in line 114) but never measures or discusses I(Y;A|X). The qualitative alignment in Figure 2 is suggestive but does not isolate the correct causal quantity.

3. **Entropy estimation uses unvalidated assumptions.** The estimation of H(A|X) via H(A|Â) (Section 3.2) assumes: (a) the L2 distances of positive and negative edges follow Gaussian distributions; (b) all edges are independent conditional on Â; (c) the L2 distance is an adequate f(X) for the upper bound. No goodness-of-fit tests, comparisons to alternative estimators, or robustness checks are provided. The numerical entropy values are also not reported — the analysis is purely qualitative via density plots. While this does not invalidate the method (which does not depend on these estimates), it weakens the theoretical contribution.

4. **Hyperparameter selection for K is ambiguously described.** Line 133 states K can be selected "without training the model" (by minimizing H(A|X_aug(K))) while also saying it "can be selected by evaluating the performance on the validation set." These are different criteria and the paper does not specify which is actually used, nor whether they yield the same K. The hyperparameters α and β in the MI loss (Eq. 7) are not analyzed for sensitivity; the paper does not describe how they were tuned across datasets.

5. **The MI estimator's validity as a mutual information bound is not justified.** Equation 7 presents a feature-decorrelation loss (L2 alignment + covariance regularization) referenced with a garbled citation. The paper cites well-known MI estimators (Belghazi et al., 2018; van den Oord et al., 2018) but then uses a different form. Why this particular loss is a valid lower bound on I(Z_mlp; Z_aug) — and what assumptions it relies on — is not explained, making the information-theoretic claim of the loss function unverifiable.

### Trivial

- The numerical H(A|Â) values are not reported alongside the density plots in Figure 2, making the categorization into small/medium/large entropy purely qualitative.
- The phrase "non-parametric" (line 133) is slightly misleading since K is a hyperparameter requiring selection.
- The garbled citation "(Zhang et al.3)" in Eq. 7 is a formatting artifact that should be corrected.

## Nice-to-Haves

- A controlled comparison on cold-start: the paper could explicitly isolate whether InfoMLP's advantage comes from its MI objective or simply from being an MLP (by comparing against a tuned vanilla MLP baseline more prominently in Table 4).
- A sensitivity analysis for α, β, and K to show that results are not overly dependent on careful tuning.
- Runtime or wall-clock comparisons against vanilla MLP, GCN, and GraphMLP to substantiate the efficiency claims.
- Computing I(Y;A|X) (which can be estimated from labeled data via a trained classifier) to more directly connect the entropy analysis to observed performance gaps.

## Removed Points

- **"Missing appendix / ablation studies / large-scale results / heterophilic results"** — Removed: the parser strips appendix sections from all papers; these exist in the original submission.
- **"Reproducibility statement not evaluable"** — Removed: the reproducibility statement section is present (Section 6) but appears empty due to PDF extraction; this is a parser artifact.
- **"Missing standard deviations for GNNs in tables"** — Removed: the tables are images and the paper states "we report the mean accuracy with standard deviation over 20 random trials" (line 176); whether standard deviations were stripped in extraction cannot be verified.
- **"The DPI argument about Markov chain Z_mlp → X_aug → A"** — Removed: the paper never makes this explicit Markov chain claim; the critic constructed a potential (failed) argument that the paper does not actually make.
- **"The MI estimator reference is garbled"** — Removed: this is a PDF extraction artifact, not an author error. The concern about lack of justification for the MI estimator is kept in Minor weaknesses.
- **Various generic strengths from Strength Finder** (e.g., "addresses an important problem") — Removed for lacking specific, verifiable content.

## Novel Insights

The most interesting insight from the reviews is that the paper's approach could be significantly strengthened by **repositioning** it. Rather than claiming InfoMLP directly maximizes I(Z_mlp; A) — a claim not supported by the optimization — the authors could present InfoMLP as a two-view representation learning method that aligns original-feature embeddings with graph-augmented feature embeddings, with the information-theoretic analysis serving purely as *interpretation* and *motivation* rather than *derivation*. This would sidestep the theoretical gap while preserving all empirical contributions. The core novel insight — that the success of MLP methods on graphs correlates with H(A|X), and can be operationalized via graph-augmented feature alignment — remains valuable regardless of the theoretical framing.

## Suggestions

1. **Address the theoretical gap directly**: Either (a) reformulate the objective and claims to match what is actually optimized (I(Z_mlp; X_aug) rather than I(Z_mlp; A)), using the information-theoretic analysis only as interpretation; or (b) provide a theorem establishing conditions under which maximizing I(Z_mlp; X_aug) implies maximizing I(Z_mlp; A).

2. **Strengthen the entropy analysis**: Report numerical H(A|Â) values, validate the Gaussian assumptions (e.g., Kolmogorov–Smirnov tests), and ideally compute the correlation with I(Y;A|X) for a more direct link to performance gaps.

3. **Clarify hyperparameter selection**: Specify whether K is chosen via H(A|X_aug(K)), validation accuracy, or both, and add a sensitivity analysis for α and β.

4. **Justify the MI estimator**: Explain why Eq. 7 is a valid lower bound on I(Z_mlp; Z_aug) and under what assumptions, with a proper citation.

## Score and Decision

The paper makes a genuine contribution: it offers a novel information-theoretic lens for understanding when MLPs work on graphs, and introduces an efficient method (InfoMLP) with strong empirical results across diverse settings. The weaknesses are real but not fatal — the most significant issue (the disconnect between the claimed objective and the actual optimization) can be addressed by recalibrating the theoretical claims or adding a proper justification. The empirical findings stand on their own merit. I recommend acceptance with the expectation that the theoretical framing is revised to match what the method actually does.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>