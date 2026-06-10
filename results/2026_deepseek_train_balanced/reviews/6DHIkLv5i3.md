## Summary

This paper studies how molecular property prediction models struggle with activity-cliff (AC) molecules — pairs of structurally similar molecules with different properties — and proposes LAC, a training algorithm with two components: (1) a weighted curriculum-learning node-level loss that up-weights AC molecules and selects hard samples via a time-varying threshold, and (2) an edge-level pairwise loss that explicitly pushes apart predictions for AC pairs. Experiments across classification (MoleculeNet) and regression (ChEMBL) datasets with six different base models show consistent improvements over baselines.

## Strengths

- **Consistent empirical improvement across all base models and datasets.** Table 2 shows LAC improves ROC-AUC over the baseline for all 6 base models (GIN, GraphGPS, GraphMVP, 3D Infomax, 3D-PGT, UniMol) on all 4 classification datasets without exception. This breadth — spanning both randomly-initialized GNNs and state-of-the-art pre-trained models — is the strongest evidence for the method's central claim.

- **Ablation study cleanly validates the two proposed components.** Table 4 demonstrates that the node-level curriculum learning and the edge-level pairwise task each independently improve performance, and their combination gives the best results across all datasets. Table 5 shows the impact of the AC weighting hyperparameter \(p\), and Table 6 validates the curriculum variant of the edge-level loss.

- **Loss distribution visualizations confirm the mechanism.** Figures 5 and 6 directly show that LAC shifts the training loss distribution of AC molecules leftward (toward lower loss) compared to the baseline, for both randomly initialized and pre-trained models. This provides direct evidence that the method achieves its stated aim of better fitting AC molecules.

- **Extension to regression tasks.** Section 5.2 (Table 3) shows LAC improves MAE on ChEMBL regression datasets with a completely different backbone (MLP on ECFP fingerprints), demonstrating the method is not limited to classification or GNN architectures.

## Weaknesses

### Major

- **"Node classification" framing is misleading.** The paper claims to "reformulate molecular property prediction as a node classification problem on graph" (Section 4.1). However, at inference time the model takes a single molecule as input — exactly as any standard predictor does. The graph is constructed only over the *training set*, and the node/edge-level losses are used solely as training regularizers. No inference is performed on the graph, and the paper does not explain how a test molecule would be inserted into the graph or how message passing over the graph would contribute to predictions. This disconnect between the claimed formulation and the actual procedure overstates the methodological novelty and sets inaccurate expectations.

- **Missing comparisons to standard alternatives for hard-example training.** The experiments compare "baseline vs. baseline+LAC" throughout, but never compare against simpler, well-established training strategies designed for hard examples — such as focal loss, hard negative mining, or static reweighting of AC molecules without the curriculum threshold. Without these baselines, it is unclear whether LAC's advantage comes from the specific proposed mechanism or simply from addressing AC molecules in any manner. This is the most significant gap in the evaluation.

- **Edge-level loss is underspecified for multi-task datasets.** The edge-level loss (Equation 2) is defined as \(-(y_i - y_j)(\hat{y}_i - \hat{y}_j)\), which assumes scalar \(y\). However, datasets such as Tox21 and ToxCast are multi-task: each molecule has multiple binary labels. The paper acknowledges that AC is defined "with respect to a given property" (Definition 3.2) and visualizes different edge types per property (Figure 4), but never specifies how the edge-level loss is computed when each molecule has a vector of labels — whether it is computed per task, aggregated, or handled some other way. This omission makes the experimental results for multi-task datasets ambiguous.

### Minor

- **The empirical motivation (Section 3) is partially tautological.** AC is defined (Definition 3.2) as a matched pair with *different labels*. The "discovery" that such molecules have higher training loss follows directly from this definition: any model forced to fit structurally similar inputs to different outputs will naturally have higher loss on those pairs. The paper presents this as a novel investigation revealing "why existing models fail," but the core observation is definitionally implied rather than causally explanatory. That said, the empirical quantification across multiple models (Figures 2–3, Table 1) is still useful as a sanity check and provides a clear motivation for the method.

- **No ablation isolating the curriculum mechanism from the static weighting.** The node-level task has two components: AC-based weighting (\(p_i\)) and the time-varying threshold \(R(t)\) that discards easy samples. Table 5 tests different \(p\) values but always uses the curriculum threshold. A baseline of "static weighted training without the \(R(t)\) selection" is missing, so the reader cannot tell whether the curriculum aspect adds any value over simple reweighting of AC molecules.

- **No analysis of generalization to unseen AC molecules.** The method is a training-time regularizer; the paper claims improved molecular property prediction broadly, but never analyzes whether the gains on test data are driven specifically by better predictions on *unseen* AC molecules. The aggregate ROC-AUC improvements could stem from better fitting of all molecules, not specifically AC pairs. This weakens the claim that the paper "solves" the AC problem as opposed to providing a generally better training strategy.

