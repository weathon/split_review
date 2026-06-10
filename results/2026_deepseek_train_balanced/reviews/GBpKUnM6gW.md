Now I have a complete picture of the paper. Let me write the final consolidated review.

## Summary

This paper benchmarks 13 deep learning models (7 spatial/connectivity-based, 6 sequential/time-series-based) across 6 fMRI datasets totaling 34,887 samples, covering cognitive task recognition (HCP-Task, HCP-WM) and disease diagnosis (ADNI, OASIS, PPMI, ABIDE). It additionally conducts post-hoc interpretability analysis via brain attention mapping. The paper releases preprocessed data and offers guidelines for model selection.

## Strengths

- **Large-scale multi-dataset benchmark with strong coverage of recent sequential models.** The paper evaluates 13 models (including Transformer, MLP-Mixer, Mamba) across 6 datasets — broader than prior benchmarks such as Said et al. (12 models, HCP only) and Gazzar et al. (UK Biobank only). Tables 2–3 provide 13 models × 6 datasets results, directly supporting the paper's claim of a comprehensive evaluation.

- **Separated Scan 1 & Scan 2 test-retest experimental design.** The paper implements a unique setting (Section 5.1, lines 117–118) where models are trained on one fMRI session and tested on a separate session of the same tasks. The large accuracy gap between the Separated and Mixed settings (e.g., GIN: 27.23% vs. 62.07% for HCP-WM, Table 2) surfaces model replicability issues that prior benchmarks did not address. This is a genuinely useful methodological contribution.

- **Neuroscience-grounded interpretation of performance patterns.** Rather than reporting scores alone, the paper provides domain-specific explanations for why different model types excel in different settings: (Remarks 1.1) sequential models outperform on task fMRI because "network organization remains stable regardless of brain states switching from task to task"; (Remarks 2.1) spatial models are more effective for neurodegenerative disease diagnosis because ND can be understood as a disconnection syndrome. This neuroscience-guided analysis adds value beyond a typical leaderboard benchmark.

- **Public release of preprocessed data** (stated in Conclusions, line 297) is a practical community contribution.

## Weaknesses

### Major

- **Spatial-vs-sequential comparison is partially confounded by asymmetric input representations.** Spatial models receive static FC matrices (Pearson correlation over the entire scan, discarding temporal information), while sequential models receive raw BOLD time series. This is described in lines 112–115. The headline result — that sequential models outperform spatial models on task fMRI (especially HCP-WM) — is therefore at least partly a consequence of the input format, not purely architectural capability. The HCP-WM task (0-back vs. 2-back) is defined by temporal dynamics that a static FC matrix *cannot in principle* capture (the ~26–30% accuracy in the Separated setting is near chance for 8 classes). The paper acknowledges this briefly in Remarks 1.1 but the overall framing presents the comparison as an informative finding about architecture types rather than an artifact of input representation. A fairer comparison would include spatial models evaluated on temporally-resolved inputs (e.g., sliding-window dynamic FC) to disentangle architecture from input modality.

- **Missing experimental details that are essential for a benchmark paper.** No optimizer, learning rate, batch size, number of epochs, early stopping criterion, or hardware are reported anywhere in the main paper. There is no description of train/validation/test splits or cross-validation protocol for any dataset except the HCP scans (lines 117–118 describe the Separated-vs-Mixed split for HCP). Standard deviations are reported for the disease datasets but completely absent for HCP-Task and HCP-WM results, making it impossible to assess the stability of those outcomes. For a paper whose stated purpose is to serve as a guideline for future work, these omissions are a serious problem — the results cannot be reproduced or compared against without this information.

### Minor

- **Hypothesis H2 is referenced but never defined.** The hypotheses listed at the start of Section 5 (lines 106–109) are H1, H3, and H4. H2 is absent. The discussion (line 294) then answers H2 ("the answer to (H2) is 'YES'") without the reader ever having seen the question. This structural error undermines the paper's narrative clarity.

- **No standard deviations for HCP-Task and HCP-WM results.** These two datasets constitute the core of the task-fMRI analysis, but the reported accuracy/precision/F1 values (Table 2 top) are point estimates without any measure of variability, unlike the disease datasets where stds are provided. It is unclear whether the reported differences between models are reliable.

