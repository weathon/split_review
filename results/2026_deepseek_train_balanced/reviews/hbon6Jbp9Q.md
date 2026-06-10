## Summary

This paper proposes a three-stage pipeline for identifying and interpreting region-specific semantic representations in the brain: (1) supervised pruning of GloVe embedding dimensions to maximize representational alignment with individual fMRI-derived activation clusters, (2) probing the pruned features against human semantic ratings (Binder et al., 2016, 534 words × 65 dimensions) to interpret their content, and (3) constructing a graph of feature co-occurrence across brain regions to identify semantic communities. The core idea—using brain data to select LM subspaces and then interpreting those subspaces via probing—is conceptually interesting and addresses genuine limitations in prior work that relies on hand-crafted semantic encoders.

## Strengths

1. **Pruning consistently improves representational alignment across all 22 clusters, validated with held-out data.** The mean Spearman correlation between GloVe and brain similarity matrices increases from M=0.025 (full 300 features) to M=0.314 (pruned, ~47 features) on the full dataset, and from M=0.031 to M=0.143 in leave-one-out cross-validation (Section 3.1, lines 85–89). The non-pruned values (~0.025) are typical of prior DNN–brain alignment studies, demonstrating a meaningful quantitative improvement.

2. **Different brain regions select markedly different GloVe subspaces, demonstrating region-specificity.** Of the 300 GloVe features, 50 were never selected in any solution, another 50 were selected only once, and no single feature appeared in more than 17 of 22 solutions (line 97). This high selectivity diversity shows that the identified subspaces are regionally differentiated rather than converging on a single semantic subspace.

3. **The probing reveals an asymmetric neurobiological pattern: sensory-motor features are encoded broadly, while social/cognitive dimensions co-occur only with sensory encoding, not vice versa.** This finding (abstract, line 4; Section 3.2, line 104) emerges from applying the probing analysis to an independent dataset (Binder et al., 534 words) that was not involved in pruning. It is an interpretable, non-trivial observation about the hierarchical organization of semantic representations.

4. **The method reduces reliance on hand-crafted semantic encoders.** The pipeline does not require collecting human feature ratings for the same stimuli used in the fMRI recordings (lines 29–30), which is a genuine advance. Pruning is driven by brain data rather than experimenter intuition, reducing a source of potential bias in encoding-model construction.

## Weaknesses

### Fatal

None.

### Major

1. **No control for dimensionality-reduction artifact (pruning vs. random subsets of equal size).** The paper compares pruned GloVe (~47–50/300 dimensions) against full GloVe (300 dimensions) and reports large improvements. However, any dimensionality reduction—even random selection—can improve alignment by discarding noisy dimensions. Without comparing against random subsets of the same size (repeated to establish a null distribution) or against PCA-reduced GloVe of equivalent dimensionality, the central quantitative claim (that pruning discovers *brain-relevant* subspaces rather than simply benefiting from any dimensionality reduction) cannot be evaluated. The diversity of feature selection across clusters (Strength 2) provides partial counter-evidence, but without a controlled baseline, the core result remains confounded. The large drop from full-data (ρ=0.314) to LOOCV (ρ=0.143) further raises overfitting concerns that a random-subset baseline would help contextualize.

2. **Probing does not validate region-specificity of the selected features.** The probing analysis (Section 3.2) shows that different pruned feature subsets F_c predict different Binder semantic dimensions. But this analysis demonstrates only that different GloVe subsets encode different information—which is likely true of any partition of GloVe dimensions. A proper validation would test whether F_c (features selected for cluster c) better predicts the neural response properties of cluster c than F_{c'} (features selected for a different cluster c'). Without this cross-validation, the probing results are descriptive rather than linked to specific brain regions. The claim that "different brain activation clusters selected for features with different levels of relevant information" (line 104) is not actually shown—what is shown is that different feature subsets encode different information, which is not the same claim.

3. **Probing uses complete-dataset pruning solutions rather than CV-based feature sets.** The probing analysis (line 103) uses pruning solutions from the "Complete Dataset, Feature 1" column of Table 1, not the leave-one-out cross-validation solutions. Since these features were selected to fit all 60 words (including noise), the probing evaluation on an independent 534-word dataset may still reflect overfitted structure. Reporting probing results from CV-derived feature sets would substantially strengthen confidence in the identified semantic patterns.

### Minor

1. **The graph/community analysis yields mixed results that weakly support the conclusions drawn.** For Simlex-999, no community outperforms the full set and the paper acknowledges "no clear conclusions can be made" (line 117). For the analogy tasks (Section 3.3.2), no community outperforms the full set, and ablation effects are tiny (e.g., 0.79 vs. 0.77 for grammar-plural; 0.61 vs. 0.60 for grammar-plural-verbs)—differences within measurement noise. The Wordsim-353 result (Community 1 at ρ=0.652 vs. full set ρ=0.658) is the strongest signal, but the overall contribution of the graph analysis to the paper's thesis is limited.

2. **The probing results (Figure 2) lack statistical testing despite reporting 1,430 values (22 clusters × 65 dimensions).** The paper draws qualitative conclusions from observed patterns—"some clusters code for Vision more precisely than Audition," "coding of Somatic and Audition features is found in clusters that also track Vision information"—without significance thresholds, confidence intervals, or multiple-comparison correction. For a top venue, descriptive reporting of this volume of correlations is insufficient to support the interpretive narrative.

