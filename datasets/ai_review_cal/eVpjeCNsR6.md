- Decision: Reject
- Avg Score: 5.60
- Scores: 6, 6, 3, 8, 5
Now I have verified all claims against the paper. Here is my consolidated review.

---

## Summary

This paper proposes EraseDiff, a method for unlearning data from diffusion models by formulating the problem as bi-level optimization. The outer objective finetunes on remaining data to preserve utility; the inner objective scrubs forgetting data by forcing the model to predict uniform noise instead of the true Gaussian noise. A first-order approximation (Liu et al. 2022a) solves the resulting problem efficiently. Experiments on CIFAR10, UTKFace, CelebA, and CelebA-HQ with conditional DDIM and unconditional DDPM models show that EraseDiff can effectively remove target classes/attributes while maintaining generation quality on remaining data, outperforming baselines like NegGrad and BlindSpot.

## Strengths

1. **Novel bi-level formulation for diffusion unlearning** (Section 3.2, Eqs. 6–9). Explicitly couples utility preservation and data scrubbing as a constrained optimization, providing a principled solution that avoids the catastrophic utility collapse observed with naive baselines. This is a genuine methodological contribution.

2. **Strong quantitative evidence of unlearning with utility preservation** (Table 3). On CIFAR10, EraseDiff achieves forgetting-class FID of 260.05 and remaining-class FID of 27.44, while NegGrad attains 256.01 and 245.20 respectively — showing that only EraseDiff scrubs the target data without destroying model quality. The retrained model's weights are closely matched (WD 1.3534 vs. oracle minimum 1.3533).

3. **Concrete efficiency gain** (Section 5.4). Unlearning takes ~10 minutes on an A100 compared to ~27 hours for retraining and ~32 hours for the original training. The complexity analysis shows the method leverages the small forget-set regime (N_f << N_r).

4. **Evaluation on public Hugging Face models** (Section 5.6, Figure 5). Demonstration on pre-trained unconditional DDPM models from Hugging Face increases practical applicability beyond models trained from scratch by the authors.

5. **First-order approximation avoids expensive Hessian computation** (Section 3.2, Eq. 8). The adoption of K-step gradient descent to approximate the inner solution makes the method scalable to high-dimensional diffusion model parameters without second-order costs.

## Weaknesses

### Fatal
None. The core claims are supported by evidence, and no verified flaw invalidates the basic contribution.

### Major

- **Factually incorrect claim in the conclusion.** Line 217 states: "In this work, we first explored the unlearning problem in diffusion models." This is directly contradicted by the paper's own Related Work (line 113), which cites Gandikota et al. (2023a,b) and Heng & Soh (2023) as prior work that "recently introduce unlearning in diffusion models." Whether those papers address the exact same setting or not, the "first explored" claim is false. This undermines credibility and must be corrected. (The abstract and introduction make more measured claims and are fine.)

- **No experimental comparison against existing diffusion unlearning methods.** The paper cites Gandikota et al. (2023a,b) and Heng & Soh (2023) but does not benchmark against them. The paper's baselines (NegGrad, BlindSpot, Finetune) are from the general machine unlearning literature, not from diffusion-specific unlearning work. While the paper notes that Gandikota focuses on text-to-image concept erasure and Heng & Soh operates without data access — making direct comparison non-trivial — the absence of any comparison or even a discussion of these differences in the experiments leaves a significant gap in the empirical evaluation. A reader cannot assess whether EraseDiff adds value beyond these existing approaches.

### Minor

- **Limited experimental scale and no variance reporting.** Only 2 classes are unlearned on CIFAR10, 1 ethnicity on UTKFace, and 1 attribute on CelebA. No results for larger forget sets (e.g., 5 or 10 classes) are reported. No error bars, confidence intervals, or multi-seed runs are provided for any table entry. Given the stochasticity of diffusion model training and unlearning, this weakens statistical reliability.

- **BlindSpot adaptation not explained.** The paper describes BlindSpot (Tarun et al., 2023b) as designed for regression tasks but does not explain how it is adapted to work with diffusion model training objectives. Without this, the fairness of the comparison is unclear.

