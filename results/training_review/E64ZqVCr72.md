Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

This paper proposes an active domain adaptation (ADA) method for medical image classification that uses feature disentanglement to separate domain-specific features ($z_{dom}$) from task-specific features ($z_{task}$). It then defines a multi-criteria informativeness score ($Q_{Inf}$) combining uncertainty, domainness, density, and novelty to select informative target-domain samples. The method is evaluated on CAMELYON17 (histopathology) and two chest X-ray datasets (NIH/CheXpert), with ablation studies for each loss term and informativeness criterion.

## Strengths

- **Novel feature disentanglement tailored for ADA**: The paper proposes a principled decomposition of features into $z_{dom}$ and $z_{task}$ with explicit loss terms (L1 minimizing cross-domain $z_{dom}$ similarity, L2 maximizing $z_{task}$ similarity, L3 encouraging orthogonality between $z_{dom}$ and $z_{task}$, and L_base preserving task-relevant information). This goes beyond prior ADA methods (AADA, CLUE) that use adversarial discriminators or uncertainty-weighted clustering without explicit feature decomposition. The ablation studies reported in Tables 2 and 4 confirm that each loss term contributes positively.

- **Comprehensive four-criteria informativeness score**: Rather than relying on uncertainty or diversity alone, $Q_{Inf}$ integrates four complementary signals — uncertainty (predictive entropy), domainness (filtering outliers and already-covered samples via cosine similarity thresholds), density (representativeness in feature space), and novelty (avoiding redundant annotation). This addresses known failure modes of single-criterion AL under domain shift (miscalibration from uncertainty-only, sampling from already-aligned regions in diversity-only). The ablation results indicate each component is necessary for best performance.

- **Evaluation across multiple medical imaging modalities**: The method is tested on histopathology (CAMELYON17, 5-center tumor classification) and chest X-ray (NIH→CheXpert and reverse), covering different imaging types, domain shifts, and classification tasks. This multi-dataset evaluation supports the claim of generalizability beyond a single domain shift scenario. The comparison includes 6+ relevant baselines (AADA, BADGE, CLUE, Entropy, Ma et al., Fu et al.) as well as UDA methods (DANN, MMD, cycleGAN, GCAN, GCN2).

## Weaknesses

### Fatal
None.

### Major

- **Ambiguous evaluation protocol creates risk of data leakage (Line 147)**. The paper states: "We use the source domain and part of the target dataset to train our feature disentanglement method, and use it on the remaining target domain samples." It does not specify what fraction of the target data is used for FDN training, how this split is made (random? stratified?), or whether these FDN-training samples are later eligible for active selection. If the same target samples used to train the FDN also appear in the candidate pool for active selection, or if the "separate test set" overlaps with either set, the results could be invalid. Without clarifying the data partitioning — how much target data goes to FDN training vs. the candidate pool vs. the held-out test set — the experimental design is not fully verifiable. This is the most significant issue in the paper.

- **Chest X-ray evaluation limited to a single disease label (Table 4, Line 185)**. The paper reports active DA results only for the "Infiltration" condition out of 14 disease labels in the NIH/CheXpert datasets. No justification is given for this narrow selection. Since the datasets have multi-label settings and the paper's central claim is state-of-the-art performance on chest X-ray classification, evaluating only one condition is insufficient to support this claim. Results on additional labels are needed, or a clear rationale for why Infiltration is representative.

- **Inconsistency in density score description (Lines 113–117)**. The text describes computing "feature distance" and states "a higher average feature distance indicates that the sample is more similar to other samples," which is contradictory under standard definitions (distance increases with dissimilarity). Meanwhile, the formula (Eq. 9) computes average cosine similarity, where higher values do indicate greater similarity. The text and formula disagree on what is being computed (distance vs. similarity). While the formula is what matters for reproducibility, the textual contradiction suggests unclear reasoning and could confuse readers implementing the method.

### Minor

