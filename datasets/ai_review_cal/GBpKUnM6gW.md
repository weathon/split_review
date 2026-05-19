- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3
I now have a thorough understanding of the paper and all reviewer inputs. Let me construct the consolidated review with rigorous filtering.

---

## Summary

This paper presents a large-scale benchmark evaluating 13 deep learning models (7 spatial/connectivity-based and 6 sequential/time-series models) across 34,887 fMRI samples from six public databases (HCP-Task, HCP-WM, ADNI, OASIS, PPMI, ABIDE). The study covers both task-evoked fMRI (cognitive task recognition) and resting-state fMRI (neurodegenerative and neuropsychiatric disease diagnosis), and additionally attempts a post-hoc interpretability analysis via logistic regression brain maps. The central finding is that model suitability depends on the neuroscience context: sequential models significantly outperform spatial models on task-evoked fMRI, while the two classes perform comparably on disease diagnosis data. Preprocessed data is released publicly.

## Strengths

- **Large-scale, multi-dataset evaluation with genuine breadth**: The paper evaluates 13 models on 34,887 samples from six datasets spanning task-evoked fMRI, neurodegenerative disease (AD, PD), and neuropsychiatric disorders (autism). This substantially exceeds prior benchmarks (Said et al.: only HCP; El-Gazzar et al.: only UK Biobank) and provides statistical power for cross-context comparisons.

- **Statistically grounded model-type comparison supporting actionable guidelines**: The paper uses two-sample t-tests to compare spatial vs. sequential model families, reporting significant differences for task fMRI (HCP-WM: p<10⁻⁴; HCP-Task Mixed: p=0.01) and non-significance for disease data (ADNI: p=0.37). These significance tests directly support the paper's main guideline — that model choice should depend on the fMRI application context — rather than relying on raw accuracy rankings alone.

- **Inclusion of recent architectures (Mamba/SSM)**: The benchmark includes the state-space model Mamba (Section 4), which had not been systematically compared on fMRI tasks in prior benchmarks, improving timeliness and breadth.

- **Public release of preprocessed data**: The paper states that "the pre-processed data is publicly available" (Section 7), enabling independent verification and follow-up studies — a practical strength many prior benchmarks lack.

- **Explainability analysis as a novel dimension**: Section 6 goes beyond pure performance comparison by generating post-hoc brain attention maps for each model and qualitatively comparing them to known motor/language regions and disease-relevant networks. While the execution has limitations (see Weaknesses), the attempt to benchmark interpretability — not just accuracy — is a genuine contribution that prior fMRI benchmarks have largely ignored.

## Weaknesses

### Fatal
None.

### Major

- **Evaluation protocol for disease datasets is not specified (Section 5, Table \ref{hcp} bottom, Table \ref{abide})**: The paper reports accuracy, precision, and F1 with standard deviations for ADNI, OASIS, PPMI, and ABIDE, but never describes how these numbers were obtained. Was it k-fold cross-validation? A fixed hold-out? Multiple random seeds? How many trials are averaged? The HCP datasets get a detailed protocol description (Separated Scan 1 & Scan 2 vs. Mixed, lines 117–118), but no analogous description exists for any disease dataset. Since sample sizes are small (ADNI: 250, PPMI: 209) and performance differences between models are often within one standard deviation, the reader cannot assess whether reported differences are real or artifacts of the evaluation protocol. For a benchmark paper, this is a core methodological gap that directly affects the trustworthiness of the quantitative conclusions.

- **Hyperparameter tuning is not described, making model comparisons potentially unfair (Section 5)**: The paper states that spatial model node embeddings follow "the optimal settings described in [7]" (line 114), but no tuning procedure is reported for any model — no search space, no optimization method, no number of trials, no learning rate, batch size, or architecture choices. If some models were tuned more extensively than others, the ranking could reflect tuning effort rather than architecture quality. This is particularly concerning given the wide performance range within each model class (e.g., GNN-AK at 73% vs. SPDNet at 94% on HCP-Task). A benchmark's central claim is to fairly compare models, and this gap undermines that claim.

### Minor

- **Interpretability analysis is qualitative only, with no quantitative validation (Section 6)**: The paper presents brain maps of logistic regression weights and makes claims such as "GCN effectively identifies most motor-related brain regions" (line 270) and "GIN selects more language-related regions" (line 270). However, there is no quantitative measure of alignment with established atlases or prior fMRI findings (e.g., Dice overlap, distance to known functional ROIs). The paper acknowledges that "findings are not yet converging" and maps are "dispersed" (lines 273, 284), which is honest, but the claims about which models identify which brain regions remain anecdotal. Additionally, the method for extracting features from each model, the specific logistic regression procedure, and the rationale for the "top 40" threshold are not described.

- **No multiple comparison correction for statistical tests**: The paper reports t-test p-values for several comparisons (HCP-Task: p=0.01, HCP-WM: p<10⁻⁴, ADNI: p=0.37) but does not apply any correction (Bonferroni, Benjamini-Hochberg) for the multiple comparisons across datasets and model families. This is common in benchmarking papers but warrants mention given the number of tests performed.

- **Class balance not reported for disease datasets**: Table 1 lists only total samples and number of classes. For datasets like ADNI (250 samples, 2 classes) and PPMI (209 samples, 4 classes), per-class counts are essential to assess whether reported accuracy, precision, and F1 are meaningful — especially since standard deviations are large (e.g., PPMI precision ranges from ±11% to ±18%).

