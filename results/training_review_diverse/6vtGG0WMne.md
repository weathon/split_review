I have thoroughly read the paper and verified the reviewer claims against the actual text. Let me now synthesize the final consolidated review.

---

## Summary

This paper addresses the underexplored problem of regulating the *degree* of class imbalance in deep models to match application-specific metrics (accuracy, F1, G-means), rather than always pursuing a balanced classifier. The authors propose (1) a formal definition of Model Imbalance State (MIS) as the average prediction probability per class, (2) a Bias Adjustment (BA) method that optimizes only the K bias parameters of the last layer to achieve a user-specified MIS, and (3) a per-epoch training strategy that corrects bias and validates after each epoch to select optimal backbone representations. Experiments on binary image (CIFAR-10) and text (SST-2, AG) classification show consistent improvements over six baselines, with particularly large gains at extreme imbalance ratios.

## Strengths

- **Formal definition of Model Imbalance State (MIS):** The paper provides a principled, quantitative measure of model bias as the average prediction probability per class (Eq. 4, Section 3.1). This enables explicit, targeted adjustment of model imbalance rather than relying on heuristic class weights or threshold-moving.

- **BA method is both efficient and metric-adaptive:** BA optimizes only K bias parameters using gradient descent on the full training batch, achieving orders-of-magnitude lower computational cost than grid-search for class weights (Figure 4 shows ~100× less time). The search strategy over the target MIS r allows any user-specified metric (F1, G-means) to determine the optimal imbalance state.

- **Per-epoch training strategy outperforms two-stage methods:** By correcting bias and validating after each epoch, the method selects optimal backbone parameters. Table 6 shows that even when two-stage methods (cRT, LWS) are tuned to their best epoch, BA still yields higher accuracy (e.g., 81.30 vs. 73.79 on SST-2 at 500:1) while taking ~10× less total time.

- **Demonstration that different metrics require different MIS:** Figure 2 provides compelling evidence that the optimal minority-class probability differs substantially across metrics — very low for F1 (<0.1), moderate for G-means (~0.3–0.5), varying for accuracy. This empirically validates the paper's central motivation.

- **Efficiency advantage over class-weight hyperparameter tuning:** Figure 4 shows that BA obtains better or comparable results in under an hour, while grid-search over 2¹⁰–2¹¹ weight combinations requires tens to hundreds of hours. This is a practically significant advantage.

## Weaknesses

### Fatal
None.

### Major

- **Unfair comparison on F1 and G-means metrics (Tables 3, 4):** The baselines (Proportion, Auto-Weighting, cRT, LWS, POT) are all designed to produce class-balanced models or to optimize for accuracy on balanced test sets. None are adapted to the target metric in Tables 3 and 4 (F1, G-means). For example, cRT retrains the classifier with balanced sampling — this intentionally targets a balanced posterior. Comparing such methods against a procedure that explicitly searches for the MIS maximizing the target metric is asymmetric. The claim that the proposed method is "superior" for these metrics is weakened because we cannot distinguish whether the improvement comes from the method itself or simply from having metric-specific tuning. A fairer evaluation would apply a simple post-hoc adjustment (e.g., threshold-moving) to each baseline to optimize the target metric on a validation set. The only baseline that receives such tuning is the class-weighting method in Figure 4, and there the comparison is limited to a single imbalance ratio (100:1). **This is the most significant issue in the paper.**

### Minor

- **Missing uncertainty quantification:** No standard deviations, confidence intervals, or per-run results are reported anywhere (Tables 2–5, Figure 2/3). Given that the BA method involves a search over r and gradient-based bias optimization, results may vary with random seed, validation split, or optimization trajectory. This makes it hard to assess whether reported improvements (especially small gaps like 0.19 points on SST-2 at 10:1 in Table 2) are statistically meaningful.

- **Ambiguity in the search procedure:** The paper does not clarify whether the search over the target MIS *r* is performed from scratch at every epoch or only once at the end (Section 3.2 vs. 3.3). If re-searched each epoch, the computational cost accumulates (up to ~47 candidate r values × number of epochs). The efficiency comparison in Table 6 and Figure 4 cannot be properly interpreted without knowing this. The authors should state explicitly how often the search runs and report the search cost separately.

- **Missing details on bias optimization:** The paper states that BA uses gradient descent to optimize the bias (Section 3.2, line 91), but does not report the learning rate, number of iterations, convergence criteria, or whether early stopping is used. While the optimization is indeed low-dimensional (K parameters), these details are necessary for exact reproducibility.

- **Binary-only validation limits the scope of claims:** The search strategy is explicitly designed for binary classification (Section 3.2, line 89: "This work mainly discusses the binary classification"). The paper's claims of "wide applicability" (abstract, conclusion) are not supported by evidence for K>2. Extending the coarse-to-fine grid search to multiple classes would require a different approach, and this limitation should be acknowledged more explicitly.