- **No statistical significance reporting.** Results are reported as single ROC-AUC values without confidence intervals or standard deviations. Given that the improvements are dataset-dependent and sometimes modest, variance matters for assessing robustness.

- **No computational cost analysis.** The graph construction requires computing matched molecule pairs across the entire training set (\(O(N^2)\)), and the edge-level loss additionally requires computing pairwise losses over all AC pairs. The paper neither reports the graph sizes (number of edges) nor discusses training time overhead.

### Trivial

- The acronym "LAC" is never expanded. (Likely "Learning from Activity Cliffs" or similar, but the paper never says.)
- Proposition 4.1 is a direct algebraic consequence of the loss definition; stating it as a proposition inflates its significance.

## Nice-to-Haves

- An analysis of whether LAC hurts performance on non-AC molecules (negative transfer).
- A comparison to the AC-prediction-based methods cited in the related work (Horvath et al., 2016; Iqbal et al., 2021; Park et al., 2022; Zhang et al., 2023; Wu, 2024), to clarify how the proposed training objective differs from or relates to the AC-classification paradigm.
- Reporting of how many edges were in the constructed graphs for each dataset.

## Removed Points

These points were raised by reviewers but are removed after cross-checking against the paper:

- **"Regression experiments feel like an afterthought"**: The paper explicitly states it follows van Tilborg et al. (2022) who found ECFP+MLP performs best on these regression datasets. This is a justified choice, not an omission.
- **"The AC-only experiment shows weak evidence that AC molecules are useful"**: The paper's own text is appropriately measured ("leads to some improvements"). The strength of this evidence is not overstated.
- **"Proposition 4.1 is inflated"**: Moved to trivial — it's a presentation choice, not a substantive flaw.
- **"LAC name never expanded"**: Moved to trivial.
- **"No comparison to other node classification graph formulations"**: The paper explicitly distinguishes itself from Zhuang et al. (2023) and Zhao et al. (2024) by incorporating AC edge types. This is adequate.
- **"Method is not applicable at inference time"**: The method is a training algorithm; most training-time regularizers are not "applicable at inference." This is not a weakness of the method class.
- **"Empirical motivation is entirely tautological"**: Overstated. While the high-level relationship is definitional, the specific quantification across multiple architectures (GIN, GraphGPS, 3D-PGT, UniMol) and the loss distribution analysis provide nontrivial empirical grounding.

## Novel Insights

The strength-finder's only genuinely novel observation beyond the paper's own contributions is that the two-level design (node-level curriculum + edge-level pairwise loss) directly mirrors the dual nature of activity cliffs: AC is simultaneously a per-molecule phenomenon (the molecule is "hard to fit") and a pairwise phenomenon (two structurally similar molecules must be separated in representation space). This observation is implicit in the paper's design but never articulated as a design principle. Neither reviewer raised this explicitly.

## Suggestions

1. **Clarify the inference procedure.** State explicitly in Sections 1 and 4.1 that the graph is a training-only construct and that at test time, predictions are made per-molecule using the base model's standard forward pass. This resolves the misleading "node classification" framing without changing any method details.

2. **Add comparisons to simpler baselines.** At minimum, compare against: (a) focal loss for hard-example emphasis, (b) static reweighting of AC molecules without the curriculum threshold \(R(t)\), and (c) a variant of the edge-level loss without curriculum selection. This would rigorously demonstrate that LAC's specific design choices add value over standard alternatives.

3. **Specify the multi-task handling.** Add a sentence or an equation explaining how the edge-level loss is computed when molecules have multiple labels — whether per-task, after aggregation, or via a vector extension.

4. **Provide a generalization analysis for unseen AC molecules.** Split the test set AC pairs into those with similar training molecules and those without, and report performance separately. This would directly demonstrate whether the method's benefits transfer to novel AC molecules.

5. **Add confidence intervals or standard deviations** over multiple runs, and report the computational cost (number of edges in \(\mathcal{G}\), training time overhead).

## Score and Decision

The paper addresses a genuine challenge in molecular property prediction, proposes an intuitively reasonable solution, and provides consistent empirical evidence across diverse settings. The core method is sound and the results are reproducible in principle. However, the misleading "node classification" framing, the missing comparisons to simpler baselines, the underspecified multi-task loss, and the absence of any analysis isolating whether the proposed components add value over simpler alternatives collectively weaken the paper's current form. These issues are addressable with revision, but in the current submission they prevent the paper from meeting the top-venue bar for clarity and evidential rigor.

**Score: 5.0**

**Decision: Reject**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>