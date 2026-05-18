Now I have all the information needed. Let me construct the final consolidated review.

---

## Summary

This paper proposes the **star domain conjecture**: that neural network solution sets (modulo permutation symmetries) form a star domain — i.e., there exists a single "star model" that is linearly mode-connected to all other solutions — as a relaxation of the convexity conjecture, which is known to fail for narrow and deep networks. The authors introduce the **Starlight** algorithm, which trains a candidate star model by minimizing expected loss along linear paths to a finite set of source models with periodic permutation alignment. Empirical results across ResNet, VGG, DenseNet, and WideResNet architectures on CIFAR-10/100 and ImageNet show that star models have substantially lower loss barriers with held-out solutions than regular-regular barriers. The paper also explores practical benefits in Bayesian Model Averaging and model fusion.

## Strengths

- **Well-motivated relaxation of the convexity conjecture.** The star domain conjecture (Conjecture 2) is clearly stated and formally positioned as a weaker condition than convexity but stronger than general mode connectivity. Table 1 provides concrete evidence across multiple settings (e.g., ResNet-18 on CIFAR-10: regular-regular barrier 0.383 vs. star-regular barrier 0.078), demonstrating the gap the conjecture fills.

- **Broad empirical sweep across architectures, datasets, and optimizers.** The paper validates the conjecture using ResNet-18, VGG11, VGG19, DenseNet, and WideResNets on CIFAR-10, CIFAR-100, and ImageNet, with both SGD and Adam. In every case, star-regular barriers are substantially lower than regular-regular barriers, establishing that the finding is not an artifact of a single experimental setup.

- **Starlight algorithm is clearly described and computationally feasible.** The algorithm (Algorithm 1) uses Monte Carlo sampling over interpolation points and periodic weight-matching alignment, making the optimization of Eq. (3) tractable. Figure 2 shows that increasing the number of source models monotonically reduces the barrier to held-out models, which is the paper's key piece of evidence that the star model generalizes beyond the finite training set.

- **Honest discussion of limitations.** The Caveats section (line 391) explicitly states that the conjecture is not theoretically proven and that loss barriers remain non-zero, tempering the paper's claims appropriately.

## Weaknesses

### Fatal
None.

### Major

1. **Insufficient diversity in verification of the star domain property.** The central claim is that a star model is linearly connected to *all* other solutions in the solution set, but the verification uses held-out models trained with the *same hyperparameters, optimizer, and training recipe* as the source models (line 364: "We largely use standard recipes to train the models in our experiments"). The paper tests only one meaningful variation — switching SGD to Adam (Table 1, second row) — but does not systematically evaluate against models trained with different learning rates, batch sizes, augmentation strengths, or training budgets. Since all held-out models are produced by the same training pipeline with only seed-level variation, they occupy a narrow region of the solution space. The evidence is thus consistent with the possibility that the star model is only connected to this specific *type* of solution, rather than to the diverse set of all SGD-reachable solutions. The paper acknowledges this in the Caveats (calling it a "lower bound in evidence"), but the abstract and introduction still assert connectivity to "all the other solutions" without this qualification. This gap between the strength of the claim and the narrowness of the verification is the paper's most significant weakness.

### Minor

1. **Permutation alignment method specificity.** The Starlight algorithm uses weight matching (maximizing dot product) for permutation alignment throughout training and evaluation. The paper does not examine whether the low barriers for held-out models would persist if a different permutation-finding method (e.g., Sinkhorn re-basin or activation matching) were used for evaluation. Since the star model is *trained* with weight-matching alignment, the low barriers could partly reflect that the same alignment method works well for the held-out models, rather than a genuinely robust geometric property of the solution set. Adding one alternative permutation method for evaluation on a subset of experiments would help rule out this artifact.

2. **Gradient update in Algorithm 1 needs clarification.** Step 4 computes gradients \(v \leftarrow \nabla_\theta \mathcal{L}((1-t)\cdot\theta + t\cdot\theta_n)\), which by the chain rule already includes a factor of \((1-t)\). Step 5 then multiplies by an additional \((1-t)\): \(\theta \leftarrow \theta - \lambda(1-t)\cdot v\). This results in an effective scaling of \((1-t)^2\) on the gradient of the loss w.r.t. the interpolation point. This may be an intentional learning-rate modulation (putting more weight on updates near the star model), but the paper does not discuss or justify this design choice, making it difficult to verify that the algorithm correctly minimizes the stated objective in Eq. (3).

