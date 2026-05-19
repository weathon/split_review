- Decision: Reject
- Avg Score: 4.20
- Scores: 5, 3, 5, 3, 5
Now I have enough information. Let me compose the final consolidated review.

## Summary

The paper identifies two causes of the DL/tree gap on tabular data — numerical features that behave categorically ("implicitly categorical features" or ICF) and neural networks' bias toward overly smooth solutions — and proposes statistical methods to detect ICF plus Learned Fourier Features (LFF) to address the smoothness bias. Experiments on 68 datasets from the Grinsztajn et al. benchmark show that when these techniques are applied on top of simple MLP and ResNet backbones, performance improves substantially and, in some configurations, matches or exceeds XGBoost on classification tasks.

## Strengths

- **Novel identification of implicitly categorical features as a specific cause of the DL/tree gap.** The paper pinpoints numerical features that are effectively discrete (e.g., assignment number, line number in the eye movements dataset, Sec. 1) and shows through statistical testing (Chi-squared, ANOVA, Mutual Info) that encoding them as categorical can yield large performance gains. This goes beyond prior work (Grinsztajn et al., 2022) that treated categorical variables broadly as a minor weakness.

- **Ablation demonstrates the complementarity of the two components.** Figure 5 (Sec. 5.4) separates runs into ResNet+C (ICF only) and ResNet+F (LFF only) and shows that each component spikes on different datasets — e.g., ResNet+C on eye movements, ResNet+F on covertype. This provides concrete evidence that both mechanisms matter and that the gain is not attributable to one component alone.

- **Large-scale, rigorous experimental setup.** The benchmark follows the Grinsztajn et al. protocol (multi-fold splits, fixed seeds, consistent preprocessing), spans 68 datasets, and involves 51,000 runs with 150 hyperparameter samples per model. This makes the performance comparisons credible and reproducible within the protocol.

- **Adaptation of Learned Fourier Features to tabular data.** The paper introduces Conv1x1LFF and LinearLFF as tailored ways to apply Fourier feature mappings to tabular inputs, which is a sensible adaptation of a technique from other domains (Sec. 3.3).

## Weaknesses

### Fatal

None.

### Major

- **The "combined" model comparison is structurally unfair.** ResNet+F|C randomly selects between two mutually exclusive variants — ResNet+F (LFF only) and ResNet+C (ICF only) — in each of its 150 runs (Sec. 4, line 120). The best run across *both* sub-models is then compared against XGBoost's best run. This means ResNet+F|C effectively gets to pick from two model families, inflating its best-result ceiling relative to a single-model baseline. The paper's headline claim ("substantially outperforms XGBOOST on both the classification tasks," Sec. 5.1) is therefore weaker than it appears. The ablation (Fig. 5) partially mitigates this by showing each component separately, but only on a hand-picked subset of datasets — aggregate per-component performance (e.g., average normalized scores for ResNet+F and ResNet+C across *all* tasks) is not reported, leaving the reader unable to assess how much the pooled selection drives the headline results.

### Minor

- **Insufficient per-component aggregate results.** The ablation (Sec. 5.4) only examines datasets with the largest best-vs-runner-up gaps. The paper should report average normalized scores across *all* datasets for ResNet+F and ResNet+C separately, so the reader can assess whether the combined method is genuinely stronger than either component alone, or whether the pooled advantage explains most of the gain.

- **"Spiking" evidence is correlational, not causal.** The paper attributes large performance spikes to the random search "latching on" to a correct ICF encoding (Sec. 5.3). This is plausible but not directly verified — the paper does not show which specific features were flagged as ICF in spiking runs, or demonstrate (e.g., by holding other hyperparameters fixed and toggling ICF on/off) that the spike disappears without it. The separation by component in Fig. 5 provides indirect support, but a causal demonstration would substantially strengthen the claim.

- **No comparison against other tabular deep learning methods.** The paper compares only against its own base models (MLP, ResNet) and XGBoost. Several other DL approaches for tabular data are cited in related work (FT-Transformer, SAINT, NODE, TabNet, line 36) but never evaluated. While the paper's main claim is about closing the gap *to tree-based methods* (not to all DL), including these baselines would clarify whether the proposed techniques offer something beyond what existing tabular DL methods already provide, and would better situate the contribution.

