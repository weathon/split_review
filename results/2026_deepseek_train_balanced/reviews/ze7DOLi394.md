## Summary

This paper introduces the interaction tensor, a tool for jointly analyzing how features (operationalized via PCA on last-layer activations) are distributed across models and data points in deep ensembles. Using this tool, the authors make four empirical observations about feature distributions on CIFAR-10 (heavy-tailed frequency, high-confidence data having fewer features, positive correlation between feature frequency and model adoption, shared features correlating with shared errors). Based on these observations, they propose a combinatorial framework with two feature types (dominant and rare) and derive closed-form expressions for expected accuracy and agreement, arguing the framework explains Generalization Disagreement Equality (GDE). Predictive power is demonstrated through class-merging and blue-intensity partition experiments.

## Strengths

1. **Novel empirical tool (interaction tensor)** — The paper operationalizes the tripartite relationship between models, data, and features (Section 3), going beyond prior pairwise comparison approaches. The tensor $\mathbf{\Omega} \in \{0,1\}^{M \times N \times T}$ simultaneously captures which features are present in which models and data points, enabling joint analysis not possible with prior methods.

2. **Empirical observations that challenge the prevailing multi-view model** — Observation O.2 (Section 4, Figure 3a) shows that high-confidence data points have *fewer* features and low-confidence data points have more, directly contradicting the multi-view data model of Allen-Zhu & Li (2020) where multi-view (feature-rich) data should be classified correctly by all ensemble members. This provides concrete empirical motivation for an alternative framework.

3. **Closed-form analytical derivation of accuracy and agreement** — Propositions 1 and 2 (Eqns. 4–5) derive exact combinatorial formulas for expected accuracy and agreement under the proposed framework without assuming calibration. Prior explanations of GDE (Jiang et al., 2022) required assuming calibration; the paper derives GDE from first principles of feature distribution properties.

4. **Demonstrated predictive power through intervention experiments** — Section 6 shows two a priori predictions (class merging does not break GDE; re-partitioning by blue intensity does break GDE) confirmed in Table 1. The blue-partition experiment provides the first non-adversarial construction of natural data distributions where a deep ensemble is not well-calibrated in-distribution (line 323), a genuinely novel finding.

5. **Feature frequency dynamics over training** — Figure 1a tracks feature distribution evolution during training, showing that untrained models have higher tail-feature frequency and the distribution stabilizes after a single epoch — a novel empirical finding that supports the claim that the observed feature structure is a product of learning, not an artifact.

## Weaknesses

### Major

1. **Quantitative gap between the theoretical framework and empirical measurements** — The closed-form expressions (Eqns. 4–5) involve six parameters ($p_d, c, t_d, t_r, n_d, n_r$) plus the agreement function $\zeta$, yet these parameters are never estimated from the interaction tensor data to produce *quantitative* predictions of accuracy and agreement. Section 6 validates only the *qualitative direction* of predictions (GDE holds/breaks). A model with this many free parameters could reproduce a wide range of accuracy-agreement relationships; without demonstrating that the parameter values implied by real data yield the observed quantitative values, it is unclear whether the framework explains GDE or merely redescribes it in combinatorial language. The paper needs to fit the model to data and compare predicted vs. observed values.

2. **No sensitivity analysis for the interaction tensor construction** — The tensor construction depends on three unvaried hyperparameters: $k=50$ PCA components, $\gamma_{\text{corr}}$ (90th percentile of pairwise correlations), and $\gamma_{\text{data}}$ (90th percentile of projection values). The paper states these choices are "sufficient" (line 105) but presents no systematic variation showing that Observations O.1–O.4 are robust across a meaningful range of thresholds. If changing these thresholds qualitatively alters the observations, the empirical motivation for the theoretical framework collapses.

3. **Binary-classification theory tested on a 10-class problem without a bridging argument** — The combinatorial framework is explicitly derived for binary classification (Section 5, line 193), with closed-form expressions depending on the 50% random-guess baseline and binary class-conditional structure. All experiments use CIFAR-10 (10 classes). The class-merging experiment reduces to 2 superclasses in one condition, which partially addresses this, but the blue-partition experiment (Table 1, groups $G_1$–$G_5$) remains on 10 classes without any argument that the binary expressions apply. The paper references a discussion (likely in the stripped appendix) at line 216, but a principled bridging argument is absent from the main text.

