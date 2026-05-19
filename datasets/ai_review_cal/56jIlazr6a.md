- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 3, 5, 8
Now I have a thorough, verified understanding of both the paper and the reviews. Let me produce the consolidated review.

## Summary

The paper proposes Unified Uncertainty Calibration (U2C), a framework that combines aleatoric and epistemic uncertainty estimates by learning a non-linear calibration function τ_u that maps a scalar epistemic uncertainty u(x) into a logit, then appending it as an extra dimension in a softmax over c+1 classes. This contrasts with the standard reject-or-classify (RC) rule which uses a hard threshold on u(x) to either predict an in-domain class or abstain. The paper provides a theoretical comparison (Lemmas 5.1, 5.2) and experiments on ImageNet-family benchmarks showing consistent improvements in classification error and expected calibration error over RC across four epistemic uncertainty estimators.

## Strengths

- **Non-linear epistemic calibration as a principled integration mechanism (Section 4):** The paper introduces τ_u: ℝ→ℝ, a learned non-linear function that resamples u(x) into logit space, enabling aleatoric and epistemic uncertainties to compete in a joint softmax. This cleanly addresses the "units" problem (Section 3.3) where u(x) and the in-domain logits may operate at incompatible scales. This is the paper's core methodological innovation and is concretely implemented.

- **Formal demonstration of RC's NLL pathology (Lemma 5.2):** Lemma 5.2 proves that RC's negative log-likelihood is infinite whenever in-domain test examples fall into the reject region or out-domain examples fall into the accept region — both inevitable under the 5% validation relabeling scheme. U2C produces soft probabilities over all c+1 classes, yielding finite NLL in those same regions. This is a crisp theoretical advantage of the proposed approach.

- **Consistent empirical improvement across multiple benchmarks and uncertainty estimators (Table 1):** Across four benchmark types (in-domain, covariate shift, near-OOD, far-OOD) and four epistemic uncertainty methods (MaxLogit, ASH, Mahalanobis, KNN), U2C improves both classification error and expected calibration error over RC in the large majority of settings. Deteriorations are small when they occur. The results cover a meaningful spectrum of distribution-shift difficulty within the ImageNet ecosystem.

- **Interpretable decision-region analysis (Figure 1a, Lemma 5.1):** The paper partitions the (max-logit, τ(u(x))) plane into four regions (A–D) and derives the error difference between RC and U2C as a function of probability mass in regions B and C. This provides a concrete explanation of when unified calibration helps — e.g., when out-domain mass falls in region B (high aleatoric uncertainty, low epistemic uncertainty).

## Weaknesses

### Fatal
None.

### Major

- **The τ_u function architecture is not specified in the paper.** The method description (Section 4) states "learn a non-linear epistemic calibration function τ_u: ℝ→ℝ" via cross-entropy minimization and later references "(nonlinear!) Platt scaling" (line 137), but never specifies what form τ_u takes — is it a small MLP, a spline, isotonic regression, a parametric non-linear transformation? The optimization in Eq. (7) is written as argmin over a function space with no discussion of how that space is parameterized or how overfitting is controlled. This is the central component of the method, and leaving its architecture unspecified makes the method irreproducible from the paper text alone and prevents readers from assessing the complexity or limitations of the approach.

- **The claim of "state-of-the-art performance" (abstract, line 22) is unsupported by the experimental design.** The paper only compares U2C against RC — a single baseline that uses a fixed threshold. No comparisons are made to other OOD detection or uncertainty combination methods (e.g., energy-based OOD detection, Mahalanobis-based methods that produce soft predictions, baseline approaches that directly add a constant c+1-th logit, or other post-hoc calibration methods). "State-of-the-art" implies surpassing all known competitors; the evidence only shows improvement over one specific baseline.

- **No standard OOD detection metrics are reported.** The paper evaluates using classification error (err) and expected calibration error (ece) on the extended c+1 problem. While internally consistent, the absence of AUROC, FPR@95TPR, and AUPR — the standard metrics in the extensive OOD detection literature — makes it impossible to situate U2C's performance relative to existing methods or to assess its OOD detection effectiveness in terms the community recognizes.

### Minor

- **Evaluation is limited to ImageNet-family datasets.** All experiments use ImageNet variants (ImageNet-va/te, ImageNet-C/R/v2, NINCO, SSB-Hard, iNaturalist, Texture, OpenImage-O). This is a single base dataset family. Evaluating on other standard benchmarks (e.g., CIFAR-10/100, SVHN, TinyImageNet) would strengthen claims of generality. While the benchmarks used are appropriate and cover four types of distribution shift, the lack of diversity in base dataset is a limitation.

