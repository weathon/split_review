- Decision: Reject
- Avg Score: 5.20
- Scores: 5, 6, 3, 6, 6
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

KambaAD proposes an encoder-reconstructor framework for time series anomaly detection that integrates Kolmogorov–Arnold Networks (KAN) for coarse-grained filtering, self-attention for global dependencies, and MAMBA for local sequential modeling. The paper evaluates on multiple multivariate benchmarks and reports state-of-the-art F1 scores on SMD, MSL, SMAP, and PSM against 15 baselines.

## Strengths

- **State-of-the-art F1 on four standard benchmarks (SMD, MSL, SMAP, PSM).** The paper reports (Table 1) that KambaAD achieves the highest F1 scores on all four datasets, outperforming 15 baselines including AnomalyTransformer, DCdetector, and ModernTCN. This is the paper's central piece of evidence for its contribution.

- **Window-based KAN input consistently outperforms point-based KAN (Table 3).** Using the entire window as KAN input yields higher precision, recall, and F1 across all eight datasets, with gains of up to ~7 points on SWAN (70.13 vs. 63.16 F1). This supports the claim that cross-temporal dependencies are useful at the KAN stage.

- **Channel-independent (CI) reconstruction consistently beats channel-dependent (CD) (Table 6).** CI yields higher F1 on every dataset (e.g., 91.05 vs. 85.35 on CCard), validating the paper's argument that independent reconstruction avoids cross-feature interference during anomalies.

- **Stepwise visualization shows additive module contributions (Figure 3).** The reconstruction of individual features is shown after KAN, after Attention+MAMBA, and after the Reconstructor, with visible progressive normalization of anomalous features. This provides qualitative support for the design rationale.

- **Novel integration of KAN, attention, and MAMBA in an encoder-reconstructor pipeline.** The paper is the first to combine these three components in a two-stage encoding process for anomaly detection, offering a new architectural approach to the problem.

## Weaknesses

### Fatal
None.

### Major

- **The full model underperforms its own components on 2 of 8 datasets, weakening the core integration claim.** Section 4.3.3 reports that on the Mulva dataset, KambaAD is inferior to using only the Encoder, and on GECCO it is inferior to using only the Reconstructor. The paper speculates this may be due to overfitting from more parameters, but provides no supporting evidence (no training dynamics, no regularization analysis, no failure analysis). If an architecture that claims integration as its main novelty is strictly worse than its own parts on multiple datasets, the central thesis that the combination is reliably beneficial is materially weakened. This is the most consequential weakness in the paper.

- **No efficiency or complexity analysis despite explicit efficiency claims in the abstract and introduction.** The paper states that KAN enables "swift enforcement of data consistency" and "rapid detection," and that patch-based operations "reduce computational complexity." Yet the experiments contain zero runtime measurements, no FLOPs analysis, no parameter count comparison with baselines, and no inference-time benchmarks. Given that the model stacks KAN, multi-head attention, and an SSM (each with non-trivial overhead), these claims are unsubstantiated. This is a significant evidential gap for a paper that advertises efficiency as a key advantage.

- **KAN's specific contribution is not isolated from simpler alternatives.** The paper demonstrates (Table 5) that removing KAN hurts performance, which does show the module's usefulness. However, it does not compare KAN against a simple linear layer or MLP of matched parameter count in the same architectural position. Since KAN is a named contribution (appearing in the title), the claim that KAN specifically — rather than any differentiable function approximator at that position — is beneficial remains unsupported. A controlled ablation replacing KAN with a linear projection or MLP is needed.

### Minor

- **Contradictory statement in the conclusion.** The final sentence reads: "Future work will explore extending KambaAD to multivariate time series." The paper defines the problem in §2 as multivariate (§2: "Consider a multivariate time series with k variables"), evaluates on multivariate datasets (SMAP, MSL, SMD, PSM, NIPS), and uses channel-independent reconstruction designed for multivariate data. This sentence is internally contradictory and suggests a careless error.