### Minor

4. **No error bars or confidence intervals on empirical results** — Table 1 reports accuracy, agreement, and differences as single values with no variance estimates across random seeds. For a study that interprets differences as small as 0.02–0.03 (between merging conditions and G$_4$–G$_5$), statistical grounding is important. Figure 3 likewise lacks error bars.

5. **ℓ∞-normalization before thresholding could systematically bias observations** — Features are ℓ∞-normalized before thresholding at the 90th percentile (line 107). A feature with uniformly moderate values across data could be declared "absent" everywhere, while one with a single extreme outlier would be declared "present" in many data. The effect of this nonlinear transformation on the downstream observations (especially the long-tailed frequency distribution) is not discussed or analyzed.

6. **SVHN results mentioned but not shown** — The experimental setup (line 119) states the same process was run on SVHN, but no SVHN results appear in the paper. This is a missed opportunity for cross-dataset validation that would substantially strengthen the empirical claims.

7. **The agreement function $\zeta(k,c)$ is set to an arbitrary constant without ablation** — In numerical simulations (line 288), $\zeta(k,c) = 0.9 \cdot \mathbb{1}\{k>0\}$ is chosen without demonstrating that GDE behavior is robust to the specific form of $\zeta$. While $\zeta$ is unlikely to be the sole driver of results (the GDE pattern depends more on feature-distribution parameters as shown in Figure 4), the paper would benefit from ablating this choice.

### Trivial

None that are not parser artifacts.

## Nice-to-Haves

- Estimating the model parameters ($t_d, t_r, n_d, n_r, p_d$) from interaction-tensor measurements on CIFAR-10 and plugging them into the closed-form expressions to compare predicted vs. observed accuracy/agreement would convert qualitative validation into a quantitative test.
- Extending the theoretical framework to multi-class settings or providing a formal bridging argument between the binary model and the multi-class experimental setting.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that the paper's reading of the multi-view model is imprecise** (harsh critic, para on Section 1–2, regarding learning vs. classification distinction) — REMOVED. The paper's claim (line 179) that multi-view data should be classified correctly is a reasonable high-level reading of Allen-Zhu & Li; this nuance does not invalidate the paper's contrast.
- **Criticism about the greedy clustering algorithm not being summarized** — REMOVED. The main text (line 105) describes the matching logic (thresholding absolute correlations, greedy matching). The appendix detail was stripped by the parser.
- **Criticism that $\zeta$ carries the explanatory load for GDE** — REMOVED. This overstates $\zeta$'s role. The numerical simulations show GDE holding/failing based on feature distribution parameters ($t_r, t_d, n_r, n_d$ ratios, Figure 4 right column), not on $\zeta$. $\zeta$ is an auxiliary assumption about agreement magnitude.
- **Criticism about no limitations paragraph** — REMOVED. This is a presentation preference, not a substantive weakness.
- **Strength about "addressing an important problem"** — REMOVED as generic/superficial.

## Novel Insights

The most striking observation from these reviews is the structural disconnect between the paper's two main contributions. The interaction tensor is a rich empirical tool that could be independently valuable, but the theoretical framework is too loosely coupled to it. Parameters that *could* be measured from the tensor ($t_d, t_r, n_d, n_r, p_d$) are treated as free variables in the theory, and the closed-form expressions are never validated against the tensor's actual measurements. This suggests an alternative path: the paper could have used the interaction tensor to directly test whether the distributional properties it measures predict GDE behavior without a new abstraction layer. As written, the theoretical abstraction sits uneasily between the empirical tool and the phenomena it aims to explain — the framework provides a *vocabulary* for discussing GDE but not a *verified mechanism*.

## Suggestions

1. Estimate the model parameters ($t_d, t_r, n_d, n_r, p_d$) from interaction-tensor measurements on CIFAR-10, plug them into the closed-form expressions, and compare predicted vs. observed accuracy/agreement. This is the single highest-leverage improvement.
2. Run a sensitivity analysis varying $k$ (number of PCA components), $\gamma_{\text{corr}}$, and $\gamma_{\text{data}}$ over a reasonable range and report whether O.1–O.4 hold, with visualizations.
3. Add error bars (e.g., bootstrap or across random seeds) to Table 1 and key quantitative claims.
4. Include SVHN results or remove the mention.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>