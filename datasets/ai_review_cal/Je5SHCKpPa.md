- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6
Now I have all the information needed. Let me compose the final consolidated review.

## Summary

The paper introduces MUSE, a framework for multimodal patient representation learning that jointly handles both missing modalities and missing labels — a realistic clinical setting overlooked by prior work. MUSE models patients and modalities as a bipartite graph (allowing flexible missing-modality patterns) and employs a mutual-consistent contrastive loss with edge-dropout augmentation to learn modality-agnostic and label-decisive features. Its unsupervised contrastive objective can incorporate unlabeled patients. Evaluated on MIMIC-IV, eICU, and ADNI, MUSE outperforms all baselines (~2% absolute AUC-ROC improvement when training only on labeled patients, ~4% when also using unlabeled patients), with supporting ablations and robustness analyses.

## Strengths

- **Concrete contribution: handles the combined missing-modalities-and-labels problem.** The paper clearly identifies a gap (Fig. 1) that prior methods handle missing modalities only, while real clinical data frequently has missing labels too. MUSE's unsupervised contrastive loss (Eq. 5) requires no label information, and Table 1 shows that MUSE+ improves ~4% AUC-ROC over MUSE alone by exploiting unlabeled patients — a direct, practically meaningful benefit.

- **Bipartite graph design is well-motivated and effective.** Section 3.1 constructs a patient–modality bipartite graph where edges exist only for available modality pairs. This naturally handles arbitrary missing-modality patterns without imputation or complex hypergraph structures. The empirical results (Tables 1–2) show this graph-based approach beats both imputation (CM-AE, SMIL) and direct-prediction (MT) methods, while being more scalable than HGMF's hypergraph.

- **Strong and consistent empirical evidence.** Results are reported across three distinct datasets (MIMIC-IV, eICU, ADNI), two clinical tasks (mortality, readmission), with statistical significance tests and bootstrapped confidence intervals. The improvements are practically meaningful (2–4% absolute AUC-ROC) with low variance. The robustness analysis (Fig. 3) systematically varies missing rates from 0.1 to 0.7, showing MUSE's advantage grows as missingness increases.

- **Ablation study cleanly validates design choices.** Table 3 isolates the contribution of each component: A1 (feature dropout vs. edge dropout) confirms edge dropout is crucial; A2 (no contrastive loss) drops to near-baseline levels; A3/A4 show both supervised and unsupervised contrastive objectives contribute. This provides clear evidence that the mutual-consistent contrastive loss is responsible for the gains.

- **Cosine similarity analysis (Fig. 4) provides direct evidence for modality-agnostic representations.** MUSE achieves the highest cosine similarity between representations of the same patient under different modality subsets, quantitatively supporting the claim that the method learns modality-agnostic features.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are well-supported by the evidence presented.

### Minor

- **Factual error in eICU dataset description.** Line 144 states: "eICU (Pollard et al., 2018) covers 431K visits for 180K patients admitted to the ICU in the Beth Israel Deaconess Medical Center." This is incorrect on two counts: (1) eICU is a multi-hospital dataset from Philips, not from Beth Israel Deaconess Medical Center; (2) the identical statistics to MIMIC-IV (431K/180K) are suspiciously duplicate. The experiments presumably used the correct eICU data, so results are likely unaffected, but this reporting error raises a credibility concern about dataset statistics in the paper. The authors must correct this and verify all dataset descriptions.

- **Edge dropout rate (0.15) is stated without justification or ablation.** The 15% edge dropout is the core augmentation mechanism driving the unsupervised contrastive loss, yet the paper provides no sensitivity analysis or rationale for this specific value. The ablation (A1) replaces edge dropout with feature dropout (a fundamentally different operation), which is not informative about sensitivity to the dropout rate itself. This leaves a gap: would performance degrade at higher or lower rates under different missingness regimes?

- **Baseline hyperparameter tuning protocol is under-specified.** The paper states that all models are trained for 100 epochs with validation-based early stopping (line 137), but it does not describe whether hyperparameter search (e.g., learning rate, hidden dimensions, dropout) was conducted for each baseline. This concern is partially mitigated by the ablation study: A2 (MUSE without any contrastive loss) essentially reduces to a GRAPE-like method with edge augmentation, and it performs comparably to GRAPE, suggesting the comparison is not severely skewed. Nevertheless, a clear statement of the tuning protocol for each baseline would strengthen the paper.

- **No discussion of limitations.** The paper lacks a limitations section. Notable omissions: MUSE requires at least one modality per patient (it cannot handle patients with zero modalities); it assumes a fixed set of modalities at training time; the edge-dropout augmentation simulates uniform random missingness which may not match the structured missing patterns in real clinical data (e.g., certain modality pairs are frequently missing together). Acknowledging these would improve scientific rigor without weakening the contribution.

- **Key hyperparameters are not reported or analyzed in the main text.** The temperature hyperparameter τ (Eqs. 5–6) appears in the contrastive losses but its value is not stated. The three loss objectives are "added together" (line 123) without specifying the relative weighting or whether a search was performed. These details may reside in the appendix, but they are important enough for the main text, and the absence of any sensitivity analysis for these choices weakens the paper's rigor.

### Trivial
None.

## Nice-to-Haves

- **Edge dropout rate ablation.** A sweep over {5%, 10%, 15%, 20%, 30%} would either justify the choice of 15% or reveal sensitivity that should be discussed.
- **Structured missingness evaluation.** Testing MUSE under block-missing patterns (where certain modality pairs are jointly absent) would test whether the method generalizes beyond uniform random edge dropout.
- **Qualitative visualization of learned representations.** t-SNE or UMAP plots of patient representations colored by label and missing-modality status would further substantiate the claim of learning "modality-agnostic and label-decisive" features, complementing the cosine similarity analysis in Fig. 4.

## Removed Points

These points are flagged to be removed — treat with caution:

1. **"The handling of missing labels is straightforward and novelty is modest."** — Removed because this is a subjective judgment about degree of innovation, not a verifiable weakness. The method is simple (including unlabeled patients in the unsupervised contrastive loss), but effectiveness is not the same as complexity. The paper's contribution is a complete system that works well, not a theoretically novel mechanism for semi-supervised learning, and it does not overclaim this aspect. The ablation study (Table 3) shows that removing the unsupervised loss (A4) causes a significant performance drop, confirming its practical importance.

2. **"Missing related works."** — Removed per instructions: I do not have external sources to confirm or deny missing related works.

3. **A criticism about the comparison with GRAPE being "not fully controlled" due to possible suboptimal default hyperparameters.** — This is retained above but weakened from the original formulation. The harsh critic presented this as a "critical issue," but the paper's own ablation (A2 = MUSE without contrastive losses, which is structurally similar to GRAPE + edge augmentation) shows performance at GRAPE's level, indicating the comparison is not severely biased. It is listed under Minor rather than Major.

## Novel Insights

None beyond the paper's own contributions. The reviews affirm the paper's stated strengths (effective bipartite graph design, mutual-consistent contrastive loss, thorough empirical validation) and surface specific areas for improvement (factual correction, missing ablations, lack of limitations section), but no reviewer observation fundamentally reframes or extends the paper's technical narrative.

## Suggestions

- Correct the eICU dataset description (location and statistics) and verify all dataset numbers in the paper to avoid future credibility concerns.
- Add a brief sensitivity analysis for the edge dropout rate in the main text or supplement — this is the central augmentation mechanism and its sensitivity should be characterized.
- Include a limitations section in the final version to improve scientific completeness.
- Report the temperature τ value and the relative weighting of the three loss terms in the main text.
- Clarify the hyperparameter tuning protocol for each baseline method.
