Now I have a thorough understanding of the paper and can verify the reviewer claims against the actual content.

## Final Review

## Summary

This paper proposes SelMix, a selective mixup fine-tuning technique for optimizing non-decomposable objectives (e.g., Min Recall, H-mean, coverage-constrained recall) in both semi-supervised and supervised settings. The core idea is to compute a gain matrix that estimates how much each class-pair mixup would improve the target objective, then sample mixup pairs according to a softmax over this gain matrix. The method is evaluated across CIFAR-10/100 LT, ImageNet-1k/100 LT, and STL-10, showing consistent improvements over prior empirical and theoretical methods.

## Strengths

1. **Strong empirical gains on non-decomposable objectives across settings.** Table 1 shows SelMix improves Min Recall on CIFAR-10 LT from 74.1 (ABC) to 79.1, and Min Head-Tail Recall on CIFAR-100 LT from 48.4 (CSST) to 57.8. The radar plot (Fig. 1) confirms SelMix achieves the best values across four different non-decomposable metrics simultaneously — breaking the typical trade-off where theoretical methods sacrifice mean recall and empirical methods sacrifice worst-case metrics.

2. **Principled approximation of the gain matrix makes optimization tractable.** Theorem 1 provides a closed-form approximation for the change in a non-decomposable objective induced by each (i,j) mixup pair, avoiding differentiation through the non-smooth confusion matrix. This allows SelMix to handle non-linear objectives (G-mean, H-mean) that prior theoretical methods (CSST, Narasimhan et al.) could not optimize without re-training from scratch.

3. **Robust performance under mismatched label distributions.** Figure 2 shows SelMix outperforms all baselines on CIFAR-10 LT when the unlabeled data distribution is balanced ($\rho_u=1$) or inverted ($\rho_u=1/100$). On STL-10, where the unlabeled distribution is unknown, SelMix improves Min Recall by 12.7% over CSST — a realistic scenario where prior methods (CReST, CSST) that assume matched distributions degrade.

4. **Generalizes to supervised learning and large-scale datasets.** Table 2 shows SelMix fine-tuning of MiSLAS improves Min Recall on CIFAR-10 LT from 72.5 (MiSLAS stage-2) to 79.2. Table 3 demonstrates scalability to ImageNet-1k LT (Min Head-Tail Recall: 29.7→45.1) and ImageNet-100 LT (Min Recall: 12.1→24.0).

## Weaknesses

### Fatal
None.

### Major

1. **Semi-supervised baseline comparison conflates pre-training and fine-tuning effects.** In Table 1, SelMix pre-trains with FixMatch(LA) and then fine-tunes, while methods like DASO, ABC, and CSST are trained from scratch using their own procedures. The paper acknowledges this asymmetry (caption: "SelMix is an inexpensive fine-tuning technique compared to other expensive full pre-training-based baselines"), and the inclusion of FixMatch(LA) as a direct baseline (same pre-training, no fine-tuning) partially addresses the concern — SelMix improves over FixMatch(LA) by large margins (Min Rec: +23.2 points on CIFAR-10). However, the core question of whether the gains come from having a fine-tuning stage at all versus from the *selective* nature of the mixup remains. An ablation where the same pre-trained model is fine-tuned with uniform mixup, or where a method like CSST is applied as a fine-tuning step from the same FixMatch(LA) pre-trained model, would directly isolate the benefit of the selective sampling distribution. The paper references a policy comparison table in the appendix (Table policy-comparison) but this comparison should be in the main body to substantiate the core claim. Without this, the reader cannot fully separate the effect of "fine-tuning helps" from "selective mixup fine-tuning specifically helps."

2. **Key hyperparameters missing from the main paper.** The softmax temperature $s$ in $\mathcal{P}_{\text{SelMix}}$ (Eq. 4) governs the exploration-exploitation trade-off and is never specified numerically. The number of outer cycles $T$ and inner SGD steps $n$ per cycle are not given. Learning rates for the linear classifier and backbone are described only as "cosine learning rate" without concrete values. These are the control knobs of the algorithm; without them, the method cannot be reproduced from the main paper alone. The paper references a hyperparameter table in the appendix (Tab. \ref{tab:hyperparams}), but values governing the central algorithmic mechanism (especially $s$) should appear in the main text.

