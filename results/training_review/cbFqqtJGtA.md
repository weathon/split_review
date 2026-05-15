Now I have a thorough understanding of the paper. Let me write the final consolidated review.

## Summary

The paper proposes CDN (Causal Differential Networks), a two-stage approach for predicting which variables (genes) were perturbed in an intervention. First, a pretrained amortized causal discovery model (SEA) featurizes observational and interventional gene expression datasets into paired graph representations. Then, an axial-attention classifier learns to map these paired graphs to intervention targets. The method is evaluated on seven single-cell transcriptomics datasets (outperforming baselines including Gears, GenePT, and PDGrapher) and on synthetic benchmarks (outperforming causal discovery algorithms like DCDI, BaCaDI, UT-IGSP, and DCI).

## Strengths

- **Consistent state-of-the-art on real biological data**: CDN outperforms all baselines (Gears, GenePT, Linear, MLP, PDGrapher) across five Perturb-seq and two Sci-Plex datasets on rank, recall@k, and Pearson correlation (Tables 1 and 2). The advantage is particularly clear in recall curves (Figure 3), where CDN is the only model that consistently ranks ground-truth targets above random. Notably, CDN achieves this without any external domain knowledge, unlike all competing baselines.

- **Generalization to unseen cell lines**: CDN maintains competitive performance on held-out cell lines without retraining (Table 1, unseen columns), demonstrating transfer across cellular contexts — a practical advantage over baselines that cannot generalize in this way.

- **Scalable and effective vs. causal discovery algorithms**: On synthetic data with up to 20 nodes (and the approach is designed for 1000+), CDN achieves high mAP (~0.9) and AUC while running in seconds, whereas DCDI and BaCaDI require hours and do not scale to biologically relevant sizes (Table 3, runtime table). The MLP ablation cleanly demonstrates that graph-level information is essential for soft intervention detection.

- **Ablation studies validate design choices**: Replacing axial attention with an MLP causes significant performance drops on soft interventions (Table 3), confirming that edge-level graph information is critical. Additional ablations on architecture components and summary statistics further justify the design.

## Weaknesses

### Fatal
None.

### Major

1. **Causal featurizer is unvalidated on real biological data.** The paper's core step is to featurize real gene expression data using a pretrained amortized causal discovery model. While the paper acknowledges that "we cannot 'prove' that a pretrained model extracts correct graphs on real data, as the true graphs are unknown" (Section 3.4), it provides no sanity checks — e.g., whether predicted edges overlap with known regulatory interactions (STRING, ENCODE), whether graph representations are stable across random seeds, or whether control-vs-perturbation graph differences correlate with known biological responses. Without such validation, it remains unclear whether the classifier exploits genuine causal structure changes or spurious artifacts of the frozen featurizer. Given that the whole pipeline depends on this step, the lack of even basic validation is a significant gap.

2. **Biological baseline comparisons do not control for knowledge-base coverage asymmetry.** The paper acknowledges that "not all genes can be mapped to the baselines' domain knowledge" (Section 4.1), yet the evaluation uses the same candidate set (top 1000 DE genes) for all methods. Baselines like PDGrapher and Gears are inherently limited to genes present in their external knowledge graphs (human interactome, GO), so for perturbations whose true target is absent from those graphs, the baseline cannot rank it highly. CDN suffers no such restriction. The reported advantage over PDGrapher may partially reflect this coverage gap rather than superior causal reasoning. A fairer evaluation would either restrict the candidate set to genes present in all baselines' knowledge bases, or report performance as a function of coverage. The inclusion of Linear and MLP baselines (which also use no external knowledge) partially mitigates this concern, since CDN outperforms them too — but the strongest baselines (PDGrapher, Gears) are the ones most affected by this asymmetry.

3. **Synthetic comparison is supervised vs. unsupervised, not directly interpretable.** CDN is trained with full supervision on ~4000 synthetic datasets with known intervention targets sampled from the same generative process used for testing. The baselines (DCDI, BaCaDI, UT-IGSP, DCI) are fully unsupervised, inferring both graph and targets from scratch on each test dataset. The paper's claim that CDN "outperforms causal discovery algorithms" is technically true but conflates method quality with the availability of labeled training data. A fairer comparison would also give the baselines access to labeled training data (e.g., by pretraining on synthetic graphs). The asymmetry is implicitly acknowledged (the paper notes runtime differences), but the framing in the abstract and conclusion overstates what the comparison demonstrates.

### Minor

