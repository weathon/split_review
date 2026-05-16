Now I have a thorough understanding of the paper and can write the consolidated review.

---

## Summary

This paper introduces the Conditional Density Ratio (CDR) score for post-hoc OOD detection. Unlike prior work that marginalizes class-conditional distributions (e.g., Energy score, GEM), CDR estimates the marginal density log p(z) as log p̂(z|y) - log p̂(y|z), combining a generative class-conditional model in latent space with the discriminative classifier head. The paper also proposes an automatic temperature tuning procedure that uses only ID validation data (no OOD samples needed). Two variants are explored: CDR_Maha (Gaussian mixture / Mahalanobis) and CDR_KDE (Parzen window). Experiments on CIFAR-10, CIFAR-100, and ImageNet show strong performance.

## Strengths

1. **Principled alternative to marginalization-based density estimation**: The CDR score avoids summing over classes, which is the core mechanism of Energy and GEM scores. The paper correctly identifies that the Energy score's validity depends on a constant partition function (Section 3.2, line 69), which may not hold in practice, whereas CDR conditions on class and remains valid even when this assumption fails (line 99).

2. **Automatic temperature tuning using only ID data**: Algorithm 1 provides a method to tune T_ψ (via standard NLL calibration) and T_φ (via a novel objective) without any OOD samples. This is a practical contribution because prior temperature-scaling approaches (Liang et al., 2017) require held-out OOD data, which violates the paper's setup. Figure 3 shows that temperature scaling often significantly improves CDR performance, and Figure 4 shows the automatically selected temperature is near-optimal.

3. **Strong empirical results across benchmarks**: The paper's numbers (from text) indicate substantial gains: on CIFAR-10, CDR_Maha achieves 97.41% average AUROC vs. Energy at 91.99%; on CIFAR-100, CDR_Maha at 95.66% vs. Energy at 77.20% (Section 4.1). The robustness gap (Energy drops ~15pp from CIFAR-10 to CIFAR-100 while CDR_Maha drops <2pp) directly validates the claim that the dual-source formulation reduces reliance on classifier accuracy.

4. **General framework with two validated estimators**: CDR is demonstrated with both Mahalanobis and KDE estimators (CDR_Maha and CDR_KDE), showing the framework's flexibility. The trade-offs are discussed: KDE is more robust but computationally heavier.

5. **Informative theoretical decomposition**: Equation 2 rewrites CDR as Energy score + GCR term. Figure 2 empirically shows GCR is near zero for ID and positive for OOD, providing clear intuition for why the combination works.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Heuristic temperature scaling loss for T_φ lacks formal justification**: The loss in Algorithm 1 optimizes T_φ by maximizing the gap between true-class density and the average of wrong-class densities, plus a regularization term R. While the intuition is plausible, the paper does not connect this loss to a well-defined statistical objective (e.g., marginal likelihood, divergence minimization). The term inside the log—p̂_φ(z_i|y=y_i) - (1/(K-1)) Σ_{j≠y_i} p̂_φ(z_i|y=j)—can become negative for some temperature choices, making the loss undefined. The paper says grid search is used, which would skip invalid values, but this numerical fragility is not discussed. This gap weakens the "principled" framing the paper uses for CDR as a whole.

2. **Baseline comparison conflates formulation advantage with tuning advantage**: The paper sets all baselines at T=1 ("original configurations") while CDR uses automatic temperature tuning (line 155). This means the reported gap conflates two differences: the CDR formulation itself and the benefit of temperature tuning. The ablation (Figure 3) shows temperature tuning often gives large gains for CDR, so it is reasonable to expect similar gains for baselines if they could also be tuned. Because the paper's setup prohibits OOD data access, the standard way to address this would be to compare CDR (with automatic tuning) against baselines also operating at their best achievable performance under the same data constraints—or at minimum to explicitly acknowledge that the comparison is between "CDR with tuning" and "baselines without tuning" rather than between scoring functions per se.

3. **Validation set size not characterized as "small" as claimed**: The paper states M << N (line 37), but the actual sizes are substantial: 5,000 samples for CIFAR-10/100 (10% of training data) and 25,000 for ImageNet. For the KDE variant, all validation samples are used as support vectors, which means the method's practical deployment could require storing thousands of latent vectors. A sensitivity analysis with much smaller validation budgets (e.g., 1, 5, 10, 50 samples per class) would clarify the practical regime where CDR remains effective and would substantiate the "small data" framing.

