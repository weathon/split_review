Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper systematically investigates camera bias in person ReID models, focusing on the overlooked problem of bias on unseen domains. It provides empirical analysis of why camera-specific feature normalization has a debiasing effect (showing that camera-sensitive dimensions dominate the effect), extends the analysis to detailed bias factors (low-level image properties, body angle), and identifies camera bias risks in unsupervised learning, proposing simple mitigation strategies that yield large improvements. The paper is primarily an empirical analysis/study rather than a new method paper.

## Strengths

1. **First systematic quantification of camera bias on unseen domains**: While prior work focused on training-domain bias, this paper measures camera bias via NMI across four datasets (Market-1501, CUHK03-NP, PersonX, MSMT17) using models trained on MSMT17, showing that all model types—supervised, unsupervised, camera-aware, and domain-generalizable—exhibit substantial bias on unseen domains (Table 1). This establishes a previously overlooked problem.

2. **Mechanistic explanation of why feature normalization debiases**: The paper analyzes the 384-dimensional embedding space and shows that features move consistently in camera-sensitive dimensions under camera changes (Figure 2b). Camera-specific centering on just the top-50 sensitive dimensions (~13%) achieves roughly half the total mAP gain, while bottom-50 dimensions contribute almost nothing (Figure 2c). This goes beyond the ad-hoc use of normalization in prior work (Gu et al., 2020; Luo et al., 2021a) by revealing the underlying mechanism.

3. **Comprehensive evaluation across architectures and methods**: Camera-specific feature normalization is tested on 12 different ReID models including ResNet-50, ViT, domain-generalized (ISR, PAT), and unsupervised (CC, PPLR) methods on three unseen domains (Table 3), consistently improving mAP and reducing bias. The ablation (Table 4) cleanly isolates that camera-specific mean centering is the dominant factor, with scaling providing small additional gain and ZCA rotation offering no definite benefit.

4. **Identification of camera bias risk in unsupervised learning with actionable mitigation**: Toy experiments (Figure 6) demonstrate that pseudo labels with higher camera bias degrade performance despite having higher accuracy, and that single-camera clusters are harmful. The proposed simple strategies (debiased pseudo labeling via feature normalization, discarding single-camera clusters) yield substantial gains on MSMT17 (Table 6). This is a practical contribution that can be easily integrated into existing USL pipelines.

5. **Generalizability of debiasing to detailed bias factors**: The paper shows that feature normalization extends to low-level image properties (brightness, sharpness, area) and body angle (Table 2), and that combining property groups with camera labels yields further gains (Figure 3c). This demonstrates broader applicability and suggests that camera bias is just one component of a larger family of feature-space biases in ReID.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Body-angle label acquisition method unspecified**: The paper defines three body angle classes (front, back, side) and constructs angle-labeled datasets from Market-1501 (Section 4.3, Table 2), but never describes how these labels were obtained—whether via manual annotation, an automatic pose estimator, camera geometry, or another method. This is a reproducibility gap for the analysis experiments. The paper should specify the labeling procedure so readers can assess the reliability of the angle-based results.

2. **Unsupervised learning gains lack adequate baseline context in text**: The paper reports a "19.3% mAP increase for CC" on MSMT17 (Section 5.4) and similar large gains. While Table 6 contains the before/after numbers and the paper states baselines are reproduced with official code, the text does not quote the absolute baseline mAP/Rank-1 values, making it difficult for a reader to contextualize whether these are large relative or absolute gains. Given that these improvements are unusually large for simple post-hoc modifications, providing baseline numbers in the text (e.g., "CC improves from X% to Y% mAP") would substantially improve credibility. The current presentation forces readers to rely solely on the (image-embedded) table.

3. **No variance or statistical significance reporting**: The main results (Tables 3, 6) are reported as single numbers without standard deviation across runs. For an empirical claims paper where some improvements are large (e.g., +19.3% mAP), reporting at least mean and std over multiple runs would increase confidence that the gains are not artifacts of a single seed.

4. **Clustering method for NMI measurement not justified**: The paper uses InfoMAP (Section 3) for clustering to compute NMI bias scores. InfoMAP is not standard in ReID; a brief justification or a note that the qualitative conclusions are robust across clustering methods would strengthen the analysis. As the reviewer notes, this is unlikely to change the main message since the conclusions are qualitative (bias exists), but a brief justification would be helpful.