- **Clustering algorithm not specified for density score (Line 113)**. The paper states "We cluster the target domain samples into $N$ clusters using the task specific features" but does not name the algorithm (e.g., KMeans, spectral clustering). Since the density score depends on cluster assignments, this omission affects reproducibility. (Note: KMeans++ is mentioned for BADGE in the baselines, but not for the proposed method's own clustering.)

- **Percentile thresholds $\eta_1, \eta_2$ not justified (Line 111)**. The paper sets $\eta_1$ at the 30th percentile and $\eta_2$ at the 75th percentile of the cosine similarity distribution, with no rationale for these specific values. Since thresholds likely affect which samples are filtered as outliers vs. redundant, and the values differ across datasets (CAMELYON17: 0.21/0.82, NIH: 0.24/0.78, CheXpert: 0.29/0.8), the paper should discuss sensitivity to these choices or provide a principled method for setting them.

- **Feature normalization for cosine similarity not specified**. All four criteria ($L1, L2, L3, L_{base}, Q_{dom}, Q_{density}, Q_{novel}$) compute cosine similarity, but the paper never states whether feature vectors are L2-normalized before the dot product. This is a standard prerequisite for cosine similarity to be meaningful, and the omission is a reproducibility gap.

- **No visualization of disentanglement quality**. The paper claims that $z_{task}$ clusters by class and $z_{dom}$ captures domain identity, but provides no empirical support (e.g., t-SNE plots, domain classification accuracy from $z_{dom}$). Without this, the core claim that disentanglement is working as intended rests entirely on downstream task performance.

### Trivial

- **Repeated variable name in hyperparameter listing (Line 156)**: $\lambda_{Density}$ appears multiple times in the CAMELYON17 parameter string due to a parser artifact.
- **Minor formatting issues** in the parsed text (e.g., line 99 garbled text) — these are parser artifacts from PDF extraction, not author errors.

## Nice-to-Haves

- Evaluate on additional disease labels from NIH/CheXpert beyond Infiltration to substantiate the chest X-ray claims.
- Provide t-SNE visualizations of $z_{task}$ (colored by class) and $z_{dom}$ (colored by domain) to validate the disentanglement qualitatively.
- Compare against a variant that uses the same four scoring criteria computed from standard (non-disentangled) features (e.g., DenseNet-121 penultimate layer) to isolate whether disentanglement itself improves sample selection.
- Report sensitivity analysis for the percentile thresholds $\eta_1, \eta_2$.
- Clarify the proportion of target data used for FDN training vs. the candidate pool vs. held-out test set.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Missing experimental results / tables contain no numeric values"**: The tables (Tables 1–4) appear as image placeholders in the parsed text, but they exist as embedded images in the original PDF. The paper explicitly references them and discusses comparative performance. This is a PDF parsing artifact, not an author omission. **Reason: Parser artifact (hard rule).**

- **"Unclear alignment between ASDA and AUDA settings"**: The paper clearly separates UDA results (Tables 1, 3) from active DA results (Tables 2, 4) and explains the distinction in Section 3 (ASDA = selecting samples to label, AUDA = selecting unlabeled samples for the training pool). The tables and text are consistently structured. **Reason: Misreading of the paper (hard rule).**

- **"Claim that 'none explore DA with active learning' is false"**: This claim (Line 27) refers specifically to the UDA methods discussed in that paragraph (Ahn et al., Chang et al., Ma et al., Wu et al.), not to the general literature. The paper's separate ADA section (Lines 31–33) correctly cites AADA and CLUE as prior ADA methods. **Reason: Misreading of the paper (hard rule).**

- **"No-ADA baseline is missing"**: The No-ADA baseline is explicitly described in Line 160: "As a baseline, we perform the experiment without domain adaptation denoted as No-ADA." **Reason: Factually incorrect (hard rule).**

- **"Motivation for combining AL with DA is unsupported by concrete example"**: The paper provides a concrete motivation in Lines 33–34, citing miscalibration under domain shift (Ovadia et al., 2019) and the tendency of diversity sampling to select from already-aligned regions (Prabhu et al., 2021). This adequately grounds the motivation in prior work. **Reason: Strawman weakness (hard rule).**

- **"Missing related works"**: Cannot be verified without external sources. Per instructions, this is removed. **Reason: Cannot verify existence (hard rule).**

- **Formatting/style nitpicks** (e.g., "shallow" literature review, "overstates novelty"). These are subjective judgments that do not affect the technical evaluation. **Reason: Soft, overruled.**

- **Stepwise hyperparameter tuning being suboptimal**: The paper acknowledges this (Line 194) and states it takes "extra precautions of multiple cross checks and using fixed seed values." This is a standard practice in many medical imaging papers. **Reason: Weakens to minor/trivial; not a core flaw.**

## Novel Insights

The most interesting observation from the reviews — which the paper itself could exploit more — is the dual role of the disentangled features. $z_{dom}$ is used for domainness filtering (rejecting outliers and already-covered samples), while $z_{task}$ is used for the other three scoring criteria. This creates an implicit feature selection: samples are filtered by domain relevance first, then ranked by task informativeness. The paper's ablation studies suggest that removing the $L_{base}$ loss term (which ties $z_{task}$ to the original classifier's features) causes the largest performance drop at the disentanglement stage, while the novelty criterion $Q_{novel}$ contributes most at the selection stage. This hierarchy of importance (feature quality > selection criterion) could inform future ADA system design. However, the paper does not draw this connection explicitly.

## Suggestions

1. **Clarify the target data partitioning**: Specify how much target data is used for FDN training, how the candidate pool for active selection is constructed, and how the held-out test set is separated. Explicitly state that the FDN training samples are excluded from the candidate pool and test set to prevent leakage.

2. **Expand chest X-ray evaluation**: Report results on additional disease labels (at least a subset covering different prevalence regimes) or provide a principled justification for why Infiltration is the most informative condition to evaluate.

3. **Fix the density score description**: Replace "feature distance" with "feature similarity" (or cosine similarity) throughout the text to match the formula, and correct the contradictory statement that "higher distance indicates more similarity."

4. **Specify the clustering algorithm** used for the density criterion (e.g., KMeans, spectral clustering) and whether features are L2-normalized before computing cosine similarity throughout the method.

5. **Visualize disentanglement quality**: Add t-SNE or UMAP plots of $z_{task}$ (colored by label across both domains) and $z_{dom}$ (colored by domain) to provide direct evidence that the disentanglement is working as intended.

## Score and Decision

The paper presents a methodologically sound approach to a practically important problem. The core ideas — explicit feature disentanglement for ADA and a multi-criteria informativeness score — are novel and well-motivated. The evaluation spans multiple datasets and includes thorough ablations. However, the ambiguous evaluation protocol (risk of data leakage) and the limited chest X-ray evaluation (one disease out of 14) are substantive concerns that weaken the strength of the empirical claims. These are addressable with clarifications and additional experiments, but in their current form, they leave the evidence base incomplete.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>