4. **The regularization term R in the T_φ loss has no weighting coefficient and is not ablated**: The loss includes R(z_i, y_i) = (1/K) Σ_j |log p̂_φ(z_i|y=j) - log p̂_ψ(y=j|z_i)|, which is added directly without a tunable coefficient. The paper does not ablate the effect of R or show how sensitive CDR performance is to the scale balance between the two components. This matters because a naive reader cannot tell whether the method's success depends critically on the specific form of R or whether simpler alternatives (e.g., post-hoc scaling of log-densities) would suffice.

5. **No computational cost comparison**: The paper notes that CDR_KDE is computationally expensive (line 133) but provides no quantitative comparison (e.g., ms/sample or FLOPs) between CDR_Maha, CDR_KDE, and baseline methods. For practitioners evaluating the performance-computation trade-off, this information is essential.

### Trivial

- The paper states "the partition function for normalization is a constant in this case" for GEM (line 77); the phrasing could be misread as applying to the Energy score. The actual meaning is clear from context.

## Nice-to-Haves

- An experiment with zero validation samples (fully unsupervised) using a class-agnostic generative model would clarify how CDR performs in the most restricted settings. The current setup assumes labeled validation data, whereas MSP and Energy require none.
- An ablation of different CDR aggregation methods (mean vs. max vs. median of CDR_i across classes) would strengthen the claim that averaging is a reasonable default.

## Removed Points

- **"Unfair comparison is a structural flaw"**: Removed as a Fatal/Major designation. The paper's experimental setup is internally consistent: it compares CDR (with its automatic tuning, which is part of the contribution) against baselines at their default configurations (T=1). This is standard practice for "off-the-shelf" comparison. The ablation in Figure 3 isolates the effect of temperature tuning for CDR. However, the point is retained as Minor weakness #2 above because the comparison conflates formulation and tuning benefits.
- **"The partition function remark for the energy score is an oversimplification"**: Removed. The paper makes this remark about GEM (Gaussian mixture), not the energy score. For the energy score, the paper correctly notes the assumption may not hold in practice (line 69).
- **"KNN hyperparameter k=50 not justified"**: Removed. The paper explicitly states "a good hyper-parameter that worked well for a range of tasks in the original paper" (line 142).
- **"Related work does not discuss temperature tuning for baselines"**: Removed. The related work discusses temperature scaling for MSP (Liang et al., 2017), and the experimental setup explains why it is not applicable.
- **"The sum inside log can become negative" is a fatal flaw**: Downgraded to Minor. Grid search naturally avoids invalid temperature values, so this is a numerical concern rather than a fundamental invalidation.
- **Various formatting/style nitpicks**: Removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the paper's authors would not have considered.

## Suggestions

1. **Address the comparison confound**: Add a variant where baselines are evaluated with an oracle-tuned temperature (swept over a range using OOD data, presented as an upper bound) alongside the main T=1 comparison. This bounds the gap and clarifies how much of CDR's advantage is from the formulation vs. from temperature tuning.

2. **Justify or simplify the T_φ loss**: Either (a) derive the loss from a formal objective (e.g., matching the scale of log-densities via minimizing KL divergence between p̂_φ(z|y) and p̂_ψ(y|z) under the validation distribution), or (b) replace it with a simpler grid-search over T_φ using a proxy like validation set likelihood of the CDR score itself, and show the current loss matters more than simple alternatives.

3. **Characterize sensitivity to validation set size**: Systematically reduce the validation set to 1, 5, 10, 50 samples per class, showing when CDR degrades to baseline performance. This would directly substantiate the "small data" claim.

4. **Ablate the regularization term R**: Show performance with and without the regularization term, and with a simple post-hoc scaling of log-densities as an alternative.

5. **Report inference latency**: Include milliseconds per sample for CDR_Maha, CDR_KDE, and key baselines (Energy, MSP) on a representative GPU/CPU.

## Score and Decision

The paper presents a novel and well-motivated approach to post-hoc OOD detection with a clean theoretical foundation (avoiding marginalization), a practical automatic temperature tuning method, and strong empirical results across multiple benchmarks. The weaknesses identified are addressable and do not undermine the core contribution. The paper provides solid value to the OOD detection community.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>