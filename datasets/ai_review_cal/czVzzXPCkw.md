- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 5, 3
Now I have all the evidence I need. Let me produce the final consolidated review.

---

## Summary

This paper tackles extrapolation in material property regression (MPR) — predicting properties outside the training label range — an important but understudied problem. It contributes (1) a benchmark of seven tasks with extreme-value splits from four Matminer datasets, and (2) the Matching-based EXtrapolation (MEX) framework, which reframes regression as a material-property matching problem using cosine-similarity alignment and a noise-contrastive-estimation loss. Experiments across two equivariant GNN backbones (PaiNN, EquiformerV2) and several baselines show MEX achieves the best average rank on MAE and geometric mean metrics.

## Strengths

- **Novel extrapolation benchmark for MPR.** The paper creates the first dedicated benchmark for evaluating label extrapolation in material property regression, using extreme-value splits (top/bottom 15% for test/validation). This fills a clear gap, as existing benchmarks use random splits assuming i.i.d. data (Section 4.1, Table 1). The benchmark is a reusable resource for the community.

- **MEX reframes regression as matching with a well-motivated training objective.** Instead of direct scalar regression, MEX optimizes a matching function between material and label embeddings using both an absolute alignment loss (negative cosine similarity) and a relative NCE loss. The intuition that matching is a simpler learning target than precise numerical prediction is clearly articulated and substantiated by experimental results (Section 3.2, Figure 2).

- **Consistent performance advantage across backbones and metrics.** MEX achieves the best average rank under both PaiNN and EquiformerV2 on both MAE and GM. It obtains the lowest MAE on 5/7 datasets for PaiNN and 6/7 for EquiformerV2, with the best GM on 4/7 and 5/7 respectively (Tables 2, 3). The advantage over strong DIR baselines (especially BalancedMSE) is consistent even if not universal.

- **Demonstrated detection capability for extrapolative materials.** MEX achieves recall over 80% on three datasets and exceeds 60% on six of seven for detecting whether a material falls in the extrapolation region, substantially outperforming all five DIR baselines (Figure 5). This addresses a practically relevant use case: flagging candidates for expensive DFT validation.

- **Thorough evaluation of existing methods.** The paper benchmarks four DIR methods (LDS, Ranksim, BalancedMSE, Conr), two regression DA methods (C-Mixup, FOMA), and ERM under two backbones. The finding that no prior method consistently beats ERM across all datasets is a useful empirical contribution (Section 4.3).

## Weaknesses

### Fatal

None.

### Major

- **The candidate label range used during inference is informed by the test set, conflicting with the extrapolation problem statement.** MEX samples candidate labels uniformly from the *entire dataset label range* (training + test), meaning the set of candidate values includes the very extrapolation targets the model is supposed to predict without prior knowledge. The paper notes "this interval can be freely adjusted based on prior knowledge of material properties" (line 135), which is a reasonable hedge, but the evaluation as conducted uses oracle-range information. This makes it impossible to tell how much of MEX's performance advantage comes from the matching framework versus from having the search space constrained to the correct interval. The paper should at minimum include an experiment using only the training label range (or a conservatively wide physical bound) as the candidate interval, and report the degradation.

- **The central claim of "state-of-the-art" performance is not backed by statistical significance testing.** MEX's average rank advantage over BalancedMSE is clear, but on individual datasets the difference is modest (e.g., Shear Modulus bottom, Refractive Index top). Only three random seeds are used, and no significance tests (paired tests, confidence intervals, or win/loss counts per seed) are provided. Given the abstract's strong language ("MEX outperforms all existing methods"), the reader deserves confidence that the advantage is systematic rather than driven by a few datasets. The paper should either add significance measures or soften the claims to match the evidence (e.g., "MEX achieves the best average rank").

- **A simpler matching baseline is not evaluated.** The most direct competitor to MEX's inference procedure is to train only with the cosine-similarity objective (L_abs) and then predict by nearest-neighbor search in the joint embedding space. The paper does not compare against this variant, making it unclear whether the NCE loss and the iterative Monte Carlo refinement are necessary or whether the core benefit comes from the matching formulation itself. Since the inference procedure (1500 candidates × 10 iterations) is substantially more complex than a single forward pass, this baseline would help the reader understand the source of improvement.