5. **The "detailed bias factors" analysis acknowledges applicability limitations only implicitly**: The analysis on low-level image properties (brightness, sharpness, area) and body angle (Section 4.3) requires property-group labels that are not available at inference time in standard deployment. The paper could more clearly state that these experiments are diagnostic (to understand *what* the normalization captures) rather than providing a ready-to-use technique. The current framing could be read as implying broader applicability than is justified for practitioners.

6. **Element-wise operations in normalization formula could be more precise**: Equation 1 in Section 4.1 uses `√(·)` over an element-wise product, and it would benefit from clarifying that the square root is applied element-wise and that an epsilon smoothing term is needed for numerical stability in dimensions where a camera has near-zero variance.

### Trivial

1. **Section 4.2 dimension analysis**: The dimension ordering by variance of camera means is an approximate proxy for camera-sensitivity; a direct measure (e.g., mutual information between dimension value and camera label) would be cleaner. The paper could note this approximation.

## Nice-to-Haves

- Comparison to global (non-camera-specific) feature normalization: Does subtracting the global mean and dividing by global std achieve a similar debiasing effect, or is per-camera treatment necessary? This would strengthen the motivation for camera-specific treatment.
- A limitations paragraph covering: (a) the need for camera labels at test time, (b) potential harms when few samples per camera are available, (c) trade-offs of discarding single-camera clusters on small datasets.
- Discussion of whether the USL improvements are robust across different clustering algorithms (DBSCAN vs. others).

## Removed Points

These points are flagged to be removed, treat them with caution:
- **Color coding lost / garbled tables**: Parser extraction artifacts, not author errors. The original submission contains these correctly.
- **"Implausibly large gains" framed as structural/fatal flaw**: The reviewer's concern about baseline quality is partially addressed by the paper stating results are reproduced with official code. The issue is real but minor (presentation clarity), not fatal. The paper provides baseline numbers in Table 6 (image-embedded) and discusses experimental setup.
- **"Domain shift already known to degrade performance"**: The paper already acknowledges this; the novelty is measuring the camera-specific component of that degradation.
- **Missing related work on normalization**: The paper already discusses prior normalization work (Gu et al., 2020; Luo et al., 2021a; Zhuang et al., 2020) and frames its contribution as analyzing *why* it works.
- **Formatting/style nitpicks about specific sentences or figures**: These are subjective or cosmetic and do not affect the contribution.

## Novel Insights

The reviews surface an important tension: the paper's strongest contribution (mechanistic analysis of why feature normalization debiases, Sections 4.2–4.3) is the most defensible and original part, while the most practically striking results (USL improvements in Section 5.4) are the least verified from a reproducibility standpoint. This asymmetry means the paper does not need the USL results to stand as a valuable empirical study—the core analysis of camera bias across domains and the dissection of normalization's effect on camera-sensitive dimensions is a genuine contribution regardless. Conversely, if the USL gains are genuine, they substantially raise the paper's practical impact. The reviews correctly identify that the paper would be strengthened by transparently contextualizing the USL gains so readers can assess them, without undermining the rest of the work.

## Suggestions

1. In Section 5.4, add a sentence quoting the exact baseline mAP/Rank-1 numbers (e.g., "CC improves from X% to Y% mAP (+19.3%)") so readers can immediately contextualize the gains without consulting the table.
2. Specify how body-angle labels were obtained (manual annotation, pose estimator, camera geometry) in Section 4.3.
3. Add a brief limitations paragraph discussing the need for camera labels at test time, the diagnostic (not deployment-ready) nature of the detailed bias factor analysis, and the potential trade-off of discarding single-camera clusters on small datasets.
4. Clarify whether "mAP increase" refers to absolute percentage points or relative improvement in Section 5.4.

## Score and Decision

This paper makes a solid empirical contribution. The core analysis (Sections 3–4) is well-executed and reveals genuinely novel insights about camera bias on unseen domains and the mechanism of feature normalization. The USL section (Section 5) identifies a real problem and proposes sensible solutions, though the presentation of the large gains could be more transparent. There are no fatal or major flaws, and the weaknesses identified are addressable presentation issues. The paper would be a valuable addition to the ReID literature and is ready for acceptance with minor revisions.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>