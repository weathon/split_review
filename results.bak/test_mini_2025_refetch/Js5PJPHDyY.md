Now I have a solid calibration. Let me write the final consolidated review.

## Summary

This paper proposes applying Gaussian Discriminant Analysis (GDA) to CLIP visual features—estimating class means and a shared precision matrix via an empirical Bayes ridge-type estimator—and ensembling the resulting linear classifier with CLIP's zero-shot classifier. The method requires no gradient-based training and is evaluated across 17 datasets in four settings: few-shot classification, imbalanced learning, base-to-new generalization, and unsupervised learning. The central claim is that this classical generative classifier serves as a "hard-to-beat baseline" for training-free CLIP adaptation.

## Strengths

- **State-of-the-art among training-free methods and competitive with training-required methods on few-shot classification.** Table 1 shows that on the 16-shot 11-dataset average, the method achieves 76.05%, outperforming all training-free baselines (best APE at 73.23%) and matching the best training-required method (Tip-Adapter-F at 75.83%). The margin over training-free methods is consistent (2.82% lead) and the method leads on 9 of 11 individual datasets.

- **Surpasses training-required methods on imbalanced learning without any training.** In Table 3, the method achieves 62.34% overall accuracy on ImageNet-LT and 42.07% on Places-LT, exceeding all baselines including fully fine-tuned MARC and CRT, which require extensive training and specialized loss functions. The improvement is concentrated in medium- and few-shot classes (e.g., 54.35% few-shot vs. 32.91% for MARC on ImageNet-LT), which the paper correctly attributes to the shared covariance structure transferring knowledge from many-shot classes.

- **Consistent improvement over zero-shot CLIP across all four evaluation scenarios.** The ensemble (Eq. 5) outperforms both the GDA-only and zero-shot-only classifiers at every shot level (Figure 4). The method improves over zero-shot CLIP by 17.28% (16-shot average, Table 1), 8.72%/9.90% overall (ImageNet-LT/Places-LT, Table 3), 7.02% harmonic mean (base-to-new, Table 4), and 4.69% average (unsupervised, Table 5). This breadth confirms the robustness and generality of the approach.

- **Scalability to full datasets demonstrated.** Table 7 shows that the method scales to the full ImageNet training set (80.0% accuracy) in 3.6 seconds without out-of-memory errors, unlike cache-based methods (Tip-Adapter) that fail on the full set. Figure 3 further shows a near-linear relationship between performance and the logarithm of sample size, suggesting the method benefits predictably from more data.

- **Clean, principled use of high-dimensional covariance estimation.** Table 6 compares six precision matrix estimators on EuroSAT; the Kubokawa-Srivastava (KS) estimator used in the paper achieves the best accuracy (86.12% at 16 shots), validating the choice of this training-free shrinkage method.

## Weaknesses

### Fatal
None.

### Major

- **Table 7 comparison is between incompatible backbones and inflates the apparent advantage.** The table pits "Ours" using CLIP ViT-L/14 against ResNet-50, ResNet-101, DeiT-T, and DeiT-S trained from scratch on ImageNet. ViT-L/14 is a vastly larger and better-pretrained model. The paper's claim that "our approach achieves the highest performance compared to both efficient fine-tuning methods and *conventional training methods*" is misleading because it attributes the gap to the method rather than the backbone. A fair comparison would use the same backbone (e.g., linear probe or fine-tune of CLIP ViT-L/14 on ImageNet). The observation about scalability (no OOM) is valid and should be kept, but the performance comparison should be restructured or dropped.

- **Base-to-new generalization (Table 4) follows a fundamentally different protocol from the baselines.** The paper's KNN-based variant (Eq. 6) uses text embeddings of *new* classes to retrieve base-class examples, assigning pseudo-labels from those new classes. This effectively gives the method access to new-class information during training. Standard methods like CoOp, CoCoOp, and KgCoOp have no access to new-class examples at all—they train only on base classes and evaluate on new classes directly. The high harmonic mean (78.72% vs. 77.00% for KgCoOp) may partly reflect this additional information. The paper should clearly acknowledge this methodological difference and present the result as a *different adaptation strategy*, not a direct comparison under the same protocol.

- **The shared covariance assumption is asserted without empirical scrutiny.** GDA's core assumption—that features of all classes share an identical covariance matrix—is mentioned (Section 3.1) but never validated. The paper provides no diagnostics (e.g., comparison of per-class covariance eigenstructures, likelihood ratio against a heteroscedastic model, or ablation testing whether shared vs. class-specific covariances perform differently). While the empirical success suggests the assumption is approximately reasonable for CLIP features, the lack of any analysis leaves a methodological gap. The paper would be strengthened by even a simple diagnostic showing that the shared estimate yields comparable or better classification than per-class estimates.

### Minor

- **Standard deviations are not reported for any result.** The paper states it runs three seeds and averages results (Section 4.1), but no variance information is reported anywhere. Many comparisons (e.g., the 0.22% lead over Tip-Adapter-F on 16-shot average) could be within noise. This is the single most easily fixable omission that would substantially increase reader confidence.

- **Out-of-distribution generalization evaluation (Table 2) omits source accuracy on ImageNet.** The paper reports only OOD accuracy on ImageNet-V2, -Sketch, -A, and -R but does not report the corresponding source (ImageNet 16-shot) accuracy for the ViT-B/16 backbone used in these experiments. Without this, the reader cannot assess whether the OOD improvements reflect genuine robustness or simply less overfitting to the source distribution. The source accuracy is reported elsewhere only for ResNet-50 (Table 1), which is a different backbone.

