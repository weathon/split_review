- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5
Now I have all the information I need. Let me synthesize the final review, carefully cross-checking each claim against the actual paper.

## Summary

This paper proposes BiLoRA, a bi-level optimization (BLO) framework for fine-tuning low-rank adapters. It parameterizes the incremental matrix ΔW = PΛQ (pseudo-SVD form) and trains the pseudo singular vectors {P,Q} on one data subset (lower level) and the pseudo singular values Λ on another disjoint subset (upper level). The motivation is to reduce overfitting that the paper argues arises from training all adapter parameters on a single dataset. Experiments on GLUE (RoBERTa, DeBERTa) and E2E NLG (GPT-2) show consistent improvements over LoRA, AdaLoRA, and other PEFT baselines.

## Strengths

1. **Principled separation of parameter training onto different data subsets.** The bi-level formulation explicitly trains pseudo singular vectors and pseudo singular values on disjoint data (Section 3.2, Figure 1). This is a structurally novel departure from LoRA and AdaLoRA, which train all parameters on the same data. The SVD-parameterization is inherited from AdaLoRA, but the BLO-based split is new.

2. **Consistent empirical improvements across diverse settings.** BiLoRA outperforms LoRA and AdaLoRA on nearly all tasks in Tables 1, 2, and 3, covering RoBERTa-base/large, DeBERTa-v3-base, and GPT-2 medium/large across both NLU and NLG tasks. The gains are directionally consistent (e.g., ~1–2.5 points on several GLUE tasks), and larger margins are observed on smaller datasets (CoLA, RTE, MRPC) where overfitting risk is higher (Section 4.2).

3. **Scalability demonstrated on a 1.5B model.** Table 4 shows BiLoRA matches or exceeds LoRA and full fine-tuning on DeBERTa-xxlarge (1.5B params) without additional hyperparameter tuning, suggesting the method scales.

4. **Ablation on key design choices.** Table 5 compares three pseudo-singular-value parameterizations (Real-Value, Softmax, Approximately Binary), and Table 6 tests sensitivity to the orthogonality regularizer weight γ₁. The results show the method is relatively robust to these choices, supporting practical usability.

## Weaknesses

### Fatal
None.

### Major

1. **Baseline comparisons rely on published numbers rather than re-implemented controls.** The paper states it "used the reported results in previous work" (Section 4.1) for LoRA, AdaLoRA, and other baselines. The tables mark numbers from prior works with `*`. Because BiLoRA uses its own training framework (Betty for BLO), a different data split (8:2 for NLU), and a larger learning rate enabled by the Softmax parameterization (Section 4.4), the baseline numbers from prior work were produced under different conditions. Without re-running LoRA and AdaLoRA under *identical* conditions—same codebase, same data splits, same learning rate schedules—the reported improvements cannot be cleanly attributed to the BLO framework rather than to implementation differences or hyperparameter choices. This undermines the central claim that "BiLoRA outperforms LoRA/AdaLoRA."

2. **The overfitting motivation is asserted but not directly demonstrated.** The paper repeatedly claims that training all parameters on a single dataset "often leads to overfitting" (Abstract, Section 1), but provides no direct evidence—no training vs. validation loss curves, no generalization gap analysis—showing that LoRA or AdaLoRA actually overfit on the evaluated tasks. The only supporting observation is that BiLoRA shows larger gains on small datasets (CoLA, RTE, MRPC), which is indirect evidence at best. If the overfitting claim is the primary motivation, its lack of direct verification weakens the paper's narrative and leaves open the possibility that BiLoRA's improvements come from a different mechanism (e.g., the larger LR, the SVD parameterization itself, or the validation-based loss for Λ).

3. **No ablation isolating the BLO contribution from other design differences.** The ablation studies (Tables 5, 6) compare parameterizations and regularizer weights, but do not include the most important control: training the SVD-parameterized model (same PΛQ form) on the *full* training set (i.e., the standard AdaLoRA setup, without the BLO split). Without this comparison, it is unclear whether the improvement comes from the BLO framework, the Softmax parameterization, the larger learning rate, or some combination.

### Minor

1. **No confidence intervals or variance reported for main results.** Table 1 (the primary RoBERTa results) reports single numbers without variance. Table 2 says "average result of five runs" but does not report the standard deviation or per-run spread. Without measures of uncertainty, it is impossible to assess whether the often small (1–2 point) improvements are statistically reliable.