3. **Star-regular barriers at large widths approach the convex regime.** Figure 3 shows that the star-regular barrier at 8× width is approximately 0.004, which is very close to zero. This raises a question the paper does not address: is the star model simply approximating the convex regime (which is known to emerge at large widths), rather than demonstrating a *distinct* star domain property that holds where convexity does not? A discussion of whether the star model's advantage persists or collapses as width increases would strengthen the conceptual framing.

4. **Practical applications are exploratory with mixed results.** The BMA experiments (Figure 4) show better AUROC but *worse* ECE compared to ensembles — a mixed outcome that the paper acknowledges. The model fusion results (Table 2) show star models underperform ensembles by non-trivial margins (e.g., 78.4% vs. 81.3% on CIFAR-100 with 50 models). While star models offer an inference-cost trade-off, the incremental improvement over individual models is modest (≈1 point). These sections are clearly secondary contributions, but the paper overstates them somewhat in the abstract ("better uncertainty estimates" without noting the ECE degradation).

### Trivial

1. **Figure 3 (width/depth ablation) lacks error bars.** The paper reports "one standard deviation over several runs" for other experiments but the width/depth plots show only single points per condition. Given the stochasticity of SGD and the Starlight algorithm, error bars would increase confidence in the observed trends.

## Nice-to-Haves

- **Evaluate with an alternative permutation method** on held-out barriers (e.g., Sinkhorn re-basin) to rule out alignment artifact.
- **Widen the held-out set** to include models trained with varied hyperparameters (different learning rates, batch sizes, augmentation strengths) to strengthen the central claim.
- **Analyze cases where Starlight fails** to find a low-barrier star model, to bound the conjecture's applicability.
- **Empirical comparison with the "simultaneous linear connectivity" approach** of Sharma et al. (2024) mentioned in related work would be informative.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that "held-out models are trained with the same hyperparameters...so they occupy a very narrow region" was kept** (it is a valid concern about insufficient verification scope, retained as Major weakness #1). However, the reviewer's characterization that the paper "does not test against solutions obtained with different learning rates, different batch sizes, different amounts of data augmentation, or different training budgets" was cross-checked and confirmed as accurate — the paper does not systematically vary these. The Adam experiment provides one point of diversity but is not a systematic sweep. **Kept with adjusted framing.**
- **Request for error bars in Figure 3** is a valid point (kept as Trivial).
- **Request for comparison with Sharma et al. (2024)** was moved to Nice-to-Haves — this is a useful extension but not a core flaw.
- **Request for analysis of failure cases** was moved to Nice-to-Haves.
- **Critique that "practical benefits section does not provide strong evidence for the paper's core thesis"** was downgraded to Minor — the practical applications are labeled as secondary contributions and the paper is candid about the mixed results. The thesis of the paper is the star domain conjecture, not the practical benefits.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an observation about the paper not already present in its own discussion.

## Suggestions

1. **Broaden the held-out verification.** Evaluate the star model's barrier against models trained with a range of learning rates (e.g., factors 0.1×, 0.5×, 2× of the default), different batch sizes, and different levels of data augmentation. Report the distribution of barriers (e.g., violin plots) rather than a single mean. This directly addresses the gap between the "all solutions" claim and the current evidence base.

2. **Add an alternative permutation method for evaluation only.** Compute barriers between the star model and held-out models using Sinkhorn re-basin or activation matching in addition to weight matching. If barriers remain low, this rules out the concern that results are an artifact of the alignment procedure.

3. **Clarify the gradient update in Algorithm 1.** Explain whether the extra \((1-t)\) factor in Step 5 is intentional and what effect it has on optimization (e.g., damping updates when \(t\) is large, near the source model side). Providing the full derivation of the gradient of Eq. (3) with respect to \(\theta\) would help.

4. **Qualify the abstract's claims** to match the evidence level (e.g., "linearly connected to a diverse set of other solutions" instead of "all the other solutions"), and note the mixed ECE results when claiming "better uncertainty estimates."

5. **Add error bars to Figure 3** by running each width/depth condition with at least 3 random seeds.

## Score and Decision

The paper makes a genuine conceptual contribution (the star domain conjecture) and provides a practical algorithm (Starlight) for finding candidate star models. The empirical evidence is suggestive and spans a reasonable range of architectures and datasets. However, the central claim is only partially supported because the held-out verification set lacks diversity in hyperparameters and training configurations. The practical applications are exploratory and do not add substantial weight. With strengthened verification and tempered claims, this paper would represent a meaningful advance in understanding neural network loss landscape geometry. As it stands, the contribution is worthwhile but the evidence falls short of fully substantiating the headline claim.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>