- **Section 4.3.4 (Order of Components) asserts a crucial claim without experimental support.** The section states that "the positioning of components within KambaAD is crucial" but provides no permutation ablation or empirical evidence varying the order of KAN, attention, and MAMBA. The tables that follow (Tables 4 and 5) are from the ablation study (4.3.3), not an order analysis. This is a missing experiment for a stated design claim.

- **The KAN module's internal architecture is underspecified.** The function \(F_{\mathrm{KAN}}\) is described only as reshaping, processing, and reshaping back (Section 3.2.1). No details are given on the number of KAN layers, spline order, grid size, or activation functions used inside \(F_{\mathrm{KAN}}\). This hurts reproducibility.

### Trivial
None.

## Nice-to-Haves
- Reporting variance (standard deviations or confidence intervals) across runs would strengthen the evaluation, though point estimates are common in this field.
- A failure analysis explaining why the full model struggles on Mulva and GECCO could turn the weakness into a strength, providing insights about when the architecture is and isn't appropriate.
- Replacing the contradictory future-work sentence with a genuinely forward-looking statement.

## Removed Points
These points were raised by reviewers but removed from the main review for the following reasons:
- **MAMBA discretization detail missing**: The paper presents a simplified SSM formulation without the discretization parameter Δ. This is a common level of abstraction when MAMBA is used as a component; the original MAMBA paper handles discretization. Not a meaningful weakness given the paper's scope.
- **RMSNorm vs. LayerNorm not justified**: A stylistic/preference nitpick. Either choice is standard.
- **CI vs. CD evidence based on only four features from one example**: The claim ignores Table 6, which provides quantitative results across all 8 datasets. The visualization is supplementary.
- **Parameter sensitivity showing fragility**: The paper itself acknowledges cases where performance drops and discusses potential overfitting. This is transparent reporting, not a weakness.
- **Strength finder overclaims about "full-model superiority"**: Claimed the full model achieves best/second-best in every case, but the paper explicitly states it underperforms its components on Mulva and GECCO. Removed as factually inaccurate.
- **Strength finder's "parameter sensitivity demonstrates stability"**: Overstated; the paper acknowledges sensitivity on some datasets.
- **Generic strengths** about problem importance or non-specific praise: Removed per filtering rules.
- **No variance/statistical tests**: Moved to Nice-to-Haves as this is typical practice in the anomaly detection benchmark literature.

## Novel Insights

None beyond the paper's own contributions. The reviewer discussion largely converges on the paper's stated findings and gaps rather than revealing unexpected patterns.

## Suggestions

1. **Perform a controlled KAN-vs-MLP ablation.** Replace \(F_{\mathrm{KAN}}\) with a linear layer (or 2-layer MLP) of matched parameter count and report results on all 8 datasets. This directly tests whether KAN's specific inductive bias (learnable univariate spline functions) provides any benefit over standard alternatives.
2. **Add runtime/FLOPs comparisons.** Report per-window inference time, training time, and total parameter count for KambaAD and at least 3–5 baselines (e.g., AnomalyTransformer, DCdetector, ModernTCN). This is necessary to back the efficiency claims in the abstract.
3. **Acknowledge and analyze the two datasets where the full model underperforms.** Provide a dedicated failure analysis — show training curves, examine whether overfitting is actually occurring, and discuss when the full architecture may not be beneficial. This would strengthen credibility.
4. **Conduct the order permutation experiment.** Vary the sequence of KAN, attention, and MAMBA, measure F1 on at least 4 datasets, and report whether the chosen order is indeed optimal.
5. **Fix the conclusion sentence.** Remove or rephrase the contradictory "future work will extend to multivariate time series."
6. **Specify \(F_{\mathrm{KAN}}\) internals** (number of layers, spline order, grid size) in the methodology section.