### Minor

1. **The theoretical analysis rests on assumptions that are acknowledged but clearly unrealistic.** Theorem 2 assumes the objective $\psi$ is concave in $W$ and that the mixup direction has sufficient alignment with the gradient — neither holds for a deep network even when only the linear layer is updated. The paper is transparent about this ("we assume... for the analysis"), but the theorem functions more as a sanity check than a substantive guarantee. This does not undermine the empirical results, which stand on their own.

2. **The gain matrix approximation (Theorem 1) relies on a small-variance assumption that is not empirically verified.** The paper states that for each class $k$, the random vector $V_{ij}^\top g(x)$ must have small variance for $x \sim D_k^{\text{val}}$, and provides an intuitive justification ("if $g$ is a sufficiently good feature extractor..."). However, no empirical evidence (e.g., histogram of feature norms or variance statistics) is provided to verify this assumption holds for the actual models used. This is a gap between theory and practice that the paper does not quantify.

3. **Coverage constraint threshold $\tau = 0.95/K$ is used without justification or sensitivity analysis.** The threshold appears in all coverage-constrained experiments, but no discussion explains why 0.95 is chosen or how results vary with this choice. A sensitivity study (varying $\tau$) would strengthen confidence in the method's robustness.

4. **Total computational cost is underreported.** The paper states SelMix fine-tuning takes "~2 min" but does not report the total GPU-hours for the full pipeline (FixMatch(LA) pre-training + SelMix fine-tuning). Since pre-training is not negligible, the efficiency claim should account for the full cost, especially when comparing against methods that do only a single training pass.

### Trivial
- The wrapped figure and algorithm in the main body are hard to read; the pseudocode uses coarse phrases like "using Thm. 1" without specifying the actual computation. A more detailed algorithm description would improve clarity.

## Nice-to-Haves
- An ablation comparing SelMix against fine-tuning the same FixMatch(LA) pre-trained model with uniform mixup (or no mixup) for the same number of steps. (The paper references this in the appendix via Table policy-comparison, but including it in the main body would strengthen the core claim.)
- Sensitivity analysis for the softmax temperature $s$ and the coverage threshold $\tau$.
- Empirical verification (e.g., variance statistics) of the small-variance assumption in Theorem 1.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **"Missing comparison with uniform mixup fine-tuning"** — The paper explicitly references this comparison in Table \ref{tab:policy-comparison} (appendix). The absence from the main body is a presentation choice, not a missing experiment.
- **"Theoretical weaknesses about concavity assumption"** — The paper acknowledges these limitations transparently ("we assume… for the analysis"). This is standard practice for convergence analyses in deep learning; the theory is presented as a sanity check.
- **"Standard deviations are small, suggesting stable runs"** — This is a positive observation, not a weakness.
- **"The paper references tables in the appendix, making it feel incomplete"** — The appendix was stripped by the parser; these references exist in the original submission and are standard in conference papers with page limits.
- **"Gap between theory and practice is large"** — Already addressed by the paper's own caveats. Restated in Minor weakness 1 in a more measured form.
- **"The softmax distribution is heuristic, not derived"** — The paper provides theoretical optimality claims in the appendix (Theorem on SelMix policy vs. non-adaptive policies) and acknowledges the heuristic nature.
- **"The confusion matrix reformulation feels abrupt"** — Subjective presentation preference; not a substantive weakness.

## Novel Insights
None beyond the paper's own contributions. The reviews largely converge on the paper's strengths and identify the same central concern about baseline comparison fairness.

## Suggestions
1. Add a semi-supervised ablation where alternative methods (uniform mixup fine-tuning, CSST-style fine-tuning) start from the same FixMatch(LA) pre-trained model. This would directly isolate the benefit of the selective distribution.
2. Report the softmax temperature $s$, number of cycles $T$, inner steps $n$, and learning rates in the main paper body (not just the appendix).
3. Include a brief sensitivity analysis for the temperature $s$ and coverage threshold $\tau$.
4. Report total pipeline cost (pre-training + fine-tuning) rather than just the fine-tuning cost.
5. Clarify the exact computation of $G_{ij}$ in the algorithm pseudocode rather than deferring to "using Thm. 1."

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>