3. **No direct comparison against the Mitchell et al. (2008) encoding model that the paper claims to advance on.** The paper frames itself as improving upon Mitchell et al. and Fernandino et al. (lines 29–30), who use 25 handcrafted semantic features. The authors already possess this model (they use it for voxel selection). A comparison of how well the 25-feature encoding model predicts the same 22 cluster similarity matrices would directly calibrate the improvement offered by pruning.

4. **Large drop from full-data (ρ=0.314) to LOOCV (ρ=0.143) suggests overfitting that is not adequately discussed.** While LOOCV still shows improvement over the baseline (0.031→0.143), the correlation more than halves when moving to held-out words. The paper does not report the stability of selected feature indices across CV folds (e.g., mean overlap of selected dimensions across folds), which would help quantify overfitting. The LOOCV design (leave one word out of 60) is also relatively weak compared to k-fold with larger held-out sets.

### Trivial

1. The feature ranking metric for sequential selection (Section 2.4, line 57) is not specified. The paper states features are "ranked by their importance in predicting the brain-derived S_c" without stating whether this is mutual information, correlation, regression coefficient, or another measure.

2. Figure 2 does not link cluster rows to the anatomical labels in Table 1, making it impossible to relate probing profiles to specific brain areas.

3. Several arbitrary thresholds in the clustering pipeline (median split of R², 10mm distance, r≥0.5 for grouping similarity matrices, minimum 3 members) are not tested for sensitivity.

## Nice-to-Haves

- A comparison against random GloVe subsets (repeated 1000x to establish a null distribution) and PCA-reduced GloVe at matched dimensionality would address the central confound and is the single most impactful addition possible.
- Cross-validating the probing: test whether each cluster's F_c predicts that cluster's neural similarity structure better than other clusters' F_{c'}.
- Reporting feature-selection stability across CV folds (e.g., Jaccard overlap of selected feature indices).

## Removed Points

*These points were surfaced by the reviewers but removed from the main review after verification against the paper. They are included for completeness but should be treated with caution.*

From Harsh Critic:
- *Criticism about the word "objective" being misleading*: The paper explicitly states the method provides "interpretation... without requiring human annotations for the items producing the neurobiological responses" (line 29), which is factually accurate. The probing step uses annotations from Binder et al. for a different set of words, which is a separate, interpretative step, not part of the encoding model.
- *Criticism that the graph analysis is "null or very weak"*: The Wordsim-353 result (Community 1: ρ=0.652 vs. full set: ρ=0.658) shows a meaningful signal. While overall graph results are mixed, calling them "null" overstates the case; the paper also acknowledges its own limitations here.
- *Claim that the second improvement is "overstated" because probing uses human annotations*: The paper's claim is specifically about not needing annotations for the *same* stimuli as the recordings. This is properly scoped and accurate.

From Strength Finder:
- *Overstated strength about graph analysis providing "converging evidence" via three benchmarks*: The graph results are mixed (null for Simlex-999, differential but not superior for analogies). This strength claim was overstated and removed; the main review appropriately reflects the mixed nature of these results.

## Novel Insights

The most interesting observation from synthesizing the reviews is the tension between the paper's two strongest findings. The high diversity of selected features across clusters (50 features never selected, no feature in >17/22 solutions) argues for genuine region-specificity, yet the absence of a random-subset baseline leaves open the question of whether any dimensionality reduction would produce similar correlation improvements. Resolving this tension (by running the random-subset control) would either substantially strengthen or substantially weaken the paper's core claim. Second, the asymmetric hierarchical pattern in probing (social/cognitive regions also encode sensory features, but not vice versa) is the most novel neurobiological observation, but it rests entirely on qualitative pattern-reading of Figure 2 without statistical testing. The paper would benefit from formalizing this as a testable hypothesis with proper inferential statistics rather than presenting it as a confirmed finding.

## Suggestions

1. **Most critical: add a random-subset baseline.** Run pruning with random subsets of the same size (≥1000 random draws of ~47 features per cluster) and compare the distribution of Spearman correlations against brain-supervised pruning. This directly addresses the central confound.
2. **Cross-validate the probing region-specificity.** Test whether each cluster's pruned features better predict that cluster's neural similarity structure than other clusters' features. This would link the descriptive probing profiles to brain data.
3. **Add statistical rigor to Figure 2.** Report which correlations are significant after FDR correction, or clearly label the analysis as exploratory. Provide confidence intervals via bootstrap.
4. **Report probing results using CV-derived feature sets** (not just complete-dataset solutions) to demonstrate the interpretable structure is not an artifact of fitting all 60 words.
5. **Compare against the Mitchell et al. (2008) encoding model** for predicting the 22 cluster similarity matrices. This is trivially computable and would directly calibrate the improvement.

## Score and Decision

The paper proposes a genuinely interesting pipeline and produces compelling descriptive results, particularly the diversity of feature selection across clusters and the asymmetric sensory-vs-social pattern in probing. However, the core quantitative claim (that pruning discovers brain-relevant subspaces) is undermined by the absence of a basic dimensionality-reduction control. The probing narrative lacks statistical rigor and region-specificity validation. These are substantive issues that prevent the paper from meeting the evidentiary bar of a top venue in its current form. The approach is worth pursuing, but the evidence as presented does not adequately support the conclusions drawn.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>