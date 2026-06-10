I have analyzed the paper thoroughly and verified each reviewer claim against the actual text. Here is my consolidated review.

---

## Summary

The paper proposes a hybrid anomaly detection method combining a familiarity-based score (nearest-neighbor distance in feature space, FFS) with a novelty score derived from B-cos network explanations (ENS). The core insight is that familiarity-only methods miss anomalies caused by truly novel features the encoder cannot represent. The method is evaluated across sensory and semantic anomaly benchmarks, and the paper claims that adding the ENS score reduces errors by up to 40% while eliminating the need for dense feature matching and complex background models.

## Strengths

1. **Novel conceptual contribution**: Using explanation alignment (what the encoder cannot explain) as a signal for novelty in anomaly detection is genuinely new and well-motivated. The paper clearly articulates the limitation of the familiarity hypothesis (lines 15, 80) and proposes a principled alternative.

2. **Bridges the sensory/semantic performance gap**: The paper demonstrates (lines 167–168) that while PatchCore excels at sensory AD and FITYMI excels at semantic AD, no prior single method handles both well. The hybrid approach narrows this gap, providing evidence that combining familiarity and novelty scores unifies these regimes that prior work treats as separate.

3. **ENS alone achieves competitive sensory performance without feature memory**: On MVTec, ENS alone (no FFS, no KNN retrieval) performs competitively with familiarity-based methods "without using feature representations of normal samples" (line 154), offering a structural advantage in memory and computation cost over dense-matching approaches like PatchCore.

4. **Gaussian background approximation works comparably to diffusion models**: Section 5.3 (lines 186–190) shows that a simple Gaussian fit to the normal class yields a mean improvement of ~0.2% AUROC over using a prematurely-stopped diffusion model, directly supporting the claim of reduced reliance on expensive background generation.

5. **Method provides interpretable anomaly explanations**: For sensory anomalies, the B-cos explanation maps to the input image, giving pixel-level localization (Figure 4, lines 152–154), which contrasts with the opacity of prior methods noted in Section 2.

## Weaknesses

### Major

1. **Inconsistent metric labeling for the headline quantitative claim**: The abstract and conclusion consistently claim "reduce false negative anomalies by up to 40%" (lines 5, 24, 197). However, the results text in Section 5.2 says "reduces the number of false positives by about 40%" (line 173), and Figure 6's caption reads "Comparing the false positives... rate of FP... % reduction in FP" (line 171). The section header calls it "Reduced False negatives" but the body describes false positive reduction. These are different error types with different practical interpretations. This inconsistency undermines confidence in the evaluation's precision and must be resolved — the reader cannot tell which metric improved by 40%.

2. **Oracle-threshold protocol overstates practical significance of the 40% figure**: The paper states "We use an oracle to find the optimum threshold for each class of each dataset" (line 173) when converting scores to binary predictions. An oracle-chosen threshold yields the *maximum possible* reduction under perfect threshold selection, not what a practitioner would achieve at deployment. The 40% figure should be supplemented with results at fixed, realistic operating points (e.g., the threshold that achieves 95% TPR on normal data).

### Minor

3. **Limited scope of the ablation isolating ENS from backbone choice**: The ablation comparing FFS vs. FFS+ENS (Section 5.2, Figure 6) is the key evidence that ENS adds value beyond the B-cos backbone. It does exist — the paper verifiably includes it — but it is only reported on 3 datasets and uses oracle-threshold evaluation. The main benchmark (Table 1) compares the full method against prior methods but does not include an FFS-only baseline with the same B-cos backbone. This means the relative contribution of ENS vs. the backbone switch cannot be assessed from the primary results table, which is where the SOTA claim is anchored.