### Minor

- **The recall rate metric is informative but incomplete.** A sample is "detected" as extrapolative if its predicted value falls anywhere within the extrapolation interval. This metric rewards models that predict boundary-near values, even if those predictions are inaccurate. Reporting precision or a thresholded F1 score would provide a fuller picture of detection quality. That said, MEX's recall advantage over baselines is large enough that this does not undermine the detection claim.

- **No ablation on inference hyperparameters (number of candidates M, number of iterations).** The paper ablates the score module design and the λ trade-off parameter, but not the inference hyperparameters (C=1500 candidates, 10 iterations). These directly affect computational cost and could influence accuracy. A brief sensitivity analysis would strengthen the contribution.

- **The split percentage (15%) is not justified or ablated.** Extrapolation difficulty depends on the gap between train and test ranges. Reporting only one split configuration makes it unclear how robust the findings are. A sensitivity analysis (e.g., 10%, 20%) would be informative.

### Trivial

None.

## Nice-to-Haves

- **Report the actual label ranges (min/max) for each train/validation/test split**, so readers can assess the extrapolation gap (currently absent despite being listed as "to appear" in Table 1's image).
- **Analyze how the linear label encoder extrapolates** for values far outside the training range. A simple plot of ℰ_l(y) across the full range would reveal whether the embedding saturates or remains discriminative.
- **Consider a dedicated Limitations section**, given the practical issues noted above.
- **Ablate the split percentage** (e.g., 10%, 20%) to test sensitivity to extrapolation gap difficulty.

## Removed Points

These points were flagged but removed with justifications:

- **"Benchmark ignores covariate shift"** — Scope creep. The paper explicitly focuses on *label* extrapolation. Evaluating input distribution shift is a different research question.
- **"Narrow benchmark base (4 datasets)"** — 7 tasks from 4 datasets is a reasonable size for a dedicated extrapolation benchmark. Many accepted benchmark papers use fewer.
- **"Hyperparameter grid asymmetry concerns"** — The paper states "hyper-parameter selection was performed based on validation MAE via grid search" for all methods. Reporting MEX's grid explicitly without also printing each baseline's grid is standard practice; the paper provides no evidence of unfair tuning.
- **"NCE loss has been used before"** — The paper cites Gustafsson et al. (2020). Applying existing techniques to a new problem domain is a valid contribution; this is a related-work positioning observation, not a weakness of the method.
- **"No theoretical analysis of why matching helps"** — The paper provides intuitive justification in Section 3.2. For an empirical systems paper, this is sufficient.
- **"No ablation on M or iterations"** — Moved to Minor; this is a genuine suggestion but not severe enough to be a standalone weakness in its own tier.
- **"Why 15%?"** — Moved to Nice-to-Have as a sensitivity suggestion.

## Novel Insights

The most interesting observation from the reviews is the tension between the practical value of MEX's detection capability (high recall, flagging candidates for DFT) and the methodological concern about the candidate range. If MEX's recall advantage persists even when the candidate interval is set conservatively (e.g., a physically plausible but wide bound), the detection contribution would be substantially more impressive. Conversely, if performance degrades sharply without oracle-range information, the paper's main experimental framing would need revision. This sensitivity question is the single highest-priority item for revision and is not addressed in the current paper.

## Suggestions

1. **Run an ablation with the candidate interval set to the training label range only** (or a conservatively wide physical bound). Report the degradation and discuss what it implies about the method's genuine extrapolation capability. This directly addresses the most critical concern.

2. **Add statistical significance.** Bootstrap confidence intervals across the three seeds, or report per-dataset win/loss counts. If the advantage is not significant on several datasets, state this plainly and temper the "outperforms all" language accordingly.

3. **Evaluate the simple matching baseline**: train only with the cosine similarity loss (L_abs) and predict via argmax nearest-neighbor search over candidate labels in the embedding space. Report how this compares to full MEX. This isolates the benefit of the NCE loss and the iterative refinement.

4. **Soften the abstract's claim** from "outperforms all existing methods" to something like "achieves the best average performance" or "consistently ranks first across benchmarks." The data supports the latter, not the former.

5. **Add a precision or F1 metric** alongside recall for the detection analysis, so the reader can assess whether high recall comes at the cost of many false positives.
