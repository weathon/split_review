Now I have a thorough understanding of the paper and the reviews. Let me write the final consolidated review.

## Summary

The paper identifies a genuine blind spot in contrastive-learning-based anomaly detection: the same augmentation (e.g., rotation) can preserve semantics for one class but alter them for another, yet prior methods apply a fixed positive/negative pairing across all classes. The authors propose Knowledge Exposure (KE), which uses the Wasserstein distance between CLIP embeddings of original and transformed datasets to dynamically select per-class positive/negative transformations for contrastive learning, followed by one-class SVM for anomaly scoring.

## Strengths

- **Identifying the "dual effect" of augmentations is a genuinely novel and well-motivated problem framing.** The paper shows concretely (Section 1, Figure 2) that rotation preserves semantics for flowers but alters them for cars, and that this mismatch undermines generalization in prior contrastive methods. This is not a trivial observation — it targets a structural limitation of how contrastive anomaly detection methods are designed.

- **The SPD evaluation protocol eliminates the shortcut that standard benchmarks provide.** Standard SD (Standard Detection) benchmarks let models learn a linear correlation between "is transformed" and "is anomalous." The SPD setup (Section 3, lines 100–104) removes this by applying transformations to both inlier and outlier classes, forcing the model to rely on semantic content rather than transformation presence. This is a stricter and more realistic test.

- **The framework is encoder-agnostic, not a one-off CLIP trick.** Section 3.1 (lines 190–192) tests DINOv2 and Wide-ResNet-50 as alternatives, showing the method is not restricted to CLIP. The ablation in Table 3 (line 125) further demonstrates that raw CLIP features alone perform poorly compared to the KE-trained ResNet-18, indicating the Wasserstein-based selection genuinely adds value beyond inheriting CLIP's biases.

- **The K-pairs contrastive formulation follows naturally from the KE selection and is ablated.** Table 4 (line 127) and the accompanying discussion (lines 186) explore K=2 as optimal, with an argument that multiple positive/negative pairs reduce feature collapse — a non-trivial design choice backed by analysis.

## Weaknesses

### Fatal

None.

### Major

- **A structural tension exists between the contrastive training objective and the SPD evaluation protocol that the paper does not acknowledge, let alone resolve.** For an inlier class C, KE identifies certain transformations (e.g., rotation for cars) as *negative* pairs — the model is explicitly trained to push their representations away from the normal cluster. Yet in the SPD evaluation, those same transformed inliers (e.g., rotated cars) are treated as *normal*. The paper provides no analysis of whether the one-class SVM boundary trained on original (untransformed) features can still encompass these KE-negative transformed samples, or whether the SPD evaluation is testing the model on a signal it was trained to suppress. This is not a speculative concern — it is a direct consequence of how the method and evaluation are defined (contrastive loss in Eq. 7, anomaly scoring in line 84, SPD definition in line 102). Without resolving this, the SPD results are difficult to interpret.

- **Per-class AUROC results are not reported, which is a critical omission for a method whose core claim is *per-class* dynamic selection.** The paper reports only mean AUROC aggregated across all classes (line 104). For a method that selects different transformations for each class, the central evidence should be a class-wise breakdown showing that the KE choices are sensible and beneficial for each class individually. A mean can mask classes where the method hurts performance.

- **The evaluation is limited to three 32×32 datasets (CIFAR-10, CIFAR-100, SVHN) with no statistical significance or variance estimates.** All comparisons rely on point estimates of AUROC. For a paper targeting "real-world" and "generalization" claims at a top venue, this narrow evaluation basis weakens the empirical support. No commonly used industrial anomaly detection benchmarks (e.g., MVTec AD) are included.

### Minor

- **CLIP's potential prior exposure to CIFAR/SVHN-like images creates an unaddressed confound.** CLIP was trained on 400M internet image-text pairs, which almost certainly include images visually similar to CIFAR-10/100/SVHN classes. The KE selection depends on CLIP's representations to determine which transformations are "semantic-preserving." If CLIP's judgment partly derives from having seen these exact dataset classes during pre-training, then KE may be exploiting dataset-specific knowledge rather than learning a general principle about transformation semantics. The paper's limitations section mentions reliance on pre-trained CLIP generally but does not discuss this specific confound.

- **The contrastive loss formulation (Eq. 7, line 77) is unusual and ambiguous.** The denominator sums only over the positive and negative *augmented versions of the same anchor*; it does not mention whether other samples in the batch serve as implicit negatives (as in standard SimCLR/NT-Xent). This matters enormously for the effective number of negatives and the optimization behavior. The paper never clarifies whether batch-level negatives are used.

- **The choice of Wasserstein distance over simpler alternatives (e.g., MMD, cosine similarity between centroids) is not empirically justified.** The paper provides only a brief qualitative rationale (line 58: "considering differences in values and positions"). Given that Wasserstein distance is computationally expensive on high-dimensional CLIP embeddings, a direct comparison to cheaper alternatives would strengthen the method.

### Trivial

- The acronyms "SSA" and "SPA" are used in the ablation section (line 188) without ever being defined. They appear to be typos for SD and SPD. This is a minor editing oversight but confusing for the reader.

## Nice-to-Haves

- An analysis or controlled experiment isolating whether the benefit comes from KE selection versus simply using CLIP features for any other purpose would sharpen the contribution.
- The candidate pool of transformations should be explicitly enumerated. Which transformations are in the set T? Which are applied at test time in SPD? This information is presented only through examples (Figure 4) but never as a complete list.

## Removed Points

These points are flagged to be removed and should be treated with caution:

- **Criticism that tables are unreadable/unverifiable:** REMOVED — embedded table images are a PDF parsing artifact. The original submission contains proper tables.
- **Criticism about one-vs-rest training interacting with KE selection:** REMOVED — this misunderstands the one-class-per-class setup; there is no cross-class representation conflict when each class trains a separate model.
- **Criticism about missing baseline configuration details:** REMOVED — the paper references an appendix (Section C) for implementation details, which was stripped by the parser.
- **Criticism about missing proof/appendix/references:** REMOVED per hard rules — parser strips supplementary material from all papers.
- **"Strengthening the Paper on Its Own Terms" section:** MOVED to Nice-to-Haves — these are constructive suggestions rather than weaknesses.

## Novel Insights

The single most interesting observation across the reviews is that the SPD evaluation creates a tension the paper does not address: a transformation identified as "semantic-changing" (negative pair) during KE-guided contrastive training is simultaneously expected to be treated as "normal" when applied to inliers during SPD testing. This is not merely a benchmark design issue — it calls into question what exactly the SPD results measure. Either the one-class SVM post-processing absorbs this tension (which the paper should demonstrate), or the SPD evaluation is testing a model on a task that partly contradicts its training objective. This tension is worth probing because it might reveal deeper insights about what kinds of "generalization" contrastive anomaly detectors can and cannot achieve.

## Suggestions

1. **Resolve the training/evaluation tension in SPD.** Explicitly analyze whether KE-negative inlier transformations fall inside or outside the one-class SVM boundary at test time. If they fall inside, explain why the contrastive push does not exclude them. If they fall outside, the SPD results need re-examination.
2. **Report full per-class AUROC results.** For a per-class method, this is the primary evidence.
3. **Add variance estimates** (standard deviations over multiple runs).
4. **Enumerate the transformation candidate pool** explicitly rather than through examples only.
5. **Clarify the contrastive loss:** specify whether batch-level negatives are used and how Eq. 7 relates to standard NT-Xent.

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>