- Decision: Reject
- Avg Score: 6.25
- Scores: 8, 8, 3, 6
Now I have verified the claims against the paper. Let me produce the consolidated review.

---

## Summary

This paper proposes CRISP, a framework for single-positive multi-label learning (SPMLL) that estimates class-priors and derives an unbiased risk estimator from those estimates. The key idea is to relax the existing assumption of identical class-priors for all labels, which the authors argue is unrealistic. The method alternates between estimating per-label class-priors (via a threshold-optimization procedure with convergence guarantees for a fixed classifier) and training the classifier using a risk estimator built from those priors. Experiments on ten datasets (four MLIC, six MLL) show the method achieves the highest mAP on all four large-scale image datasets and best or tied-best ranking loss on all six MLL datasets.

## Strengths

- **Consistent state-of-the-art empirical results.** CRISP achieves the highest mAP on all four MLIC datasets (VOC 89.93, COCO 74.91, NUS 50.05, CUB 22.15; Table 1), and best or tied-best Ranking Loss on all six MLL datasets (Table 2). The margin over competitors on COCO (74.91 vs. 73.27 for the next best, Boost+LLR) is notable.

- **Two theoretical results supporting the framework.** Theorem 1 proves that the estimated class-prior $\hat\pi_j$ converges to the ground-truth $\pi_j$ with probability at least $1-\delta$, with an error term that depends on the classifier's ability to separate positives from negatives. Theorem 2 establishes that the risk minimizer from the proposed unbiased risk estimator approximately converges to the optimal fully-supervised minimizer, with error bounded by Rademacher complexity terms that are intrinsic even to full supervision.

- **Empirical validation of class-prior estimation accuracy.** Figure 2 compares predicted class-priors on the Yeast dataset and shows CRISP's estimates closely match ground-truth values, while competing methods deviate substantially. This directly validates the core claim that the estimator is practically effective.

- **Practical computational overhead is low.** Table 4 shows class-prior estimation takes only a small fraction of total epoch time (e.g., 0.24s out of 2.19s for VOC), and updating priors every three epochs incurs only minor performance degradation (≤2.7 mAP on CUB, ≤0.8 on others).

- **Ablation confirms estimated priors are beneficial.** Figure 3(b) shows that CRISP (using estimated priors) outperforms every fixed uniform class-prior setting, and Table comparing against Crisp-val (estimating from validation set) shows CRISP's estimator is more effective.

## Weaknesses

### Fatal
None.

### Major

- **The convergence analysis does not cover the iterative estimation-training loop.** Theorem 1 bounds the class-prior estimation error for a *fixed* classifier $f$. In the algorithm (Algorithm 1), however, the classifier $f$ changes every epoch, and the estimated priors are fed back to update the same classifier that produced them. No analysis is provided for this coupled dynamics, which could be unstable—especially early in training when the classifier is poor. The paper claims theoretical guarantees for the overall procedure, but the actual guarantee only covers a static snapshot. This is a genuine gap between the theory and the implemented method.

### Minor

- **Only two of five MLL metrics are reported in the main tables.** The paper lists five metrics (Ranking loss, Hamming loss, One-error, Coverage, Average precision) in the experimental setup (line 207), but Tables 2 and 3 show only Ranking loss and Average precision. The main text then makes a summary claim of "43 out of 60 test cases score win" (line 335). While the appendix may contain the full results, the main text's empirical claim relies on data not shown. The paper would be self-contained and stronger with all five metrics visible.

- **The significance claim is not supported with standard statistics.** The text at line 335 mentions "0.05 significance level" (garbled by parser) and a win count of 43/60, but no test statistic, $p$-value, or correction for multiple comparisons is reported. A proper paired test (e.g., Wilcoxon signed-rank) would substantiate the claim.

- **The unbiased risk estimator's derivation implicitly assumes random selection of the observed positive label.** The method estimates $p(\mathbf{x} \mid y_j=1)$ using $\mathcal{S}_{L_j}$, the set of instances where label $j$ happens to be the *single annotated positive label*. This set is a faithful sample from the positive distribution only if the annotated label is selected uniformly at random among each instance's true positive labels. While the experimental setup (line 207) states "One positive label is randomly selected for each training instance," this assumption is not stated or discussed in the method section (Section 4). The paper should state it explicitly in the derivation and discuss implications when it is violated (e.g., annotator bias toward salient categories).