- **No limitations or failure case discussion.** The paper does not discuss scenarios where the method might underperform (e.g., 1-shot regimes where the precision matrix estimate is poorest, or settings where the Gaussian assumption is clearly violated). Adding a brief limitations section would strengthen the paper's scholarly rigor.

### Trivial
None.

## Nice-to-Haves

- Sensitivity analysis for the ensemble weight α (Eq. 5), showing how performance varies with α across a few datasets.
- Ablation study for the KNN parameter k in the base-to-new variant (currently fixed at 64).
- Computational cost discussion for the full-set covariance matrix computation (memory and time for, e.g., ImageNet with 1.28M images).

## Removed Points

These points were raised by reviewers but are removed from the main evaluation for the following reasons:

- *"Missing standard deviations"* — kept as Minor (it is a real and fixable issue).
- *"No analysis of computational cost beyond training time"* — moved to Nice-to-Have. The paper already discusses training time (Table 7) and the scalability advantage; the specific concern about memory for large covariance matrices is a reasonable extension but not a core weakness.
- *"No ablation for KNN parameter k"* — moved to Nice-to-Have. Reasonable request but not central to evaluating the paper's core claim.
- *"Missing sensitivity analysis for α"* — moved to Nice-to-Have. Useful but not required for assessing validity.
- *"Missing related works"* — removed per instruction; I cannot verify whether related works are missing without external sources.
- Any formatting, typos, or parsing artifact criticisms — removed per instruction (these are PDF parser issues, not author errors).

## Novel Insights

None beyond the paper's own contributions. The reviews surface a useful observation not fully developed in the paper: the shared covariance assumption in GDA serves as a form of implicit knowledge transfer from many-shot to few-shot classes (which the paper does note in the imbalanced learning discussion, Section 4.4), but the connection to shrinkage-based estimation as a principled way to enable this transfer under high-dimensional low-sample regimes is worth deeper exploration. The harsh critic's suggestion to compare GDA with class-specific covariances could produce an interesting analysis of when and why the shared-covariance assumption is justified for CLIP features.

## Suggestions

1. **Restructure Table 7** to focus on fair comparisons: compare Ours (ViT-L/14) with linear probe / full fine-tune of the *same* ViT-L/14 backbone. Remove or clearly footnote the comparison with ResNet/DeiT as illustrating scalability rather than performance.
2. **Add standard deviations to all main tables** (Tables 1–5). This is trivial given three runs.
3. **Acknowledge the base-to-new protocol difference** in Section 4.5. Clearly state that the KNN synthesis step uses new-class text embeddings to retrieve base data, and explain why this is different from the standard protocol.
4. **Add a simple diagnostic for the shared covariance assumption** (e.g., Frobenius-norm distance between per-class covariance matrices, or comparison of shared vs. per-class covariance accuracy on one dataset).
5. **Report source (ImageNet) accuracy alongside OOD results** in Table 2 so readers can assess robustness independently of underfitting.
6. **Add a limitations paragraph** discussing when the method may struggle (very low shot counts, non-Gaussian features, high-dimensional regimes with very few samples per class).

## Score and Decision

### Calibration

**Round 1 (Bracketing):**
- Low band (scores < 3.5): Papers like bESxQeXTlo.md (3.00), MbtUctg3KW.md (2.50), ZbOSRZ0JXH.md (3.00) — all withdrawn/rejected, clearly weaker than the current paper.
- Middle band (3.5–7.5): Papers like O1cLOzgi81.md (3.80, withdrawn), KNtcoAM5Gy.md (5.50, rejected BaFTA), g6rZtxaXRm.md (6.00, accepted), TD3SGJfBC7.md (6.25, accepted), buC4E91xZE.md (6.17, accepted), kIP0duasBb.md (6.67, accepted), FE2e8664Sl.md (7.00, accepted).
- High band (>7.5): Papers like rmg0qMKYRQ.md (8.00, spotlight), 5Ca9sSzuDp.md (8.00, oral), 9bMZ29SPVx.md (7.50, spotlight) — clearly stronger papers with deeper analysis or broader impact.

**Initial bracket: [4.5, 7.5]**

**Round 2 (Narrowing):**
- BaFTA (KNtcoAM5Gy.md, avg 5.50, rejected): A training-free CLIP test-time adaptation method using online clustering. The current paper has broader experiments (17 vs. fewer datasets, 4 vs. 1 scenario), a cleaner method, and stronger results. **The current paper is clearly stronger.**
- TD3SGJfBC7.md (avg 6.25, accepted poster): Few-shot TTA with CLIP using a side branch. Similar quality of work; both have well-supported results with some methodological concerns. **Comparable, slight edge to current paper for breadth.**
- kIP0duasBb.md (avg 6.67, accepted poster): CLIP reward-based TTA. Strong method with 3-task generalization. Current paper has cleaner method and more datasets but fewer task types. **Comparable quality.**
- buC4E91xZE.md (avg 6.17, accepted poster): AnomalyCLIP. Mixed reviews (two 8s, two 5s, one 6). Similar tier with well-supported experiments and some methodological concerns. **Comparable.**

**Final score: 6.5** — This paper sits slightly above the median of accepted posters in this space. It has a genuinely clean and well-executed idea, broad experimental coverage, and results that convincingly support the central claim of a "hard-to-beat baseline" for training-free CLIP adaptation. The weaknesses (Table 7 comparison, base-to-new protocol difference, unexamined covariance assumption, missing std devs) are real and prevent a higher score, but they are fixable and do not invalidate the core contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>