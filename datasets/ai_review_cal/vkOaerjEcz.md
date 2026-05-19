- Decision: Reject
- Avg Score: 5.20
- Scores: 5, 5, 5, 6, 5
Now I have a thorough picture of the paper. Let me write the consolidated review.

## Summary

This paper proposes MTMC (Maximum Token Manifold Capacity), a plug-in regularizer for Generalized Category Discovery that maximizes the nuclear norm of the class token matrix from a ViT across unlabeled samples in a mini-batch. The goal is to prevent dimensional collapse and produce richer feature representations, leading to improved clustering accuracy and category-number estimation. MTMC is added as a simple loss term (≈3 lines of code) to existing GCD frameworks (SimGCD, CMS) and is evaluated on six image benchmarks.

## Strengths

- **Consistent accuracy improvements across diverse GCD benchmarks, especially on novel classes**: Table 1 shows that adding MTMC to SimGCD improves accuracy by +4.7% on ImageNet100 (all classes) and +2.4% on novel classes of CUB-200-2011, while CMS+MTMC improves overall accuracy on ImageNet100 by +1.5%. The gains are especially notable on novel class discovery, which is the harder sub-task.

- **High-quality category-number estimation**: Table 2 (confirmed by the strength finder's reading) reports that CMS+MTMC estimates the number of clusters with zero error on ImageNet100. The paper leverages CMS's built-in K-estimation mechanism, and MTMC consistently improves estimation accuracy across datasets.

- **Empirical evidence that MTMC produces higher von Neumann entropy and more uniform eigenvalue distributions**: Figure 2 shows MTMC yields higher von Neumann entropy than SimGCD or CMS. Figure 4 demonstrates reduced Frobenius norm ∥A−c·I_d∥²_F, and Figure 5 plots singular value distributions showing MTMC flattens the tail — all consistent with preventing dimensional collapse.

- **Extremely simple implementation**: The loss is implemented in three lines of code using SVD on the class token matrix. This makes integration into existing GCD pipelines trivial and requires no architectural changes.

- **Hyperparameter robustness**: Figure 3 shows stable accuracy for λ ∈ [0.1, 1.0] and D ∈ [256, 768], indicating the method does not require careful tuning.

## Weaknesses

### Fatal
None.

### Major

- **Mismatch between the "intra-class" framing and the actual batch-level loss**: The paper's motivation and abstract repeatedly claim MTMC enhances **intra-class** representation completeness and operates "for each cluster." However, the loss in Equation 5 (ℒ_MTMC = −∥[cls]^u∥_*) is computed over **all unlabeled samples in a mini-batch** with no per-class or per-cluster decomposition. The nuclear norm of a (B, D) matrix of class tokens from multiple classes is a batch-level regularization that prevents global dimensional collapse. The paper provides no mechanism — pseudo-labels, clustering assignments, or otherwise — to tie the loss to individual classes. While preventing collapse is a worthwhile goal and likely beneficial for GCD, the claimed **intra-class** effect is asserted rather than demonstrated. This misalignment between the central claim and the actual loss function needs to be resolved, either by reframing the contribution as a batch-level collapse regularizer (with appropriate baselines) or by modifying the loss to operate per predicted cluster.

### Minor

- **Theoretical justification is correlational, not derivational**: Theorem 1 states the well-known inequality log(rank(A)) ≥ Ĥ(A) for the autocorrelation matrix A. Figures 2 and 4 show that after training with MTMC, von Neumann entropy is higher and the Frobenius norm is lower. But the paper does not formally prove that minimizing −∥[cls]∥_* leads to higher von Neumann entropy of the autocorrelation. The connection is empirical — this is a reasonable analysis but weaker than the paper's framing suggests. A derivation or proof sketch connecting the loss to the claimed entropy increase would substantially strengthen the work.

- **Missing experimental comparisons with other collapse-prevention regularizers**: The paper motivates MTMC by arguing that contrastive GCD losses produce collapsed representations. However, it does not compare against alternative collapse-prevention regularizers applied to the same GCD backbone — e.g., adding a decorrelation loss (Barlow Twins style), a VICReg-style variance/invariance/covariance loss, or a spectral-norm constraint to SimGCD or CMS. Since the core claim is that preventing collapse improves GCD, comparison against at least one such alternative is needed to establish that the nuclear-norm objective offers a specific advantage over generic collapse prevention.

- **No variance or multiple-seed reporting**: The paper reports single-run results without standard deviations. While single-run evaluation is common in some GCD papers, the improvements are often small (<2%), and without variance estimates the reader cannot assess statistical significance.

- **Uneven gains on CIFAR100 and Herbarium19**: The paper acknowledges these cases (Section 4.3) and provides plausible explanations. However, the discussion is post-hoc and the explanations are not experimentally validated. For instance, the claim that CIFAR100's small image size causes high-frequency information loss could be tested by an ablation (e.g., comparing performance on 32×32 vs. resized-up versions). This would strengthen the otherwise speculative analysis.

### Trivial

- The notation in Equations 2–5 is at times garbled by parser artifacts (the equation rendering in the PDF is likely cleaner). The paper would benefit from a notation table clarifying when [cls] denotes a vector vs. a matrix, especially in Equation 3 (where the nuclear norm of a single vector is just its L2 norm) vs. Equation 5 (where it is clearly a batch matrix).

## Nice-to-Haves

- Include the CMS-alone baseline row explicitly in Table 2 for K estimation (if not already present) so readers can quantify MTMC's marginal contribution.
- Compare against a token-level alternative: for instance, maximizing the nuclear norm of patch tokens rather than class tokens, to test whether the class token is indeed the critical locus.
- Extend the analysis in Figures 4–5 to also show the baseline (without MTMC) curves on the same plot for direct visual comparison.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Paper does not discuss negative/flat cases on CIFAR100 and Herbarium19"** — Removed because Section 4.3 (line 163) explicitly states "the accuracy gains on the CIFAR100 and Herbarium19 datasets are insignificant" and provides a two-part analysis of why. The paper does discuss these cases.

2. **"Missing CMS baseline for K estimation in Table 2"** — Removed because the strength finder confirms CMS baseline numbers are present in the table. The paper frames Table 2 as presenting "the gap between MTMC and SOTAs."

3. **"Reducing D alone is suboptimal is obvious"** — Removed as a subjective presentation nitpick that does not affect the paper's contribution.

4. **Various formatting/style nitpicks, speculation about missing appendix content, and hypothetical concerns about confounders** — Removed per filtering rules; these are parser artifacts, assumptions about stripped supplementary material, or generic area-of-concern sweeps without concrete anchors in the paper.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine tension — that the loss is batch-level while the framing is intra-class — but this is an observation about the paper's presentation, not a new scientific insight.

## Suggestions

1. **Reframe the contribution**: Either (a) modify the loss to operate per predicted cluster using the model's own pseudo-labels, or (b) reframe MTMC as a batch-level collapse regularizer for GCD and explicitly discuss why it is preferable to alternative regularizers (decorrelation, whitening, etc.).

2. **Add at least one alternative collapse-prevention baseline**: For example, add a Barlow Twins-style covariance regularization loss to SimGCD/CMS and compare against MTMC. This would establish whether the specific nuclear-norm formulation offers advantages over generic decorrelation.

3. **Report results over 3–5 random seeds with mean and standard deviation**, especially for datasets where gains are small (CIFAR100, Herbarium19).

4. **Strengthen the theoretical connection**: Provide a derivation or at minimum a clear argument linking the nuclear-norm objective on the batch-level class token matrix to increased von Neumann entropy of the autocorrelation matrix of individual sample features.

5. **Test the CIFAR100 explanation**: Run a controlled ablation where CIFAR100 images are resized to larger resolutions (e.g., 224×224) before feeding into ViT, to validate the claim that small image size limits MTMC's effectiveness.