- **Statistical test thresholds are not analyzed.** The ICF detection method depends on thresholds (\(\chi^2\_\text{thresh}\), \(F\_\text{thresh}\), \(MI\_\text{thresh}\)) whose choice critically determines which features are flagged as categorical. The paper does not discuss how these thresholds are set in the random search or provide any sensitivity analysis, which would help gauge robustness.

- **Regression categorical task weakness is underexplored.** The method still lags behind XGBoost on regression with categorical features (Fig. 2). This failure case is noted but not analyzed — e.g., whether the statistical tests are less effective for regression, or whether LFF is insufficient. Understanding this gap would strengthen the paper.

### Trivial

- **Inconsistent notation.** The paper uses "CFD" (Categorical Feature Detection) in the abstract and contributions, then mostly switches to "ICF" (Implicitly Categorical Features) in the method section, without clarifying whether these refer to the same thing. The naming should be unified.

## Nice-to-Haves

- Provide a synthetic-data experiment where the implicit categorical structure is known, to directly validate that ICF detection correctly identifies the relevant features and that encoding them recovers the performance lost by a plain MLP.
- Compare ICF detection against a baseline of randomly selecting features to treat as categorical, to demonstrate that the statistical tests provide real signal beyond chance.
- Report per-dataset normalized scores in a table, enabling readers to inspect patterns and apply standard statistical tests (e.g., Wilcoxon signed-rank) over the benchmark.

## Removed Points

These points from the reviewer inputs were removed with justification:

- *"No code release"* — Removed per instructions to exclude reproducibility nitpicks about code availability.
- *"Abstract/Introduction claim overstated"* — Subjective opinion without a concrete anchor in the paper.
- *"Section 3.1 encoding is unusual"* — A design choice, not a weakness; the motivation of using one-hot + original value is described.
- *"Section 3.4 rotational variance not supported"* — Speculative; the paper does not claim to prove this hypothesis, only to study it.
- *"Section 4 merging medium/large datasets reduces granularity"* — The paper explicitly justifies this ("due to the number of large datasets being much smaller," Sec. 4).
- *"XGBoost default hyperparameters question"* — The paper clearly states that hyperparameter search is run for all models including XGBoost (Sec. 4), so this criticism is factually wrong.
- *"Missing related works"* — Removed per instructions as the reviewer cannot confirm existence of missing references.
- *"Formatting nitpicks"* — Removed per instructions (parser artifacts).
- *"The term CFD and ICF are used inconsistently"* — This is retained as a Trivial point above (inconsistent notation), not removed.
- *"Cannot be independently verified"* — Removed per hard rules; all cited models/tools/datasets are assumed to exist.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a specific methodological concern (the pooled comparison) that the paper does not adequately address, and identify several gaps in evidence quality (causal validation of spiking, sensitivity analysis of thresholds), but these are evaluation critiques rather than novel observations about the problem domain.

## Suggestions

1. **Fix the comparison.** Report ResNet+F and ResNet+C as separate methods with their own 150-run random searches, in addition to (or instead of) the pooled ResNet+F|C. If a fully combined method is desired (applying both ICF and LFF to the same input), define and evaluate it explicitly rather than pooling exclusive variants.
2. **Add per-component aggregate results.** Provide a table of average normalized scores across all tasks for each individual component (ResNet+F, ResNet+C), so readers can assess whether the pooled advantage drives the headline results.
3. **Include at least one competitive tabular DL baseline** (e.g., FT-Transformer) to contextualize how much of the improvement is new versus already achievable with existing neural approaches.
4. **Validate the spiking mechanism causally.** For a few datasets where spikes occur, show which features were flagged as ICF, and run a controlled experiment with ICF toggled on/off while holding other hyperparameters fixed.
5. **Analyze threshold sensitivity.** Vary the ICF detection thresholds and report how many features are flagged and how performance changes.
