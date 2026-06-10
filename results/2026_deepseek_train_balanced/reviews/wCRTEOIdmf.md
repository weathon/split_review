## Summary

This paper proposes using graph kernels (WL-based kernels and their variants) for subgraph isomorphism counting, framing it as a regression problem where Gram matrix entries between patterns and data graphs are used to predict subgraph counts. The main technical contribution is the Neighborhood-Information-Extraction (NIE) modification, which adds pairwise edge colors to the WL color histogram. The paper reports experiments on 6 datasets showing that the 3-WL kernel with RBF and NIE achieves dramatically lower RMSE than neural baselines on homogeneous datasets (IMDB-BINARY, IMDB-MULTI).

## Strengths

- **Clean decomposition of the NIE-WL kernel.** The paper shows mathematically (Eq. 8, lines 324–328) that the NIE-WL kernel decomposes into \(k_{\text{WL}} + k_{\text{NIE}}\), making the addition of edge-color information modular and interpretable. The modification itself (Algorithm 1, highlighted line) is clearly specified.

- **Strong empirical results on homogeneous datasets.** Table 1 shows 3-WL+RBF+NIE achieving RMSE 757.7 on IMDB-BINARY and 833.0 on IMDB-MULTI, compared to the best neural baseline (CNN, RMSE 4808.2 and 4185.1 respectively). The paper honestly notes where NIE provides no benefit (synthetic graphs, lines 623–625) and where neural methods still dominate (ENZYMES, NCI109, line 634).

- **Practical implementation insight for Gram matrix construction.** The paper identifies (lines 518–520) that the D×D data submatrix is pattern-independent, enabling a single (Q+D)×(Q+D) matrix to be built once and sliced, instead of Q separate constructions.

- **Systematic comparison of regressors and kernel tricks.** Section 5.1 compares SVM vs. Ridge regression with justification for Ridge; Section 5.2 documents polynomial kernel overflow issues, providing practical guidance.

## Weaknesses

### Fatal
None.

### Major

- **Underspecified evaluation protocol.** The paper never describes how train/test splits are performed. Section 4.2.2 describes constructing a (Q+D)×(Q+D) Gram matrix "only once" (line 520), which if test graphs are included is a transductive setting. The neural baselines (CNN, LSTM, RGIN, etc.) are inductive models that receive no test-graph information during training. Without knowing the evaluation protocol, the comparison to neural baselines and the central quantitative claims are uninterpretable. The paper also does not specify whether the neural baseline numbers (lines 580–585) are re-implemented or cited from Liu et al. (2020), nor whether the pattern sets and filtering criteria match.

- **Dramatic NIE improvements lack sufficient analysis.** The NIE modification adds edge colors to the WL histogram without changing the WL algorithm's expressive power (acknowledged line 319). On IMDB-BINARY, 3-WL+RBF+NIE achieves RMSE 757.7 vs. 89,532.7 for 3-WL+RBF (a ~118× improvement). On synthetic datasets (Erdos-Renyi, Regular), NIE produces *identical* numbers. The paper's explanation (line 624: "uniform distribution of neighborhoods results in uniform distributions of edge colors") does not account for why a representation-equivalent modification produces such massive swings on some datasets but none on others. The possibility of a confound (e.g., how the Gram matrix interacts with Ridge regression on imbalanced counts, or how pattern-graph kernel values behave differently with edge colors) is not investigated. Ablations with random edge labels or controlled synthetic experiments that disentangle the effect would be needed to trust that the improvement is structural.

### Minor

- **No variance or uncertainty quantification.** Every result in Table 1 is a single point estimate with no standard deviations, confidence intervals, or information about the number of runs/splits. Given the dramatic performance swings across kernel variants, this makes it impossible to assess whether rankings are stable or driven by noise.

- **Missing experimental details.** Key hyperparameters are not reported: number of WL iterations \(T\), RBF width \(\sigma\), and Ridge regularization strength. Dataset statistics (number of graphs, average graph size, number of patterns \(Q\) after filtering) are absent. These omissions hinder reproducibility.

- **Limited theoretical grounding for the approach.** The paper asserts (lines 29, 299–300) that kernel values "implicitly" capture substructure information relevant to subgraph counts, but provides no formal argument, intuition, or analysis for when or why global WL histogram similarity should correlate with local subgraph counts. This is acceptable for an empirical exploration, but the paper's strong claims (e.g., "state-of-the-art performance," line 631) would benefit from at least a characterization of the failure modes.

- **Thin technical novelty.** The NIE modification is a straightforward addition of edge colors to the histogram, and the kernel tricks are textbook material applied without modification. The primary contribution is the *application* of graph kernels to subgraph counting, but the evaluation gaps limit its impact.

### Trivial
None.

## Nice-to-Haves

- **Runtime comparison** between kernel methods and neural baselines would strengthen the practical motivation (graph kernels are motivated as efficient, but no timing data is provided).
- **Pattern-level analysis** (which patterns are easy/hard for kernel methods) would deepen understanding.
- **Transductive vs. inductive clarification** should be resolved (this is a Major weakness; the "nice-to-have" here is that if the protocol is properly inductive, a description of out-of-sample kernel computation would suffice).

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Incomparable color histogram dimensions between pattern and graph"** (from Harsh Critic, Issue 1). Removed: WL kernels compare graphs of different sizes naturally via shared color-space histograms; this is standard kernel methodology and not a problem.
- **"Polynomial kernel absent from main results table"** (from Harsh Critic, "Missing Parts"). Removed: the paper discusses polynomial kernel issues in Section 5.2 and explains it causes overflow—this is a documented negative result, not a missing experiment.
- **"OOM treated as zero distorts comparison"** (from Harsh Critic, Section-by-Section Notes). Removed: this concerns a visualization figure caption; the main Table 1 correctly marks OOM entries as "OOM."
- **"No proof that edge histogram reveals subgraph counts"** (echoed across multiple inputs). Partially removed from Weaknesses: retained as a Minor concern about missing theoretical grounding, not as a fatal flaw, since the paper is empirical.
- Several strengths from Strength Finder that were generic ("addressed an important problem") or sycophantic were dropped.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an insight about the method or results that the paper itself does not already state or imply.

## Suggestions

1. **Clarify the train/test protocol immediately.** State explicitly whether the setup is transductive or inductive. If the latter, describe how out-of-sample kernel values are computed for test graphs (requires kernel computation between each test graph and all training graphs + all patterns). If transductive, explain why this is appropriate and add a caveat to the comparison with inductive neural baselines.
2. **Investigate the NIE effect systematically.** Run ablations with randomized edge labels to distinguish structural from numerical confounds. Report whether the improvement persists across multiple random splits. Show the distribution of Gram matrix entries with and without NIE to understand why the Ridge regression benefits so dramatically.
3. **Add variance estimates.** Report mean ± std over multiple train/test splits (or cross-validation folds) for the key configurations.
4. **Report all hyperparameters** (T, σ, Ridge α) and dataset statistics (|D|, |V| avg, |E| avg, |Q|, label distribution).
5. **Provide the source of neural baseline numbers** and confirm experimental conditions (pattern set, filtering, split) are matched.

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>