2. **Data split design differs between NLU and NLG without justification.** For NLU (GLUE), the training set is split 8:2 for lower/upper levels (Section 4.2). For NLG (E2E), "the training set and validation set are used as the lower-level and upper-level datasets respectively" (Section 4.3). This is a fundamentally different setup: using the validation set for upper-level training means the model effectively optimizes Λ on held-out data that would normally only be used for evaluation. The paper offers no rationale for this discrepancy or analysis of how it affects results.

3. **Training time comparison lacks controlled detail.** Table 7 reports lower total training time for BiLoRA vs. LoRA. The paper explains this is due to fewer epochs from a larger learning rate (Section 4.4). However, no epoch counts, convergence criteria, or GPU specifications are provided for either method. Since LoRA's training times are not produced in the same controlled setup (and may come from different sources), the efficiency claim cannot be properly evaluated.

4. **The BLO approximation is underspecified.** The lower-level problem is posed as `argmin_V L(V,E;D1)` (Eq. 3), but the paper does not specify how this is solved in practice—how many inner-loop steps, whether it is solved to convergence, or how the hypergradient is computed. The Betty library is cited but not described, and different approximations yield different hypergradients. This makes the method difficult to reproduce without reverse-engineering from the Betty code.

5. **No comparison with simple regularization baselines for LoRA.** If the claimed benefit is reduced overfitting, basic baselines (LoRA with weight decay, dropout, or data augmentation) would help contextualize whether BiLoRA's complexity is warranted. This is a scope gap.

### Trivial
None.

## Nice-to-Haves

- An analysis of how the 8:2 data split ratio affects performance. The paper uses a fixed split but does not explore sensitivity to this choice.
- Theoretical justification for why the BLO separation reduces overfitting (e.g., connection to cross-validation or bilevel regularization).
- Acknowledgment of the added complexity from two-level optimization, the need to split data, and the fact that absolute improvements over well-tuned LoRA/AdaLoRA are modest.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The average score weights tasks of very different difficulty equally"**: This is standard practice for GLUE reporting (used by the original GLUE paper, LoRA, and AdaLoRA alike). It is not a weakness specific to this paper. *(Removed: not a valid weakness.)*
- **"Faster total training time despite more complex optimization" (from Strength Finder)**: This strength conflicts with verified weakness #3 (training time comparison lacks controlled detail and may rely on uncontrolled baselines). Per filtering rules, when a strength and weakness disagree, the weakness wins. *(Removed: conflicts with verified weakness.)*
- **"If LoRA were also run with a similar learning rate, it might converge just as quickly"**: This is speculative and assumes facts not in evidence. The paper explains that the larger LR is specifically enabled by the Softmax initialization within the BLO framework (Section 4.4). While the training time comparison is still insufficiently controlled, this particular counterfactual is not justified by any evidence on the page. *(Removed: speculative, not grounded in paper content.)*
- **Criticism about the paper not documenting hyperparameter values for each task**: The paper states hyperparameters are kept "exactly the same as LoRA/AdaLoRA where necessary" (Section 4.2). Since the LoRA and AdaLoRA papers specify these values, this criticism is partially addressed. It is a reproducibility concern, but an overly strict one given the citation to prior work. *(Demoted from original to Removed: the paper's explicit reference to prior-work settings reasonably addresses this.)*

## Novel Insights

The reviews surface two unstated tensions in the paper. First, the BLO formulation is motivated by overfitting, but the experiments evaluate *test* performance (GLUE dev set), not generalization gap. The paper conflates "generalization" (test accuracy) with "overfitting reduction" (gap between training and test accuracy) without measuring the latter. Second, there is a subtle irony: the BLO split is designed to prevent Λ from overfitting to the training data by training it on a held-out subset, yet for NLG, the held-out data is literally the validation set, which is *supposed* to be held out entirely. This means the method's upper level uses data that in standard pipelines would only inform hyperparameter choices, not parameter updates—which may actually be more information being used during training, not less. These tensions are not discussed in the paper.

## Suggestions

1. **Re-implement LoRA and AdaLoRA in the same codebase** with the same data splits, learning rate schedules, and training setup. This is the single most impactful improvement for establishing credibility.
2. **Add a controlled ablation**: train the PΛQ-parameterized model on the full dataset (no BLO split) and compare to the full BiLoRA. This would isolate the BLO contribution from the SVD parameterization and Softmax init.
3. **Report variance** (standard deviation or confidence intervals) across multiple seeds for all main results.
4. **Show training/validation loss curves** for at least one representative task (e.g., CoLA or RTE) comparing LoRA, AdaLoRA, and BiLoRA, to directly validate the overfitting motivation.
5. **Provide the missing implementation details** for the BLO solver: number of inner-loop iterations, convergence tolerance, and hypergradient computation method. This is essential for reproducibility.
