Now I have all the information needed to compile the final consolidated review. Let me write it.

## Summary
The paper proposes applying Gaussian Discriminant Analysis (GDA) to CLIP visual features for training-free downstream adaptation. By estimating class means and a shared precision matrix (via empirical Bayes ridge-type shrinkage) from few labeled examples, the method constructs a linear classifier and ensembles it with CLIP's zero-shot classifier. Extensions using KNN (for base-to-new) and EM (for unsupervised learning) are also presented. Experiments across 17 datasets cover few-shot, imbalanced, OOD, base-to-new, and unsupervised settings.

## Strengths
- **Training-free few-shot performance is genuinely competitive.** In Table 1 (16-shot, 11 datasets), Ours (76.05% average) surpasses the best training-free baseline APE (73.23%) by 2.82% and matches the best training-required method Tip-Adapter-F (75.83%). Notably, on Flowers102 (95.72%), FGVCAircraft (40.61%), and EuroSAT (86.12%), Ours leads by >3% over all baselines including training-required ones. These margins on specific datasets are large and cannot be explained by variance.
- **Strongest OOD generalization among compared methods.** Table 2 shows Ours achieves the highest average accuracy (60.37%) across 4 OOD target datasets without any training, outperforming both training-free (Tip-Adapter: 60.08%) and training-required (Tip-Adapter-F: 60.21%, CoOp: 58.41%) methods.
- **Scalability advantage over cache-based methods.** Table 6 demonstrates that Ours scales to the full ImageNet training set (80.0%, 3.6 sec) while cache-based methods (Tip-Adapter, Tip-Adapter-F) run out of memory. This is a practical advantage for large-scale deployment.
- **Ensemble of GDA + zero-shot classifiers consistently helps.** Figure 5 verifies that ensembling outperforms either classifier alone across all shot settings (1–16), confirming that integrating visual and textual modality knowledge is beneficial.
- **Imbalanced learning gains on medium/few shots are substantial.** In Table 3, Ours achieves 62.34% overall on ImageNet-LT (vs. best training-required 60.97%) and 42.07% on Places-LT (vs. 37.81%), with particularly large gains on few-shot categories. This supports the paper's motivation that shared covariance estimation transfers statistical strength from many-shot to few-shot classes.

## Weaknesses

### Fatal
None.

### Major
- **No variance or error bars reported despite running 3 trials.** The paper states "we conduct three runs with different random seeds and averaged the results" (line 209) but never reports standard deviations, confidence intervals, or individual trial results anywhere. This is critical because several key comparisons involve very small margins: Ours vs. Tip-Adapter-F in Table 1 (76.05% vs. 75.83%, ∆=0.22%), OOD average in Table 2 (60.37% vs. 60.21%, ∆=0.16%), and unsupervised in Table 4 (63.46% vs. 63.38%, ∆=0.08%). Without any measure of variability, these cross-method comparisons are uninterpretable. While the method's advantage over training-free baselines on many-shot settings is large enough to be robust, the paper's claims about being "comparable to or even better than training-required methods" rest partly on these small-margin comparisons.

### Minor
- **Precision matrix ablation is on a single dataset only.** Table 5 compares shrinkage estimators exclusively on EuroSAT. While EuroSAT is a reasonable starting point (where the method shows a large gain), the relative performance of shrinkage methods depends on feature dimensionality, sample size, and data geometry, which vary across datasets. Without ablations on at least one additional diverse dataset (e.g., a fine-grained dataset like Flowers102 or a generic one like ImageNet), the choice of KS estimator is not convincingly justified as broadly optimal.
- **KNN parameter k=64 for base-to-new is not ablated or motivated.** Line 207 states k is set to 64, but no sensitivity analysis or justification is provided. The base-to-new harmonic mean (78.72%) is a highlight result, and the value of k directly controls the quality of pseudo-labeled data for new classes. A brief ablation on one dataset would improve reproducibility.
- **No discussion of failure cases on DTD and OxfordPets.** In Table 1, Ours underperforms Tip-Adapter-F on OxfordPets (88.81% vs. 89.70%) and APE on DTD (66.51% vs. 67.38%). A brief analysis of why (e.g., high intra-class variance, non-Gaussian features for textures) would strengthen the paper's methodological transparency.