- **The bias modification $\lambda b^j$ (Eq. 9) is heuristic.** The paper introduces a bias term in the sigmoid logits to counteract decision boundary bias toward positive samples. The motivation is explained (lines 160–167), but no theoretical analysis is provided for how this modification affects the earlier unbiasedness claim or the risk bound. This should be presented as an engineering heuristic rather than a principled extension of the theory.

### Trivial
- The "assume-negative" warm-up phase is used but no sensitivity analysis is provided for its quality (e.g., number of warm-up epochs).
- No sweep for hyperparameter $\lambda$ is shown (only $\delta$ is swept in Figure 3(a); $\lambda$ is fixed in the ablation of Figure 3(b)).

## Nice-to-Haves
- A combined theoretical bound that accounts for both the prior-estimation error (Theorem 1) and the risk bound (Theorem 2) under the iterative process would strengthen the stability argument.
- A small simulation or analysis testing the method under biased (non-uniform) annotation selection would clarify the limits of the unbiasedness guarantee.
- A table showing the actual class-prior distributions across benchmark datasets would reinforce the motivation that priors differ significantly.

## Removed Points
These points are flagged to be removed, treat them with caution:

1. **"The paper never discusses the random-selection assumption"** — The paper *does* state "One positive label is randomly selected for each training instance" at line 207 in the experimental setup. The criticism was partially valid (the method section does not restate it), but the absolute claim "never discusses" is factually incorrect. Retained as a softened Minor weakness above, not a structural flaw.

2. **"Missing intermediate steps from Eq. (4) to Eq. (5)"** — Presentation nitpick. The derivation follows standard algebraic rewriting of the classification risk. No meaningful information is lost.

3. **"Validation split 20% is unusually large and could reduce training signal"** — This applies equally to all compared methods, so the comparison is fair. Standard practice in this literature.

4. **"The irreducible error term in Theorem 1 does not vanish as $n\to\infty$"** — The paper explicitly acknowledges this (line 115) and explains it depends on classifier quality. This is an inherent property of the estimator bound, not an oversight.

5. **"The claim 'for the first time' is hard to verify"** — This is a standard claim format; the paper's framework is novel within the SPMLL literature as acknowledged by the contribution.

## Novel Insights
The reviews surface one key observation that goes beyond the paper's own contribution framing: the paper's theoretical guarantees (Theorem 1 on class-prior convergence) are proven for a *static* classifier, but the algorithm operates by alternately updating the classifier and the priors. This creates a gap between the theoretical narrative ("theoretically guaranteed to converge") and the actual analysis. The reviewers' cross-examination reveals that the empirical success is stronger than the theory that purports to support it — the experiments show the method works despite the coupled dynamics not being theoretically characterized. This suggests the alternating procedure is empirically stable for reasons not yet explained, which could be an avenue for future theoretical work.

## Suggestions

1. In Section 4, explicitly state that the unbiasedness of the risk estimator relies on the assumption that the observed single positive label is selected uniformly at random from each instance's set of true positive labels. Add a brief discussion of what happens when this assumption fails (e.g., annotator bias toward salient classes).

2. Report all five MLL metrics (Hamming loss, One-error, Coverage, along with the two already shown) in the main paper — or at minimum provide a citation to a specific appendix table. The "43/60 win" claim should be backed by visible per-metric, per-dataset results.

3. Add a proper statistical test (e.g., Wilcoxon signed-rank with corrected thresholds) to substantiate the significance claim, and report the actual $p$-values.

4. Qualify the convergence claims to match what is actually proved. Replace language suggesting full theoretical support for the iterative procedure with language that acknowledges the static-classifier assumption of Theorem 1 and notes that convergence of the alternating procedure is empirically observed but not yet theoretically characterized.

5. Provide a sensitivity analysis for the warm-up phase duration and a sweep for hyperparameter $\lambda$ to strengthen the empirical evaluation.