- **No ablation of the relabeling proportion α.** The relabeling proportion is fixed at α = 0.95 (5% of the most uncertain validation examples are labeled as OOD). There is no sensitivity analysis — how robust is U2C's performance to this choice? Would α = 0.90 or 0.99 change the results substantially? The relabeling assumption (marking the 5% most uncertain in-domain examples as OOD) is a strong assumption that could fail under misspecified u(x), and this is not analyzed.

- **The RC baseline could be strengthened to isolate the source of improvement.** RC uses a fixed α=0.95 percentile threshold (standard practice). U2C also uses the same α to determine which examples to relabel, then learns τ_u. To isolate whether the improvement comes from data-driven calibration vs. the soft combination, the paper could have compared against RC with a tuned threshold (e.g., optimized on the same cross-entropy objective). The paper references "additional experiments on linear U2C" (line 192) but these appear to be in the appendix, not the main text.

### Trivial
- The claim "error-bars are absent because there is no randomness involved in our experimental protocol" (line 192) is correct for a fixed split but does not address randomness from neural network training itself.

## Nice-to-Haves

- Evaluating on standard OOD detection benchmarks (CIFAR-10/100, SVHN, TinyImageNet) would broaden the paper's reach and enable direct comparison with the existing literature.
- Reporting AUROC, FPR@95TPR, and AUPR as complementary metrics to err/ece would enable situating U2C within the broader OOD detection landscape.
- Comparing against additional baselines such as energy-based OOD detection, a simple c+1 baseline where the extra logit is a learned constant, and RC with an optimized threshold would strengthen the evaluation.
- An ablation varying the relabeling proportion α would help assess the robustness of the method.

## Removed Points

- **"RC baseline is artificially weak"** (Harsh Critic #1): Both RC and U2C use the same α=0.95 percentile threshold, which is standard practice in OOD literature. U2C's advantage comes from learning τ_u on top of this same thresholding scheme. The comparison is between the standard RC recipe and the proposed improvement, which is a valid experimental design. The point about also comparing RC with an optimized threshold is constructive but does not make the current comparison "artificially weak." A toned-down version is retained as a Minor weakness.

- **"Theoretical analysis provides little insight"** (Harsh Critic #4): Lemma 5.1 and 5.2 are valid theoretical observations. Lemma 5.2's point about RC's infinite NLL under hard decisions is a genuine advantage of U2C and is not trivial in the context of the paper's argument. The lemmas are correctly stated and provide useful framing. Removed as overcritical.

- **"Method is less novel than presented"** (Harsh Critic #5): While appending an extra logit for "unknown" exists in open-set recognition, the specific contribution — learning a non-linear calibration of the scalar u(x) into logit space for unified integration — is novel. The paper is not claiming the c+1 softmax itself is new; the innovation is the τ_u calibration and the unified framework. Removed.

- **Formatting/style nitpicks/missing reproducibility trivia** (Harsh Critic §2, "Section-by-Section Notes"): Removed per instructions (parser artifacts, standard details deferred to code/appendix).

- **Strength Finder's generic/sycophantic strengths** (e.g., "the paper addressed an important problem"): Removed. Retained only concrete, evidenced strengths.

## Novel Insights

The reviews do not surface a genuinely novel insight beyond the paper's own contributions. The tension between the two reviews is instructive: the Harsh Critic identifies valid gaps (τ_u specification, unsupported SOTA claim, narrow metrics) while the Strength Finder correctly identifies the paper's core contributions (the τ_u framework, Lemma 5.2, consistent empirical gains). Neither review identifies a structural flaw or a path forward that the paper's own discussion section doesn't already gesture toward (e.g., feature myopia, adversarial examples). None beyond the paper's own contributions.

## Suggestions

1. **Specify the τ_u architecture explicitly in the main paper.** Even a brief description (e.g., "a 2-layer MLP with hidden dimension 16 and ReLU activation, trained with weight decay λ=1e-4") would resolve a major reproducibility concern. If the appendix already contains this, summarize it in the main text.
2. **Remove or qualify the "state-of-the-art" claim.** The paper only compares to RC, which is insufficient to claim SOTA. Reframe as "significantly outperforms the standard reject-or-classify baseline" — this is supported by the evidence.
3. **Add standard OOD detection metrics** (AUROC, FPR@95TPR, AUPR) alongside err and ece. This is essential for community adoption and comparison.
4. **Ablate the relabeling proportion α.** Show sensitivity to α ∈ {0.90, 0.95, 0.99} to demonstrate robustness.
5. **Include at least one additional baseline** beyond RC — e.g., a simple c+1 baseline where the extra logit is a learned scalar constant (no dependence on u(x)), or energy-based thresholding.