### Trivial
- The paper claims "surpasses state-of-the-art training-required methods" in the abstract but the comparison set (CoOp, CLIP-Adapter, Tip-Adapter-F) dates to 2021–2022. While this does not invalidate the contribution (the paper's primary focus is training-free methods, and the training-required comparison is secondary), the wording could be tempered to "comparable to early efficient fine-tuning methods" to avoid overclaiming.

## Nice-to-Haves
- **Gaussian assumption discussion.** The paper assumes CLIP features are Gaussian with identical covariance. While this is a standard GDA assumption, CLIP features are known to be multi-modal for fine-grained classes. A brief discussion of when this assumption might break down and how the method might be affected would improve methodological honesty.
- **Wall-clock time for the unsupervised EM variant.** The paper reports training time for the few-shot variant but not for the EM-based unsupervised variant, which requires multiple iterations. Reporting this would give a more complete efficiency picture.

## Removed Points
These points are flagged to be removed; treat them with caution as they were filtered for being factually wrong, speculative, or not grounded in the paper's content:
- **"Misleading comparison in Table 6 (full training set)"** — REMOVED. The critic claimed the table creates a strawman by comparing Ours (full set) with Tip-Adapter-F (16-shot) without including linear probe on full features. However: (a) the table's stated purpose is to show scalability vs. cache-based methods that OOM on full set, (b) ResNet and DeiT conventional full-training baselines ARE included and Ours matches/beats them, (c) linear probe is already compared in other tables. The criticism misreads the table's intent.
- **"Base-to-new comparison is unequal because Ours uses new-class text embeddings"** — REMOVED. The text embeddings of new class names are trivially available from CLIP to all methods. KgCoOp and CoCoOp also use CLIP's text encoder; Ours simply uses the same embeddings differently. This is a design choice, not an unfair advantage.
- **"Imbalanced learning baselines perform anomalously low"** — REMOVED. The critic speculates baselines are "not well-tuned" without evidence. The paper cites these numbers from Wang et al. (2023). Without external evidence of miscalibration, this is speculation.
- **"Method loses on OxfordPets and DTD — no discussion of why"** — MOVED from Major to Minor (already in Minor section above). The critic presented this as part of a broader claim but the paper does acknowledge this briefly (line 335: "Our method surpasses the baselines on almost all datasets except OxfordPets and DTD").
- **"Outdated training-required baselines"** — MOVED from Major to Trivial. The paper's primary contribution is as a training-free baseline, not as a SOTA-chasing training-required method. The comparison to training-required methods is supportive, not central. The claimed margins over these methods are also small; the paper's main value is in the training-free comparison, which is comprehensive.
- **"Unsupervised improvement is negligible"** — MERGED with Major weakness #1 (lack of variance reporting). This is the same underlying issue.

## Novel Insights
None beyond the paper's own contributions. The reviewer analyses did not uncover any observation about the method or results that the paper itself does not already articulate.

## Suggestions
1. **Report standard deviations or confidence intervals** for all main results (Tables 1–4). Since you ran 3 trials, the standard deviation is trivially computable. This directly resolves the most substantive weakness.
2. **Extend the precision matrix ablation** to at least 2–3 additional datasets (e.g., Flowers102, ImageNet) to demonstrate robustness of the KS estimator choice.
3. **Add a brief ablation of k for the KNN base-to-new variant** on one dataset (e.g., ImageNet).
4. **Tone down the claim about "surpassing training-required methods"** to "comparable to early efficient fine-tuning methods" or add newer training-required baselines.
5. **Add a brief paragraph in the main text discussing the Gaussian assumption** and when it might be violated, with some qualitative justification from the results (e.g., why DTD texture features might be less Gaussian).

## Score and Decision
The paper presents a clean, well-motivated, and practically useful method. The core contribution — a training-free GDA-based classifier for CLIP — is genuinely effective, especially on fine-grained and unusual datasets where covariance matters. The experimental scope across 17 datasets and 5 settings is commendable. The main weakness (missing error bars) is significant for papers making fine-grained comparative claims but is straightforward to fix. The remaining issues are minor and do not undermine the core contribution.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>