- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 5, 3
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes a denoising module for knowledge tracing that combines explicit (masking) and implicit (SVD-based regularization) denoising strategies, integrated into the CL4KT framework. The key idea is to apply denoising to both original and augmented interaction sequences, using SVD to distinguish between "hard" noise (handled via explicit masking) and "soft" noise (handled via implicit regularization), and to select which samples receive which treatment. Experiments on four KT datasets show AUC/RMSE improvements over several baselines.

## Strengths

- **Consistent predictive accuracy gains across four benchmarks**: Table 1 shows the proposed method (CL4KT-DA) achieving the highest AUC on all four datasets (Algebra05, Algebra06, Assistment09, Slepemapy) compared to seven baselines including DKT, SAKT, AKT, CL4KT, and DTransformer. The improvement over the base CL4KT model directly validates that the denoising module adds value beyond the augmentation strategy alone.

- **Robustness to injected Gaussian noise**: Table 2 demonstrates that as noise ratio increases from 0% to 40%, the combined denoising method consistently maintains higher AUC than explicit-only or implicit-only variants on two datasets. This provides direct evidence that the hybrid strategy is more stable under controlled noise conditions.

- **Data-fusion ordering ablation confirms design choice**: Table 3 compares different fusion strategies and shows that denoising after fusing original and augmented sequences (CL4KT-DA) outperforms denoising each stream separately (CL4KT-SDS) or fusing first then denoising (CL4KT-FDS). This directly supports the paper's specific design choice in Equation (4).

- **Qualitative validation of denoising effect**: Figure 3 shows kernel density plots where post-denoising feature distributions are consistently smoother and less jagged across all four datasets, visually confirming that the method alters the feature distribution in the intended direction.

## Weaknesses

### Major

- **"Plug and play" claim is unsubstantiated**: The paper claims the denoising module is "plug and play" (abstract, conclusion), yet all experiments use CL4KT as the base model. No experiment demonstrates the module working with DKT, AKT, or any other architecture. Supporting this claim requires at minimum one additional base model (DKT would be the natural and simplest choice). This is the most significant gap between what the paper claims and what it demonstrates.

- **SVD-based sample selection mechanism is significantly underspecified**: Several aspects of the core technical contribution (Equations 6–13) are presented with insufficient clarity to assess correctness or reproducibility:
  - The matrices being decomposed are never defined in terms of dimensions (per-student sequence? per-batch? what size?). The notation switches between indexed variables ($q_{u_i}$) and global matrices with no mapping.
  - The threshold $\rho$ (Equation 12) is introduced as a threshold value ("the higher the noise, the higher the threshold $\rho$"), but then used as a count ("top-$\lfloor\rho/4\rfloor$ samples"). This inconsistency makes the selection procedure ambiguous.
  - The entropy term $H(\Delta_{global})$ is invoked without specifying how entropy is computed from a set of scalar difference values (histogram estimation? kernel density?).
  - The divisor $4$ in $\lfloor\rho/4\rfloor$ is used without any justification or ablation. These clarity gaps collectively prevent a reader from understanding or reproducing the core selection mechanism.

### Minor

- **Core denoising function $f_{den}$ is deferred to citations**: Equation (3) defines the central denoising operation through $f_{den}$, which is described only by citations to (Zhang et al., 2022; Lin et al., 2023b) and a high-level description ("filters noise by leveraging intra-sequence information"). While citing prior work is standard, the paper's contribution is a denoising pipeline, and the primary denoising operation is left entirely unspecified—no architecture, no parameter count, no training details. Providing even a 2–3 sentence summary of what $f_{den}$ does would substantially improve the paper's self-containedness.

- **No comparison against denoising-specific KT methods**: The paper compares against standard KT baselines (DKT, SAKT, AKT, CL4KT) but does not compare against prior work on denoising for KT, including (Zhang et al., 2023) which is cited in the related work. While this is a young sub-area, comparing to at least one denoising-aware KT method would strengthen the evaluation.

- **No standard deviations or statistical significance**: Table 1 reports AUC/RMSE aggregated over five folds but no standard deviations, confidence intervals, or significance tests are provided. Given the number of comparisons, it is unclear whether the reported gains are statistically meaningful.

- **Ablation covers only the proposed method's own variants**: The ablation compares -ID (implicit only), -ED (explicit only), and -DA (combined) variants, and tested on the base models (DKT-ED, etc.). However, parameters $\alpha$, $\beta$, $\gamma$, $k$, $\lambda$ are introduced without reported values or sensitivity analysis. Only $\eta = 0.01$ is mentioned.

### Trivial

- Typo in conclusion: "preocess" should be "process".
- Equation (7) has a notation issue: $\delta_j$ is introduced as "the maximum singular value" but then summed over $j$ as if it varies per index.

## Nice-to-Haves

- The Gaussian noise robustness experiment (Table 2) tests only two datasets (chosen for shorter runtime). Adding at least one more dataset would strengthen the claim of general robustness.
- A case study showing whether the samples selected for explicit denoising actually correspond to guessing/slipping events would ground the qualitative claims (Figures 3–4) in concrete evidence.
- The $\mathcal{L}_{des}$ loss (Equation 5) maximizes the ratio of the largest singular value to the sum of all singular values. The paper would benefit from a short intuitive explanation of why this corresponds to noise reduction in the KT context (e.g., what spectral property of student interaction matrices indicates noise).

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Criticism that "the paper does not specify how it differs from Zhang et al. (2023) methodologically"**: The related work section clearly distinguishes its approach from prior work — it states that prior methods use only one type of denoising (implicit or explicit), while the proposed method combines both and uses SVD-based sample selection. The difference is stated, albeit briefly.

2. **Criticism that "Table 3 does not compare against training on both sequences without denoising"**: The baseline CL4KT (reported in Table 1) already provides this comparison — it trains on augmented sequences without denoising. Table 3 specifically isolates the fusion ordering effect, which is a different question.

3. **Claim that "the paper's own thesis that denoising must be applied to both original and augmented sequences is not backed by any analysis"**: The paper provides this analysis implicitly — Tables 1 and 3 show that denoising (applied to both streams) outperforms no-denoising and separate-denoising alternatives. The motivation (augmentation amplifies noise from the original sequence) is stated in the introduction and related work.

4. **Criticism about missing hyperparameter sensitivity for $\alpha, \beta, \gamma, k$**: Per the hard rules, criticisms about undisclosed hyperparameters in a conference submission should be removed as nitpicks. The paper reports $\eta=0.01$; the other parameters would ideally be ablated but their omission alone is not a structural weakness.

5. **Strength about "Novel SVD-based sample selection"**: This claimed strength conflicts with the verified weakness that the SVD mechanism is significantly underspecified. Since the weakness wins when they disagree, this strength is dropped from the main review.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the clarity/evaluation gaps but do not add a new perspective on the method or problem.

## Suggestions

1. **Fully specify the SVD selection mechanism**: Provide a pseudocode or step-by-step algorithm defining the matrix dimensions for each SVD call, how $\rho$ transitions from threshold to count, and how $H(\Delta_{global})$ is computed. Justify or ablate the $\rho/4$ divisor.

2. **Address the "plug and play" claim**: Add at least one experiment with a different base model (DKT is the natural choice) to demonstrate generality.

3. **Summarize $f_{den}$**: Add 2–3 sentences describing what $f_{den}$ does architecturally — is it a learned denoiser? What is its architecture, loss, or filtering rule? This does not require full pseudocode, but the current treatment is too opaque for a paper whose central subject is denoising.

4. **Add error bars or significance tests**: Report standard deviations over the five folds or conduct paired tests against the best baseline.