1. **Trivial/non-trivial target stratification is mentioned but not analyzed.** The paper stratifies genetic perturbations based on whether the target is trivially identifiable as the gene with the largest log-fold change (Section 4.1), which suggests the authors anticipated an important confound. However, results are never broken down by this stratification, making the inclusion feel incomplete.

2. **No sensitivity analysis of the frozen featurizer.** The paper uses a single pretrained SEA aggregator (FCI-based marginal estimates). There is no analysis of how performance changes with different random seeds, different pretrained checkpoints, or different marginal estimators. The robustness of the pipeline to the choice of featurizer is therefore unknown.

3. **Vague description of key preprocessing details.** The causal featurizer's variable sub-sampling procedure mentions "heuristics like pairwise correlation" for selecting likely-related variables (Section 3.1), but does not specify thresholds or criteria. This step is critical for scaling to thousands of nodes, but the description is too imprecise for reproducibility without referring to the SEA paper.

### Trivial
None.

## Nice-to-Haves
- A case study visualizing predicted graph differences for a few perturbations alongside known biology would significantly strengthen interpretability.
- Analysis of how the model performs on weak-effect perturbations (those filtered out by the >10 DE genes threshold) would clarify the method's limitations.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism that the third contribution (datasets) is "padding" or not described**: The statistics table (\input{table/0-data_stats}) was likely present in the original submission but stripped by the parser. Dataset contributions are standard and the paper clearly states these were prepared. The hard rules prohibit questioning existence/release status of cited contributions.

- **Criticism about the "seen cell line" split being a "strong and unusual choice"**: The paper explicitly justifies this (line 238: "To ensure that our train and test splits are sufficiently distinct, we cluster perturbations based on their log-fold change and assign each cluster to the same split"). This is a deliberate design choice to prevent trivial leakage, not a flaw.

- **Criticism that the model generalizing from hard to soft interventions is a weakness because "the mechanism is unclear"**: The paper presents this as an interesting empirical finding (Section 4.2), and the mechanism is discussed — the MLP ablation shows that graph-level information becomes crucial precisely for this transfer. This is a strength, not a weakness.

- **Pure formatting/style nitpicks** from the section-by-section notes that do not identify substantive errors.

- **Criticism about the abstract stating "three-fold contributions" as overstatement**: The three contributions are clearly enumerated in the paper (lines 58-62), and the datasets are a legitimate contribution even if details are brief in the main text.

## Novel Insights

The most interesting insight emerging from the review is that the MLP ablation (Table 3) reveals a clean performance dissociation: on hard interventions, the MLP (which ignores graph structure) performs nearly as well as the full axial-attention model, but on soft interventions the gap is large. This suggests that for hard interventions, node-level statistics (likely marginal variances) are nearly sufficient to identify targets, whereas soft interventions require detecting subtle changes in conditional dependency structure that only edge-level information can capture. This finding is both a validation of the method's design philosophy and a practical insight for future work: the value of causal structure modeling depends on the intervention type. The paper could strengthen this point by probing whether this dissociation holds on real data (e.g., comparing CRISPRi vs. chemical perturbations).

## Suggestions

1. **Validate the causal featurizer on real data at least minimally**: Report overlap of predicted edges with known regulatory networks (STRING, ENCODE) or stability across random seeds. Even a simple sanity check would significantly increase confidence that the pipeline rests on meaningful features rather than artifacts.

2. **Control for baseline coverage in biological evaluation**: Either (a) restrict the candidate set to genes present in all baselines' knowledge bases and re-run comparisons, or (b) report performance stratified by whether the true target is present in each baseline's knowledge graph. This would clarify whether CDN's advantage is genuine or partially artifactual.

3. **Report results broken down by trivial/non-trivial targets**: The paper already collects this information; reporting it would clarify when CDN adds value beyond simple differential expression ranking.

4. **Acknowledge the supervised vs. unsupervised asymmetry more explicitly** in the abstract and conclusions, and consider adding a controlled experiment where a baseline (e.g., DCI) is also given access to labeled training data.

## Score and Decision

The paper proposes a well-motivated, practically useful pipeline that achieves consistent state-of-the-art results across seven real transcriptomics datasets and demonstrates clear advantages in scalability over existing causal discovery methods. The main concerns — unvalidated featurizer on real data, coverage asymmetry in biological baselines, and asymmetric synthetic comparisons — are real but not fatal. The paper acknowledges most of these limitations and the core empirical finding (consistent SOTA across multiple datasets and metrics) is robust even accounting for the coverage asymmetry (since CDN also outperforms non-knowledge-based baselines like Linear and MLP). The work is a solid contribution to an important problem.

**Score**: 7.0

**Decision**: Accept

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>