- **KL divergence metric lacks calibration.** The paper proposes KL divergence between the model's output distribution and Gaussian noise as a metric (Section 5.1, item iv), but does not establish what range of KL values corresponds to successful vs. failed unlearning, or how this metric correlates with privacy leakage. Figure 3 shows histograms but provides no numerical summary (e.g., mean KL per set), making cross-condition comparison difficult.

- **"User Study" section title is misleading** (Section 5.6). The section contains qualitative example images, not an actual user study with human participants. This should be renamed.

### Trivial

- **Equation notation is dense** (Eqs. 4–5, Section 3.1). The transition from KL-maximization (Eq. 4) to the noise-replacement objective (Eq. 5) would benefit from a short intuitive explanation in the main text rather than relying on the paragraph between them.

## Nice-to-Haves

- A comparison against a simple weighted-gradient baseline (gradient descent on D_r + gradient ascent on D_f with a balancing weight, i.e., L = L_r − λL_f) would clarify whether the bi-level machinery provides a practical advantage over a simpler alternative. This is the natural ablation of the bi-level formulation itself.
- Using established membership inference attacks for diffusion models (e.g., Carlini et al. 2023, already cited by the paper) would strengthen the privacy evidence beyond the loss-based MIA that the paper acknowledges as limited.
- A dedicated Limitations section (rather than one sentence in the conclusion) discussing scalability to larger forget sets, dependence on forgetting data access, and sensitivity to the noise target would improve credibility.

## Removed Points

These points were flagged by reviewers but are removed with justification:

- **"Core design choice (uniform noise target) is under-justified — no ablation."** The paper states (line 69) that the uniform target is chosen because it requires no extra hyperparameters, and results for N(μ, I) with μ≠0 are reported in the paper (likely in the appendix, which the parser strips). The hard rules prohibit penalizing missing appendix content. The justification provided (no extra hyperparameters) is reasonable.
- **"Weight distance is not a standard unlearning metric."** WD is cited from Tarun et al. (2023a) and the paper explains its purpose. This is a valid metric in the unlearning literature.
- **"Computational complexity uses undefined symbols."** Line 190 defines E, S, K, N_rs, N_f in context; the notation is adequate.
- **"Related Work placed after the method is non-standard."** Many papers place Related Work after the method; this is a formatting preference, not a substantive weakness.
- **"The claim to 'introduce' an unlearning algorithm is exaggerated."** The abstract says "we introduce an unlearning algorithm for diffusion models" — this is accurate: they *do* introduce a new algorithm. Only the conclusion's "first explored" claim is problematic (already flagged above).
- **"Generic speculation about generalization"** (e.g., "results may not generalize"). This is area-of-concern noise without a specific concrete anchor. The concrete concern about limited experimental scope is already captured above.
- **"Missing hyperparameters"** (e.g., learning rate ζ, inner steps K, outer epochs E). These are standard details likely in the appendix (stripped). The paper provides λ=0.1 and basic complexity terms (K, E, S).

## Novel Insights

None beyond the paper's own contributions. The reviews surface no insight that the paper itself does not already provide.

## Suggestions

1. **Correct the "first explored" claim** in the conclusion. Acknowledge prior diffusion unlearning work (Gandikota et al., Heng & Soh) and position EraseDiff's specific contribution relative to them (bi-level formulation, different experimental setting, etc.).
2. **Add at least one experiment with Gandikota et al. or Heng & Soh as a baseline**, or provide a detailed justification in the experimental section for why direct comparison is infeasible, along with a clear statement of how EraseDiff's setting differs from theirs.
3. **Report results from at least 3 random seeds** with means and standard deviations for all main metrics (Tables 1, 2, 3).
4. **Rename Section 5.6** from "User Study" to "Qualitative Results on Hugging Face Models" or similar.
5. **Provide numerical summaries** (mean, std) for the KL divergence histograms in Figure 3.
6. **Clarify how BlindSpot is adapted** to the diffusion model setting.