- **Conclusion overstates evidence:** The claim of "significant improvement compared with the SOTA method" (conclusion) is not fully justified given the evaluation issues above. The accuracy results (Table 2) and efficiency results (Figure 4, Table 6) are solid, but the F1/G-means superiority claims rest on an unfair comparison.

### Trivial

- The paper states that the training strategy "keeps the backbone module constant and only adjusts the bias" (line 98), which already implies that W is unchanged. The reviewer's suggestion to state this more explicitly is a presentation preference, not a weakness.
- The concern about how MIS *P* would behave on a balanced vs. imbalanced validation set is partially misdirected — the search uses the validation set to evaluate the target *metric* (F1, G-means), not to compute MIS. Section 3.2 (line 87) states this clearly.

## Nice-to-Haves

- **Ablation of the per-epoch strategy:** A direct comparison of "Ours with per-epoch BA" vs. "Ours with only final BA" would isolate whether the per-epoch correction adds value beyond the final bias adjustment. Table 6 hints at this indirectly, but a clean ablation would be informative.

- **Multi-class discussion or small experiment:** Even a brief discussion of how the search strategy could be extended to K>2 (e.g., by optimizing a temperature parameter or using validation to tune per-class biases via gradient descent on the metric) would strengthen the "wide applicability" claim.

- **Metric-tuned baselines for Table 6:** The comparison to two-stage methods in Table 6 tunes only the epoch, not the metric. Applying threshold-moving to cRT/LWS for F1 and G-means would make this comparison more informative.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Critical Issue 3's claim that "the paper does not discuss how P would behave on a balanced validation set"** — The validation set is used to evaluate the target metric (F1, G-means), not to compute MIS. The paper clearly states this in Section 3.2 line 87. The reviewer's concern about validation set imbalance ratio is valid but the specific framing about MIS on a validation set is a misreading.

- **The claim that the paper doesn't state whether W is unchanged** — The paper explicitly states "keeps the backbone module constant and only adjusts the bias" (line 98). This is adequately stated.

- **The "up to ~180 candidate r values" estimate** — The coarse-to-fine search over binary r1 involves at most ~47 candidates (9 + 19 + 19), not 180. However, the reviewer's broader point about ambiguity in search frequency is valid (kept under Minor).

## Novel Insights

The most insightful observation from the reviews is that the paper's central methodological contribution — bias-only optimization for metric-adaptive imbalance control — is strongest where it is evaluated fairly (accuracy on balanced test sets, efficiency comparisons), but the evidence for metric-specific superiority (F1, G-means) is structurally weaker than the paper claims because the baselines are not given the same metric-specific tuning. This suggests the paper should either (a) add metric-tuned baselines, or (b) reframe its contribution more modestly as an efficient way to *approximately* achieve metric-optimal imbalance without expensive hyperparameter search, rather than definitively outperforming all existing methods on every metric.

## Suggestions

1. **Add metric-tuned baselines for Tables 3 and 4:** For each baseline (cRT, LWS, Proportion, Auto-Weighting, POT), apply a simple threshold-moving on the validation set to optimize F1 or G-means. This would isolate the benefit of the proposed bias-only adjustment versus full-model + threshold tuning. This is the single most important improvement.
2. **Report variance:** Add results from 3 random seeds with standard deviations for all tables. Given the large margins at high imbalance ratios (10+ points), the main conclusions are likely robust, but this would substantially improve credibility.
3. **Clarify search procedure:** State explicitly whether r* is searched once (then reused) or at every epoch. If re-searched each epoch, report the total search cost separately from the training cost.
4. **Report BA optimization hyperparameters:** Provide learning rate, number of gradient steps, and convergence criterion for the bias optimization.
5. **Acknowledge the binary-only limitation** in the conclusion and discuss potential extensions.

## Score and Decision

The paper tackles a genuinely important and underexplored problem — regulating the *degree* of model imbalance rather than always pursuing balance. The MIS definition and BA method are conceptually clean, and the efficiency advantages over hyperparameter-tuned class weighting (Figure 4) are convincingly demonstrated. The accuracy results (Table 2) provide fair evidence of effectiveness.

However, the evaluation of F1 and G-means superiority (Tables 3, 4) is structurally weakened because baselines are not tuned for those metrics. This is the paper's primary claimed contribution (metric-adaptive imbalance control), and the evidence for it is not fully persuasive in its current form. The remaining issues (missing variance, procedural ambiguities) are fixable but collectively reduce confidence.

The paper has a solid idea and strong initial results in efficiency and accuracy. With fairer metric-specific baselines, it would be a meaningful contribution. In its current form, the evidence supports the efficiency and accuracy claims but not the full breadth of the metric-superiority claims.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>