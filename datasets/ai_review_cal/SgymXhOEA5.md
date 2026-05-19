- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 8, 6
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper conducts an extensive empirical investigation of camera bias in person re-identification (ReID) models. It makes two main contributions: (1) documenting that camera bias is large on *unseen* domains across many model types (supervised, unsupervised, camera-aware, domain-generalizable), and providing an insightful feature-space analysis showing that camera-specific feature normalization debiases effectively because camera variations produce consistent translational movements in a small set of high-variance dimensions; and (2) identifying camera-bias risks inherent in unsupervised learning (biased pseudo labels and single-camera clusters) and showing that simple modifications — debiased pseudo labeling via normalized features and discarding single-camera clusters — yield substantial gains on existing USL algorithms.

---

## Strengths

1. **Broad and systematic measurement of camera bias across models and domains.** Table 1 reports NMI-based camera bias for nine models spanning supervised, unsupervised, camera-aware, and domain-generalizable methods on four datasets. The finding that camera bias is consistently large on unseen domains (30–50+ NMI) regardless of model type is convincingly demonstrated and supports the claim that this phenomenon has been overlooked.

2. **Empirical feature-space analysis that explains *why* normalization works.** Figure 2 provides a clear causal chain: (a) some dimensions have much higher variance across camera means; (b) displacement vectors from camera changes are more similar in those high-variance dimensions, meaning features move consistently under camera variation; (c) centering on just the top-50 camera-sensitive dimensions achieves roughly half the total mAP gain, while centering on the bottom-50 gives almost no gain. This insight goes beyond simply applying a known trick.

3. **Generalization demonstrated across 12 models on unseen domains.** Table 3 consistently shows mAP improvements for every model evaluated on unseen domains (e.g., CC on Market-1501: +7.5 mAP; TransReID-SSL: +9.4 mAP), supporting the claim of "general applicability" of the normalization approach.

4. **Controlled toy experiments (Figure 6) causally linking camera-biased pseudo labels to degraded training.** The comparison "Random at 91.9% accuracy beats Camera at 93.8% accuracy" is a clean and compelling demonstration that pseudo-label camera bias matters more than raw accuracy, and provides strong motivation for the proposed training strategies.

5. **Ablation showing both proposed USL strategies contribute independently.** Figure 7(a) demonstrates that debiased pseudo labeling (+8.6 mAP) and discarding single-camera clusters (+11.3 mAP) each help, and combining them (+19.3 mAP) gives the best result, with the single-camera cluster rate dropping from ~80% to below 20%.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **No measures of variance for the USL experiments (Table 6).** The reported improvements are large (e.g., CC on MSMT17: +19.3 mAP), but the paper provides no error bars, standard deviations, or statements about consistency across runs. Since unsupervised clustering-based methods are sensitive to initialization, clustering hyperparameters, and randomness, single-run reporting limits confidence in the exact magnitude of the gains. The fact that improvements are shown across multiple methods (CC, PPLR, PPLR-CAM) and datasets (MSMT17, VeRi-776) provides some reassurance that the effect is real, but variance reporting would strengthen the evidence.

2. **The detailed bias factor analysis (Section 4.3) is suggestive rather than conclusive.** The gain from (property, camera) over camera-only normalization is modest (~1.5 mAP) and requires additional group-level annotations. The analysis correctly identifies these as exploratory directions, but the claims of applicability to detailed bias factors are not as thoroughly validated as the core camera-bias findings.

### Trivial

1. **Minor reproducibility gaps.** The paper does not specify certain training hyperparameters for the USL modifications (e.g., the clustering threshold used when generating pseudo labels, whether camera normalization is applied at every clustering step or only initial). These are small omissions that make reproduction slightly harder.

---

## Nice-to-Haves

- **Discussion of failure cases.** The paper's Figure 5 already shows that performance degrades with too few samples per camera (~5 samples). A brief discussion of minimum sample requirements or when per-camera statistics become unreliable would be useful but is not a core flaw.
- **Comparison to other test-time adaptation methods** (e.g., style transfer, domain normalization) would contextualize the approach but is outside the paper's stated scope of analyzing camera bias specifically.

---

## Removed Points

- **"Methods require camera labels — a significant practical constraint that the paper understates."** The paper's entire premise is the study of camera bias; using camera labels is inherent to this analysis, not an oversight. The paper clearly states in Section 4.1 that it "postprocesses embedding vectors leveraging camera labels at test time." Criticizing the paper for requiring camera labels is akin to criticizing a face-recognition paper for requiring face labels. This is a scope-creep criticism.
- **"Cross-dataset NMI comparisons are problematic."** The paper uses NMI to compare models *within* each dataset, not to compare absolute values across datasets. Ground-truth NMI values are reported for reference, and the paper's observations (e.g., "unsupervised models have high bias on seen domains") hold regardless of cross-dataset comparability. This criticizes a claim the paper does not make.
- **"Missing comparison to other test-time adaptation methods."** Scope creep. The paper analyzes camera bias and shows normalization works; it does not claim to propose a new SOTA method.
- **"Potential failure cases"** — The paper partially addresses this in Figure 5 (sample volume analysis), and the critic acknowledges this. The suggestion is already partially present in the paper.
- **"Ground-truth NMI varies across datasets"** — Not a weakness of the paper; it's a property of the data that the paper correctly reports.
- Several generic strengths from the Strength Finder (e.g., "this paper addressed an important problem") were removed as they lack specific, concrete evidence or are generic praise.

---

## Novel Insights

The strongest novel observation in this paper is the dimensional analysis in Section 4.2: the finding that the debiasing effect of normalization is dominated by a small fraction (~13%) of feature dimensions, and that camera variations produce consistent translational movement specifically in those camera-sensitive dimensions. This provides an intuitive geometric explanation for why a simple normalization works, and it goes beyond prior work that merely applied camera mean subtraction without justification.

---

## Suggestions

1. **Report variance for the USL experiments.** Run 3–5 seeds for the key Table 6 results (especially CC on MSMT17, where the gain is largest) and report mean ± std. This would substantially strengthen the evidence for the proposed training strategies.
2. **Add a brief scope note** acknowledging that the approach assumes camera labels are available, and note that scenarios with missing/noisy camera labels are outside the paper's scope.
3. **Specify the clustering threshold and other key hyperparameters** for the USL modifications in the main text or a reference to the appendix.

---