4. **Conceptual gap between formal definition and operational proxy is unexamined**: Novel features are formally defined as $\hat{x}_{\text{test}} - \hat{F}(\theta)$ — features the encoder *cannot encode* (line 74). But ENS measures cosine similarity between the input and the B-cos explanation of the *classifier's decision* — i.e., features that do not align with the classifier's logic. The paper acknowledges this as an "approximation" (line 111) but does not discuss what systematic errors this proxy introduces. A feature could be misaligned with the anomaly-classifier's explanation because it supports the "normal" decision rather than because the encoder cannot represent it. This gap between "encoder cannot encode" and "explanation does not align with classifier's decision" is conceptually significant and unaddressed.

5. **Layer-selection hyperparameter $i$ is not explored**: The choices ($i=0$ for sensory, $i=6$ for far semantic, $i=L-1$ for near semantic) are stated without sensitivity analysis. The paper says "further exploration of this parameter is left for future work" (line 161). While the fixed choices are reasonable, the absence of any ablation means the reader cannot gauge how critical these values are or whether performance could vary substantially with tuning.

### Trivial

6. **No variance or confidence intervals reported**: No standard deviations, confidence intervals, or per-run variability is reported for any result. Given that results appear to be from single runs, the stability of the reported improvements is unclear.

## Nice-to-Haves

- Reporting the 40% error reduction at a fixed, non-oracle operating point (e.g., 95% TPR on normal data) would substantially strengthen practical relevance, with the oracle result retained as an upper bound.
- A systematic exploration of the layer parameter $i$ on at least one dataset per anomaly type would help understand the method's sensitivity.
- Adding the FFS-only baseline (same B-cos backbone, without ENS) to the main benchmark table would allow direct assessment of the ENS contribution in the primary results.

## Removed Points

These points from the input reviews are removed per filtering rules:

- Criticisms about parser artifacts (truncated sentence "$1." on line 168, OCR-distorted math notation in lines 62–63, inaccessible Table 1 / Figure 6 content): these are PDF parsing artifacts, not author errors — the content exists in the original submission.
- The "sensory and sensory anomalies" duplication (line 47): this is either a typo or a parser artifact; removed as a formatting-level issue.
- The harsh critic's assertion that the controlled ablation is "absent": this is factually inaccurate — the ablation comparing FFS vs. FFS+ENS exists in Section 5.2 (line 173); the criticism is retained above in weakened form (limited scope, not absence).
- Criticisms about missing related works: per hard rules, I cannot assess completeness without external sources.
- Reproducibility nitpicks about undisclosed hyperparameters: these are standard implementation details that are impractical to fully enumerate in a conference submission.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Resolve the false-negative/false-positive inconsistency** throughout the paper, ensuring the abstract, results text, and figure captions describe the same metric consistently.
2. **Add the FFS-only baseline (same B-cos backbone, without ENS) to the main benchmark table** so the ENS contribution can be directly assessed across all 8 datasets, not just the 3 in the ablation figure.
3. **Report the 40% reduction at a fixed, non-oracle operating point** (e.g., the threshold achieving 95% TPR on normal data) to demonstrate practical significance, with the oracle result retained as an upper bound.
4. **Discuss the conceptual gap** between formal novel features (features the encoder cannot encode) and the ENS proxy (features not aligned with the classifier's explanation), including what types of errors this approximation might introduce.
5. **Add standard deviations or confidence intervals** for all main results, or at minimum note that results are single-run and discuss expected variance.

## Score and Decision

The paper proposes a genuinely novel approach to anomaly detection — using explanation alignment to capture novelty — which is a well-motivated and creative contribution. The method is clearly described, and several experiments support its promise. However, the evaluation is undermined by a metric inconsistency in the headline quantitative claim (false negatives vs. false positives, swapped between abstract and results text), the use of oracle-threshold evaluation without a real-world operating point comparison, and the absence of an FFS-only baseline in the main benchmark table. These issues do not invalidate the core idea but prevent the paper from convincingly supporting its SOTA claims in the current form. A major revision with consistent reporting, proper ablation baselines in the main table, and non-oracle evaluation is needed.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>