- **Interpretability analysis is qualitative and non-conclusive.** The post-hoc analysis extracts "critical" brain regions by fitting logistic regression on learned features (Section 7). No quantitative validation is provided — no overlap metrics with known functional atlas labels, no comparison to task-specific activation maps from the literature, no statistical test of whether identified regions are more task-relevant than chance. The section concludes with "the findings are not yet converging" and "further investigation is necessary" (Remarks 4.2), which essentially says the method does not work well. This is a known limitation, not a finding. The section would be better framed as preliminary exploration or moved to supplementary material.

- **Ceiling effects in HCP-Task Mixed are not discussed.** Mixer achieves 99.78%, LSTM 99.51%, and Transformer 99.60% in this setting, which strongly suggests the task variant may be saturated. This reduces its informativeness for differentiating models, yet the paper draws conclusions from it without caveat.

- **Class balance information is not reported for disease datasets.** This is a notable omission since ABIDE, in particular, is known to have substantial class imbalance, which affects the interpretation of reported metrics.

### Trivial

- The paper lists SPDNet as a spatial model (line 94) but then describes it as having a "spatial-temporal framework" (line 242). The categorization is functional but inconsistent.

## Nice-to-Haves

- Adding spatial-model baselines using dynamic FC (sliding-window or per-block) would strengthen the architecture-vs-input disentanglement.
- Reporting computational cost (training time, inference time, parameter counts) across the 13 models would increase practical utility.
- Correction for multiple comparisons across the 13 models × 6 datasets tested would increase statistical rigor.

## Removed Points

These points were flagged by the reviewers but removed per filtering rules:
- **Self-promotional citations in contributions paragraph** (line 35–36): Style/formatting critique, not a substantive weakness.
- **No multiple comparison correction**: Generic area-of-concern speculation; the paper's t-tests are between model groups, not all pairs.
- **H4 not explicitly answered**: The discussion (line 294) does address H4 substantively, just without a structured label; this is overly pedantic.
- **Code/data accessibility not specified**: The paper states data is publicly available (line 297); the critic assumes no URL was provided, but this may exist in a stripped section.
- **SPDNet classification inconsistency**: Trivial categorization issue that does not affect any result.
- **Strength Finder's interpretability claim**: The strength says the interpretability analysis is a meaningful contribution; this directly conflicts with the verified weakness that it is superficial and non-conclusive. Per rules, the weakness wins.

## Novel Insights

The most interesting observation that emerges from the reviews — and that is not fully developed in the paper itself — is the interaction between the Separated Scan 1 & Scan 2 design and model type. The large accuracy drops in the Separated setting suggest that many models (particularly spatial ones) are learning scan-specific confounds rather than task-general representations. The fact that sequential models degrade less severely (e.g., RNN drops from 90.67% to 61.55% on HCP-WM, while GCN drops from 68.97% to 26.83%) hints at systematic differences in how these model families generalize across sessions. This could be a fruitful direction for future work on fMRI model robustness, but the paper does not pursue it.

## Suggestions

1. **Report full training details** (optimizer, learning rate schedule, batch size, epochs, hardware, cross-validation protocol) and add standard deviations to all results — not just the disease datasets.
2. **Acknowledge the input confound explicitly** in the spatial-vs-sequential comparison and either (a) add dynamic-FC baselines for spatial models, or (b) reframe the comparison as evaluating input representations rather than architectural families.
3. **Define H2** in the hypothesis list and either explicitly frame the answer to H4 or remove it from the hypothesis set.
4. **Substantially deepen or remove the interpretability section.** Either add quantitative validation (overlap with known functional atlases, statistical enrichment tests) or acknowledge it as preliminary exploratory analysis and move it to supplementary material, reserving the main paper for the core benchmark results.
5. **Add a discussion of ceiling effects** in the HCP-Task Mixed setting and caveat conclusions drawn from that condition.

## Score and Decision

The paper makes a genuinely useful contribution to the fMRI deep learning community — the scale of the benchmark (13 models, 6 datasets, 34,887 samples) and the novel separated-scans experimental design provide value beyond existing benchmarks. The neuroscience-grounded interpretation of results adds depth that pure accuracy tables lack.

However, the missing experimental details are a significant problem for a paper that aims to serve as a definitive reference: results without training configuration, validation splits, or standard deviations on the core HCP experiments cannot be reliably used by practitioners. The spatial-vs-sequential comparison is partly confounded by input representation, and while the paper acknowledges this, its framing overstates what can be concluded about architecture. The hypothesis structure has an internal error (H2 undefined). The interpretability section is too weak to support the claims made about it.

These issues are fixable, but in its current form the paper does not meet the standard for a top venue.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>