- **Data harmonization method not specified**: The paper states in a footnote that "data harmonization has been applied" (line 110) but provides no details on the method (ComBat, normalization, or other), which is relevant for a multi-site benchmark combining data from six sources.

### Trivial

- **Model descriptions are generic textbook summaries (Section 4)**: Descriptions like "Transformers are selected for their powerful attention mechanisms" and "1D-CNN is selected for its strength in capturing temporal patterns" add no value for the target audience. The space could be better used to describe model-specific adaptations for fMRI (graph construction, sequence length handling, pooling strategies).

## Nice-to-Haves

- Computational cost (training time, memory, inference speed) is not discussed. For practitioners choosing a model, this is highly relevant — especially given that SPDNet is highlighted as top-performing but may be computationally expensive. Remark 2.2 briefly notes that "GSN is more complex and needs more computational time" (line 217), but no systematic comparison is provided.
- The biological interpretations in Remarks 1.1, 2.1, and 3.1 are plausible and well-cited, but framing them explicitly as hypotheses ("consistent with the hypothesis that...") rather than conclusions would better match the level of indirect evidence.
- Code release (beyond preprocessed data) would further strengthen reproducibility.

## Removed Points

These points were flagged in the input reviews but are removed with justification:

- **"Abstract framing is overly ambitious"** (Harsh Critic): The abstract promises "guidelines for designing deep models for functional neuroimages." The paper delivers empirically grounded guidelines (Remarks 1.1, 1.2, 2.1, 2.2, 3.1, 3.2, 4.1, 4.2) specific to the tested scenarios. This is appropriate for an empirical benchmark paper. Removed as scope-creep.
- **"Section 3 hand-waves about atlases and preprocessing"**: The paper addresses atlas choice through a citation to Said et al. and notes that harmonization was applied. For a benchmark, referencing established prior work for preprocessing choices is reasonable. Removed as scope-creep — the paper is not a preprocessing methods paper.
- **"Remarks 1.1 and 2.1 are overconfident biological interpretations"**: The paper uses appropriately hedged language ("One possible explanation," "could be attributed to," "can be understood as") and cites relevant literature (Buckner et al., Chiesa et al., etc.). These are plausible scientific interpretations grounded in cited evidence. Removed as overly harsh characterization.
- **"Missing related works comparison"**: The paper clearly distinguishes itself from Said et al. (only HCP), El-Gazzar et al. (only UK Biobank, only GNNs), and Xu et al. (traditional ML methods) in Section 2 (lines 48–51). Removed as factually wrong.
- **"Models not released" / reproducibility concerns rooted in code availability**: The paper states preprocessed data is publicly available. The parser strips appendix content which may contain further details. Removed per hard rule about citing existence and appendix stripping.
- **"Low-resolution brain maps hard to interpret in print"**: Formatting nitpick about figure quality. Removed.
- **"Typos/grammar issues"**: Parser artifacts, not author errors. Removed.
- **Strength Finder's generic/delusional strengths**: Claims about the paper "addressing an important problem" or "targeting an interesting question" are generic and removed. Kept only concrete, evidence-grounded strengths.

## Novel Insights

The most interesting observation emerging from cross-referencing the reviews is that the harsh critic and the strength finder largely agree on the paper's profile: it is a genuinely large-scale, multi-context benchmark — the most comprehensive in fMRI to date by sample count and model diversity — but its trustworthiness as a reference comparison is reduced by missing methodological documentation (evaluation protocol, hyperparameter tuning, class balance). This tension between breadth of execution and depth of reporting is the paper's defining characteristic. A second notable point is that the interpretability section is simultaneously a strength (few benchmarks attempt it) and a weakness (it is done qualitatively), which suggests that the community would benefit from adoption of standardized quantitative interpretability metrics for fMRI — a direction the paper could help pioneer rather than merely gesture at.

## Suggestions

1. **Add a dedicated "Experimental Protocol" subsection** specifying the exact evaluation procedure for every dataset: number of cross-validation folds (or train/val/test split), stratification, whether subjects are kept together across folds, and number of independent trials. This is the single highest-leverage improvement.

2. **Report hyperparameter tuning for every model**: search space, optimization method (grid/Bayesian/hand), budget (number of trials), and final selected hyperparameters. A table in the appendix would suffice.

3. **Add per-class sample counts** for all disease datasets and consider reporting balanced accuracy or AUC alongside accuracy.

4. **Quantify the interpretability analysis**: compute Dice overlap or distance-to-centroid between model-identified regions and canonical task-activation maps from NeuroSynth or HCP task contrasts. This would transform a qualitative illustration into a rigorous evaluation.

5. **Apply a multiple-comparison correction** (Benjamini-Hochberg or Bonferroni) to the reported t-tests, or explicitly note which comparisons were pre-registered.

6. **Add a computational cost table** (training time, inference time, GPU memory) for all 13 models across representative datasets.

7. **Provide details on the data harmonization method** (ComBat parameters, site covariates, etc.).

8. **Tone down the biological conclusions** in the Remarks by reframing them as hypotheses consistent with the observed data, noting that direct evidence linking model performance to specific biological mechanisms is not provided.
